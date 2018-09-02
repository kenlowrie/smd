#!/usr/bin/env python

from re import findall, compile, IGNORECASE


# TODO: These exceptions and regex classes are temporary until we merge the code into avs/
class _Error(Exception):
    """Base exception class for this module."""
    pass


class NestingError(_Error):
    """Regex exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg


class LogicError(_Error):
    """Logic exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg


class Regex(object):
    """Wrapper class for regular expressions."""
    def __init__(self, regex, flags=0):
        """Regex class constructor.

        Compiles the regex string with any required flags for efficiency.
        """
        self.regex = compile(regex, flags)


class RegexMD(Regex):
    """This class holds the regular expressions used when applying markdown
    to inline formatting syntax."""
    def __init__(self, regex, new_repl_str, flags=0):
        """Constructor for the RegexMD class.

        Arguments:
        regex -- the regex string used to detect markdown in the line
        new_repl_str -- the string that will be used to insert the markdown into
            the line. If this is None, then the handler for the regex markdown type
            is responsible for constructing the replacement text.
        flags -- flags to re.compile()
        """
        super(RegexMD, self).__init__(regex, flags)
        self.new_str = new_repl_str


class DummyNamespaces(object):
    def exists(self, s):
        return False

class Markdown(object):
    _max_nesting_level = 25     # arbitrary
    def __init__(self):
        self._current_nesting_level = 0
        # Dictionary of each markdown type that we process on each line
        self._regex_markdown = {
            #'inline_links': RegexMD(r'(\[([^\]]+)\]:[ ]*\([ ]*([^\s|\)]*)[ ]*(\"(.+)\")?\))', None),
            #'link_to_bookmark': RegexMD(r'([@]\:\[([^\]]*)\]\<{2}([^\>{2}]*)\>{2})', None),
            #'links_and_vars': RegexMD(r'(\[([^[\]]+)\](?!(:(.+))|(\=(.+))))', None),
            'vars': RegexMD(r'(\[(\w[^[\]\)]+)([\(](.+)[\)])?\](?!(\=(.+))))', None),
            #'automatic_link': RegexMD(r'(<((?:http|ftp)s?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\[?[A-F0-9]*:[A-F0-9:]+\]?)(?::\d+)?(?:/?|[/?]\S+))>)', '<a href=\"{0}\">{0}</a>', IGNORECASE),
            'strong': RegexMD(r'(\*{2}(?!\*)(.+?)\*{2})', '<strong>{0}</strong>'),
            'emphasis': RegexMD(r'(\*(.+?)\*)', '<em>{0}</em>'),
            'ins': RegexMD(r'(\+{2}(.+?)\+{2})', '<ins>{0}</ins>'),
            'del': RegexMD(r'(\~{2}(.+?)\~{2})', '<del>{0}</del>')
        }
        self._special_parameter = Regex(r'([\w]+)\s*=\s*\"(.*?)(?<!\\)\"')
        self._namespaces = DummyNamespaces()

    def _inc_nesting_level(self):
        self._current_nesting_level += 1
        if self._current_nesting_level > Markdown._max_nesting_level:
            raise NestingError('Expansion nested too deeply')

    def _dec_nesting_level(self):
        self._current_nesting_level -= 1
        if self._current_nesting_level < 0:
            raise LogicError('_current_nesting_level fell below zero')

    def _md_value(self, value):
        last_value = value
        # keep processing until no more expansion happens
        while(1):
            value = self.markdown(value)
            if value == last_value:
                return value
            last_value = value

    def _stripClass(self, s):
        return None, s

    def setNSxface(self,ns):
        self._namespaces = ns

    def markdown(self, s):
        """
        Apply markdown to the passed string.

        As each line is read, it is inspected for markdown tags and those
        tags are processed on the fly. That way, the line is ready to be
        output without additional processing.

        A copy of the unmodified line is also retained in the main loop,
        since certain parse tags require the use of the original line.
        In those cases, the _markdown() method can be invoked later, to
        apply markdown to specific elements of a given parse type. For
        an example, take a look at the contact parse type.

        Arguments:
            s -- the string to process markdown elements in

        Returns:
            A string that has all the markdown elements applied.
        """

        """
        Start with some helper functions to process each markdown type.
        Each markdown element has a method to handle the specifics. Each
        method is passed the following parameters:

        Arguments:
            m -- a list of the elements parsed for the match. m[0] is
                 the full matched substring within s.
            s -- the string to process
            new_str -- the string used to build the replacement string.
                       Generally of the format 'stuff{}stuff', where
                       'stuff' is markdown, and {} is replaced with the
                       text between the markdown tags.

        Returns:
            Modified string with inline markdown element expanded.
        """
        def md_vars(m, s, new_str):
            """
            Handle inline link and vars: [variable_name]

            See docstring in code for argument information.
            """
            def makeJitAttrs(params):
                d = {l[0]: l[1] for l in self._special_parameter.regex.findall(params)}
                #print("{}".format(d))
                return d

            #print("CALLED WITH:****{}----{}----{}****".format(m[0],m[1],s))
            jit_attrs = None if not m[3] else makeJitAttrs(m[3])
            if self._namespaces.exists(m[1]):
                # Substitute the variable name with the value
                c, v = self._stripClass(self._namespaces.getValue(m[1], jit_attrs))
                v = self._md_value(v)
                if(not c):
                    s = s.replace(m[0], v)
                else:
                    s = s.replace(m[0], '<{0}{1}>{2}</{0}>'.format('span', c, v))
            else:
                # No need to do anything here, just leave the unknown link/variable alone
                pass

            return s

        def md_plain(m, s, new_str):
            """
            Handle simple replacement markdown. e.g. *foo* or **bar**, etc.

            See docstring in code for argument information.
            """
            return s.replace(m[0], new_str.format(m[1]))

        # A map linking markdown keys to processor functions
        markdownTypes = [
            ('vars', md_vars),
            ('strong', md_plain),
            ('emphasis', md_plain),
            ('ins', md_plain),
            ('del', md_plain),
        ]

        self._inc_nesting_level()
        #print("CALLED: {}".format(s))
        # For each type of markdown
        for key, md_func in markdownTypes:
            md_obj = self._regex_markdown[key]
            matches = findall(md_obj.regex, s)    # find all the matches
            for m in matches:
                # for each match, process it
                s = md_func(m, s, md_obj.new_str)

        #print("RETURN: {}".format(s))
        self._dec_nesting_level()
        return s    # return the processed string


if __name__ == '__main__':
    print(Markdown().markdown('++***this is a test***++'))
