#!/usr/bin/env python

import sys
import os
import re

"""
This script is a BBEdit-compliant Markup Previewer (if that's a thing)... When
invoked from BBEdit, it reads from sys.stdin, which will be the current contents
of the markdown document you are editing, formats it on the fly, writing out
HTML. Using BBEdit's Preview in BBEdit Markup support, you can see your AV
script come to life.

To quickly see how it works, copy "avscript_md.py" and "avscript_md.css":

cp avscript_md.py ~/Library/Application\sSupport\BBEdit\Preview\sFilters
cp avscript_md.css ~/Library/Application\sSupport\BBEdit\Preview\sCSS

And then open "example.md" in BBEdit, Choose Markup|Preview in BBEdit, and then
in the Preview: example.md window:

Select "avscript_md.css" from the CSS: popdown
Select "avscript_md.py" from the Filter: popdown

BAM! You should see a nicely formatted Audio/Visual script. You'll likely see
error near the top about "Unable to import /.../heading.md". Don't worry, we'll
fix that later.

For now, take a look at userdocs.md (in a BBEdit preview window of course!), and
you should quickly get up and running with the A/V Script Markdown Processor.

Future - aka Wish List
0. Image (both inline and reference-style) would be nice too.


TODO (Punch list):
4. Finish the documentation for this thing
5. Test with Python2 and Python3
6. Make it pass flake8 (mostly)

a. Search for TODO and fix/cleanup
b. Improve markdown parsing to take advantage of group(0) like links does???

CSS Clean Up
1. Reorganize, make consistent.
2. Make it pass lint
3. Add more useful styles
4. Create multiple versions: All, Visuals and Narration only, User Guide
5. Ability to pass requested version to mkavscript_md

"""


class C_fileObj(object):
    """A simple file class to keep track if we need to issue a close on a file."""
    def __init__(self, f, closeOnEOF=True, name=None):
        self.file = f
        self.closeOnEOF = closeOnEOF
        self.name = name


class C_file_handler(object):
    """This class abstracts the readline() built-in API so it can support
    having multiple files open, ala the @import keyword. When a new file
    is opened, the current file object is saved on a stack, and the file
    becomes the current file until EOF. At that point, it's closed, and
    the previous file is then popped off the stack, and we resume reading
    from it until EOF."""
    def __init__(self):
        self.filestack = []
        self.idx = -1
        self.line = ''

    def _open(self, filename):
        """Open a file. Initially, sys.stdin might be passed, indicating
        that we should be reading from stdin. If that's the case, add it
        to the stack, but signal that it should not be closed, since that
        file is handled by the built-in Python library.

        TODO: Should sys.stdin only be allowed at the start?"""

        # If name is prefixed with '$', it means we need to prefix the
        # filename with the path of the current file being read...

        if(filename[0] == '$'):
            # Make sure this isn't the first file we are opening, and also
            # that the current file isn't stdin!
            if(self.idx >= 0 and self.filestack[self.idx].name):
                # print("abs-->{0}<br />".format(self.filestack[self.idx].name))
                filename = os.path.join(os.path.split(os.path.abspath(self.filestack[self.idx].name))[0], filename[1:])

        if(filename == 'sys.stdin'):
            self.filestack.append(C_fileObj(sys.stdin, False))
            self.idx += 1

        elif os.path.isfile(filename):

            name = os.path.abspath(filename)
            file = open(filename, "r")
            self.filestack.append(C_fileObj(file, True, name))
            self.idx += 1

            return 0
        else:
            print("ERROR: Unable to import '{0}'. File does not exist.".format(filename))

        return 1

    def _readline(self):
        """Read the next line of input and return it. If we are at EOF and
        there's a file object on the stack, close the current file and then
        pop the prior off the stack and return the next line from it."""
        self.line = self.filestack[self.idx].file.readline()
        if(self.line == ''):
            if(len(self.filestack)):
                f = self.filestack.pop()
                if (f.closeOnEOF):
                    f.file.close()
                self.idx -= 1

                if (self.idx >= 0):
                    return self._readline()

        return self.line


