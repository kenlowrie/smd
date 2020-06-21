// ns needs to be set to a valid namespace
// maybe add [code.defined("variable", trueLine2push, falseline2push)]

// because this is shared code, we don't want to rely on the shorthand notation '@ns name="value"' in here...
//@var __stop_cmd="{{code.pushline(\"@stop\")}}"
//@set _ns="code" _id="equals" true="{{code.pushline(\"@stop\")}}, false="Testing namespace {{ns}}")]}}
//[code.equals(v1="[var.ns._format]", v2="")]

@var dump="dump [ns]"

[plain(t="Generic Namespace testing for ***@[ns]*** namespace")]


@[ns] _="a1" _format="a1_rval"
@[ns] _="a2"
@[ns] _id="a3"
@[ns] _id="a4" _format="a4_rval"
[code.encode_smd(t="[[ns].a1]")] --> [[ns].a1]
[code.encode_smd(t="[[ns].a2]")] --> [[ns].a2]
[code.encode_smd(t="[[ns].a3]")] --> [[ns].a3]
[code.encode_smd(t="[[ns]._a4]")] --> [[ns]._a4]
Setting default rvalue for a2 and a3
@set _ns="[ns]" _id="a2" _format="a2_rval"
@set _ns="[ns]" _id="a3" _format="a3_rval"
[code.encode_smd(t="[[ns].a2]")] --> [[ns].a2]
[code.encode_smd(t="[[ns].a3]")] --> [[ns].a3]

@[dump] = "^a[0-9]{1,2}$"

// attempt to add all the reserved attributes
//TODO: should I account for _ns in the reserved list? It is now an option to @SET, but stripped out before creating the variable
@[ns] _="invalid-attribute" _private_attrs_="no" _public_attrs_="no" _private_attrs_esc_="no" _public_attrs_esc_="no" _public_keys_="no" _private_keys_="no" _all_attrs_="no" _all_attrs_esc_="no" _null_="no" _rval="no" public="yes" not_private="yes"
@[dump] = "invalid"
***public*** = [invalid-attribute._public_attrs_]
***public_esc*** = [invalid-attribute._public_attrs_esc_]
***private*** = [invalid-attribute._private_attrs_]
***private_esc*** = [invalid-attribute._private_attrs_esc_]
***all_attrs*** = [invalid-attribute._all_attrs_]
***all_attrs_esc*** = [invalid-attribute._all_attrs_esc_]
***public_keys*** = [invalid-attribute._public_keys_]
***private_keys*** = [invalid-attribute._private_keys_]
***null*** = [invalid-attribute._null_]
***rvalue*** = [invalid-attribute._rval]
***_rval*** on legimate variable = [_a4._rval]

[invalid-attribute._null_(not_private="YES")]
invalid-attribute.not_private = [invalid-attribute.not_private]

