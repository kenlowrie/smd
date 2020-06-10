#//TODO: Do I need this class?
class ConfigData(object):
    def __init__(self, okay2load):
        self.okay2load = okay2load
        self._data = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,data):
        self._data = data

    def datastack(self):
        return self.data[::-1]



#------------
        # //TODO: Should this be a namespace?
        def handle_shotlist(m, lineObj):
            # """Handle a shotlist parse line."""
            self.oprint(self._html.formatLine("<div class=\"shotlist\">", 1))
            self.oprint(self._html.formatLine("<hr />"))
            self.oprint(self._html.formatLine("<p>Shotlist</p>"))
            self.oprint(self._html.formatLine("<code>", 1))
            shotnum = 1
            for shot in self._shotListQ.getBookmarkList():
                self.oprint(self._html.formatLine("<div class=\"shot\">", 1))
                self.oprint(self._html.formatLine("<p>{1}&#160;"
                                                  "<a class=\"shotlist-backref\""
                                                     " href=\"#{0}\" rel=\"tag\""
                                                     " title=\"Jump back to shot {2} in the script\""
                                                  ">&#8617;</a></p>".format(shot[0], shot[1], shotnum), -1))
                self.oprint(self._html.formatLine("</div>"))
                shotnum += 1

            self.oprint(self._html.formatLine("</code>", -1, False))
            self.oprint(self._html.formatLine("</div>", -1, False))

        def handle_alias(m, lineObj):
            """Handle the alias parse line type"""
            if(m is not None and len(m.groups()) == 3):
                #self._variables.addVar(m.group(1), self._markdown(m.group(3)))
                #TODO: Should m.group(3) be self._md.markdown(m.group(3))?
                self._ns.addVariable(self._md.markdown(m.group(3)), name=m.group(1), ns="basic")
            else:
                self.oprint(lineObj.original_line)

#------------

        def handle_shot(m, lineObj):
            """Handle a shot parse line"""
            if(m is not None):
                li = "" if len(m.groups()) < 1 else "%s" % m.group(1)
                divstr = self._html.formatLine("<div class=\"av\">\n", 1)
                divstr += self._addBookmark(li)
                divstr += self._html.formatLine("<ul>\n", 1)
                divstr += self._html.formatLine("<li{1}>{0}</li>\n".format(li, lineObj.css_prefix))
                divstr += self._peekNextLine("li", True)
                divstr += self._html.formatLine("</ul>\n", -1, False)
                divstr += self._peekPlainText()
                divstr += self._html.formatLine("</div>", -1, False)
                self.oprint(divstr)
            else:
                self.oprint(lineObj.current_line)

        def handle_div(m, lineObj):
            """handle a DIV parse line"""
            if(m is not None):
                divClas = "" if not lineObj.css_prefix else lineObj.css_prefix
                divPcls = "" if len(m.groups()) < 1 or m.group(1) == "." else " class=\"%s\"" % m.group(1)
                divText = "" if len(m.groups()) < 2 else "%s\n" % m.group(2)
                divstr = self._html.formatLine("<div%s>\n" % divClas, 1)
                divstr += self._html.formatLine("<p%s>%s</p>\n" % (divPcls, divText.rstrip('\n')))
                divstr += self._peekNextLine()
                divstr += self._html.formatLine("</div>", -1, False)

                self.oprint(divstr)

            else:
                self.oprint(lineObj.current_line)


# ------------
    #def _printInExtrasDiv(self, str):
    #    """
    #    Print the string argument inside an HTML DIV Element with class="extras"
    #
    #    This allows orphaned elements to be kept out of the shot/narrative
    #    sections, where floats are active.
    #    """
    #    self.oprint(self._html.formatLine("<div class=\"extras\">", 1))
    #    self.oprint(self._html.formatLine(str, -1))
    #    self.oprint(self._html.formatLine("</div>"))



