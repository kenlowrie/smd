#!/usr/bin/env python

from .debug import Debug
from .utility import HtmlUtils
from .exception import LogicError

"""

"""

class Variable(object):
    private = '_private_attrs_'
    public = '_public_attrs_'
    private_esc = '_private_attrs_esc_'
    public_esc = '_public_attrs_esc_'
    public_keys = '_public_keys_'
    private_keys = '_private_keys_'
    all = '_all_attrs_'
    all_esc = '_all_attrs_esc_'
    null = '_null_'
    rvalue = '_rval'
    prefix = '_'

    """Abstracts variable. Keeps track of the name and the value."""
    def __init__(self, name, value):
        self.name = name
        if type(value) is dict:
            self.rval = value
        else:
            self.rval = {Variable.rvalue: value}

    def getValue(self, attribute=None):
        # This doesn't really make sense, because if someone puts _rval in the dict, it won't
        # return the dict. Probably need to check also that len() is 1...
        if attribute is None:
            return self.rval[Variable.rvalue] if Variable.rvalue in self.rval else self.rval
            
        return self.rval[attribute] if attribute in self.rval else ''

    def getAttrsAsDict(self, which):
        if which == Variable.private:
            return {key: value for (key,value) in self.rval.items() if key[0] == Variable.prefix}
        elif which == Variable.public:
            return {key: value for (key,value) in self.rval.items() if key[0] != Variable.prefix}
        elif which == Variable.all:
            return {key: value for (key,value) in self.rval.items()}
        else:
            raise NameError("Invalid attr type requested {}".format(which))

        return self.rval.copy()

    def encodeAttrsAsString(self, attrsDict):
        attrs = ''
        for item in attrsDict:
            attrs += ' {}="{}"'.format(item, attrsDict[item])

        return attrs

    def getAttrsAsString(self, which):
        return self.encodeAttrsAsString(self.getAttrsAsDict(which))

    def getKeysAsString(self, which):
        attrsDict = self.getAttrsAsDict(which)
        keys = ''
        for item in attrsDict:
            keys += '{}, '.format(item)

        return keys

    def addAttribute(self, attrName, attrValue):
        self.rval[attrName] = attrValue

    def dup(self, name):
        v = Variable(name,None)
        v.rval=self.rval.copy()
        return v

    def dump(self, output):
        if len(self.rval) == 1 and Variable.rvalue in self.rval:
            output("{0}={1}".format(self.name, self.rval[Variable.rvalue]))
            return

        output("{}".format(self.name))
        for item in self.rval:            
            output("\t{0}={1}".format(item, self.rval[item]))