[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Testing creating names with invalid characters</h4>")]

Test @[ns] with no parameters
@var
[code.pushline(t="@var")]

These first ones will fail in AdvancedNamespace().addVariable() because the dictionary will be empty
@[ns] @="syntax"
@[ns] +="syntax"
@[ns] ^="syntax"
@[ns] $="syntax"
@[ns] ©="syntax"

These next ones will have the namespace parser  catch the errors and fail the variable creation.

@[ns] _="1" _format="1_rval"
@[ns] _id="@"
@[ns] _="a b" _format="syntax"

// Should I force attribute names to conform to the variable naming convention? start with [a-zA-Z_] and then only contain [-\w]?

@[ns] _="b1" _format="mix of attrs" 123attr="nope"
@[dump] = "b"

[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Testing creating variables with delayed expansion of other variables</h4>")]

@[ns] _="c0" _format="constants" a="1" b="2" c="3"
@[ns] _="c1" _format="[c0.a]"
@[ns] _="c2" _format="{{c0.a}}"

[encode_smd(t="[[ns].c1]")] = [[ns].c1]
[encode_smd(t="[[ns].c2]")] = [[ns].c2]

@[dump] = "c[0-9]{1,2}"

@set _ns="[ns]" _="c0" a="9"

@[dump] = "c[0-9]{1,2}"

@set _ns="[ns]" _="c0" a="8" _fmt="Constants"

//TODO: not the behaviour I expected. Thought c1 would have still been 1. Looks like delayed expansion my be the default behavior...
[encode_smd(t="[c1]")] = [c1]
[encode_smd(t="[c2]")] = [c2]


[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Testing creating variables with references to instance variables</h4>")]

@set _="c2" attr1="*attribute 1*" attr2="**attribute 2**" attr3="{{self.attr1}}--{{self.attr2}}" attr4="[self.attr2]--[self.attr1]"
[encode_smd(t="[c2.attr1]")] = [c2.attr1]
[encode_smd(t="[c2.attr2]")] = [c2.attr2]
[encode_smd(t="[c2.attr3]")] = [c2.attr3]
[encode_smd(t="[c2.attr4]")] = [c2.attr4]

@[dump] = "c[0-9]{1,2}"


[wrap_h.hash2]

//TODO: Seems like this should be somewhere common...
@var ENC="[code.encode_smd(t=\"&nbsp;{{self.c}}\")]" c="[smd_markdown_here]"

### Create new variable using @set

Make sure variable d0 doesn't exist...
@[dump] = "^d[0-9]{1,2}$"

// We can change the 'c' attribute of the ENC variable and it will recompile the code for us...
@set _ns="var" _="ENC" c="@set _ns=\"[ns]\" _=\"d0\" _format=\"d0_rval\""
**Now create the variable using [ENC]**
@set _ns="[ns]" _="d0" _format="d0_rval"
@[dump] = "^d[0-9]{1,2}$"

**And change its default value**
@set _ns="[ns]" _="d0" _format="d0_rval+"
@[dump] = "^d[0-9]{1,2}$"

**Now update d0 by adding the attribute newattr to @[ns] d0**
@set _="d0" newattr="newly added attribute"
@[dump] = "^d[0-9]{1,2}$"

**Now add the attribute extraattr to @[ns] d0, and change newattr = fubar**
@set _="d0" newattr="fubar" extraattr="{{self.newattr}}"
@[dump] = "^d[0-9]{1,2}$"

d0.extraattr = **[d0.extraattr]**
Changing d0.newattr="newval"
@set _="d0" newattr="newval"
Which now causes d0.extraattr to have a new value = **[d0.extraattr]**

//TODO:
can we remove an attribute?

//TODO: Make sure I document how if a variable has no _format attribute, when you reference it w/o an attribute qualifier, it dumps all attributes...
@set _id="id1" attr1="New Value"
@[dump] = "^id1$"
ATTR1 should be "New Value":
[id1]

[wrap_h(t="[hash3]")]
@set _id="id1" foo="bar"
**Added foo attribute to id1. Now id1 has values**
[id1]
@set _id="id1" foo="nubar" bar="oldfu"
**Added bar attribute to id1. Now id1 is**
[id1]
@set _ns="[ns]" _id="id2" foo="nubar" bar="oldfu"
**Created id2 with same attributes as id1 except ATTR1. *id2* =**
[id2]
@[ns] _="id2" 01="1" 02="2" 03="3" 04="4" 05="5" 06="6" 07="7" 08="8" 09="9" 10="10"\
             11="11" 12="12" 13="13" 14="14" 15="15" 16="16" 17="17" 18="18" 19="19" 20="20" 21="21" 22="22" 23="23" 24="24" 25="25"
**Added 25 new attributes to id2. It now equals**
[id2]
@set _ns="[ns]" _id="id2" 01="x1" 02="x2" 03="x3" 04="x4" 05="x5" 06="x6" 07="x7" 08="x8" 09="x9" 10="x10"\
                          11="x11" 12="x12" 13="x13" 14="x14" 15="x15" 16="x16" 17="x17" 18="x18" 19="x19" 20="x20"

**Changed some of the new attributes so their value has an *x* in front. It now equals**
[id2]


