#!/usr/bin/env python3
#pylint: disable=W1401
"""
Main module for the Script Markdown Package

Copyright (c) 2020 Ken Lowrie

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

------------------------------------------------------------------------------

When invoked from the command line w/o any parameters, it reads from sys.stdin,
formats it on the fly and outputs HTML.

//TODO: UPDATE THIS ONCE I FINALIZE THE NEW INTERFACE

To quickly see how it works, pip install from the top level directory

.. code-block:: rest

    cd smd
    pip install .
    smd

.. note::

    Alternatively, use smdparse to translate the userdocs (pip install is still required)

.. code-block:: rest

    cd smd/docs
    smdparse -f userdocs.md -c

//TODO: Talk about ismd here, but must note requirements (pip install should install what is needed)

"""

from re import IGNORECASE, findall, match
from sys import exit, exc_info, version_info
from os.path import isfile

MIN_PYTHON = (3, 7, 3)
if version_info < MIN_PYTHON:
    exit("Python %s.%s.%s or later is required.\n" % MIN_PYTHON)

from .core.line import Line
from .core.link import LinkDict
from .core.debug import DebugTracker, Debug
from .core.regex import Regex, RegexMD, RegexMain
from .core.stdio import StdioWrapper
from .core.ftrack import FileTrack
from .core.sysdef import SystemDefaults
from .core.thread import initTLS, getTLS
from .core.variable import Namespaces
from .core.bookmark import BookmarkList
from .core.markdown import Markdown
from .core.constants import Constants
from .core.exception import RegexError, LogicError, FileError


