#!/usr/bin/env python

from __future__ import print_function

from .utility import HtmlUtils
from .exception import LogicError

"""

"""

class Variable(object):
    private = '_private_attrs_'
    public = '_public_attrs_'
    public_keys = '_public_keys_'
    private_keys = '_private_keys_'
    all = '_all_attrs_'
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

        return self.rval.copy()

    def getAttrsAsString(self, which):
        attrsDict = self.getAttrsAsDict(which)
        attrs = ''
        for item in attrsDict:
            attrs += ' {}="{}"'.format(item, attrsDict[item])

        return attrs

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
    _special_attributes = [Variable.public, Variable.private, Variable.public_keys, Variable.private_keys, Variable.all, Variable.null]

    """Class to abstract a dictionary of variables"""
    def __init__(self, markdown, oprint):
        self.vars = {}
        self._md_ptr = markdown
        self.oprint = oprint
        self._debug = False

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, args):
        self._debug = True

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

    def getPublicAttrsDict(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsDict(Variable.public)

    def getPublicAttrs(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsString(Variable.public)

    def getPublicKeys(self, name):
        if self.exists(name):
            return self.vars[name].getKeysAsString(Variable.public)

    def getPrivateAttrsDict(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsDict(Variable.private)

    def getPrivateAttrs(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsString(Variable.private)

    def getPrivateKeys(self, name):
        if self.exists(name):
            return self.vars[name].getKeysAsString(Variable.private)

    def getAllAttrs(self, name):
        if self.exists(name):
            return self.vars[name].getAttrsAsString(Variable.all)

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
        elif which == Variable.public_keys:
            return self.getPublicKeys(variable)
        elif which == Variable.private_keys:
            return self.getPrivateKeys(variable)

        raise LogicError("Oops. Special attribute {} isn't valid for {}".format(which, variable))

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

    @property
    def namespace(self):
        return self._namespace


class BasicNamespace(Namespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(BasicNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        #print("BASIC: My NS is: {}".format(self.namespace))
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

    """
    """
    def _stripNamespace(self, id):
        if id.startswith(self.namespace):
            return id[len(self.namespace):]

        return id

    def exists(self, name):
        #print("basic: {}".format(name))
        #if name == 'class':
        #    raise NameError("WTF, How did I get here?")
        return super(BasicNamespace, self).exists(self._stripNamespace(name))

    def getValue(self, name):
        return super(BasicNamespace, self).getValue(self._stripNamespace(name))


class AdvancedNamespace(Namespace):
    _variable_name_str = ["_id", "_"]
    _default_format_attr = '_format'
    _inherit_attr = '_inherit'

    def __init__(self, markdown, namespace_name, oprint):
        super(AdvancedNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)

    def _missingID(self, dict, which="ADD"):
        self.oprint("{}: Dictionary is missing {}<br />{}<br />".format(which, AdvancedNamespace._variable_name_str, dict))

    def getIDstring(self, dict):
        for id in AdvancedNamespace._variable_name_str:
            if id in dict:
                return id
        return None

    def inheritsFrom(self, dict):
        return True if AdvancedNamespace._inherit_attr in dict else False

    def addVariable(self, dict, name=None):
        myID = self.getIDstring(dict)
        if myID is None:
            self._missingID(dict)
            return

        varID = dict[myID]
        del dict[myID]
        
        if self.inheritsFrom(dict):
            rval = self.getRVal(dict[AdvancedNamespace._inherit_attr])
            tempDict = rval.copy() if rval is not None else {"_format": "***{}*** does not exist".format(dict[AdvancedNamespace._inherit_attr])}
            for item in dict:
                if item != AdvancedNamespace._inherit_attr:
                    tempDict[item] = dict[item]
            dict = tempDict

        super(AdvancedNamespace, self).addVariable(self.unescapeStringQuotes(dict), varID)
        return varID

    def updateVariable(self, dict, name=None):
        myID = self.getIDstring(dict)
        if myID is None:
            self._missingID(dict, "UPDATE")
            return

        varID = dict[myID]
        if varID not in self.vars:
            return self.addVariable(dict)

        del dict[myID]
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
        id0, el0 = self._parseVariable(id)
        if el0 is not None:
            # _parseVar() only returns both elements if the attribute exists
            return True

        return id0 in self.vars

    def getVarID(self, id):
        id0, el0 = self._parseVariable(id, True)
        return id0 if el0 is not None else id

    def getValue(self, id):
        id0, el0 = self._parseVariable(id)
        if el0 is not None:
            # If they are asking for the special name (_, _id)
            if el0 in AdvancedNamespace._variable_name_str:
                # return the variable name itself, no markdown.
                return id0

            if el0 in VariableStore._special_attributes:
                # should this be marked down? Probably.
                return self._markdown(self.getSpecialAttr(el0, id0))

            # TODO: When test code in place, I need to remove this and see what happens.
            #       Feels a bit like a side affect...
            # First, apply standard markdown in case _format has regular variables in it.
            fmt_str = self._markdown(self.vars[id0].rval[el0]).replace('{{','[').replace('}}',']')
            # And now, markdown again, to expand the self. namespace variables
            #print("SETTING SELF to: {}{}".format(self.namespace,id0))
            #if self.namespace == 'image.' and id0 == 'v0':
                #raise NameError("WTF")
            return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))

        if self.exists(id0):
            # if the special _format element exists, return it with markdown applied
            fmt = AdvancedNamespace._default_format_attr
            if fmt in self.vars[id0].rval:
                #print("RETURNING _format()")
                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = self._markdown(self.vars[id0].rval[fmt]).replace('{{','[').replace('}}',']')
                # And now, markdown again, to expand the self. namespace variables
                return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))

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
        
        for var in sorted(self.vars):
            if reObj.is_match(var) is None:
                continue
            dict_str = '<br />'
            for d_item in self.vars[var].rval:
                dict_str += '&nbsp;&nbsp;<strong>{}=</strong>{}<br />\n'.format(d_item, HtmlUtils.escape_html(self.vars[var].rval[d_item]))
            self.oprint("{2}<strong>{0}=</strong>{1}<br />".format(var, dict_str, indent))

class VarNamespace(AdvancedNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(VarNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)

        #print("VAR: My NS is: {}".format(self.namespace))



class ImageNamespace(AdvancedNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        super(ImageNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        #print("IMAGE: My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None):
        var_name = super(ImageNamespace, self).addVariable(dict)

        if not super(ImageNamespace, self).exists('{}.{}'.format(var_name, AdvancedNamespace._default_format_attr)):
            super(ImageNamespace, self).addAttribute(var_name,AdvancedNamespace._default_format_attr,'<{{self._tag}}{{self._public_attrs_}}/>')

        if not super(ImageNamespace, self).exists('{}.{}'.format(var_name, '_tag')):
            super(ImageNamespace, self).addAttribute(var_name,'_tag','img')


class HtmlNamespace(AdvancedNamespace):
    _start = '<'
    _end = '>'
    _element_partials = [_start, _end]

    def __init__(self, markdown, namespace_name, oprint):
        super(HtmlNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        #print("HTML: My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None):
        var_name = super(HtmlNamespace, self).addVariable(dict)

        if not super(HtmlNamespace, self).exists('{}.{}'.format(var_name, AdvancedNamespace._default_format_attr)):
            super(HtmlNamespace, self).addAttribute(var_name,AdvancedNamespace._default_format_attr,'<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>')

        return var_name

    def _isSpecial(self, attr):
        if attr in HtmlNamespace._element_partials:
            return True

        return super(HtmlNamespace, self)._isSpecial(attr)

    def getElementPartial(self, which):
        if which == HtmlNamespace._start:
            # TODO: should do error checking here (make sure _tag is defined?)
            return '<{0}self._tag{1}{0}self.{2}{1}>'.format('{{', '}}', Variable.public)
        elif which == HtmlNamespace._end:
            # TODO: should do error checking here (make sure _tag is defined?)
            return '</{{self._tag}}>'

        raise

    def getValue(self, id):
        id0, el0 = self._parseVariable(id)
        #print("HTML.getValue({},{},{})".format(id,id0,el0))
        if el0 is not None:
            if el0 in HtmlNamespace._element_partials:

                # First, apply standard markdown in case _format has regular variables in it.
                fmt_str = self._markdown(self.getElementPartial(el0).replace('{{','[').replace('}}',']'))
                # And now, markdown again, to expand the self. namespace variables
                #print("LINK: {}".format(self.namespace))
                return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace,id0)))

        return super(HtmlNamespace, self).getValue(id)


class LinkNamespace(HtmlNamespace):
    def __init__(self, markdown, namespace_name, oprint):
        var_name = super(LinkNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)
        #print("LINK: My NS is: {}".format(self.namespace))

    def addVariable(self, dict, name=None):
        var_name = super(LinkNamespace, self).addVariable(dict)

        if not super(LinkNamespace, self).exists('{}.{}'.format(var_name, '_tag')):
            super(LinkNamespace, self).addAttribute(var_name,'_tag','a')

class CodeNamespace(AdvancedNamespace):
    _run = 'run'
    _params_ = '_params_'
    _defaults_ = '_defaults_'
    #_locals_ = '_locals_'
    _element_partials = [_run]

    def __init__(self, markdown, namespace_name, oprint):
        super(CodeNamespace, self).__init__(markdown, namespace_name, oprint)  # Initialize the base class(es)

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
        with stdoutIO() as s:
            try:
                exec(dict['_code']) if dict['type'] == 'exec' else eval(dict['_code'])
            except Exception as e:
                exceptionMessage = "{}".format(str(e))

        #print('>>>>>>>>>>>{}{}'.format(type(s.getvalue()),s.getvalue()))
        if exceptionMessage: self.oprint("<br />\n<strong><em>Exception:</em> {}</strong><br />\n<strong>src=</strong>{}<br />".format(exceptionMessage, dict['src']))
        return s.getvalue().rstrip()

    def addVariable(self, dict, name=None):
        var_name = super(CodeNamespace, self).addVariable(dict)

        """
        [code.ref.exec] - returns exec(_code)
        [code.ref.eval] - returns eval(_code)
        """
        dict = super(CodeNamespace, self).getRVal(var_name)
        if 'src' not in dict or 'type' not in dict:
            print('CODE namespace requires src= and type= attributes')
            return

        if dict['type'] not in ['exec', 'eval']:
            print('CODE namespace type= must be either "exec" or "eval"')
            return

        # TODO: Fix this so it doesn't compile here or getvalue.
        #       That should be done inside ExecutePython
        #       And that is only needed during execution, not during ADD
        
        # Compile a string for now, it isn't needed until the variable is expanded.
        src = 'print("<strong>raw src=</strong>{}")'.format(dict['src'].replace('"','\\"'))
        if self.debug: print("Compiling CODE(av) src={}<br />".format(src))
        dict['_code'] = compile(src, '<string>', dict['type'])
        dict['last'] = self.executePython(dict)
        

    # When you have special attributes for your class, you have to define your own
    # _isSpecial, so you can check yours before passing it along to the sub classes.
    def _isSpecial(self, attr):
        if attr in CodeNamespace._element_partials:
            return True

        return super(CodeNamespace, self)._isSpecial(attr)

    def exists(self, id):
        id0, el0 = self._parseVariable(id)
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
        if self.debug: print("CODE.getValue({},{},{})<br />".format(id,id0,el0))
        if el0 is None or el0 == CodeNamespace._run:
            # Get the dictionary (not a copy, the actual dictionary, so if you change it, your changing it. Got it? Good.)
            dict = super(CodeNamespace, self).getRVal(id0)

            # TODO: Don't hard code what's be skipped over
            # Build a dictionary of the attrs that need to be restored after we process this getValue()
            restoreValues = {key: value for (key, value) in dict.items() if key not in ['_code', 'last', '_params_']}
            if self.debug: self.oprint("Saving these: {}<br />".format(restoreValues))

            if self.debug: self.oprint("START CODE(gv) src={}<br />".format(dict['src']))

            # Shouldn't this always be true? Doesn't jit_attrs() add this, always?
            if CodeNamespace._params_ in dict:
                params = dict[CodeNamespace._params_]
                if self.debug: self.oprint("PARAMS: {}<br />".format(params))
                for var in params:
                    if self.debug: self.oprint("REP: {} with {}<br />".format(var, params[var]))
                    dict[var] = params[var]


            # Need to expand any variables inside src... (referencing self. overwrites _params_ :(
            src = super(CodeNamespace, self).getValue('{}.src'.format(id0))
            if self.debug: self.oprint("Markdown CODE(src)={}<br />\nDICT={}<br />".format(src, dict))

            # TODO: Is this working right? If new attrs are added, they'll be sticky. Is that okay?
            # Now build a dictionary of the attrs that need substitution (if present) in the src code
            replaceValues = {key: value for (key, value) in dict.items() if key not in ['_code', '_params_']}

            # Now translate $.attr to values from the replaceValues dictionary
            src = xlat_parameters(src, replaceValues)

            # Finally, compile it and execute it
            if self.debug: self.oprint("Compiling CODE(gv) src={}<br />".format(src))
            dict['_code'] = compile(src, '<string>', dict['type'])
            dict['last'] = self.executePython(dict)

            # And now, put back the attributes as they were on entrance. This is a requirement for @code vars.
            # The only way to change an attribute is to use @set (TODO: test that theory)
            for key in restoreValues:
                if self.debug: self.oprint("RES: {} with {}<br />".format(key, restoreValues[key]))
                dict[key] = restoreValues[key]

            return dict['last']

        return super(CodeNamespace, self).getValue(id)


class Namespaces(object):
    _default = 'basic'
    _html = 'html'
    _var = 'var'
    _link = 'link'
    _image = 'image'
    _code = 'code'
    _search_order = [_default, _var, _image, _link, _html, _code]

    def __init__(self, markdown, setNSxface, oprint=print):
        self._debug = False
        self._namespaces = {
            Namespaces._default: BasicNamespace(markdown, Namespaces._default, oprint),
            Namespaces._html: HtmlNamespace(markdown, Namespaces._html, oprint),
            Namespaces._var: VarNamespace(markdown, Namespaces._var, oprint),
            Namespaces._image: ImageNamespace(markdown, Namespaces._image, oprint),
            Namespaces._link: LinkNamespace(markdown, Namespaces._link, oprint),
            Namespaces._code: CodeNamespace(markdown, Namespaces._code, oprint),
        }
        #for ns in self._namespaces:
        #    print("Namespace for {} is set to {}".format(ns, self._namespaces[ns].namespace))

        self.oprint = oprint
        setNSxface(self)

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, args):
        self._debug = True

    def addVariable(self, value, name=None, ns=None):
        if ns is None:
            ns = Namespaces._default

        if ns not in self._namespaces:
            #TODO: Raise exception
            raise

        self._namespaces[ns].addVariable(value, name)

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
            #TODO: Raise exception
            raise

        self._namespaces[ns].updateVariable(value, name)

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
        #print("INSIDE GV: {}".format(variable_name))

        def addJITattrs(jit_attrs, ns, var):
            if ns == Namespaces._default:
                # TODO: Should I print a message or something?
                return  # For now, just return. Basic namespace doesn't support attrs...

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
                    #if self.debug: self.oprint("jit_attrs is NONE<br />")
                    jit_attrs = {}
                # Make a temp dictionary with "_" and "_params_" keys
                params = {CodeNamespace._params_: jit_attrs, 
                          '_': self._namespaces[ns].getVarID(var)}
                # Add _params_ to the variable dictionary
                #if self.debug: self.oprint("Adding/Updating _params_ to: {}<br />".format(params))
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