class C_VarObject(object):
    """Class to abstract a variable (alias). Keep track of the ID (name) and
    the value (text)."""
    def __init__(self, id, text):
        self.id = id
        self.text = text


class C_Variables(object):
    """Class to abstract a dictionary of variables (aliases)"""
    def __init__(self):
        self.vars = {}

    def addVar(self, id, text):
        """Add a variable called 'id' to the list and set its value to 'text'."""
        self.vars[id] = C_VarObject(id, text)

    def exists(self, id):
        """Returns true if the variable 'id' exists."""
        return id in self.vars

    def getText(self, id):
        """Gets the value of the variable 'id', unless it doesn't exist, in
        which case it returns (undefined).

        TODO: Should this just return an empty string if undefined?"""
        return "(undefined)" if not self.exists(id) else self.vars[id].text

    def dumpVars(self, indent=''):
        """Dumps the variable list, names and values."""
        for var in self.vars:
            print("{2}{0}:{1}<br />".format(self.vars[var].id, self.vars[var].text, indent))


class C_LinkObject(object):
    """Class to abstract a reference link. Keep track of the URL (url) and
    the optional title (title). We don't track the name here, that is done
    in the C_Links class."""
    def __init__(self, url, title=None):
        self.url = url
        self.title = title


class C_Links(object):
    """Class to abstract a dictionary of reference links"""
    def __init__(self):
        self.links = {}

    def addLink(self, id, url, title=None):
        """Add a link called 'id' to the list and set its url to 'url'
        and its title to 'title'."""
        # print("addLink()-->{0}-{1}-{2}<br />".format(id,url,title))
        self.links[id] = C_LinkObject(url, title)

    def exists(self, id):
        """Returns true if the link named 'id' exists."""
        return id in self.links

    def getLinkUrl(self, id):
        """Gets the link object named 'id', unless it doesn't exist, in
        which case it returns 'id'."""
        if(self.exists(id)):
            return self.links[id].url

        # This seems best to just return what we were given. If it doesn't
        # expand, it should be obvious, right?
        return id

    def getLinkMarkup(self, id, altText=None):
        """Returns the HTML markup for the link named 'id' if it exists.
        Otherwise, return an empty string. If altText is passed, wrap that with
        the link markup, otherwise, just wrap the 'id'."""
        title = "" if not self.exists(id) or not self.links[id].title else " title=\"{0}\"".format(self.links[id].title)
        linkText = "{0}".format(altText if altText else id)

        return '<a href=\"{0}\"{2}>{1}</a>'.format(self.getLinkUrl(id), linkText, title)

    def dumpLinks(self, indent=''):
        """Dumps the links list, names, urls and titles."""
        for link in self.links:
            print("{3}{0}:{1}:{2}<br />".format(link, self.links[link].url, self.links[link].title, indent))


class C_AnchorQueue(object):
    def __init__(self):
        self.anchorQ = []
        self.linkIDnum = 0

    def addAnchorUsingID(self, id, link):
        curItem = len(self.anchorQ)
        self.anchorQ.append((id, link))
        self.linkIDnum += 1
        return self.anchorQ[curItem][0]

    def addAnchor(self, link):
        return self.addAnchorUsingID("fnref:{0}".format(self.linkIDnum), link)
        #
        curItem = len(self.anchorQ)
        self.anchorQ.append(("fnref:{0}".format(self.linkIDnum), link))
        self.linkIDnum += 1
        return self.anchorQ[curItem][0]

    def getAnchorQ(self):
        return self.anchorQ

    def dumpAnchors(self):
        for anchor in self.anchorQ:
            print("{0}-{1}".format(anchor, self.anchorQ[anchor][1]))


