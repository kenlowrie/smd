#!/usr/bin/env python3

from .debug import Debug
from .constants import Constants

class ImportCache(object):
    def __init__(self):
        from .thread import getTLS
        from .config import ConfigFile, LocalUserConfigFile
        
        self._importCache = []
        self._importInsertionIdx = -100
        self._sysDefaults = getTLS().getObjectFromTLS(Constants.sysDefaults)

        # Start with the default body, head and html document parts, i.e. the last things to read
        #fuck = self._sysDefaultstls_data.sysDefaults
        self._importCache += ConfigFile("import/def_body.md", self._sysDefaults.load_default_body).filenameAsList()
        self._importCache += ConfigFile("import/def_head.md", self._sysDefaults.load_default_head).filenameAsList()
        self._importCache += ConfigFile("import/def_html.md", self._sysDefaults.load_default_html).filenameAsList()

        # Now, if any other imports have been specified, we need to load them right after the user
        # builtins.md, since we want to be able to have a "last chance to override" hard coded stuff.
        additionalImports = self._sysDefaults.getImportFiles()
        if additionalImports:
            for importfile in additionalImports[::-1]:
                self._importCache += [importfile]

        # The builtins.md must be treated special, since we allow one or both of them to be processed
        # during initialization. Start with the default builtins.md, and then load the user version,
        # if it's available. This way the user builtins.md can override the system defaults. In order
        # to make this work, we need to cache() them in reverse order.

        self._importCache += LocalUserConfigFile("import/builtins.md", self._sysDefaults.load_user_builtins).filenameAsList()
        self._importCache += ConfigFile("import/builtins.md", self._sysDefaults.load_default_builtins, user_ver=False).filenameAsList()

    @property
    def iCache(self):
        return self._importCache
    
    @iCache.setter
    def iCache(self,filename):
        iCache += [filename] if filename is not None else []

    def initDebug(self):
        self._debug = Debug('cache.i')

    def readyForNextCachedImport(self, index):
        if self._importInsertionIdx == -100: self._importInsertionIdx = index

        return self._importInsertionIdx == index and self.iCache

    def getNextCachedImport(self):
        if self.iCache:
            return self.iCache.pop()
        
    def gotCachedImports(self):
        return self.iCache

class Cache(object):
    """A class to abstract a line cache.
    
    Initially, this is used to process the default document components and the
    built-ins that are part of smd. However, it can also be used to cache lines 
    in the middle of processing normal files.
    """
    def __init__(self):
        self._cache = []    # assume an empty cache

        # finally, add the globals onto the stack, since these can be used during parsing of the other files
        # we just cached... specifically [sys.imports], but also [sys.basepath]. These will be the
        # first lines parsed, even if imports are cached, since readline() gives precedence to the cache

        from .globals import init_globals
        for line in init_globals():
            self._cache.append(line)

    @property
    def rawOutput(self):
        from .thread import getTLS
        return getTLS().getObjectFromTLS(Constants.rawOutput)

    def initDebug(self):
            self.debug = Debug('cache')
            self.debug.off()

    def pushline(self, s):
        self._cache.append(s)

    def readline(self):
        line = ''
        while self.gotCachedLine():
            line += self._cache.pop().strip()
            if line.endswith('\\'):
                # Remove the \ and add a space
                line = line[:-1] + ' '
                # Only continue if there are more lines, in case they put a \ on the last line
                if self._cache:
                    continue

            # If the line we have is blank, then it only has white space.
            if not line.strip():
                if self._cache:
                    # if there's more lines, then by all means, keep reading, ignore blanks
                    continue
                else:
                    # This is an odd spot. We don't want to make it difficult to add built-ins,
                    # so we need to handle this gracefully. Let's pretend the line was a comment
                    line = "// Blank line in the cache..."

            # Return the line
            from .utility import HtmlUtils
            self.debug.print('Returning: <em>{}</em>'.format(HtmlUtils.escape_html(line)))
            if self.rawOutput:
                self.rawOutput.write(f"{line}")

            return line

        raise LogicError("Cache().readline() failed while processing cache.")

    def gotCachedLine(self):
        return self._cache      # self._builtIn < len(self._builtIns)
        


if __name__ == '__main__':
    print("Library module. Not directly callable.")