class VariableStore(object):
    _special_attributes = [Variable.public, Variable.private, 
                           Variable.public_esc, Variable.private_esc, 
                           Variable.public_keys, Variable.private_keys, 
                           Variable.all, Variable.all_esc,
                           Variable.null]

    """Class to abstract a dictionary of variables"""
    def __init__(self, markdown, oprint):
        self.vars = {}
        self._md_ptr = markdown
        self.oprint = oprint

    def dbgState(self, enable):
        self.debug.state = True if enable else False

    def dbgPrint(self, msg, ctx=None):
        if not hasattr(self, 'debug') or not isinstance(self.debug, Debug):
            raise NotImplementedError("Object must define a variable 'debug' of class Debug")
        self.debug.print(msg, ctx)  #pylint: disable=E1101

    def dbgPrintDict(self, msg, d):
        self.dbgPrint(msg)
        from types import CodeType
        for i in d:
            if isinstance(d[i], (CodeType)):
                self.dbgPrint("&nbsp;&nbsp;<strong>{}</strong>: {}".format(i, HtmlUtils.escape_html('<code object>')))
            else:
                self.dbgPrint("&nbsp;&nbsp;<strong>{}</strong>: {}".format(i, HtmlUtils.escape_html(d[i])))

    def _markdown(self, s):
        markdown = self._md_ptr
        return markdown(s)

    def addVariable(self, value, name):
        """Add a variable called 'name' to the list and set its value to 'value'."""

        self.vars[name] = Variable(name, value)

    def exists(self, name):
        """Returns true if the variable 'name' exists."""
        return name in self.vars

    def getValue(self, name, attribute=None):
        """Gets the value of the variable 'name'
        
        If it doesn't exist, it returns ''."""

        self.dbgPrint('Requesting <strong>{}.{}</strong>'.format(name, attribute))

        return self.vars[name].getValue(attribute) if self.exists(name) else ""

    def dup(self, current, new):
        if self.exists(current):
            if self.exists(new):
                # TODO: raise exception
                self.oprint('{} already exists'.format(new))
                return

            self.vars[new] = self.vars[current].dup(new)
        else:
            # TODO: raise exception
            self.oprint('{} doesn\'t exist'.format(current))

    def addAttribute(self, name, attrName, attrValue):
        if self.exists(name):
            self.vars[name].addAttribute(attrName, attrValue)

    def getRVal(self, name):
        if self.exists(name):
            self.dbgPrint('<strong><span class="green">You asked for: <em>{}</em></span></strong>'.format(name))
            return self.vars[name].rval

    def setRVal(self, name, rval):
        if self.exists(name):
            # TODO: This must account for type of incoming
            # del existing, then call underlying method so
            # it handles _rval vs. dictionary...
            self.vars[name].rval['_rval'] = rval

    def setAttribute(self, name, attr, value):
        if self.exists(name):
            self.vars[name].rval[attr] = value
            return

        raise NameError("setAttribute: Variable {} is not defined".format(name))

    def getAttribute(self, name, attr):
        if self.exists(name):
            if attr in self.vars[name].rval:
                return self.vars[name].rval[attr]

            return ''   # Should I return an error instead?

        raise NameError("getAttribute: Variable {} is not defined".format(name))

    def getPublicAttrsDict(self, name):
        if self.exists(name):
            self.dbgPrint('Requesting <em>_public_attrs_</em> dict for <strong>{}</strong>'.format(name))
            # TODO: Do we need to encode HREF? Is this API even used?
            return self.vars[name].getAttrsAsDict(Variable.public)

    def getPublicAttrs(self, name, escape=False):
        if self.exists(name):
            self.dbgPrint('Requesting <em>_public_attrs_</em> string for <strong>{}</strong>'.format(name))
            if self.namespace == 'link.':
                d = self.vars[name].getAttrsAsDict(Variable.public)
                href = 'href'
                if href in d:
                    encoded = HtmlUtils.encodeURL(d[href])
                    self.dbgPrint("Encoding HREF <strong>{}</strong> as <em>{}</em>".format(d[href],encoded))
                    d[href] = encoded
                else:
                    self.dbgPrint('Namespace is link., but no HREF present')
                s = self.vars[name].encodeAttrsAsString(d)
            else:
                s = self.vars[name].getAttrsAsString(Variable.public)
            return self.escapeString(s) if escape else s

    def getPublicKeys(self, name):
        if self.exists(name):
            return self.vars[name].getKeysAsString(Variable.public)

    def getPrivateAttrsDict(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsDict(Variable.private)

    def getPrivateAttrs(self, name, escape=False):
        if self.exists(name):
            s = self.vars[name].getAttrsAsString(Variable.private)
            return self.escapeString(s) if escape else s

    def getPrivateKeys(self, name):
        if self.exists(name):
            return self.vars[name].getKeysAsString(Variable.private)

    def getAllAttrs(self, name, escape=False):
        if self.exists(name):
            s = self.vars[name].getAttrsAsString(Variable.all)
            return self.escapeString(s) if escape else s

    def getAllAttrsDict(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsDict(Variable.all)

    def getSpecialAttr(self, which, variable):
        if which == Variable.public:
            return self.getPublicAttrs(variable)
        elif which == Variable.private:
            return self.getPrivateAttrs(variable)
        elif which == Variable.all:
            return self.getAllAttrs(variable)
        elif which == Variable.null:
            return ''   # empty string, useful for adding attributes w/o printing anything
        elif which == Variable.public_esc:
            return self.getPublicAttrs(variable, True)
        elif which == Variable.private_esc:
            return self.getPrivateAttrs(variable, True)
        elif which == Variable.all_esc:
            return self.getAllAttrs(variable, True)
        elif which == Variable.public_keys:
            return self.getPublicKeys(variable)
        elif which == Variable.private_keys:
            return self.getPrivateKeys(variable)

        raise LogicError("Oops. Special attribute {} isn't valid for {}".format(which, variable))

    def escapeString(self,s):
        if type(s) != type(''):
            return s
        self.dbgPrint('escapeString({})'.format(s))
        return s.replace('"', '\\"')

    def unescapeString(self,s):
        if type(s) != type(''):
            return s
        return s.replace('\\"', '"')

    def unescapeStringQuotes(self,d):
        for item in d:
            d[item] = self.unescapeString(d[item])

        return d     

    def dumpVars(self, which='.*', indent=''):
        """Dumps the variable list, names and values."""
        from .regex import RegexSafe
        reObj = RegexSafe(which)
        for var in sorted(self.vars):
            if reObj.is_match(var) is None:
                continue

            self.oprint("{2}<strong>{0}=</strong>{1}<br />".format(self.vars[var].name, 
                                                                   HtmlUtils.escape_html(self.vars[var].rval['_rval']), indent))

    def dumpVarsAsStrings(self, which='.*', indent=''):
        """Dumps the variable list, names and values."""
        from .regex import RegexSafe
        reObj = RegexSafe(which)
        for var in sorted(self.vars):
            if reObj.is_match(var) is None:
                continue

            self.vars[var].dump(self.oprint)


class Namespace(VariableStore):
    def __init__(self, markdown, namespace_name, oprint):
        super(Namespace, self).__init__(markdown, oprint)  # Initialize the base class(es)
        self._namespace = '{}.'.format(namespace_name)
        from .regex import RegexSafe
        self._name_regex = RegexSafe(r'^[a-zA-Z_][-\w]*$')

    @property
    def namespace(self):
        return self._namespace

class AdvancedNamespace(Namespace):
    _variable_name_str = ["_id", "_"]
    _default_format_attr = '_format'
    _raw_format_attr = '_raw'               #//TODO: What is this _raw attr used for? I don't think it is. remove it??
    _inherit_attr = '_inherit'

    def __init__(self, markdown, namespace_name, oprint):
        super(AdvancedNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        # Individual namespaces can override this behavior @ns varname="initialvalue"
        self._allow_brief_def = False

    def _missingID(self, dict, which="ADD"):
        self.oprint("{}: Dictionary is missing {}<br />{}<br />".format(which, AdvancedNamespace._variable_name_str, dict))
    
    def _validateName(self, varID, which="ADD"):
        #//TODO: This is interesting. It works (limited testing), and enables you to do variable expansion on the variable name. Is this useful?
        #mdVarID = self._markdown(varID)
        #if mdVarID != varID:
        #    varID = mdVarID
        if not self._name_regex.is_match(varID):
            self.oprint(f"{which}: Invalid character used in variable name \"{varID}\". Must conform to regular expression \"{self._name_regex.regex.pattern}\"<br />")
            raise SyntaxError(f"Invalid character used in variable name during {which}")

        if varID in ['_', '_id']:
            self.oprint(f"{which}: Cannot use reserved attribute name \"{varID}\" as variable name<br />")
            raise AttributeError(f"Attempt to use reserved attribute name as variable name during {which}")

        self.dbgPrint(f"{'Adding' if which == 'ADD' else 'Updating'} variable with name {varID} values {dict}")

    def _validateAttrs(self, dict):
        for key in dict.keys():
            #//TODO: Figure out why I have to add [Variable.rvalue] manually. If I add it to _special_attributes, then you will
            # get a logic exception thrown when you attempt to access it, e.g. [variable._rval]. Need to understand why that is,
            # and whether to add it to the case in getSpecial, or just what is going on with it...
            #if key in self._special_attributes + [Variable.rvalue]:
            if self._isSpecial(key) or key in [Variable.rvalue]:
                self.oprint(f"WARNING: Use of reserved attribute name <em>{key}</em> is ambiguous within a variable declaration and will likely lead to unexpected results.<br />")

    def getIDstring(self, dict):
        for id in AdvancedNamespace._variable_name_str:
            if id in dict:
                return id
        return None

    def inheritsFrom(self, dict):
        return True if AdvancedNamespace._inherit_attr in dict else False

    def addVariable(self, dict, name=None):
        if len(dict) == 0:
            self.oprint("ERROR: addVariable called with empty dictionary.<br />")
            raise SyntaxError("addVariable called with an empty dictionary.")
    
        self.dbgPrintDict(f'<strong>addVariable("<em>{name}</em>")</strong>',dict)
        myID = self.getIDstring(dict)   # check for _/_id in dict i.e. variable name
        if myID is None:
            # no variable name present
            if self._allow_brief_def:
                # this name space allows brief declarations: e.g. @ns var="value"
                # Python 3.7+ guarantees insertion order of keys, so 1st attribute will be variable name
                varID = [i for i in dict.keys()][0]
                # if _format is in the dict, it wins; ignore "value" from 1st attribute
                if AdvancedNamespace._default_format_attr not in dict.keys():
                    # grab "value" and assign it to _format
                    dict[AdvancedNamespace._default_format_attr] = dict[varID]
                # remove the 1st attribute, we don't need it anymore
                del dict[varID]
            else:
                # if no _/_id present, and ns doesn't allow brief declaration, this is error
                self._missingID(dict)
                raise AttributeError(f"Missing {AdvancedNamespace._variable_name_str}")
        else:
            # variable declaration contains either _ or _id, so use that as name and remove from dict
            varID = dict[myID]
            del dict[myID]
        
        if self.inheritsFrom(dict):
            rval = self.getRVal(dict[AdvancedNamespace._inherit_attr])
            tempDict = rval.copy() if rval is not None else {"_format": "***{}*** does not exist".format(dict[AdvancedNamespace._inherit_attr])}
            for item in dict:
                if item != AdvancedNamespace._inherit_attr:
                    tempDict[item] = dict[item]
            dict = tempDict

        self._validateName(varID)
        self._validateAttrs(dict)
        super(AdvancedNamespace, self).addVariable(self.unescapeStringQuotes(dict), varID)
        return varID

    def updateVariable(self, dict, name=None):
        #//TODO: Should I add this as a private method so we only have one place to update?
        if len(dict) == 0:
            self.oprint("ERROR: updateVariable called with empty dictionary.<br />")
            raise SyntaxError("updateVariable called with an empty dictionary.")
    
        self.dbgPrintDict(f'<strong>updateVariable("<em>{name}</em>")</strong>',dict)
        myID = self.getIDstring(dict)

        if myID is None:
            # see docs for addVariable(). They mostly apply here too
            if self._allow_brief_def:
                varID = [i for i in dict.keys()][0]

                # if the variable isn't defined yet, @set is same as declaration
                if varID not in self.vars:
                    return self.addVariable(dict)

                # same as addVariable(). If _format not defined, use "value". If it is, ignore "value"
                if AdvancedNamespace._default_format_attr not in dict.keys():
                    dict[AdvancedNamespace._default_format_attr] = dict[varID]
                del dict[varID]
            else:
                self._missingID(dict, "UPDATE")
                return
                #raise AttributeError(f"Missing {AdvancedNamespace._variable_name_str}")
        else:
            varID = dict[myID]
            if varID not in self.vars:
                return self.addVariable(dict)
            del dict[myID]
        
        # Okay, we know the variable is there, so let's just update all the attribute values

        for item in dict:
            self.vars[varID].rval[item] = self.unescapeString(dict[item])

    def _isSpecial(self, attr):
        return True if attr in AdvancedNamespace._variable_name_str + VariableStore._special_attributes else False

    def _parseVariable(self, id, do_not_test_attr=False):
        #if id.startswith(self.namespace):
        #    id = id[len(self.namespace):]

        compoundVar = id.split('.', 1)     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            id0, el0 = compoundVar
            if id0 in self.vars and (do_not_test_attr or el0 in self.vars[id0].rval or self._isSpecial(el0)):
                return compoundVar

        return id, None

    def exists(self, id):
        self.dbgPrint('<strong>exists("<em>{}</em>")</strong>'.format(id))
        id0, el0 = self._parseVariable(id)
        if el0 is not None:
            # _parseVar() only returns both elements if the attribute exists
            return True

        return id0 in self.vars

    def getVarID(self, id):
        id0, el0 = self._parseVariable(id, True)
        return id0 if el0 is not None else id

    def getValue(self, id):
        self.dbgPrint('<strong>getValue("<em>{}</em>")</strong>'.format(id))
        id0, el0 = self._parseVariable(id)
        if el0 is not None:
            # If they are asking for the special name (_, _id)
            if el0 in AdvancedNamespace._variable_name_str:
                # return the variable name itself, no markdown.
                self.dbgPrint('Returning {} for getValue("{}")'.format(id0, el0))
                return id0

            if el0 in VariableStore._special_attributes:
                # should this be marked down? Probably.
                s = self._markdown(self.getSpecialAttr(el0, id0))
                self.dbgPrint('Returning <em>{}</em> for <strong>getValue("{}.{}</strong>")'.format(s, id0, el0))
                return s

            if el0 == AdvancedNamespace._raw_format_attr and el0 in self.vars[id0].rval:
                # We need to return this string raw.
                raw = self.vars[id0].rval[el0]
                self.dbgPrint("Returning _raw(\"<em>{}</em>\") as value for <strong>{}</strong>".format(raw, id))

                return raw

            # TODO: When test code in place, I need to remove this and see what happens.
            #       Feels a bit like a side affect...
            # First, apply standard markdown in case _format has regular variables in it.
            fmt_str = self._markdown(self.vars[id0].rval[el0]).replace('{{','[').replace('}}',']')
            self.dbgPrint("MD1: <strong>{}</strong>".format(HtmlUtils.escape_html(self.vars[id0].rval[el0])))
            self.dbgPrint("RS1: <em>{}</em>".format(HtmlUtils.escape_html(fmt_str)))

            # And now, markdown again, to expand the self. namespace variables
            s = self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))
            self.dbgPrint("MD2: fmt_str(self.-&gt;{}{}):<strong>{}</strong>".format(self.namespace,id0, HtmlUtils.escape_html(fmt_str)))
            self.dbgPrint("RS2: <em>{}</em>".format(HtmlUtils.escape_html(s)))
            # If the namespace is link. and the attribute is href, we need to encode it.
            if self.namespace == 'link.' and el0 == 'href':
                self.dbgPrint("Encoding HREF from <strong>{}</strong> to <em>{}</em>".format(s, HtmlUtils.encodeURL(s)))
            return s

        if self.exists(id0):
            # if the special _format element exists, return it with markdown applied
            fmt = AdvancedNamespace._default_format_attr
            if fmt in self.vars[id0].rval:
                self.dbgPrint("Returning _format(\"<em>{}</em>\") as value for <strong>{}</strong>".format(self.vars[id0].rval[fmt], id))
                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = self._markdown(self.vars[id0].rval[fmt]).replace('{{','[').replace('}}',']')
                self.dbgPrint("MD3: <strong>{}</strong>".format(HtmlUtils.escape_html(self.vars[id0].rval[fmt])))
                self.dbgPrint("RS3: <em>{}</em>".format(HtmlUtils.escape_html(fmt_str)))

                # And now, markdown again, to expand the self. namespace variables
                s = self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))
                self.dbgPrint("MD4: fmt_str(self.-&gt;{}{}):<strong>{}</strong>".format(self.namespace,id0, HtmlUtils.escape_html(fmt_str)))
                self.dbgPrint("RS4: <em>{}</em>".format(HtmlUtils.escape_html(s)))
                return s

            compoundVar = ''
            for item in sorted(self.vars[id0].rval):
                # This prevents a crash if a value is not a string...
                attrValue = self.vars[id0].rval[item]
                if type(attrValue) != type(''):
                    attrValue = str(attrValue)
                attrText = self._markdown(attrValue)
                compoundVar += ' {}="{}"<br />\n'.format(item, attrText)
            return compoundVar

        # logically, you won't ever get here, because everyone always
        # calls exists() first, and if false, it just echos out what you
        # passed in. But just in case...
        return '(undefined variable) {}"'.format(id)

    def dumpVars(self, which='.*', indent=''):
        """Dumps the image variable list, names and values."""
        from .regex import RegexSafe
        reObj = RegexSafe(which)
        
        from types import CodeType
        for var in sorted(self.vars):
            if reObj.is_match(var) is None:
                continue
            dict_str = '<br />'
            for d_item in self.vars[var].rval:
                if isinstance(self.vars[var].rval[d_item], (CodeType)):
                    dict_str += '&nbsp;&nbsp;<strong>{}=</strong><em>{}</em><br />\n'.format(d_item, HtmlUtils.escape_html('<code object>'))
                else:
                    dict_str += '&nbsp;&nbsp;<strong>{}=</strong>{}<br />\n'.format(d_item, HtmlUtils.escape_html(self.vars[var].rval[d_item]))
            self.oprint("{2}<strong>{0}=</strong>{1}<br />".format(var, dict_str, indent))