# ------------

    def _peekNextLine(self, element="p", addLinks=False):
        """
        Read next line, and if indented, add it as a new <element>

        If the next line has white space at the beginning, then add it to the
        current line as a new <p> or whatever 'element' is. Then keep looking,
        in case there are more indented lines. This allows us to have multiple
        lines for DIVs that are section headers, and it's also used to gather
        multiple shots when we are processing an AV DIV.
        """
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF, return ''

        # if line was indented, it's part of the previous element
        if self._line.was_indented:
            # get the link anchor and insert it ahead of the shot
            link = "" if not addLinks else self._addBookmark(self._line.current_line)
            # return this, but call myself recursively in case there are more indented lines...
            return self._html.formatLine("{3}<{0}{2}>{1}</{0}>\n".format(element, self._line.current_line.rstrip('\n'), self._line.css_prefix, link) + self._peekNextLine(element, addLinks))

        # We read 1 too many lines, so mark the cache as dirty so we can process it next time.
        self._unreadLine()
        return ""

    def _peekPlainText(self, element="p"):
        """
        Gobble up all the normal lines after one or more shot descriptions.

        "Normal" lines are the voiceover (VO) or narration that goes along with
        each shot. Usually, there are more "VO lines" than shots, so we want to
        read them all, and place them within the same DIV section. Each of these
        narrative lines can have it's own class override...
        """
        if (self._readNextLine() == ''):
            return ""   # if we hit EOF return ''

        # This internal API detects if the next line is some type of BREAK.
        # e.g. a section, new shot, heading or link...
        def isNewSection(lineObj):
            """Determines if the current line is the start of a new section.

            Arguments:
                lineObj -- a Line() instance

            Returns:
                True -- if the current line should start a new section
                False -- if the current line is part of the current section
            """
            # Look to see if the current line in the cache is the start of a new section

            for id in self._regex_main:
                obj = self._regex(id)
                # Make sure that this regex obj starts_new_div.
                if(not obj.starts_new_div):
                    continue
                # if this RE allows a class prefix, use the line with the
                # prefix stripped off, otherwise, use the original line.
                if match(obj.test_str.regex, lineObj.current_line if obj.allows_class_prefix else lineObj.original_line):
                    return True

            return False

        # if it's not a new section, keep it and peek at next line
        if not isNewSection(self._line):
            # add this line to the current DIV, and keep reading until we hit some
            # type of break element...
            if not self._line.css_prefix:
                # if there isn't a css_prefix inline, check to see if one was added
                # via markdown processing...
                new_prefix, new_line = self._stripClass(self._line.current_line)
                if new_prefix:
                    # if the markdown added a css prefix, then adjust the _line object
                    # so the css_prefix and current_line are updated before we format
                    # the element.
                    self._line.css_prefix = new_prefix
                    self._line.current_line = new_line

            return self._html.formatLine("<{0}{2}>{1}</{0}>\n".format(element, self._line.current_line, self._line.css_prefix) + self._peekPlainText(element))

        # read one too many lines, so cache the current line for the next time around...
        self._unreadLine()
        return ""

# ------------


class BasicNamespace(Namespace):
    def __init__(self, markdown, namespace_name, oprint):
        self.debug = Debug('ns.basic')
        super(BasicNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        self.dbgPrint("My NS is: {}".format(self.namespace))
        from .regex import Regex
        self.delayedExpansion = Regex(r'(\[{{([^}]+)}}\])')

    def addVariable(self, value, name):
        """Add a variable called 'name' to the list and set its value to 'value'."""
        if type(value) is not str:
            raise TypeError("BasicNamespace only supports string data type")

        # If they used the delayed expansion syntax, remove it before storing value
        from re import findall
        matches = findall(self.delayedExpansion.regex, value)
        for m in matches:
            # for each delayed expansion variable, strip the {{}} from the name
            value = value.replace(m[0],'[{}]'.format(m[1]))

        super(BasicNamespace, self).addVariable(value, name)

    def _stripNamespace(self, id):
        if id.startswith(self.namespace):
            return id[len(self.namespace):]

        return id

    def exists(self, name):
        self.dbgPrint("exists({})".format(name))
        #if name == 'class':
        #    raise NameError("WTF, How did I get here?")
        return super(BasicNamespace, self).exists(self._stripNamespace(name))

    def getValue(self, name):
        return super(BasicNamespace, self).getValue(self._stripNamespace(name))


# ------------

            if ns == Namespaces._default:
                # TODO: Should I print a message or something?
                return  # For now, just return. Basic namespace doesn't support attrs...


# ------------


# ------------


# ------------


# ------------


# ------------


# ------------


# ------------

