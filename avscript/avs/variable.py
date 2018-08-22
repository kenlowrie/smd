#!/usr/bin/env python

from __future__ import print_function


class _Variable(object):
    """Class to abstract a variable (alias). Keep track of the ID (name) and
    the value (text)."""
    def __init__(self, id, text):
        self.id = id
        self.text = text


class VariableDict(object):
    """Class to abstract a dictionary of variables (aliases)"""
    def __init__(self):
        self.vars = {}
        from .regex import Regex
        self.delayedExpansion = Regex(r'(\[{{([^}]+)}}\])')

    def addVar(self, id, text):
        """Add a variable called 'id' to the list and set its value to 'text'."""
        if type(text) is str:
            from re import findall
            matches = findall(self.delayedExpansion.regex, text)
            for m in matches:
                # for each delayed expansion variable, strip the {{}} from the name
                text = text.replace(m[0],'[{}]'.format(m[1]))

        self.vars[id] = _Variable(id, text)

    def exists(self, id):
        """Returns true if the variable 'id' exists."""
        return id in self.vars

    def getText(self, id):
        """Gets the value of the variable 'id', unless it doesn't exist, in
        which case it returns (undefined).

        TODO: Should this just return an empty string if undefined?"""
        return "(undefined)" if not self.exists(id) else self.vars[id].text

    def dumpVars(self, indent='', output=print):
        """Dumps the variable list, names and values."""
        def escape_html(s):
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        for var in sorted(self.vars):
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, escape_html(self.vars[var].text), indent))


class VariableV2Dict(VariableDict):
    """Class to abstract a dictionary of images"""
    _var_prefix = 'varv2.'

    def __init__(self):
        super(VariableV2Dict, self).__init__()  # Initialize the base class(es)

    def addVarV2(self, dict):
        varID = dict["_id"]
        del dict["_id"]
        if 'name' not in dict:
            dict['name'] = varID
        self.addVar(varID, dict)

    def _parseVar(self, id):
        if id.startswith(VariableV2Dict._var_prefix):
            id = id[len(VariableV2Dict._var_prefix):]

        compoundVar = id.split('.')     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            id0, el0 = compoundVar
            if id0 in self.vars and el0 in self.vars[id0].text:
                return compoundVar

        return id, None

    def exists(self, id):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            return id0 in self.vars and el0 in self.vars[id0].text

        return id0 in self.vars

    # TODO: what if we could specify the HTML tag that should be formed with one of these
    # Maybe have an _element=HTMLTAG, and form it like the one for IMAGE if you ask for all

    def getVarV2(self, id, _markdown):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            return _markdown(self.vars[id0].text[el0])

        if self.exists(id0):
            # if the special _format element exists, return it with markdown applied
            fmt = '_format'
            if fmt in self.vars[id0].text:
                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = _markdown(self.vars[id0].text[fmt]).replace('{{','[').replace('}}',']')
                #fmt_str = self.vars[id0].text[fmt].replace('{{','[').replace('}}',']')
                #print(fmt_str.replace('self.','{}.'.format(id)))
                # And now, markdown again, to expand the self. namespace variables
                return _markdown(fmt_str.replace('self.','{}.'.format(id)))

            compoundVar = ''
            for item in sorted(self.vars[id0].text):
                attrText = _markdown(self.vars[id0].text[item])
                compoundVar += ' {}="{}"<br />\n'.format(item, attrText)
            return compoundVar

        return '(undefined variable) {}"'.format(id)

    def dumpVars(self, indent='', output=print):
        """Dumps the image variable list, names and values."""
        for var in sorted(self.vars):
            dict_str = '<br />'
            for d_item in self.vars[var].text:
                dict_str += '&nbsp;&nbsp;{}:{}<br />\n'.format(d_item, self.vars[var].text[d_item])
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, dict_str, indent))


class ImageDict(VariableDict):
    """Class to abstract a dictionary of images"""
    _var_prefix = 'image.'

    def __init__(self):
        super(ImageDict, self).__init__()  # Initialize the base class(es)

    def addImage(self, dict):
        imageID = dict["_id"]
        del dict["_id"]
        self.addVar(imageID, dict)

    def _parseVar(self, id):
        if id.startswith(ImageDict._var_prefix):
            id = id[len(ImageDict._var_prefix):]

        compoundVar = id.split('.')     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            id0, el0 = compoundVar
            if id0 in self.vars and el0 in self.vars[id0].text:
                return compoundVar

        return id, None

    def exists(self, id):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            return id0 in self.vars and el0 in self.vars[id0].text

        return id0 in self.vars

    def getImage(self, id, _markdown):
        id0, el0 = self._parseVar(id)
        if el0 is not None:
            return _markdown(self.vars[id0].text[el0])

        if self.exists(id0):
            imageTag = '<img'
            for item in sorted(self.vars[id0].text):
                if item[0] == '_':
                    continue    # don't add any attributes that start with _
                attrText = _markdown(self.vars[id0].text[item])
                imageTag += ' {}="{}"'.format(item, attrText)
            imageTag += '/>'
            return imageTag

        return '<img src="undefined image {}"/>'.format(id)

    def dumpVars(self, indent='', output=print):
        """Dumps the image variable list, names and values."""
        for var in sorted(self.vars):
            dict_str = '<br />'
            for d_item in self.vars[var].text:
                dict_str += '&nbsp;&nbsp;{}:{}<br />\n'.format(d_item, self.vars[var].text[d_item])
            output("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].id, dict_str, indent))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
