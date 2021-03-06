#!/usr/bin/env python
"""Abstraction for input stream handling in stdio class.

These classes support the implementation of @import; that is, the
ability to import a new file while processing the current one. When a new
file is imported, it is read until EOF, and then the class will fall back
to processing the prior file. @imports can be nested to allow even more
flexibility.
"""

from sys import stdin
from pathlib import Path

from .exception import FileError, LogicError
from .debug import Debug
from .cache import ImportCache, Cache
from .constants import Constants

class _OpenFile(object):
    """A simple class to keep track of files that are opened."""
    def __init__(self, f, name, wrapStackPosition):
        self.file = f
        self.name = name
        self.wrapStackPos = wrapStackPosition


class StreamHandler(object):
    """
    Abstract open() and readline() to implement @import support

    This class abstracts the open() & readline() APIs so they can support
    having multiple files open, ala the @import keyword. When a new file
    is opened, the current file object is saved on a stack, and the file
    becomes the current file until EOF. At that point, it's closed, and
    the previous file is then popped off the stack, and we resume reading
    from it until EOF.
    """
    def __init__(self):
        self.filestack = []
        self.idx = -1
        self.line = ''
        self._started_with_stdin = None
        self._started_with_file = None
        self._cache = Cache()
        self._importcache = ImportCache()
        from .thread import getTLS
        tls = getTLS()
        self._fileTracker = tls.getObjectFromTLS(Constants.fileTracker)
        self._rawOutput = tls.getObjectFromTLS(Constants.rawOutput)
        self.debug = Debug('stdinput')

        # Easy way to force EOF no matter what we're doing
        self._fake_eof = False

    def cache(self):
        return self._cache

    @property
    def icache(self):
        return self._importcache

    @property
    def fileTracker(self):
        return self._fileTracker    # The FileTrack() instance
    
    @property
    def rawOutput(self):
        return self._rawOutput

    @property
    def fake_eof(self):
        return self._fake_eof

    @fake_eof.setter
    def fake_eof(self, flag):
        self._fake_eof = flag

    def force_eof(self):
        self.fake_eof = True

    def getWrapStackPositionOfCurrentFile(self):
        return self.filestack[-1].wrapStackPos if len(self.filestack) else -1

    def handleRelativePathMarker(self, filename):
        # If name is prefixed with '$', prefix the filename with the path of
        # CURRENT open file. If this is the first file to be opened, or if
        # the current file being read is stdin, the Path().cwd() is used.
        if(filename[0] == '$'):
            def fixname(fn):
                # allow both '$path/file.md' and '$/path/file.md'
                from os import sep
                return fn[1:] if fn[1] != sep else fn[2:]

            self.debug.print(f"self.idx is [{self.idx}]")
            if self.idx >= 0: self.debug.print(f"self.filestack[self.idx].name is {self.filestack[self.idx].name}")
            # Make sure we have an open file, otherwise use Path().cwd() as the path
            if self.idx < 0:
                cwd = Path().cwd()
                self.debug.print(f"No open file, using current directory for '$': {cwd}")
                filename = Path(filename).joinpath(cwd, fixname(filename))
            elif self.idx >= 0:
                path = Path(self.filestack[self.idx].name).resolve()
                filename = path.joinpath(path.parent, fixname(filename))

        return filename

    def push(self, fh, name=None):
        """
        Push an open file onto the stack for readline()

        This method can be used to push an open file onto the filestack,
        as an alternative to passing in a filename (open() method).
        """
        from .wrap import WrapperStack
        self.filestack.append(_OpenFile(fh, name, WrapperStack.getWrapStackPosition()))
        self.debug.print(f"Set current wsp to: {self.filestack[-1].wrapStackPos}<br />")
        self.idx += 1

    def open(self, filename):
        """
        Open a file and place the handle on the stack for readline()

        Once a file has been opened, subsequent calls to readline() use
        that handle to return data.

        None can be passed to signify that sys.stdin should be used, however
        it's not required, since that's the default behavior of this class.
        This is done primarily as a convenience for the consumer of the class.

        Arguments:
        filename -- name of the file to open, or None to process sys.stdin
        """

        if(filename is None):
            """sys.stdin can only be opened as the first file."""
            if(self.idx != -1):
                raise FileError(2, "ERROR: sys.stdin can only be opened at start")

        else:
            filename = self.handleRelativePathMarker(filename)

            # Make sure the specified file exists, and then open it
            name = Path(filename).resolve()
            self.debug.print(f"Attempting to open: {filename} using {name}")
            if name.is_file():
                # Check if we've already imported this file
                if self.fileTracker.alreadySeen(str(name)):
                    self.debug.print('File <strong><em>{}</em></strong> has already been imported'.format(name))
                    return
                file = open(name, "r")
                self.push(file, str(name))
                self.fileTracker.seen = name

            else:
                raise FileError(1, "ERROR: Unable to import '{}'. File does not exist.<br />".format(filename))

    def readline(self):
        """
        Read the next line of input and return it.

        If no file is currently opened, reads from sys.stdin. Once you hit
        EOF, return an empty string ''. This is the basic (default) behavior.

        If you open a file (via the open method of this class), the behaviour
        changes as follows. Read the next line until you hit EOF, and then,
        fall back to reading from sys.stdin until EOF.

        If another file is opened (via open() method) while reading from the
        current file, we read from the new file until EOF, and then close it,
        and fall back to the previous file.
        """
        if self.fake_eof:
            self.debug.print("<strong><em>Forced EOF</em></strong>")
            return ''

        # Process the cached imports first.
        if self.icache.readyForNextCachedImport(self.idx) and self.icache.gotCachedImports():
            return f'@import "{str(self.icache.getNextCachedImport())}"'

        self.line = ''
        if self._cache.gotCachedLine():
            return self._cache.readline()

        while 1:
            if self.idx < 0:
                # Once we've read from sys.stdin, we need to remember that,
                # so that if we've imported a file, we will fall back to
                # reading from sys.stdin after we hit EOF on the imported file.
                if self._started_with_stdin:
                    # If we started with stdin, fall back to reading from sys.stdin
                    self.line += stdin.readline()
                else:
                    break       # can't continue if we didn't start with stdin...
            else:
                # we are reading from a file, read the next line
                self.line += self.filestack[self.idx].file.readline()

            if not self.line or not self.line.rstrip():
                break
            elif not self.line.rstrip().endswith('\\'):
                break
            self.line = self.line.rstrip()[:-1]

        if(self.line == ''):
            # We hit EOF. Do we have any other files opened?
            if(len(self.filestack)):
                # Pop the current file from the stack
                f = self.filestack.pop()
                f.file.close()
                # Reset the wrap stack position to what it was when we opened the file
                from .wrap import WrapperStack
                WrapperStack.resetWrapStackPosition(f.wrapStackPos, self.debug.print)
                # set the index back 1, so future reads will use prior file
                self.idx -= 1

                if (self.idx >= 0 or self._started_with_stdin):
                    return self.readline()

        if self.rawOutput:
            self.rawOutput.write(f"{self.line}")

        return self.line


if __name__ == '__main__':
    print("Library module. Not directly callable.")