class C_regex_md(object):
    """
    This class is used to hold the regular expressions that are used when
    applying markdown to inline formatting codes. A global variable is
    used to create a list of these objects, so we can precompile the expressions
    since they are used over and over throughout the script.
    """
    def __init__(self, regex, ori_repl_str, new_repl_str, flags=0):
        self.regex = re.compile(regex, flags)
        self.ori_str = ori_repl_str
        self.new_str = new_repl_str


class C_regex_main(object):
    """
    starts_new_div - signals whether this regex will stop the peekplaintext() from processing new lines
    uses_raw_line - signals whether this regex should process the raw line or the marked_down line
    allows_class_prefix - signals whether this regex can be prefixed with a class override
    test_str - this is the regex string used to detect if the line is a match
    match_str - this is the regex string used when parsing the line into groups. If None, uses test_str
    """
    def __init__(self, starts_new_div, uses_raw_line, allows_class_prefix, test, match):
        self.test_str = re.compile(test)
        self.match_str = None if not match else re.compile(match)
        self.starts_new_div = starts_new_div
        self.uses_raw_line = uses_raw_line
        self.allows_class_prefix = allows_class_prefix

    def test_regex(self):
        return self.test_str

    def match_regex(self):
        return self.match_str if self.match_str else self.test_str


