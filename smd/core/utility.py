#!/usr/bin/env python

from .debug import Debug

# These globals are used to hold interfaces to Namespaces, line_cache, etc.
_ns_xface = None
_line_cache = None

# Called during smd initialization to save the interface to Namespaces
def _set_ns_xface(ns_ptr):
    global _ns_xface
    _ns_xface = ns_ptr

# Called during smd initialization to save the interface to the line cache
def _set_line_cache(line_cache_ptr):
    global _line_cache
    _line_cache = line_cache_ptr

def _get_ns_value(v):
    global _ns_xface
    return _ns_xface.getValue(v)

def _get_ns_value_safe(v):
    global _ns_xface
    return _ns_xface.getValue(v) if _ns_xface.exists(v) else None

def _get_debug():
    from .thread import getTLS
    from .constants import Constants
    return getTLS().getObjectFromTLS(Constants.debugTracker).utilityDebug

class HtmlUtils():

    @staticmethod
    def escape_html(s):
        if type(s) != type(''):
            # If we weren't passed a string, convert it to a string before we escape it.
            s = str(s)

        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    @staticmethod
    def escape_html_var(s):
        v = _get_ns_value_safe(s)
        return HtmlUtils.escape_html(v) if v else f"Variable {s} is not defined"

    @staticmethod
    def encode_smd(s):
        if type(s) != type(''):
            # If we weren't passed a string, convert it to a string before we escape it.
            s = str(s)

        return s.replace("[", "&#91;").replace("*", "&#42;").replace("@", "&#64;").replace("++", "&plus;&plus;").replace("~~", "&sim;&sim;")

    @staticmethod
    def encode_smd_var(s):
        v = _get_ns_value_safe(s)
        return HtmlUtils.encode_smd(v) if v else f"Variable {s} is not defined"

    @staticmethod
    def str_to_html_entity_mix(string):
        """
        Encodes a string using decimal or hexadecimal HTML character entities

        Encodes each character of the given string as either a decimal
        or hexadecimal entity, in the hopes of foiling most email address
        harvesting bots.

        Note that running the same string through this function produces
        different results (intentionally). That's good, but it makes testing
        a little more challenging.

        Based on aea_encode_str() PHP function in Till Kruss's WordPress
        Plugin; URI: http://wordpress.org/plugins/email-address-encoder/
        Which is based on Michel Fortin's PHP Markdown:
        http://michelf.com/projects/php-markdown/
        Which is based on John Gruber's original Markdown:
        http://daringfireball.net/projects/markdown/
        Whose code is based on a filter by Matthew Wickline, posted to
        the BBEdit-Talk with some optimizations by Milian Wolff.
        """
        chars = list(string)        # convert string to a list

        from random import randint
        from binascii import crc32
        # generate a pseudo-random seed
        seed = randint(0, int(abs(crc32(str.encode(string)) / len(string))))

        # for each character in the string
        for key in range(len(chars)):
            char = chars[key]
            ordc = ord(char)

            # ascii only
            if ordc < 128:

                r = (seed * (1 + key)) % 100

                if(r > 75 and char not in ['@', '.', ':', ' ']):
                    # if r > 75 and char is not [@.: ], leave it intact
                    pass
                elif (r < 42):
                    # r < 42 encode the character in hex format
                    chars[key] = '&#{};'.format(hex(ordc)[1:])
                else:
                    # otherwise encode it as a decimal number
                    chars[key] = '&#{};'.format(ordc)

        return ''.join(chars)   # return the new encoded string
    @staticmethod
    def encodeURL(url):
        if url.startswith('mailto:'):
            return HtmlUtils.str_to_html_entity_mix(url.replace(" ", "%20"))
        else:
            return url.replace(" ", "%20")