class VarNamespace(AdvancedNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(VarNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        self.debug = Debug('ns.var')
        self.dbgPrint("My NS is: {}".format(self.namespace))
        # Allow the shortened @var name="value" declaration
        self._allow_brief_def = True



class ImageNamespace(AdvancedNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(ImageNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        self.debug = Debug('ns.image')
        self.dbgPrint("My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None):
        var_name = super(ImageNamespace, self).addVariable(dict)

        if not super(ImageNamespace, self).exists('{}.{}'.format(var_name, AdvancedNamespace._default_format_attr)):
            super(ImageNamespace, self).addAttribute(var_name,AdvancedNamespace._default_format_attr,'<{{self._tag}}{{self._public_attrs_}}/>')

        if not super(ImageNamespace, self).exists('{}.{}'.format(var_name, '_tag')):
            super(ImageNamespace, self).addAttribute(var_name,'_tag','img')


class HtmlNamespace(AdvancedNamespace):
    _start = '<'
    _end = '>'
    _start_esc = '<+'
    _tag = '_tag'
    _element_partials = [_start, _end, _start_esc]

    def __init__(self, markdown, namespace_name, oprint, add_debug_obj=True):
        super(HtmlNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        if add_debug_obj:
            self.debug = Debug('ns.html')
            self.dbgPrint("My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None, addTag=True):
        var_name = super(HtmlNamespace, self).addVariable(dict)

        if not super(HtmlNamespace, self).exists('{}.{}'.format(var_name, AdvancedNamespace._default_format_attr)):
            super(HtmlNamespace, self).addAttribute(var_name,AdvancedNamespace._default_format_attr,'<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>')

        if addTag and not super(HtmlNamespace, self).exists('{}.{}'.format(var_name, '_tag')):
            super(HtmlNamespace, self).addAttribute(var_name,'_tag',var_name)

        return var_name

    def _isSpecial(self, attr):
        if attr in HtmlNamespace._element_partials:
            return True

        return super(HtmlNamespace, self)._isSpecial(attr)

    def getElementPartial(self, which):
        if which in [HtmlNamespace._start, HtmlNamespace._start_esc]:
            # TODO: should do error checking here (make sure _tag is defined?)
            return '<{0}self._tag{1}{0}self.{2}{1}>'.format('{{', '}}', Variable.public if which == HtmlNamespace._start else Variable.public_esc)
        elif which == HtmlNamespace._end:
            # TODO: should do error checking here (make sure _tag is defined?)
            return '</{{self._tag}}>'

        raise SyntaxError("Invalid element partial [{}]".format(which))

    def getValue(self, id):
        id0, el0 = self._parseVariable(id)
        self.dbgPrint('getValue("{}","{}",{})'.format(id,id0,None if el0 is None else '"{}"'.format(el0)))
        if el0 is not None:
            if el0 in HtmlNamespace._element_partials:

                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = self._markdown(self.getElementPartial(el0).replace('{{','[').replace('}}',']'))
                # And now, markdown again, to expand the self. namespace variables
                self.dbgPrint("Replace self.{}{} in {} and markdown".format(self.namespace, id0, fmt_str))
                return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace,id0)))

        return super(HtmlNamespace, self).getValue(id)


class LinkNamespace(HtmlNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(LinkNamespace, self).__init__(markdown, namespace_name, oprint, False)  # Initialize the base class(es)
        self.debug = Debug('ns.link')
        self.dbgPrint("My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None):
        tag = HtmlNamespace._tag

        var_name = super(LinkNamespace, self).addVariable(dict, addTag=False)

        if not super(LinkNamespace, self).exists('{}.{}'.format(var_name, tag)):
            super(LinkNamespace, self).addAttribute(var_name,tag,'a')

class CodeNamespace(AdvancedNamespace):
    _run_ = 'run'           # .run attribute. Optional. i.e. [code.varname] === [code.varname.run]
    _code_ = '_code'        # The private attribute that stores the compiled code
    _params_ = '_params_'   # This stores the just-in-time (jit) attrs being passed to an invocation of a code macro
    _last_ = '_last'
    #_defaults_ = '_defaults_'
    _code_str = '<strong><em><span class="blue">@code</span></em></strong>'
    #_locals_ = '_locals_'
    _element_partials = [_run_, _code_, _params_, _last_]

    def __init__(self, markdown, namespace_name, oprint):
        super(CodeNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        self.debug = Debug('ns.code')
        self.dbgPrint("My NS is: {}".format(self.namespace))

    def compileSource(self, src, src_type):
        exceptionMessage = ''   # pylint: disable=W0612
        self.dbgPrint("About to compile: <strong>{}</strong>".format(HtmlUtils.escape_html(src)))
        try:
            code = compile(src, '<string>', src_type)
        except Exception as e:
            self.dbgPrint('<strong><em>Compile error: </em>{}</strong>'.format(src))
            self.dbgPrint('<strong><em>Error message: </em>{}</strong>'.format(str(e)))
            exceptionMessage = "{}".format(str(e))
            code = None

        return code if code is not None else compile('print("Compile error: {}".format(exceptionMessage))','<string>', 'eval')

    def executePython(self, dict):
        import sys
        from io import StringIO
        import contextlib

        @contextlib.contextmanager
        def stdoutIO(so=None):
            old = sys.stdout
            if so is None:
                so = StringIO()
            sys.stdout = so
            yield so
            sys.stdout = old

        exceptionMessage = ''
        self.debug.global_suspend(True)
        with stdoutIO() as s:
            try:
                exec(dict[CodeNamespace._code_]) if dict['type'] == 'exec' else eval(dict[CodeNamespace._code_])
            except Exception as e:
                exceptionMessage = "{}".format(str(e))
        self.debug.global_suspend(False)

        if exceptionMessage: self.oprint("<br />\n<strong><em>Exception:</em> {}</strong><br />\n<strong>src=</strong>{}<br />".format(exceptionMessage, dict['src']))
        return s.getvalue().rstrip()

    def addVariable(self, dict, name=None):
        if 'src' not in dict or 'type' not in dict:
            self.oprint("@code namespace requires both <em>src='source code string'</em> and <em>type=&lt;exec or eval&gt;</em><br />") 
            raise SyntaxError("@code namespace requires src= and type= attributes")

        if dict['type'] not in ['exec', 'eval']:
            self.oprint("@code namespace <em>type=</em> must be <strong>&lt;exec or eval&gt;</strong><br />")
            raise SyntaxError('@code namespace type= must be either "exec" or "eval"')

        var_name = super(CodeNamespace, self).addVariable(dict)

        """
        [code.ref.exec] - returns exec(_code)
        [code.ref.eval] - returns eval(_code)
        """
        dict = super(CodeNamespace, self).getRVal(var_name)
        # TODO: Fix this so it doesn't compile here or getvalue.
        #       That should be done inside ExecutePython
        #       And that is only needed during execution, not during ADD
        
        # Compile a string for now, it isn't needed until the variable is expanded.
        src = 'print("<strong>raw src=</strong>{}")'.format(dict['src'].replace('"','\\"'))
        self.dbgPrint("Compiling CODE(av) src={}".format(src))
        dict[CodeNamespace._code_] = self.compileSource(src, dict['type'])
        dict[CodeNamespace._last_] = self.executePython(dict)
        

    # When you have special attributes for your class, you have to define your own
    # _isSpecial, so you can check yours before passing it along to the sub classes.
    def _isSpecial(self, attr):
        if attr in CodeNamespace._element_partials:
            return True

        return super(CodeNamespace, self)._isSpecial(attr)

    def exists(self, id):
        id0, el0 = self._parseVariable(id) # pylint: disable=W0612
        if el0 is not None:
            if el0 in CodeNamespace._element_partials:
                return True

        return super(CodeNamespace, self).exists(id)

    def getValue(self, id):
        def xlat_parameters(s, d):
            if not d: return s
            for item in d:
                s = s.replace("$.{}".format(item), d[item])
            return s

        id0, el0 = self._parseVariable(id)
        self.dbgPrint("<strong>getValue(<em>{}, {}, {}</em>)</strong>".format(id,id0,el0), CodeNamespace._code_str)
        if el0 is None or el0 == CodeNamespace._run_:
            # Get the dictionary (not a copy, the actual dictionary, so if you change it, your changing it. Got it? Good.)
            dict = super(CodeNamespace, self).getRVal(id0)

            # TODO: Don't hard code what's be skipped over
            # Build a dictionary of the attrs that need to be restored after we process this getValue()
            restoreValues = {key: value for (key, value) in dict.items() if key not in [CodeNamespace._code_, CodeNamespace._last_, CodeNamespace._params_]}
            self.dbgPrintDict("Saving these values:", restoreValues)

            self.dbgPrint("<strong>src=</strong><em>{}</em>".format(dict['src']), CodeNamespace._code_str)

            # Shouldn't this always be true? Doesn't jit_attrs() add this, always?
            if CodeNamespace._params_ in dict:
                params = dict[CodeNamespace._params_]
                self.dbgPrintDict("Parameters:", params)
                for var in params:
                    self.dbgPrint("Replacing: <strong>{}</strong> with <em>{}</em>".format(var, params[var]))
                    dict[var] = params[var]


            # Need to expand any variables inside src... (referencing self. overwrites _params_ :(
            src = super(CodeNamespace, self).getValue('{}.src'.format(id0))
            self.dbgPrint("(src)=<em>{}</em>".format(src))
            self.dbgPrintDict("[dict]=", dict)

            # TODO: Is this working right? If new attrs are added, they'll be sticky. Is that okay?
            # Now build a dictionary of the attrs that need substitution (if present) in the src code
            replaceValues = {key: value for (key, value) in dict.items() if key not in [CodeNamespace._code_, CodeNamespace._params_]}

            # Now translate $.attr to values from the replaceValues dictionary
            src = xlat_parameters(src, replaceValues)

            # Finally, compile it and execute it
            self.dbgPrint("Compiling <strong>src=</strong><em>{}</em>".format(HtmlUtils.escape_html(src)), CodeNamespace._code_str)
            dict[CodeNamespace._code_] = self.compileSource(src, dict['type'])
            dict[CodeNamespace._last_] = self.executePython(dict)

            # And now, put back the attributes as they were on entrance. This is a requirement for @code vars.
            # The only way to change an attribute is to use @set (TODO: test that theory)
            for key in restoreValues:
                self.dbgPrint("Restore: <strong>{}</strong> with <em>{}</em>".format(key, HtmlUtils.escape_html(restoreValues[key])))
                dict[key] = restoreValues[key]

            return dict[CodeNamespace._last_]

        if el0 in [CodeNamespace._code_, CodeNamespace._params_]:
            # Trying to return these will crash the markdown processor. Just bail and say we can't do it.
            return f'{id0}.{el0} is instance data and is not printable'

        return super(CodeNamespace, self).getValue(id)


class Namespaces(object):
    _html = 'html'
    _var = 'var'
    _link = 'link'
    _image = 'image'
    _code = 'code'
    _search_order = [_var, _link, _html, _image, _code]

    def __init__(self, markdown, setNSxface, oprint=print):
        self._namespaces = {
            Namespaces._html: HtmlNamespace(markdown, Namespaces._html, oprint),
            Namespaces._var: VarNamespace(markdown, Namespaces._var, oprint),
            Namespaces._image: ImageNamespace(markdown, Namespaces._image, oprint),
            Namespaces._link: LinkNamespace(markdown, Namespaces._link, oprint),
            Namespaces._code: CodeNamespace(markdown, Namespaces._code, oprint),
        }
        self.debug = Debug('ns')
        self.debugNSA = Debug('ns.add')
        for ns in self._namespaces:
            self.debug.print("Namespace for {} is set to {}".format(ns, self._namespaces[ns].namespace))

        self.oprint = oprint
        setNSxface(self)

    def addVariable(self, value, name=None, ns=None):
        if ns is None:
            ns = Namespaces._var

        if ns not in self._namespaces:
            raise SyntaxError("Invalid namespace [{}]".format(ns))

        if self.debugNSA.enabled():
            #self.debugNSA.print('val={}--name={}--ns={}'.format(value,name,ns))
            rc, nspace, varname = self.exists2(value, name)
                
            if rc:
                self.debugNSA.print('<strong>WARNING:</strong> Variable <strong><em>{}</em></strong> is already defined in namespace <strong><em>{}</em></strong>.'.format(varname, nspace))

        try:
            self._namespaces[ns].addVariable(value, name)
        except AttributeError:
            self.debugNSA.print(f'<strong>WARNING:</strong> Attribute error caught during {ns}.addVariable({value}, {name})')
        except SyntaxError:
            self.debugNSA.print(f'<strong>WARNING:</strong> Syntax error caught during {ns}.addVariable({value}, {name})')

    # TODO: Clean this up...
    def findNamespace(self, value):
        id = self._namespaces['var'].getIDstring(value)
        if id is not None:
            ns, name = self._splitNamespace(value[id])
            if ns is not None:
                if ns in Namespaces._search_order:
                    if self._namespaces[ns].exists(name):
                        #TODO: Review for kludginess
                        value[id] = name    # remove the NS prefix from the dict. Is this a kludge?
                        return ns

            for ns in Namespaces._search_order:
                if self._namespaces[ns].exists(name):
                    return ns

        return None

    # TODO: Clean this up...
    def updateVariable(self, value, name=None, ns=None):
        if ns == '?':
            ns = self.findNamespace(value)

        #print("NS IS: {}--{}<br />".format(ns, value))
        if ns is None:
            ns = Namespaces._var

        if ns not in self._namespaces:
            raise SyntaxError("Invalid namespace [{}]".format(ns))

        try:
            self._namespaces[ns].updateVariable(value, name)
        except AttributeError:
            self.debugNSA.print(f'<strong>WARNING:</strong> Attribute error caught during {ns}.updateVariable({value}, {name})')
        except SyntaxError:
            self.debugNSA.print(f'<strong>WARNING:</strong> Syntax error caught during {ns}.updateVariable({value}, {name})')

    def _splitNamespace(self, variable_name):
        compoundVar = variable_name.split('.',1)     # split at '.' if present, might be looking to get dict element
        if len(compoundVar) == 2:
            return (compoundVar[0], compoundVar[1])

        return (None, variable_name)

    def removeVariable(self, name):
        # TODO: Add this
        # name [[ns].name]
        pass

    def removeAttribute(self, name=None):
        # TODO: Add this
        # name [[ns].name.attr]
        self.oprint("inside removeAttribute")
        pass

    def dupVariable(self, curname, newname):
        # TODO: Add this
        # curname [[ns].name]
        # newname [[ns].name]
        pass

    def existsInNamespace(self, variable_name, namespace):
        ns, name = self._splitNamespace(variable_name)
        if ns != namespace:
            return False

        return True if self._namespaces[namespace].exists(variable_name) else False

    def exists2(self, value, variable_name):
        if variable_name is not None:
            # this is a basic variable
            ns, name = self._splitNamespace(variable_name)
        else:
            # this is an advanced variable, parse the ns and varname
            id = self._namespaces['var'].getIDstring(value)
            if id is None:
                # If there's no ID in the dict, nothing more we can do...
                return (False, None, None)
            
            ns, name = self._splitNamespace(value[id])

        if ns is not None:
            if ns in Namespaces._search_order:
                exists = self._namespaces[ns].exists(name)
                return (True, ns, name)

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(name):
                return (True, ns, name)

        return (False, None, None)

    def exists(self, variable_name):
        ns, name = self._splitNamespace(variable_name)
        if ns is not None:
            if ns in Namespaces._search_order:
                return self._namespaces[ns].exists(name)

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(variable_name):
                return True

        return False

    def getValue(self, variable_name, jit_attrs=None):
        self.debug.print('getValue(<em>"{}"</em>, <strong>[{}]</strong>)'.format(variable_name, jit_attrs))

        def addJITattrs(jit_attrs, ns, var):

            if ns != Namespaces._code:
                # jit_attrs are sticky on everything except code
                if jit_attrs is not None:
                    jit_attrs['_'] = self._namespaces[ns].getVarID(var)
                    self._namespaces[ns].updateVariable(jit_attrs)
            else:
                # @code namespace has special requirements. We need to pass
                # the jit_attrs inside the _params_ key, as they are substituted
                # on the fly when getValue() is called.
                if jit_attrs is None:
                    #self.dbgPrint("jit_attrs is NONE<br />")
                    jit_attrs = {}
                # Make a temp dictionary with "_" and "_params_" keys
                params = {CodeNamespace._params_: jit_attrs, 
                          '_': self._namespaces[ns].getVarID(var)}
                # Add _params_ to the variable dictionary
                #self.dbgPrint("Adding/Updating _params_ to: {}<br />".format(params))
                self._namespaces[ns].updateVariable(params)
        
        ns, name = self._splitNamespace(variable_name)
        if ns is not None:
            if ns in Namespaces._search_order:
                addJITattrs(jit_attrs, ns, name)

                # TODO: Shouldn't we check to see that it's there?
                return self._namespaces[ns].getValue(name)

        #if self.debug self.oprint("NO NAMESPACE OR UNKNOWN NAMESPACE")
        # Since the NS wasn't valid, we need to fall back to the full name again
        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(variable_name):
                # TODO: this is confusing, and will lead to errors. REFACTOR.
                addJITattrs(jit_attrs, ns, variable_name)
                return self._namespaces[ns].getValue(variable_name)

        # TODO: We may want to just return variable_name instead... like before...
        return "Variable {} is (undefined)".format(variable_name)    # I don't think this will ever happen

    def parseVariableName(self, variable_name):
        # split as many times as possible
        cv = variable_name.split('.')
        # If we have more than 3 components, it's not valid
        if len(cv) > 3:
            return (None, None, None)

        # If the variable doesn't exist, bail
        if not self.exists(variable_name):
            return (None, None, None)

        if len(cv) == 3:
            return (cv[0], cv[1], cv[2])

        elif len(cv) == 2:
            if cv[0] in Namespaces._search_order:
                return (cv[0], cv[1], None)

            for ns in Namespaces._search_order:
                if self._namespaces[ns].exists(variable_name):
                    return (ns, cv[0], cv[1])

            raise LogicError("This can't happen happened.")

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(cv[0]):
                return (ns, cv[0], None)

        raise LogicError("This really can't happen happened.")

    def parseVariableNameInNamespace(self, variable_name, namespace):
        just_no = (None, None, None)
        # split as many times as possible
        cv = variable_name.split('.')
        if len(cv) > 3:
            # If we have more than 3 components, it's not valid
            return just_no

        if len(cv) == 3 and cv[0] != namespace:
            # syntactically correct, but in wrong namespace.
            # return the fully qualified parts back to the caller, let them sort it out
            return (cv[0], cv[1], cv[2])

        elif len(cv) == 2:
            if cv[0] == namespace:
                # namespace is correct, but is the variable defined?
                if self._namespaces[namespace].exists(cv[1]):
                    # yes, it's defined, return the parts
                    return (cv[0], cv[1], None)

                return just_no

            # cv[0] must be the variable name and cv[1] the attribute. Is it defined?
            if self._namespaces[namespace].exists(variable_name):
                # yes, it's defined, and in the right namespace.
                return (namespace, cv[0], cv[1])

            return just_no

        # we have only 1 part, assume it's the variable name. Does it exist in the specified namespace?
        if self._namespaces[namespace].exists(cv[0]):
            # yes, it's there, return the parts
            return (namespace, cv[0], None)

        return just_no

    def isAttribute(self, variable_name, return_elements=False):
        left, right = self._splitNamespace(variable_name)
        if left is None:
            # if this were an attribute, you have to have 2 elements
            return False if not return_elements else (None, None, None)

        left2, right2 = self._splitNamespace(right)
        if left2 is not None and self.exists(variable_name):
            # we have 3 elements here, so this is the right format
            return True if not return_elements else (left, left2, right2)

        # okay, so we have 2 elements, we need to look further
        if left in Namespaces._search_order:
            # this isn't a valid attribute if namespace is valid
            return False if not return_elements else (left, right2, None)

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(left):
                return (ns, left, right)

        raise LogicError("This surely can't happen happened.")

    def getAttribute(self, variable_name, attr_name):
        ns, name = self._splitNamespace(variable_name)
        if ns is not None:
            if ns in Namespaces._search_order:
                if self._namespaces[ns].exists(name):
                    return self._namespaces[ns].getAttribute(name, attr_name)
                
                return "Attribute {}.{} is (undefined)".format(variable_name, attr_name)    # I don't think this will ever happen

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(variable_name):
                return self._namespaces[ns].getAttribute(variable_name, attr_name)

        return "Attribute {}.{} is (undefined)".format(variable_name, attr_name)    # I don't think this will ever happen

    def setAttribute(self, variable_name, attr_name, attr_value):
        ns, name = self._splitNamespace(variable_name)
        if ns is not None:
            if ns in Namespaces._search_order:
                if self._namespaces[ns].exists(name):
                    return self._namespaces[ns].setAttribute(name, attr_name, attr_value)
                
                return "Variable {} is (undefined)".format(variable_name)    # I don't think this will ever happen

        for ns in Namespaces._search_order:
            if self._namespaces[ns].exists(variable_name):
                #print("attribute exists")
                return self._namespaces[ns].setAttribute(variable_name, attr_name, attr_value)

        return "Variable {} is (undefined)".format(variable_name)    # I don't think this will ever happen

    def debugToggle(self, toggle):
        self.debug = toggle
        for ns in Namespaces._search_order:
            self._namespaces[ns].debug = toggle

    def dump(self):
        for ns in Namespaces._search_order:
            self.oprint("{1}\nNAMESPACE: {0}\n{1}".format(ns,'-'*40))
            self._namespaces[ns].dumpVarsAsStrings()

    def dumpVars(self):
        for ns in Namespaces._search_order:
            self.oprint("{1}<br />\nNAMESPACE: {0}<br />\n{1}<br />".format(ns,'-'*40))
            self._namespaces[ns].dumpVars()

    def dumpNamespaces(self, which):
        for item in which:
            if item in self._namespaces:
                self.oprint("{1}<br />\nNAMESPACE: {0}<br />\n{1}<br />".format(item,'-'*40))
                self._namespaces[item].dumpVars(which=which[item])
            else:
                self.oprint("{} is not a valid namespace to dump<br />".format(item))


if __name__ == '__main__':
    print("Library module. Not directly callable.")