class ScriptParser(StdioWrapper):
    """
    Parse a text file written in a markdown-like syntax and output HTML.

    Reads a text file (or reads from sys.stdin) and outputs HTML.
    """
    def __init__(self, sysDefaults=None, fileTracker=None):
        """
        Initialize the required instance variables for this class.

        """
        # before we do anything else, we need to make sure that our thread local storage is set up.
        #self._tls = initTLS().tls_data
        self._tls = initTLS()

        # Create the debug tracker object for this app
        self.tlsDebugTracker = DebugTracker(output=self.oprint)
        self.tlsDebugTracker.debug = Debug('_SYSTEM')
        self.tlsDebugTracker.utilityDebug = Debug('utility')
        
        # before we call the Constructor for StdioWrapper(), which will create a StreamHandler()
        # object, which will instantiate the Cache(), which will process all of the defaults
        # i.e. builtins, default_html, head, body..., I have to establish the global SystemDefaults()...

        # if the SystemDefaults() object is not already stored in the TLS data, we need to do that now.
        try:
            self.tlsSysDefaults = sysDefaults
        except AssertionError:
            pass    # ignore the error if it's already set up

        try:
            self.tlsFileTracker = fileTracker
        except AssertionError:
            pass    # ignore if someone already initialized.

        # If we want to output the raw data to a file as we go...
        self.tlsRawOutputFileInit()
        

        # Okay, safe to call the base class constructor now

        super(ScriptParser, self).__init__()  # Initialize the base class(es)

        # Register a tracker for this object
        self.debug_smd = Debug('smd')
        self.debug_smd_line = Debug('smd.line')
        self.debug_smd_raw = Debug('smd.raw')

        self._md = Markdown()           # New markdown support in separate class

        self._line = Line(md_func=self._md.markdown)
        self._lineInCache = False       # if we have a line in the cache
        self._shotListQ = BookmarkList()    # shot list link Q
        self._wrapper = []              # stack of wrapper tags

        # add a custom TLS object that holds the reference to the wrap stack, so we can access it from the .core.utility module.
        self.tls.addObjectToTLS('wrapstack', self._wrapper)

        self._ns = Namespaces(self._md.markdown, self._md.setNSxface, oprint=self.oprint)
        #TODO: Clean this up. _stripClass needs to be handled better than this...
        self._md.setStripClass(self._stripClass)

        # I think the reason I do the following has to do with the namespace used by exec & eval.
        # I need to figure out the reason though. //TODO: Need to verify this.

        #//TODO: Need to store these in the TLS, right? eliminate this weirdnness
        # unless it's rquired to get the vars inside the .core.utility namespace for
        # the eval/exec/compile stuff that's part of the runtime to work...

        #_set_ns_xface(ns_ptr)
        exec("from .core.utility import _set_ns_xface;_set_ns_xface(self._ns)")
        #_set_line_cache(self.stdinput.cache())
        exec("from .core.utility import _set_line_cache;_set_line_cache(self.stdinput.cache())")


        self._css_class_prefix = Regex(r'\{:([\s]?.\w[^\}]*)\}(.*)')
        self._special_parameter = Regex(r'\s([\w]+)\s*=\s*\"(.*?)(?<!\\)\"')

        # Dictionary of each line type that we can process
        self._regex_main = {
            #                     RawLine Prefix   Test Regex               Match Regex
            'header': RegexMain(   False,  True,   r'^([#]{1,6})[ ]*',      r'^([#]{1,6})[ ]*(.*)'),
            'import': RegexMain(   False,  False,  r'^[@]import[ ]*',       r'^[@]import[ ]+[\'|\"](.+[^\'|\"])[\'|\"]'),
            'embed': RegexMain(    False,  False,  r'^[@]embed[ ]*',        r'^[@]embed[ ]+[\'|\"](.+[^\'|\"])[\'|\"]'),
            'watch': RegexMain(    False,  False,  r'^[@]watch[ ]*',        r'^[@]watch[ ]+[\'|\"](.+[^\'|\"])[\'|\"]'),
            'var': RegexMain(      True,   False,  r'^@var[ ]*',            r'^(@var(\s*.*))'),  # r'^(@var(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)'), 
            'set': RegexMain(      True,   False,  r'^@set[ ]*',            r'^(@set(\s*.*))'),  # r'^(@set(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)'),
            'code': RegexMain(     True,   False,  r'^@code[ ]*',           r'^(@code(\s*.*))'),  # r'^(@code(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)'), 
            'link': RegexMain(     True,   False,  r'^@link[ ]*',           r'^(@link(\s*.*))'),  # r'^(@link(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)'), 
            'html': RegexMain(     True,   False,  r'^@html[ ]*',           r'^(@html(\s*.*))'),  # r'^(@html(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)'), 
            'image': RegexMain(    True,   False,  r'^@image[ ]*',          r'^(@image(\s*.*))'),  # r'^(@image(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)'),
            'dump': RegexMain(     True,   False,  r'^@dump[ ]*',           r'^(@dump(\s*.*))'),    # r'^(@dump(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")*)'),
            'break': RegexMain(    True,   False,  r'^[@](break|exit)[ ]*', r'^[@](break|exit)\s*$'),
            'stop': RegexMain(     True,   False,  r'^[@](stop|quit)[ ]*',  r'^[@](stop|quit)\s*$'),
            'raw': RegexMain(      False,  False,  r'^@(@|raw)[ ]*',        r'^@(@|raw)[ ]*(.*)'),
            'wrap': RegexMain(     False,  False,  r'^@(wrap|parw)[ ]*',    r'^@(wrap|parw)[ ]*(.*)'),
            'debug': RegexMain(    True,   False,  r'^@debug[ ]*',          r'^(@debug(\s*.*))'),  # r'^(@debug(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")*)'),
        }

    @property
    def tls(self):
        return self._tls
    
    @tls.setter
    def tls(self, tls_object):
        self._tls = tls_object
    
    @property
    def tlsDebugTracker(self):
        return self.tls.getObjectFromTLS(Constants.debugTracker)
    
    @tlsDebugTracker.setter
    def tlsDebugTracker(self, dbgTrk):
        if self.tlsDebugTracker is not None:
            raise AssertionError("DebugTracker already initialized in TLS")
        elif dbgTrk and not isinstance(dbgTrk, DebugTracker):
            raise TypeError("debugTracker must be of type .debug.DebugTracker")

        # all is good, store the object in the TLS
        self.tls.addObjectToTLS(Constants.debugTracker, dbgTrk if dbgTrk else DebugTracker())

    @property
    def tlsSysDefaults(self):
        return self.tls.getObjectFromTLS(Constants.sysDefaults)
    
    @tlsSysDefaults.setter
    def tlsSysDefaults(self, sd):
        if self.tlsSysDefaults is not None:
            raise AssertionError("SystemDefaults already initialized in TLS")
        elif sd and not isinstance(sd, SystemDefaults):
            raise TypeError("sysDefaults must be of type .sysdef.SystemDefaults")

        # if nothing passed in, then set to an empty instance...
        self.tls.addObjectToTLS(Constants.sysDefaults, sd if sd else SystemDefaults())

    @property
    def tlsFileTracker(self):
        return self.tls.getObjectFromTLS(Constants.fileTracker)
    
    @tlsFileTracker.setter
    def tlsFileTracker(self, ft):
        if self.tlsFileTracker is not None:
            raise AssertionError("FileTracker already initialized in TLS")
        elif ft and not isinstance(ft, FileTrack):
            raise TypeError("fileTracker must be of type .ftrack.FileTrack")

        # if nothing passed in, then set to an empty instance...
        self.tls.addObjectToTLS(Constants.fileTracker, ft if ft else FileTrack())
    
    @property
    def tlsRawOutputFile(self):
        return self.tls.getObjectFromTLS(Constants.rawOutput)
    
    def tlsRawOutputFileInit(self):
        # if -o was passed (we will have a filename)
        if self.tlsSysDefaults.raw_output_file:
            if self.tlsRawOutputFile is not None:
                raise AssertionError("Raw output file is already open")

            self.tls.addObjectToTLS(Constants.rawOutput, open(self.tlsSysDefaults.raw_output_file, "w"))


    def tlsRawOutputFileDeinit(self):
        # if -o was passed (we will have a filename)
        if self.tlsRawOutputFile:
            self.tlsRawOutputFile.close()
            self.tls.removeObjectFromTLS(Constants.rawOutput)

    @property
    def wrapper(self):
        return self._wrapper
        
    def _regex(self, id):
        """
        Returns the RegexMain object for a specific parse type.

        Arguments:
            id -- the parse type identifier that you want.

        Returns:
            RegexMain Object for parse type if defined.

        Throws exception RegexError() if invalid ID is passed.
        """
        if(id in self._regex_main):
            return self._regex_main[id]

        raise RegexError("ERROR: Invalid regex ID: [{0}]".format(id))

    def _unreadLine(self):
        """
        Mark the current line in the buffer as unread

        This will cause it to be returned on the next call to readline.
        """
        if(self._lineInCache is True):
            raise LogicError("ERROR: _unreadLine called with line in cache.")

        self._lineInCache = True

    def _reprocessLine(self):
        """Reparse the current line if it had markdown
        
        If the processed line and the raw line are different, then some
        type of markdown was applied. Cache the processed line as the
        new 'raw' line, and try again.
        """
        if self._line.original_line.strip() != self._line.current_line.strip():
            # Save the current css_prefix, cause we'll lose it in _setLineAttrs()
            saved_css_prefix = self._line.css_prefix
            self._setLineAttrs(self._line.current_line)
            # If we had a css prefix on the original line, then put it back.
            # The original css prefix should have precedence, since it was explicit on the
            # outermost line. I hope this is right!
            if saved_css_prefix:
                self._line.css_prefix = saved_css_prefix
            self._unreadLine()
            return True
        
        # The original_line and the current_line are the same, so no need to reprocess it...
        return False

    def _setLineAttrs(self, line):
        """Initialize the data members of the Line() object
        
        In order to properly implement the reprocessLine() method, we need
        to set all the attributes of the Line() as if the marked down line
        was just read from the file. This logic has been placed in a class
        method so it can be used in both places.
        """
        # remember if this line was indented...
        self._line.was_indented = True if match('[ \t]', line) else False

        # save a copy of the original line...
        self._line.original_line = line

        # strip the class, if any, and initialize css_prefix
        self._line.css_prefix, self._line.stripped_line = self._stripClass(line.strip())

    def _readNextLine(self):
        """
        Read next line from the current file (or whatever is cached)

        If something is in the cache, return that instead
        """
        if(self._lineInCache):
            self._lineInCache = False    # reset the flag since we are returning it
            return self._line.current_line

        # read the next line from the file buffer
        while(1):
            line = self.ireadline()
            if not line:
                break
            if not line.strip():
                continue
            if line[0:2] != '//':
                break
            if line[0:3] == '///':
                break

        self._setLineAttrs(line)
        #self._line.reprocessed = False

        # return the non-marked down version
        return self._line.original_line

    def _addBookmark(self, linktext):
        """
        Generate unique HTML bookmark and return the inline <a> tag to define it.

        Arguments:
            linktext -- optional text to wrap the <a> element around.

        Returns:
            HTML <a> element as string: <a id="GENERATED UNIQUE_ID">linktext</a>
        """
        return "<a id=\"{0}\"></a>\n".format(self._shotListQ.addBookmark(linktext))

    def _stripClass(self, line):
        """
        Strip the {:.class} prefix off line, and return tuple of (class, line)

        The class is formatted for use as an HTML class ATTR, along with the
        rest of the line. If no class is present, just return the line as-is.
        """

        def make_CSS_class(tmpClass):
            """Create a proper class="class1 class2" string from .class1.class2 notation.

            Arguments:
                The class(es) specified in the {:.class1.class2} wrapper

            Returns:
                String in proper class attribute format. e.g.:
                    {:.ignore.red} would become ' class="ignore red"'
            """
            # remove all extraneous spaces, then change '.' to ' ' then strip leading blanks
            s = tmpClass.replace(" ", "").replace(".", " ").strip()

            return " class=\"{0}\"".format(s)

        if(match(self._css_class_prefix.regex, line)):
            m = match(self._css_class_prefix.regex, line)

            if(m is not None and len(m.groups()) == 2):
                # format it like this: " class=cls1"
                return make_CSS_class(m.group(1)), m.group(2)

        # no class found, so return '' and the line, as-is
        return '', line


    def parse(self):
        """Parse a Script File in text format and emit HTML code."""

        """
        Following are the helper functions for the parse() method.

        testLine() and matchLine() are used in the main loop below, and
        then each line parse type has a method that can process it and
        output the HTML that goes with it.
        """
        def testLine(regex_obj, line_obj):
            """See if the current line matches the test_regex() expression."""
            line = line_obj.current_line if not regex_obj.uses_raw_line else line_obj.original_line
            return match(regex_obj.test_regex(), line)

        def matchLine(regex_obj, line_obj):
            """See if the current line matches the match_regex() expression."""
            line = line_obj.current_line if not regex_obj.uses_raw_line else line_obj.original_line
            return match(regex_obj.match_regex(), line)

        def handle_header(m, lineObj):
            """Handle a header parse line"""
            if(m is not None and len(m.groups()) > 1):
                hnum = len(m.group(1))
                header = "<h{0}{2}>{1}</h{0}>".format(hnum, m.group(2).strip(), lineObj.css_prefix)
                # if we have a wrapper tag in play
                if self.wrapper:
                    tag = self.wrapper[-1]
                    self.oprint(f'{tag.start}{header}{tag.end}')
                else:
                    self.oprint(header)
            else:
                self.oprint(lineObj.current_line)

        def handle_watch(m, lineObj):
            """Handle a watch parse line"""
            if(m is not None and len(m.groups()) == 1):
                try:
                    watch_fn = m.group(1)
                    if not isfile(watch_fn):
                        self.oprint(f"WARNING: Watch file \"{watch_fn}\" does not exist. Not adding to watch list")
                    else:
                        self.tls.fileTracker.seen = watch_fn
                except FileError as fe:
                    self.oprint(fe.errmsg)

        def handle_import(m, lineObj):
            """Handle an import parse line"""
            if(m is not None and len(m.groups()) == 1):
                try:
                    self.iopen(m.group(1))
                except FileError as fe:
                    self.oprint(fe.errmsg)

        def handle_embed(m, lineObj):
            """Handle an embed parse line"""
            if(m is not None and len(m.groups()) == 1):
                try:
                    embed_fn = m.group(1)
                    if not isfile(embed_fn):
                        raise FileError(1, "ERROR: Unable to embed \"{}\". File does not exist.<br />".format(embed_fn))

                    self.tls.fileTracker.seen = embed_fn

                    with open(embed_fn) as f:
                        self.oprint(f.read())
                except FileError as fe:
                    self.oprint(fe.errmsg)
                except IOError as e:
                    self.oprint(f"I/O error({e.errno}): {e.strerror}")
                except:
                    self.oprint(f"Unexpected error processing @embed file[{embed_fn}]:", exc_info()[0])

        def handle_break(m, lineObj):
            """Handle a break parse line"""
            self.oprint('<div class="extras"><h1></h1></div>')  #//TODO: Is this needed? Still being used in scripts, but is it really needed, or can we workaround it?
            pass    # don't do anything with @break or @exit

        def handle_stop(m, lineObj):
            """Handle a stop parse line"""
            self.stdinput.force_eof()

        def handle_raw(m, lineObj):
            """Handle a raw line"""
            from .core.utility import HtmlUtils
            if(m is not None):
                self.debug_smd_raw.print('&nbsp;&nbsp;lineObj.current_line=<br />'   \
                                         '{}<br />&nbsp;&nbsp;m.group(2)=<br />{}'
                                            .format(HtmlUtils.escape_html(lineObj.current_line),
                                                    HtmlUtils.escape_html(m.group(2)))
                )
                self.oprint(self._md.markdown(m.group(2)))
            else:
                self.oprint(lineObj.current_line)

        def handle_wrap(m, lineObj):
            """Handle a wrap line"""

            class wrapTag(object):
                def __init__(self,tags, ns_parseVariableNameInNamespace, markdown, oprint):
                    # add ability to push a null or nop onto the stack, to temporarily disable @wrap output
                    if tags.lower() in ['null', 'nop']:
                        self._start = self._end = ''
                        return

                    self._start = None
                    self._end = None
                    tag_names = []
                    html_ns = 'html'
                    ns_parseVariableNameInNamespace
                    from .core.utility import HtmlUtils
                    # in case they've listed multiples, split them at the ','
                    for tag in tags.split(','):
                        stripped_tag = tag.strip()
                        if not stripped_tag.startswith(f"{html_ns}."):
                            # if they didn't specify a namespace, force it to html. Even if they specified a valid NS, we don't care.
                            stripped_tag = f"{html_ns}." + stripped_tag

                        self._ns, self._name, self._attr = ns_parseVariableNameInNamespace(stripped_tag)
                        if self._ns != html_ns:
                            oprint(f"ERROR: @wrap tags must <em><strong>exist</strong></em> in the {html_ns} namespace. Tag: [<em>{HtmlUtils.escape_html(stripped_tag)}</em>]<br />")
                            return
                        if self._attr is not None:
                            oprint(f"WARNING: @wrap tags cannot specify an attribute. Tag: [<em>{HtmlUtils.escape_html(stripped_tag)}</em>]. Removed [{self._attr}].<br />")

                        tag_names.append(f"{html_ns}.{self._name}")
                    # we successively parsed all the tags, now let's build the start and end tag strings and save them.
                    self._start = ''
                    self._end = ''
                    # For the opening, do them in order, picking up tag.< for each
                    for tag in tag_names:
                        self._start += markdown(f"[{tag}.<]")
                    
                    # For the ending, do them in reverse order, picking up tag.> for each
                    for tag in tag_names[::-1]:
                        self._end += markdown(f"[{tag}.>]")

                @property
                def start(self):
                    return self._start

                @property
                def end(self):
                    return self._end


            from .core.utility import HtmlUtils
            if(m is not None):
                self.debug_smd_raw.print('&nbsp;&nbsp;lineObj.current_line=<br />'   \
                                         '{}<br />&nbsp;&nbsp;m.group(2)=<br />{}'
                                            .format(HtmlUtils.escape_html(lineObj.current_line),
                                                    HtmlUtils.escape_html(m.group(2)))
                )
                if( m.group(1) == 'wrap'):
                    # Parse the tag(s) and construct the object instance
                    tag = wrapTag(m.group(2), self._ns.parseVariableName, self._md.markdown, self.oprint)
                    if tag.start is not None and tag.end is not None:
                        # Append the new wrap tag to our stack
                        self.wrapper.append(tag)
                    else:
                        # This is a debug only message indicating the instance wasn't valid for some reason
                        self.debug_smd.print(f"WARNING: wrapTag object instance is not valid<br />")
                else:
                    # Don't pop off more items that were queued while this file was running
                    topOfWrapStack = self.stdinput.getWrapStackPositionOfCurrentFile()
                    if topOfWrapStack < 0: topOfWrapStack = 0

                    # handling the @parw (pop() top most stack item from wrapper queue)
                    if not hasattr(self, 'wrapper'):
                        raise AssertionError("No wrapper list is set in our instance")
                    elif not self.wrapper or len(self.wrapper) < topOfWrapStack:
                        # @parw invoked with empty stack
                        self.oprint('WARNING: wrapper stack is empty<br />')
                    elif len(self.wrapper) < topOfWrapStack:
                        # @parw invoked with empty stack in currently imported file
                        self.oprint('WARNING: wrapper stack is empty for this input stream<br />')
                    elif m.group(2) == '':
                        # @parw invoked with no parameters
                        if len(self.wrapper) > topOfWrapStack:
                            self.wrapper.pop()
                    else:
                        # parse the parms: [*|all|#]
                        parameter = m.group(2)
                        if parameter in ['*', 'all']:
                            # empty the stack
                            while self.wrapper and len(self.wrapper) > topOfWrapStack:
                                self.wrapper.pop()
                        elif parameter.isnumeric():
                            # pop specified number of items from stack
                            count = int(parameter)
                            while self.wrapper and count > 0 and len(self.wrapper) > topOfWrapStack:
                                #print(f"+++>{len(self.wrapper)} and {topOfWrapStack} and {len(self.wrapper) > topOfWrapStack}")
                                self.wrapper.pop()
                                count -= 1
                            if count != 0:
                                self.oprint(f'WARNING: only {int(parameter)-count} items found on the stack that can be cleared<br />')
                        else:
                            self.oprint(f'WARNING: unknown option <em>{parameter}</em> passed to @parw<br />')

            else:
                self.oprint(lineObj.current_line)

        def handle_debug(m, lineObj):
            """Handle a debug line"""

            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                if not d:
                    self.oprint("<br />Toggling Debug Mode<br />")
                    self.tlsDebugTracker.toggle('.')
                else:
                
                    for key in d:
                        if key not in ['on', 'off', 'enabled', 'toggle', 'tags']:
                            self.oprint("<br /><strong>Unknown debug key: <em>{}</em></strong>".format(key))
                        elif key == 'on':
                            self.tlsDebugTracker.on(d[key])
                        elif key == 'off':
                            self.tlsDebugTracker.off(d[key])
                        elif key == 'enabled':
                            self.tlsDebugTracker.enabled(d[key])
                        elif key == 'toggle':
                            self.tlsDebugTracker.toggle(d[key])
                        elif key == 'tags':
                            self.tlsDebugTracker.dumpTags()
                        
            else:
                self.oprint(lineObj.current_line)

        def handle_dump(m, lineObj):
            """Handle the dump parse line type."""
            # Check to see if the dump parameters are embedded in macro of some type.
            # If so, then rematch using the current_line instead of original_line
            if lineObj.original_line.strip() != lineObj.current_line:
                matcher = self._regex_main['dump'].match_regex()
                m = match(matcher, lineObj.current_line)

            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                self.oprint("<div class=\"variables\">")
                self.oprint("<code>")
                if not d:
                    self.tlsSysDefaults.dump(which=None, oprint=self.oprint)
                    self.tlsFileTracker.dump(which=None, oprint=self.oprint)
                    self._ns.dumpVars()
                else:
                    if 'sysdef' in d:
                        self.tlsSysDefaults.dump(d['sysdef'], self.oprint)
                        del d['sysdef']
                    
                    if 'tracked' in d:
                        self.tlsFileTracker.dump(d['tracked'], self.oprint)
                        del d['tracked']
                    
                    if d is not None:
                        self._ns.dumpNamespaces(d)
                self.oprint("</code>")
                self.oprint("</div>")
            else:
                self.oprint(lineObj.original_line)

        def handle_varv2(m, lineObj):
            """Handle the @var parse line type."""
            from .core.utility import HtmlUtils
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                self.debug_smd.print(HtmlUtils.escape_html(f"d={d}, {d.keys()}"))
                self._ns.addVariable(d, ns="var")

            else:
                self.oprint(lineObj.original_line)

        def handle_setv2(m, lineObj):
            """Handle the @set parse line type."""
            if(m is not None):
                d = {self._md.markdown(l[0]): l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                nskey = '_ns'
                namespace = '?'
                if nskey in d:
                    #self.oprint(f"dict-->{d}")
                    namespace = self._md.markdown(d[nskey])
                    del d[nskey]
                #self.oprint(f"namespace={namespace}")
                #//TODO: catch the exception here to prevent parser crash...
                self._ns.updateVariable(d, ns=namespace)

            else:
                self.oprint(lineObj.original_line)

        def handle_image(m, lineObj):
            """Handle the @image parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                self._ns.addVariable(d, ns="image")

            else:
                self.oprint(lineObj.original_line)

        def handle_link(m, lineObj):
            """Handle the @link parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                self._ns.addVariable(d, ns="link")

            else:
                self.oprint(lineObj.original_line)

        def handle_html(m, lineObj):
            """Handle the @html parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                self._ns.addVariable(d, ns="html")

            else:
                self.oprint(lineObj.original_line)

        def handle_code(m, lineObj):
            """Handle the @code parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                self.debug_smd_line.print('handle_code: {}'.format(d))
                self._ns.addVariable(d, ns="code")

            else:
                self.oprint(lineObj.original_line)

        # --------------------------------------------------------------------
        # This is the ENTRY point to the parse() method!
        rc = 0

        # A map linking line parse types to processor functions
        # IMPORTANT: The order of these is important in that all parse types that require
        # a RawLine must be checked first, or you risk something being evaluated in Markdown()
        # that should not be.
        parseTypes = [
            ('var', handle_varv2),
            ('set', handle_setv2),
            ('code', handle_code),
            ('link', handle_link),
            ('html', handle_html),
            ('image', handle_image),
            ('break', handle_break),
            ('stop', handle_stop),
            ('debug', handle_debug),
            ('dump', handle_dump),
            ('raw', handle_raw),
            ('wrap', handle_wrap),
            ('header', handle_header),
            ('import', handle_import),
            ('embed', handle_embed),
            ('watch', handle_watch),
        ]
        
        try:
            # Read the file until EOF and parse each line
            while(self._readNextLine() != ''):
                # For each parse type
                matched = False
                for key, parse_func in parseTypes:
                    parse_obj = self._regex_main[key]
                    if(testLine(parse_obj, self._line)):
                        m = matchLine(parse_obj, self._line)
                        if m is None:
                            # This is because we detected a valid keyword tag, but there is some type of 
                            # syntax or parsing issue. Just break and let it be printed ...
                            break
                        #TODO: Should we HTMLESC what we're printing here?
                        self.debug_smd_line.print('Match <strong>{}=<em>{}</em></strong>'.format(m[0],self._line._oriLine))
                        parse_func(m, self._line)
                        matched = True
                        break

                # if no parse type was matched, then just write it out
                if not matched and self._line.current_line.rstrip() and not self._reprocessLine():
                    # If the line has a class prefix, then write it out inside a span
                    span = f'<span{self._line.css_prefix}>{{}}</span>' if self._line.css_prefix else '{}'
                    formatted_line = span.format(self._line.current_line)
                    # if we have a wrapper tag in play
                    if self.wrapper:
                        tag = self.wrapper[-1]
                        self.oprint(f'{tag.start}{formatted_line}{tag.end}')
                    else:
                        self.oprint(formatted_line)

            from .core.config import ConfigFile, SpecificConfigFile
            closing = []

            from pathlib import Path
            if self.tlsSysDefaults.bodyclose_name:
                # if -bodyclose filename.md specified on command line, it always wins
                if not Path(self.tlsSysDefaults.bodyclose_name).is_file():
                    closing += [f"ERROR: Filename {self.tlsSysDefaults.bodyclose_name} does not exist!"]
                else:
                    closing += SpecificConfigFile(self.tlsSysDefaults.bodyclose_name, self.tlsSysDefaults.load_default_body).data()
            else:
                closing += ConfigFile(SystemDefaults.DefaultBodyCloseName, self.tlsSysDefaults.load_default_body).data()

            if self.tlsSysDefaults.close_name:
                # if -close filename.md specified on command line, it always wins
                if not Path(self.tlsSysDefaults.close_name).is_file():
                    closing += [f"ERROR: Filename {self.tlsSysDefaults.close_name} does not exist!"]
                else:
                    closing += SpecificConfigFile(self.tlsSysDefaults.close_name, self.tlsSysDefaults.load_default_html).data()
            else:
                closing += ConfigFile(SystemDefaults.DefaultHtmlCloseName, self.tlsSysDefaults.load_default_html).data()

            for c in closing:
                if self.tlsRawOutputFile is not None:
                    self.tlsRawOutputFile.write(c)
                c = c.strip()
                if c is None: continue
                self.oprint(self._md.markdown(c))

            # Need to close it so it's available to view if a consumer doesn't delete the TLS right away...
            # Ultimately might want the caller to decide when to close, but for now, this works for what I need.
            self.tlsRawOutputFileDeinit()

        except RegexError as regex_error:
            self.oprint("{}".format(regex_error.errmsg))
            rc = 3
        
        return rc
    
    def open_and_parse(self, script=None):
        """Open a Script Markdown file in text format and emit HTML code.

        Arguments:
        script -- the script to parse or None to parse sys.stdin
        """
        # Ok, open the specified file (or sys.stdin if avscript is None)
        try:
            if(script is not None):
                # If the file doesn't exist, bail now.
                if not isfile(script):
                    return 1

            self.iopen(script)

        except IOError:
            return 2

        # Set the flags saying whether we started with stdin or a file
        self.isetio(True if script is None else False)
        return self.parse()

def smd_add_std_cmd_line_parms(parser, sysDefaults, args=None):
    group0 = parser.add_mutually_exclusive_group()
    group0.add_argument('-ldb', '--load-default-builtins', dest='load_default_builtins', action='store_true', help=f'load default builtins during startup. Default is: {sysDefaults.load_default_builtins}')
    group0.add_argument('-ndb', '--no-default-builtins', dest='load_default_builtins', action='store_false', help=f'do not load default builtins during startup. Default is: {not sysDefaults.load_default_builtins}')

    # 'user builtins', 'flags controlling the user specific builtins.md file'
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('-lub', '--load-user-builtins', dest='load_user_builtins', action='store_true', help=f'load user builtins during startup. Default is: {sysDefaults.load_user_builtins}')
    group1.add_argument('-nub', '--no-user-builtins', dest='load_user_builtins', action='store_false', help=f'do not load user builtins during startup. Default is: {not sysDefaults.load_user_builtins}')

    # These flags control whether the HTML Document defaults are loaded during initialization.
    parser.add_argument('-nd', '--no-document-defaults', dest='load_document_defaults', action='store_false', help=f'do not load any document defaults during startup. Default is: {False}')
    parser.add_argument('-nohtml', '--no-default-html', dest='load_default_html', action='store_false', help=f'do not load default html during startup. Default is: {not sysDefaults.load_default_html}')
    parser.add_argument('-nohead', '--no-default-head', dest='load_default_head', action='store_false', help=f'do not load default head during startup. Default is: {not sysDefaults.load_default_head}')
    parser.add_argument('-nobody', '--no-default-body', dest='load_default_body', action='store_false', help=f'do not load default body during startup. Default is: {not sysDefaults.load_default_body}')

    parser.add_argument('-html', '--set-html-name', dest='html_name', help=f'set filename of document html markdown. Default is: {sysDefaults.html_name}')
    parser.add_argument('-head', '--set-head-name', dest='head_name', help=f'set filename of document head markdown. Default is: {sysDefaults.head_name}')
    parser.add_argument('-body', '--set-body-name', dest='body_name', help=f'set filename of document body markdown. Default is: {sysDefaults.body_name}')
    parser.add_argument('-bodyclose', '--set-bodyclose-name', dest='bodyclose_name', help=f'set filename of document body close markdown. Default is: {sysDefaults.bodyclose_name}')
    parser.add_argument('-close', '--set-close-name', dest='close_name', help=f'set filename of document close markdown. Default is: {sysDefaults.close_name}')

    # No user files means disallow searching ~/.smd/import for any of the default markdown files
    parser.add_argument('-nu', '--no-user-files', dest='load_user_files', action='store_false', help=f'do not load any files from ~/.smd. Default is: {not sysDefaults.load_user_files}')

    parser.add_argument('-o', '--output-raw-data', dest="raw_output_file", nargs='?', const='smd_rawdata.out', help=f'write the raw data to output file. Default is: {sysDefaults.raw_output_file}')

    # okay, set the defaults in the parser to the systemDefaults
    parser.set_defaults(load_default_builtins=sysDefaults.load_default_builtins)
    parser.set_defaults(load_user_builtins=sysDefaults.load_user_builtins)
    parser.set_defaults(load_default_html=sysDefaults.load_default_html)
    parser.set_defaults(load_default_head=sysDefaults.load_default_head)
    parser.set_defaults(load_default_body=sysDefaults.load_default_body)
    parser.set_defaults(load_user_files=sysDefaults.load_user_files)
    parser.set_defaults(raw_output_file=sysDefaults.raw_output_file)
    parser.set_defaults(html_name=sysDefaults.html_name)
    parser.set_defaults(head_name=sysDefaults.head_name)
    parser.set_defaults(body_name=sysDefaults.body_name)
    parser.set_defaults(bodyclose_name=sysDefaults.bodyclose_name)
    parser.set_defaults(close_name=sysDefaults.close_name)

    # parse the arguments
    args = parser.parse_args(args)

    # transfer the argument values from the args over to the systemDefaults object
    sysDefaults.load_default_builtins = args.load_default_builtins
    sysDefaults.load_user_builtins = args.load_user_builtins
    sysDefaults.raw_output_file = args.raw_output_file
    sysDefaults.html_name = args.html_name
    sysDefaults.head_name = args.head_name
    sysDefaults.body_name = args.body_name
    sysDefaults.bodyclose_name = args.bodyclose_name
    sysDefaults.close_name = args.close_name

    # if -nd is specified, then no matter what, all document files will be ignored
    sysDefaults.load_default_html = args.load_default_html if args.load_document_defaults else False
    sysDefaults.load_default_head = args.load_default_head if args.load_document_defaults else False
    sysDefaults.load_default_body = args.load_default_body if args.load_document_defaults else False

    # if -nu is specified, then the LocalUserConfigFile class will ignore allowing them to override the system versions
    sysDefaults.load_user_files = args.load_user_files

    # a few last minute checks to avoid potential confusion
    if sysDefaults.load_default_html is False and (sysDefaults.html_name or sysDefaults.close_name):
        parser.error("you can't say -nohtml and then specify -html or -close")

    if sysDefaults.load_default_body is False and (sysDefaults.body_name or sysDefaults.bodyclose_name):
        parser.error("you can't say -nobody and then specify -body or -bodyclose")

    if sysDefaults.load_default_head is False and sysDefaults.head_name:
        parser.error("you can't say -nohead and then specify -head")

    return args

def smd_parse_file(args=None):
    """Parse specified input file as Script Markdown text file.

    if args is None, uses sys.argv - via argparse
    if no filename is specified, parses sys.stdin

    Exit code:
        0 -- Success
        1 -- File not found
        2 -- IO Error processing input file
        3 -- Invalid regex ID in main loop
    """
    from argparse import ArgumentParser

    sysDefaults = SystemDefaults()

    parser = ArgumentParser(description='Parse Script Markdown text files into HTML format.',
                            epilog=".")
    parser.add_argument('-f', '--filename', help='the file that you want to parse. Default is stdin if not specified')

    args = smd_add_std_cmd_line_parms(parser, sysDefaults, args)

    if args.filename and not isfile(args.filename):
        return 1

    return ScriptParser(sysDefaults).open_and_parse(args.filename)


if __name__ == '__main__':
    exit(smd_parse_file())