class CodeHelpers():

    @staticmethod
    def wrap_stack(item=None, encode=False):
        from .wrap import WrapperStack
        from .exception import ObjectNotFoundError
        try:
            stack = WrapperStack.getWrapStack()
        except ObjectNotFoundError:
            print("ERROR: Failed getting the wrap stack from the TLS")
            return
        if len(stack) > 0:
            tag = stack[-1]
            if item == '<':
                rs = f"{tag.start}"
            elif item == '>':
                rs = f"{tag.end}"
            elif item == '#':
                rs = f"{len(stack)}"
            else:
                # anything else just return the entire tag
                rs = f"{tag.start}{tag.end}"
            # now format as specified
            print(rs if not encode else HtmlUtils.escape_html(rs))
        else:
            print("" if item != '#' else f"{len(stack)}")   # return an empty string if stack is empty

    @staticmethod
    def b(i):
        return '{{' if i == 0 else '}}'

    @staticmethod
    def split_as(s):
        from .regex import Regex
        r = Regex(r'\s?([\w]+)\s*=\s*\"(.*?)(?<!\\)\"')

        d = {l[0]: l[1] for l in r.regex.findall(s)}
        news = ''
        for i in d:
            news += '***{}***={}<br />'.format(i, HtmlUtils().escape_html(d[i]))

        return news

    @staticmethod
    def get_ns_var(v=None):
        global _ns_xface
        if not _ns_xface:
            print("interface not initialized")
            return

        if not v:
            print("missing variable name")
        elif _ns_xface.exists(v):
            print(_ns_xface.getValue(v))
        else:
            print("{} is undefined.".format(v))


    @staticmethod
    def default(v=None, default_value=""):
        if not v:
            print("existing variable name is required")
            return

        print("{}".format(default_value if not _ns_xface.exists(v) else _ns_xface.getValue(v)))

    @staticmethod
    def append(v=None, text="ns.var.attr"):
        debug = _get_debug()

        fn="append"
        if not v or not _ns_xface.exists(v):
            debug.print(f"{fn}: existing attribute variable name is required: {v}")
            return

        v_ns, v_name, v_attr = _ns_xface.isAttribute(text, True)
        if v_attr is not None:
            v_var = '{}.{}'.format(v_ns, v_name)
            v_val = _ns_xface.getAttribute(v_var, v_attr)
        else:
            v_val = "{} is not a valid attribute".format(text)

        ns, name, attr = _ns_xface.isAttribute(v, True)
        if attr is not None:
            var = '{}.{}'.format(ns, name)
            val = _ns_xface.getAttribute(var, attr) + v_val
            _ns_xface.setAttribute(var, attr, val)
            #print("{}={}+{}".format(v,val,text))
        else:
            debug.print(f"{fn}: Attribute [{v}] is not defined")

    @staticmethod
    def equals(v1=None, v2=None, true=None, false=None):
        def getAttrVal(var):
            v_ns, v_name, v_attr = _ns_xface.isAttribute(var, True)
            if v_attr is not None:
                return _ns_xface.getAttribute('{}.{}'.format(v_ns, v_name), v_attr)
            return None
        
        for v in [v1, v2, true, false]:
            if not v or not _ns_xface.exists(v):
                print("existing attribute variable name is required for {}".format(str(v)))
                return

        v1val = _get_ns_value(v1)   # use getValue so it runs through markdown()
        v2val = _get_ns_value(v2)   # otherwise you can't use indirect values for expressions
        trueval = getAttrVal(true)
        falseval = getAttrVal(false)
        
        if not v1val or not v2val:
            print("v1 and v2 cannot be None ({},{})".format(v1val,v2val))

        if v1val == v2val:
            # if there's no trueval to push, don't push a blank line...
            if trueval:
                CodeHelpers.pushlines(trueval)
        elif falseval:
            # don't push blank lines
            CodeHelpers.pushlines(falseval)
                
    @staticmethod
    def replace(search_str=None, replace_str_var_name=None, attr=None):        
        debug = _get_debug()

        fn="replace"
        for v in [search_str, replace_str_var_name, attr]:
            if not v:
                debug.print(f"{fn}: missing required parameter {str(v)}")
                return

        # Go get the replacement value for "var"
        val_ns, val_name, val_attr = _ns_xface.isAttribute(replace_str_var_name, True)
        if val_attr is None:
            debug.print(f"{fn}: no variable named {replace_str_var_name} was found to get replacement value.")
            return

        repval = _ns_xface.getAttribute('{}.{}'.format(val_ns, val_name), val_attr)

        debug.print(f"{fn}: repval={repval}<br />")
        # Get the string that we're going to operate on
        v_ns, v_name, v_attr = _ns_xface.isAttribute(attr, True)
        if v_attr is None:
            debug.print(f"{fn}: no variable named {attr} was found.")
            return

        repstr = _ns_xface.getAttribute('{}.{}'.format(v_ns, v_name), v_attr)

        debug.print(f"{fn}: search_str={search_str} repstr={repstr}<br />")
        if repstr:
            # make sure we have a valid string to work with
            CodeHelpers.pushlines(repstr.replace(search_str, repval).replace('\\n','\n'))
        else:
            debug.print(f"{fn}: {attr} value is empty; nothing to replace.")

    @staticmethod
    def attr_replace(search_str=None, replace_str_var_name=None, attr=None):        
        debug = _get_debug()

        fn="attr_replace"
        for v in [search_str, replace_str_var_name, attr]:
            if not v:
                debug.print(f"{fn}: missing required parameter {str(v)}")
                return

        # Go get the replacement value for "var"
        val_ns, val_name, val_attr = _ns_xface.isAttribute(replace_str_var_name, True)
        if val_attr is None:
            debug.print(f"{fn}: no variable named {replace_str_var_name} was found to get replacement value.")
            return

        repval = _ns_xface.getAttribute('{}.{}'.format(val_ns, val_name), val_attr)

        debug.print(f"{fn}: repval={repval}<br />")
        # Get the string that we're going to operate on
        v_ns, v_name, v_attr = _ns_xface.isAttribute(attr, True)
        if v_attr is None:
            debug.print(f"{fn}: no variable named {attr} was found.")
            return

        fq_name = f"{v_ns}.{v_name}"
        repstr = _ns_xface.getAttribute(fq_name, v_attr)

        debug.print(f"{fn}: search_str={search_str} repstr={repstr}<br />")
        if repstr:
            # make sure we have a valid string to work with
            _ns_xface.setAttribute(fq_name, v_attr, repstr.replace(search_str, repval).replace('\\n','\n'))
            #new_attr_val = f'@set _="{fq_name}" {v_attr}="{repstr.replace(search_str, repval)}"'
            #CodeHelpers.pushline(new_attr_val)
        else:
            debug.print(f"{fn}: {attr} value is empty; nothing to replace.")

    @staticmethod
    def attr_replace_str(search_str=None, replace_str=None, attr=None):
        debug = _get_debug()

        fn="attr_replace_str"
        for v in [search_str, replace_str, attr]:
            if not v:
                debug.print(f"{fn}: missing required parameter {str(v)}")
                return

        debug.print(f"{fn}: search_str={search_str} --- replace_str={replace_str}")

        # Get the string that we're going to operate on
        v_ns, v_name, v_attr = _ns_xface.isAttribute(attr, True)
        debug.print(f"{fn}: v_ns={v_ns}--v_name={v_name}--v_attr={v_attr}")
        if v_attr is None:
            debug.print(f"{fn}: no variable named {attr} was found.")
            return

        fq_name = f"{v_ns}.{v_name}"
        repstr = _ns_xface.getAttribute(fq_name, v_attr)

        debug.print(f"{fn}: current value for {attr}={repstr}")
        if repstr:
            # make sure we have a valid string to work with
            _ns_xface.setAttribute(fq_name, v_attr, repstr.replace(search_str, replace_str).replace('\\n','\n'))
        else:
            debug.print(f"{fn}: {attr} value is empty; nothing to replace.")

    @staticmethod
    def pushline(s=None):
        debug = _get_debug()
        if s is not None and type(s) is type(''):
            #//TODO: What if I marked the line down here?
            #This would be useful when pushlines pushes multiple lines which
            # would end up allowing other things to resolve... hmmmm.
            debug.print(f"push1:-->{s}<--")
            _line_cache.pushline(s)

    @staticmethod
    def pushlines(s=None):
        #_line_cache.pushline("#### I was passed this: {}".format(HtmlUtils.escape_html(s)))
        debug = _get_debug()
        if s is not None and type(s) is type(''):
            lines = s.split('\n')[::-1]
            for line in lines:
                debug.print(f"push*:-->{line}<--")
                _line_cache.pushline(line)

    @staticmethod
    def pushvar(v=None):

        #_line_cache.pushline("#### I was passed this: {}".format(v))
        if v is not None and type(v) is type(''):
            #_line_cache.pushline("#### get_ns_value returns: {}".format(HtmlUtils.escape_html(_get_ns_value(v))))
            lines = _get_ns_value(v).split('\n')[::-1]
            for line in lines:
                _line_cache.pushline(line)


if __name__ == '__main__':
    print("Library module. Not directly callable.")
