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

To quickly see how it works, copy "avscript_md.py" and "avscript_md.css":

.. code-block:: rest

    cp avscript_md.py ~/Library/Application\sSupport\BBEdit\Preview\sFilters

.. note::

    Alternatively, create a symbolic link to these files in your

.. code-block:: rest

    ln -s /yourpathrepopath/avscript_md.py ~/Library/Application\sSupport\BBEdit\Preview\sFilters/avscript_md.py

And then open "docs/example.md" in BBEdit, Choose Markup|Preview in BBEdit,
and then in the Preview: example.md window:

For now, take a look at userdocs.md (in a BBEdit preview window of course!), and
you'll quickly get up and running with the A/V Script Markdown Processor.

Future - aka Wish List

"""

from re import IGNORECASE, findall, match
from sys import exit, exc_info, version_info
from os.path import isfile

MIN_PYTHON = (3, 7, 3)
if version_info < MIN_PYTHON:
    exit("Python %s.%s.%s or later is required.\n" % MIN_PYTHON)

from .core.line import Line
from .core.link import LinkDict
from .core.debug import DebugTracker, set_default_debug_register, Debug
from .core.regex import Regex, RegexMD, RegexMain
from .core.stdio import StdioWrapper
from .core.ftrack import FileTrack
from .core.sysdef import SystemDefaults
from .core.thread import initTLS, getTLS
from .core.variable import Namespaces
from .core.bookmark import BookmarkList
from .core.markdown import Markdown
from .core.constants import Constants
from .core.htmlformat import HTMLFormatter
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

        # Create the debug tracker object for this app
        self._dbgTracker = DebugTracker(output=self.oprint)
        set_default_debug_register(self._dbgTracker)

        # Register a tracker for this object
        self.debug_smd = Debug('smd')
        self.debug_smd_line = Debug('smd.line')
        self.debug_smd_raw = Debug('smd.raw')
        self.stdinput.initDebug()

        self._md = Markdown()           # New markdown support in separate class

        self._line = Line(md_func=self._md.markdown)
        self._html = HTMLFormatter()    # format HTML output (indent for readability)
        self._lineInCache = False       # if we have a line in the cache
        self._shotListQ = BookmarkList()    # shot list link Q

        self._ns = Namespaces(self._md.markdown, self._md.setNSxface, oprint=self.oprint)
        #TODO: Clean this up. _stripClass needs to be handled better than this...
        self._md.setStripClass(self._stripClass)

        # I think the reason I do the following has to do with the namespace used by exec & eval.
        # I need to figure out the reason though. //TODO: Need to verify this.

        #_set_ns_xface(ns_ptr)
        exec("from .core.utility import _set_ns_xface;_set_ns_xface(self._ns)")
        #_set_line_cache(self.stdinput.cache())
        exec("from .core.utility import _set_line_cache;_set_line_cache(self.stdinput.cache())")
        #_init_debug()
        exec("from .core.utility import _init_debug;_init_debug()")


        self._css_class_prefix = Regex(r'\{:([\s]?.\w[^\}]*)\}(.*)')
        self._special_parameter = Regex(r'\s([\w]+)\s*=\s*\"(.*?)(?<!\\)\"')

        # Dictionary of each line type that we can process
        self._regex_main = {
            # //TODO: Is NewDiv still needed?
            #                   NewDiv RawLine Prefix   Test Regex                                              Match Regex
            'header': RegexMain(True,   False,  True,   r'^([#]{1,6})[ ]*',                                  r'^([#]{1,6})[ ]*(.*)'),
            'import': RegexMain(True,   False,  False,  r'^[@]import[ ]+[\'|\"](.+[^\'|\"])[\'|\"]',         None),
            'embed': RegexMain(True,    False,  False,  r'^[@]embed[ ]+[\'|\"](.+[^\'|\"])[\'|\"]',          None),
            'var': RegexMain(True,      True,   False,  r'^(@var(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)',      None), 
            'set': RegexMain(True,      True,   False,  r'^(@set(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)',      None),
            'code': RegexMain(True,     True,   False,  r'^(@code(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)',     None), 
            'link': RegexMain(True,     True,   False,  r'^(@link(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)',     None), 
            'html': RegexMain(True,     True,   False,  r'^(@html(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)',     None), 
            'image': RegexMain(True,    True,   False,  r'^(@image(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")+)',    None),
            'dump': RegexMain(True,     True,   False,  r'^(@dump(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")*)',     None),
            'break': RegexMain(True,    True,   False,  r'^[@](break|exit)\s*$',                             None),
            'stop': RegexMain(True,     True,   False,  r'^[@](stop|quit)\s*$',                              None),
            'raw': RegexMain(True,      False,  False,  r'^@(@|raw)[ ]+(.*)',                                None),
            'debug': RegexMain(True,    True,   False,  r'^(@debug(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")*)',    None),
            'defaults': RegexMain(True, True,   False,  r'^(@defaults(\s*([\w]+)\s*=\s*\"(.*?)(?<!\\)\")*)', None),
        }

    @property
    def tls(self):
        return self._tls
    
    @tls.setter
    def tls(self, tls_object):
        self._tls = tls_object
    
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
        
        #//TODO: Should we trap this failure? What does it mean?
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
        return self._html.formatLine("<a id=\"{0}\"></a>\n".format(self._shotListQ.addBookmark(linktext)))

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
                self.oprint("<h{0}{2}>{1}</h{0}>".format(hnum, m.group(2).strip(), lineObj.css_prefix))
            else:
                self.oprint(lineObj.current_line)

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
                        raise FileError(1, "ERROR: Unable to embed '{}'. File does not exist.<br />".format(embed_fn))

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
            self.oprint('<div class="extras"><h1></h1></div>')  #//TODO: Is this needed?
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
                self.oprint(self._html.formatLine(self._md.markdown(m.group(2))))
            else:
                self.oprint(lineObj.current_line)

        def handle_defaults(m, lineObj):
            """Handle a defaults parse line"""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #//TODO: Maybe add a custom class for this?
                self.oprint(self._html.formatLine("<div class=\"variables\">", 1))
                self.oprint(self._html.formatLine("<code>", 1))
                if not d:
                    self._systemDefaults.dump(self.oprint)
                else:
                    # future: maybe add ability to dump specific things?
                    pass
                self.oprint(self._html.formatLine("</code>", -1, False))
                self.oprint(self._html.formatLine("</div>", -1, False))
            else:
                self.oprint(lineObj.original_line)

        def handle_debug(m, lineObj):
            """Handle a debug line"""

            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                if not d:
                    self.oprint("<br />Toggling Debug Mode<br />")
                    self._dbgTracker.toggle('.')
                else:
                
                    for key in d:
                        if key not in ['on', 'off', 'enabled', 'toggle', 'tags']:
                            self.oprint("<br /><strong>Unknown debug key: <em>{}</em></strong>".format(key))
                        elif key == 'on':
                            self._dbgTracker.on(d[key])
                        elif key == 'off':
                            self._dbgTracker.off(d[key])
                        elif key == 'enabled':
                            self._dbgTracker.enabled(d[key])
                        elif key == 'toggle':
                            self._dbgTracker.toggle(d[key])
                        elif key == 'tags':
                            self._dbgTracker.dumpTags()
                        
            else:
                self.oprint(lineObj.current_line)

        def handle_dump(m, lineObj):
            """Handle the dump parse line type."""
            if(m is not None):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                self.oprint(self._html.formatLine("<div class=\"variables\">", 1))
                self.oprint(self._html.formatLine("<code>", 1))
                if not d:
                    self._ns.dumpVars()
                else:
                    self._ns.dumpNamespaces(d)
                self.oprint(self._html.formatLine("</code>", -1, False))
                self.oprint(self._html.formatLine("</div>", -1, False))
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
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(m.groups()[0])}

                #TODO: This needs to have an option for "finding namespace"
                self._ns.updateVariable(d, ns="?")

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

                # TODO: What about self.oprint()? Doesn't that need to be passed to NS?
                self.debug_smd_line.print('handle_code: {}'.format(d))
                self._ns.addVariable(d, ns="code")

            else:
                self.oprint(lineObj.original_line)

        # --------------------------------------------------------------------
        # This is the ENTRY point to the parse() method!
        rc = 0

        # A map linking line parse types to processor functions
        parseTypes = [
            ('var', handle_varv2),
            ('set', handle_setv2),
            ('code', handle_code),
            ('link', handle_link),
            ('html', handle_html),
            ('header', handle_header),
            ('import', handle_import),
            ('embed', handle_embed),
            ('break', handle_break),
            ('image', handle_image),
            ('stop', handle_stop),
            ('debug', handle_debug),
            ('dump', handle_dump),
            ('defaults', handle_defaults),
            ('raw', handle_raw),        #//TODO: Is this needed still?
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
                        #TODO: Should we HTMLESC what we're printing here?
                        self.debug_smd_line.print('Match <strong>{}=<em>{}</em></strong>'.format(m[0],self._line._oriLine))
                        parse_func(m, self._line)
                        matched = True
                        break

                # if no parse type was matched, then just write it out
                if not matched and self._line.current_line.rstrip() and not self._reprocessLine():
                    # If the line has a class prefix, then write it out inside a span
                    span = f'<span{self._line.css_prefix}>{{}}</span>' if self._line.css_prefix else '{}'
                    self.oprint(span.format(self._line.current_line))

            from .core.config import ConfigFile
            closing = []
            closing += ConfigFile("import/def_bodyclose.md", self.tls.sysDefaults.load_default_body).data()
            closing += ConfigFile("import/def_close.md", self.tls.sysDefaults.load_default_html).data()
            for c in closing:
                self.oprint(self._html.formatLine(c, 0, False))
                if self.tlsRawOutputFile is not None:
                    self.tlsRawOutputFile.write(c)

            #//TODO: Do I need to track this better? 
            # Need to close it so it's available to view if a consumer doesn't delete the TLS right away...
            # Ultimately might want the caller to decide when to close, but for now, this works for what I need.
            self.tlsRawOutputFileDeinit()

            #//TODO: Remove this; it's for testing the file tracker.
            self.tls.fileTracker.dump()
            
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
    parser.add_argument('-ldb', '--load-default-builtins', dest='load_default_builtins', action='store_true', help=f'load default builtins during startup. Default is: {sysDefaults.load_default_builtins}')
    parser.add_argument('-ndb', '--no-default-builtins', dest='load_default_builtins', action='store_false', help=f'do not load default builtins during startup. Default is: {not sysDefaults.load_default_builtins}')
    parser.add_argument('-lub', '--load-user-builtins', dest='load_user_builtins', action='store_true', help=f'load user builtins during startup. Default is: {sysDefaults.load_user_builtins}')
    parser.add_argument('-nub', '--no-user-builtins', dest='load_user_builtins', action='store_false', help=f'do not load user builtins during startup. Default is: {not sysDefaults.load_user_builtins}')
    parser.add_argument('-html', '--load-default-html', dest='load_default_html', action='store_true', help=f'load default builtins during startup. Default is: {sysDefaults.load_default_html}')
    parser.add_argument('-nohtml', '--no-default-html', dest='load_default_html', action='store_false', help=f'do not load default builtins during startup. Default is: {not sysDefaults.load_default_html}')
    parser.add_argument('-head', '--load-default-head', dest='load_default_head', action='store_true', help=f'load default builtins during startup. Default is: {sysDefaults.load_default_head}')
    parser.add_argument('-nohead', '--no-default-head', dest='load_default_head', action='store_false', help=f'do not load default builtins during startup. Default is: {not sysDefaults.load_default_head}')
    parser.add_argument('-body', '--load-default-body', dest='load_default_body', action='store_true', help=f'load default builtins during startup. Default is: {sysDefaults.load_default_body}')
    parser.add_argument('-nobody', '--no-default-body', dest='load_default_body', action='store_false', help=f'do not load default builtins during startup. Default is: {not sysDefaults.load_default_body}')

    parser.add_argument('-nu', '--no-user-files', dest='load_user_files', action='store_false', help=f'do not load any files from ~/.smd. Default is: {not sysDefaults.load_user_files}')
    parser.add_argument('-nd', '--no-document-defaults', dest='load_document_defaults', action='store_false', help=f'do not load any document defaults during startup. Default is: {False}')

    parser.add_argument('-o', '--output-raw-data', dest="raw_output_file", nargs='?', const='smd_rawdata.out', help=f'write the raw data to output file. Default is: {sysDefaults.raw_output_file}')

    parser.set_defaults(load_default_builtins=sysDefaults.load_default_builtins)
    parser.set_defaults(load_user_builtins=sysDefaults.load_user_builtins)
    parser.set_defaults(load_default_html=sysDefaults.load_default_html)
    parser.set_defaults(load_default_head=sysDefaults.load_default_head)
    parser.set_defaults(load_default_body=sysDefaults.load_default_body)
    parser.set_defaults(load_user_files=sysDefaults.load_user_files)
    parser.set_defaults(raw_output_file=sysDefaults.raw_output_file)

    args = parser.parse_args(args)

    sysDefaults.load_default_builtins = args.load_default_builtins
    sysDefaults.load_user_builtins = args.load_user_builtins
    sysDefaults.raw_output_file = args.raw_output_file

    # if -nd is specified, then no matter what, all document files will be ignored
    sysDefaults.load_default_html = args.load_default_html if args.load_document_defaults else False
    sysDefaults.load_default_head = args.load_default_head if args.load_document_defaults else False
    sysDefaults.load_default_body = args.load_default_body if args.load_document_defaults else False

    # if -nu is specified, then the LocalUserConfigFile class will ignore allowing them to override the system versions
    sysDefaults.load_user_files = args.load_user_files

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

    return ScriptParser(sysDefaults).open_and_parse(args.filename)


if __name__ == '__main__':
    exit(smd_parse_file())