class C_AVScriptParser(object):
    def __init__(self):
        """The constructor for the class. Initialize the required member
        variables:

        """
        self.line = None                # the current line "marked down"
        self.ori_line = None            # the current line as it was read in
        self.fmtlevel = 0               # indentation level for HTML tags
        self.lineInCache = False        # if we have a line in the cache
        self.classInCache = False       # if we have a class in the cache
        self.av = C_file_handler()
        self.shotListQ = C_AnchorQueue()  # shot list link Q

        self.links = C_Links()          # dict of links
        self.variables = C_Variables()  # dict of document variables

        self.regex_main = {
            #                   NewDiv RawLine Prefix   Test Regex                                        Match Regex
            'shot': C_regex_main(True, False, True, r'^[-|\*|\+][ ]*(?![-]{2})', r'^[-|\*|\+][ ]*(?![-]{2})(.*)'),
            'div': C_regex_main(True, False, True, r'^[-@]{3}[ ]*([^\s]+)[ ]*([\w\.]+)?[ ]*', r'^[-@]{3}[ ]*([^\s]+)[ ]*([\w\.]+)?[ ]*(.*)'),
            'h#': C_regex_main(True, False, True, r'^([#]{1,6})[ ]*', r'^([#]{1,6})[ ]*(.*)'),
            'links': C_regex_main(True, True, False, r'^\[([^\]]+)\]:\(?[ ]*([^\s|\)]*)[ ]*(\"(.+)\")?\)?', None),
            'alias': C_regex_main(True, True, False, r'^\[([^\]]+)\](?=([\=](.+)))', None),
            'import': C_regex_main(True, False, False, r'^[@]import[ ]+[\'|\"](.+[^\'|\"])[\'|\"]', None),
            'anchor': C_regex_main(True, True, False, r'^[@]\+\[([^\]]*)\]', None),
            'shotlist': C_regex_main(True, False, False, r'^[/]{3}Shotlist[/]{3}', None),
            'variables': C_regex_main(True, False, False, r'^[/]{3}Variables[/]{3}', None),
            'dumplinks': C_regex_main(True, False, False, r'^[/]{3}Links[/]{3}', None),
            'cover': C_regex_main(True, True, False, r'^[\$]{2}cover[\$]{2}:(.*)', r'^[\$]{2}cover[\$]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}'),
            'revision': C_regex_main(True, True, False, r'^[\$]{2}revision[\$]{2}:(.*)', r'^[\$]{2}revision[\$]{2}:[\<]{2}(.[^\>]*)[\>]{2}'),
            'contact': C_regex_main(True, True, False, r'^[\$]{2}contact[\$]{2}:(.*)', r'^[\$]{2}contact[\$]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}:[\<]{2}(\w*[^\>]*)[\>]{2}'),
        }

        self.regex_md_list = [
            # Next one is to match LINK & ALIAS substitutions, but NOT DEFs.
            C_regex_md(r'\[([^\]]+)\](?!(:(.+))|(\=(.+)))', '[{0}]', None),
            # TODO: Next one kind of complex. Do we need this?
            C_regex_md(r'<((?:http|ftp)s?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\[?[A-F0-9]*:[A-F0-9:]+\]?)(?::\d+)?(?:/?|[/?]\S+))>', '<{0}>', '<a href=\"{0}\">{0}</a>', re.IGNORECASE),
            C_regex_md(r'\*{2}(?!\*)(.+?)\*{2}', '**{0}**', '<strong>{0}</strong>'),
            C_regex_md(r'\*(.+?)\*', '*{0}*', '<em>{0}</em>'),
            C_regex_md(r'\+{2}(.+?)\+{2}', '++{0}++', '<ins>{0}</ins>'),
            C_regex_md(r'\~{2}(.+?)\~{2}', '~~{0}~~', '<del>{0}</del>')
        ]

    def _regex(self, id):
        if(id in self.regex_main):
            return self.regex_main[id]

        print("ERROR: Invalid regex ID: [{0}]".format(id))

        # TODO: Throw exception here
        return None

    def _unreadLine(self):
        """Mark the current line in the buffer as unread, so it will be returned next time."""
        self.lineInCache = True

    def markdown(self, s):
        """This method is used to apply markdown to the passed in string."""

        # TODO: nice if we could integrate this into main loop...
        # This handles inline links in this format: [linkID]:(url)
        # Might be able to fix if I can eliminate the extra group... linkID,(url),url
        spec = C_regex_md(r'(\[([^\]]+)\]:[ ]*\([ ]*([^\s|\)]*)[ ]*(\"(.+)\")?\))', '', '')

        # This special case handles inline links
        matches = re.findall(spec.regex, s)
        for m in matches:
            optTitle = '' if len(m) < 5 or not m[4] else " title=\"{0}\"".format(m[4])
            s = s.replace(m[0], '<a href=\"{0}\"{2}>{1}</a>'.format(m[2], m[1], optTitle))
            self.links.addLink(m[1], m[2], m[4])
            # print("MD:AL:{0}{1}{2}<br />".format(m[1],m[2],m[3]))

        # TODO: nice if this were also integrated into main loop...
        # This handles inline links to local anchors: @:[anchorID]<<text>>
        # This special case handles links to local anchors
        spec = C_regex_md(r'([@]\:\[([^\]]*)\]\<{2}([^\>{2}]*)\>{2})', '', '')

        matches = re.findall(spec.regex, s)
        for m in matches:
            s = s.replace(m[0], '<a href=\"#{0}\">{1}</a>'.format(m[1], m[2]))
            # print("MD:AA:{0}{1}{2}<br />".format(m[0],m[1],m[2]))

        for item in self.regex_md_list:
            matches = re.findall(item.regex, s)
            for m in matches:
                # if item.new_str is None, it means we have a link or a variable
                if item.new_str is None:
                    # If m[0] is an ID for a LINK, then replace apply the link URL to the text
                    if self.links.exists(m[0]):
                        s = s.replace(item.ori_str.format(m[0]), self.links.getLinkMarkup(m[0]))
                    elif self.variables.exists(m[0]):
                        # Get the variable value
                        varValue = self.variables.getText(m[0])
                        # See if there is a link ID by that name
                        if self.links.exists(varValue):
                            s = s.replace(item.ori_str.format(m[0]), self.links.getLinkMarkup(varValue, m[0]))
                        else:
                            s = s.replace(item.ori_str.format(m[0]), self.variables.getText(m[0]))
                    else:
                        pass    # TODO: should we do anything here?
                else:
                    # These are the simple search/replace expressions...
                    s = s.replace(item.ori_str.format(m), item.new_str.format(m))

        return s

    def _readNextLine(self):
        """Read the next line from the buffer, unless something is cached, in which case return that"""
        if(self.lineInCache):
            self.lineInCache = False    # reset the flag since we are returning it
            return self.line

        # read the next line from the file buffer
        while(1):
            self.ori_line = self.av._readline()
            if self.ori_line[0:2] != '//':
                break
            if self.ori_line[0:3] == '///':
                break

        # mark it down
        self.line = self.markdown(self.ori_line)
        # return the marked down version
        return self.line

    def _addLink(self, link):
        return self.fmt("<a id=\"{0}\"></a>\n".format(self.shotListQ.addAnchor(link)))

    def _makeCSSclass(self, tmpClass):
        # remove all extraneous spaces, then change '.' to ' ' then strip leading blanks
        s = tmpClass.replace(" ", "").replace(".", " ").strip()

        return " class=\"{0}\"".format(s)

    def _stripClass(self, line):
        """Strip the {:.class} prefix off the line, and return the class formatted
           for use as an HTML class ATTR, along with the rest of the line. If no
           class is present, just return the line as-is."""
        if(re.match(r'\{:([\s]?.\w[^\}]*)\}(.*)', line)):
            regex = r'\{:([\s]?.\w[^\}]*)\}(.*)'
            m = re.match(regex, line)

            if(m is not None and len(m.groups()) == 2):
                # format it like this: " class=cls1"
                return self._makeCSSclass(m.group(1)), m.group(2)

        # no class found, so return '' and the line, as-is
        return '', line

    def _peekNextLine(self, element="p", addLinks=False):
        """Read the next line, and if it's got white space at the beginning, then add it to the
           current line as a new <p> or whatever 'element' is. Then keep looking, in case there
           are more indented lines. This allows us to have multiple lines for DIVs that are section
           headers, and it's also used to gather multiple shots when we are processing an AV DIV."""
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF, return ''

        if re.match('[ \t]', self.line):
            # line was indented, strip any leading space, and then indent it at current level
            self.line = self.line.strip()
            # TODO: Remove This--> indentSp = " " * self.fmtlevel*4
            #
            cssClass, rest = self._stripClass(self.line)
            # get the link anchor and insert it ahead of the shot
            link = "" if not addLinks else self._addLink(rest)
            # return this, but call myself recursively in case there are more indented lines...
            return self.fmt("{3}<{0}{2}>{1}</{0}>\n".format(element, rest.rstrip('\n'), cssClass, link) + self._peekNextLine(element, addLinks))

        # We read 1 too many lines, so mark the cache as dirty so we can process it next time.
        self._unreadLine()
        return ""

    def _peekPlainText(self, element="p"):
        """Gobble up all the normal lines after one or more shot descriptions. "Normal"
           lines are the voiceover or narration that goes along with each shot. It's
           common that there are more "lines" than shots, so we want to read them all,
           and place them within the same DIV section. Each of these narrative lines
           can have it's own class override...
        """
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF return ''

        # This internal API detects if the next line is some type of BREAK.
        # e.g. a section, new shot, heading or link...

        def isNewSection(line, ori_line):
            # Look to see if the current line in the cache is the start of a new section

            for id in self.regex_main:
                obj = self._regex(id)
                # Make sure that this regex obj starts_new_div.
                if(not obj.starts_new_div):
                    continue
                # if this RE allows a class prefix, use the line with the
                # prefix stripped off, otherwise, use the original line.
                if re.match(obj.test_str, line if obj.allows_class_prefix else ori_line):
                    return True

            return False

        # Strip class, check the raw line to see if we should break
        tCls, tRst = self._stripClass(self.ori_line.strip())

        # if the RAW line is empty or if it's not a new section,
        #   keep it and peek at next line
        if not tRst or not isNewSection(tRst, self.ori_line.strip()):
            # TODO: Remote this --> indentSp = " " * self.fmtlevel * 4
            tmpClass, rest = self._stripClass(self.line.strip())
            # add this line to the current DIV, and keep reading until we hit some
            # type of break element...
            return self.fmt("<{0}{2}>{1}</{0}>\n".format(element, rest, tmpClass) + self._peekPlainText(element))

        # read one too many lines, so cache the current line for the next time around...
        self._unreadLine()
        return ""

    def fmt_getIndent(self, after=True):
        """Create a string of blanks for printing at the start of a line in order
        to keep things lined up properly."""
        howmany = self.fmtlevel if after else self.fmtlevel - 1
        return " " * (howmany * 4)

    def fmt(self, str, in_out_same=0, after=True):
        """Prefix the string passed in so it will align properly in the HTML file
           for keeping things in pretty print format."""
        s = self.fmt_getIndent(after)

        # in_out_same = 1, increase indent for next time
        # in_out_same = -1, decrease indent for next time
        # if 0, leave indent alone

        if(in_out_same > 0):
            self.fmtlevel += 1
        elif(in_out_same < 0):
            self.fmtlevel -= 1

        return "{0}{1}".format(s, str)

    def printInExtrasDiv(self, str):
        """Print the passed in string inside of a DIV with ID="extras". This allows
           orphaned elements to be kept out of the shot/narrative sections, where
           floats are active."""
        print(self.fmt("<div id=\"extras\">", 1))
        print(self.fmt(str, -1))
        print(self.fmt("</div>"))

    def parse(self):
        def testLine(regex_obj, line_obj):
            line = line_obj.curLine if not regex_obj.uses_raw_line else line_obj.oriLine
            return re.match(regex_obj.test_regex(), line)

        def matchLine(regex_obj, line_obj):
            line = line_obj.curLine if not regex_obj.uses_raw_line else line_obj.oriLine
            return re.match(regex_obj.match_regex(), line)

        print(self.fmt("<div id=\"wrapper\">", 1))
        while(self._readNextLine() != ''):
            # DOC this entire method better...
            # Start by stripping any class override from the beginning of the line
            cssClass, curLine = self._stripClass(self.line)

            # TODO: would this (a line class) be better to help doc code below?
            class C_LineObj:
                def __init__(self, curLine, oriLine):
                    self.curLine = curLine
                    self.oriLine = oriLine

            lineObj = C_LineObj(curLine, self.ori_line)

            if (testLine(self._regex('shot'), lineObj)):
                m = matchLine(self._regex('shot'), lineObj)

                if(m is not None):
                    li = "" if len(m.groups()) < 1 else "%s" % m.group(1)
                    divstr = self.fmt("<div id=\"av\">\n", 1)
                    divstr += self.fmt("<ul>\n", 1)
                    divstr += self._addLink(li)
                    divstr += self.fmt("<li{1}>{0}</li>\n".format(li, cssClass))
                    divstr += self._peekNextLine("li", True)
                    divstr += self.fmt("</ul>\n", -1, False)
                    divstr += self._peekPlainText()
                    divstr += self.fmt("</div>", -1, False)
                    print(divstr)
                else:
                    print(curLine)

            elif(testLine(self._regex('div'), lineObj)):
                m = matchLine(self._regex('div'), lineObj)

                if(m is not None):
                    divID = "" if len(m.groups()) < 1 else " id=\"{0}\"{1}".format(m.group(1), cssClass)
                    divPcls = "" if len(m.groups()) < 2 or m.group(2) == "." else " class=\"%s\"" % m.group(2)
                    divText = "" if len(m.groups()) < 3 else "%s\n" % m.group(3)
                    divstr = self.fmt("<div%s>\n" % divID, 1)
                    divstr += self.fmt("<p%s>%s</p>\n" % (divPcls, divText.rstrip('\n')))
                    divstr += self._peekNextLine()
                    divstr += self.fmt("</div>", -1, False)

                    print(divstr)

                else:
                    print(curLine)

            elif(testLine(self._regex('h#'), lineObj)):
                m = matchLine(self._regex('h#'), lineObj)

                if(m is not None and len(m.groups()) > 1):
                    hnum = len(m.group(1))
                    self.printInExtrasDiv("<h{0}{2}>{1}</h{0}>".format(hnum, m.group(2).strip(), cssClass))
                else:
                    print(curLine)

            elif(testLine(self._regex('import'), lineObj)):
                m = matchLine(self._regex('import'), lineObj)
                if(m is not None and len(m.groups()) == 1):
                    self.av._open(m.group(1))

                # TODO: Need to handle error here and print if we cannot open the file, etc.

            elif(testLine(self._regex('shotlist'), lineObj)):
                print(self.fmt("<div class=\"shotlist\">", 1))
                print(self.fmt("<hr />"))
                shotnum = 1
                for shot in self.shotListQ.getAnchorQ():
                    print(self.fmt("<div id=\"shot\">", 1))
                    print(self.fmt("<p>{1}&#160;<a class=\"shotlist-backref\" href=\"#{0}\" rev=\"shotlist\" title=\"Jump back to shot {2} in the script\">&#8617;</a></p>".format(shot[0], shot[1], shotnum), -1))
                    print(self.fmt("</div>"))
                    shotnum += 1

                print(self.fmt("</div>", -1, False))

            elif(testLine(self._regex('variables'), lineObj)):
                print(self.fmt("<div class=\"variables\">", 1))
                print(self.fmt("<hr />"))
                self.variables.dumpVars(self.fmt_getIndent())
                print(self.fmt("</div>", -1, False))

            elif(testLine(self._regex('dumplinks'), lineObj)):
                print(self.fmt("<div class=\"links\">", 1))
                print(self.fmt("<hr />"))
                self.links.dumpLinks(self.fmt_getIndent())
                print(self.fmt("</div>", -1, False))

            # links handles the various formats that allow a title to be specified.
            # [linkID]:url "title"
            # [linkID]:(url "title")
            # [linkID]:url
            # [linkID]:(url)
            # This has precedence over the [var]:[value], so we process it first
            elif(testLine(self._regex('links'), lineObj)):
                m = matchLine(self._regex('links'), lineObj)

                optTitle = '' if len(m.groups()) < 4 or not m.group(4) else m.group(4)

                # TODO: Should we markdown the Link Text?? m.group(1)?
                if(m is not None and len(m.groups()) == 4):
                    self.links.addLink(m.group(1), m.group(2), optTitle)
                    # print("RL:AL:{0}{1}{2}<br />".format(m.group(1),m.group(2),m.group(3)))
                else:
                    print(self.ori_line)

            elif(testLine(self._regex('alias'), lineObj)):
                m = matchLine(self._regex('alias'), lineObj)

                # TODO: Should we markdown the Link Text?? m.group(1)?
                if(m is not None and len(m.groups()) == 3):
                    self.variables.addVar(m.group(1), m.group(3))
                else:
                    print(self.ori_line)

            elif(testLine(self._regex('anchor'), lineObj)):
                # For this case, we just need to drop an anchor.
                m = matchLine(self._regex('anchor'), lineObj)

                if(m is not None and len(m.groups()) == 1):
                    print(self.fmt("<a id=\"{0}\"></a>".format(m.group(1))))
                else:
                    print(self.ori_line)

            # These "special" keywords require that we use the original
            # raw line and not the markdown line in order to parse. Once
            # we parse out these special lines, we'll markdown the individual
            # groups before writing them...
            elif(testLine(self._regex('cover'), lineObj)):
                m = matchLine(self._regex('cover'), lineObj)

                if(m is not None):
                    title = "" if len(m.groups()) < 1 or not m.group(1) else self.markdown(m.group(1))
                    author = "" if len(m.groups()) < 2 or not m.group(2) else self.markdown(m.group(2))
                    summary = "" if len(m.groups()) < 3 or not m.group(3) else self.markdown(m.group(3))

                    divstr = self.fmt("<div id=\"cover\">\n", 1)
                    if title:
                        divstr += self.fmt("<h3>%s</h3>\n" % title)
                    if author:
                        divstr += self.fmt("<p>%s</p>\n" % author)
                    if summary:
                        divstr += self.fmt("<p class=\"coverSummary\">%s</p>\n" % summary.rstrip())
                    divstr += self.fmt("</div>", -1, False)

                    print(divstr)
                else:
                    print(self.ori_line)

            elif(testLine(self._regex('revision'), lineObj)):
                m = matchLine(self._regex('revision'), lineObj)

                if(m is not None and len(m.groups()) == 1):
                    from time import strftime
                    revision = self.markdown(m.group(1))

                    divstr = self.fmt("<div id=\"revision\">\n", 1)
                    divstr += self.fmt("<p class=\"revTitle\">Revision: {0} ({1})</p>\n".format(revision.rstrip(), strftime("%Y%m%d @ %H:%M:%S")), -1)
                    divstr += self.fmt("</div>")

                    print(divstr)
                else:
                    print(self.ori_line)

            elif(testLine(self._regex('contact'), lineObj)):
                m = matchLine(self._regex('contact'), lineObj)

                if(m is not None):
                    cName = "" if len(m.groups()) < 1 or not m.group(1) else "{0}<br />".format(self.markdown(m.group(1)))
                    cPhone = "" if len(m.groups()) < 2 or not m.group(2) else "{0}<br />".format(self.markdown(m.group(2)))
                    cEmail = "" if len(m.groups()) < 3 or not m.group(3) else "{0}<br />".format(self.markdown(m.group(3)))
                    cLine1 = "" if len(m.groups()) < 4 or not m.group(4) else "{0}<br />".format(self.markdown(m.group(4)))
                    cLine2 = "" if len(m.groups()) < 5 or not m.group(5) else "{0}<br />".format(self.markdown(m.group(5)))
                    cLine3 = "" if len(m.groups()) < 6 or not m.group(6) else "{0}<br />".format(self.markdown(m.group(6)))

                    divstr = self.fmt("<div id=\"contact\">\n", 1)
                    divstr += self.fmt("<table>\n", 1)
                    divstr += self.fmt("<tr>\n", 1)
                    divstr += self.fmt("<td class=\"left\">{0}{1}{2}</td>\n".format(cLine1, cLine2, cLine3))
                    divstr += self.fmt("<td class=\"right\">{0}{1}{2}</td>\n".format(cName, cPhone, cEmail), -1)
                    divstr += self.fmt("</tr>\n", -1)
                    divstr += self.fmt("</table>\n", -1)
                    divstr += self.fmt("</div>")

                    print(divstr)
                else:
                    print(self.ori_line)

            else:
                if curLine.rstrip():
                    # TODO: we are orphaning things because of this... Why???
                    # self.printInExtrasDiv("<p>{0}</p>".format(curLine.rstrip()))
                    self.printInExtrasDiv("<p{1}>{0}</p>".format(curLine. rstrip(), cssClass))

        print(self.fmt("</div>", -1, False))

        return 0

    def load(self, avscript=None):
        """This method is used to open and initiate a parse on an AV format text file.
           If the scriptname is passed in, open it for reading, and invoke the parser.
           Otherwise, invoke the parser with the default input stream, which is stdin."""

        rc = 0

        # Ok, open the file and process each line we find in there.
        try:
            if(avscript is not None):
                # If the file doesn't exist, bail now.
                if not os.path.isfile(avscript):
                    return 1

                self.av._open(avscript)

                rc = self.parse()

                # close the file when we have processed all of it.
                # TODO: No longer needed, right? Handled by the C_file_handler() class
                # self.av.close()
            else:
                # no filename passed in, default to sys.stdin...
                self.av._open('sys.stdin')

                self.parse()

        except IOError:
            rc = 2

        return rc


if __name__ == '__main__':
    sys.exit(C_AVScriptParser().load(None if len(sys.argv) < 2 else sys.argv[1]))