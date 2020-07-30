// ns needs to be set to a valid namespace
// maybe add [code.defined("variable", trueLine2push, falseline2push)]

// because this is shared code, we don't want to rely on the shorthand notation '@ns name="value"' in here...
//@var __stop_cmd="{{code.pushline(\"@stop\")}}"
//@set _ns="code" _id="equals" true="{{code.pushline(\"@stop\")}}, false="Testing namespace {{ns}}")]}}
//[code.equals(v1="[var.ns._format]", v2="")]

@var _id="in_code_namespace" \
    code="code"\
    namespace="[ns]"\ 
    _format="{{code.equals(v1=\"self.code\", v2=\"self.namespace\", true=\"self.true\", false=\"self.false\")}}"\
    true="in code namespace"\
    false=""

[var.in_code_namespace(true="We are testing the <em><strong>@code</strong></em> namespace" false="We are not testing the <em><strong>@code</strong></em> namespace")]


@var dump="dump [ns]"

[plain(t="Generic Namespace testing for ***@[ns]*** namespace")]


@[ns] _="a1" _format="a1_rval"
@[ns] _="a2"
@[ns] _id="a3"
@[ns] _id="a4" _format="a4_rval"
[code.encode_smd(t="<<ns>.a1>")] --> [[ns].a1]
[code.encode_smd(t="<2{ns2}.a2>")] --> [[ns].a2]
[code.encode_smd(t="<2{ns2}.a3]")] --> [[ns].a3]
[code.encode_smd(t="<[ns].a4>")] --> [[ns].a4]

[hash3]
### Old school way of encoding SMD
[E.lb][E.lb]ns].a1] --> [[ns].a1]
[E.lb][ns].a2] --> [[ns].a2]

### And now just trying all the combinations...
[code.encode_smd(t="2{<ns>.a12}")] --> {{[ns].a1}}  -- Delayed expansion ***{{}}*** does not work inline
[code.encode_smd(t="<<ns>.a1>")] --> [[ns].a1]
[code.encode_smd(t="<2{ns2}.a1>")] --> [{{ns}}.a1] -- Delayed expansion ***{{}}*** does not work inline


[hash3]


Setting default rvalue for a2 and a3
@set _ns="[ns]" _id="a2" _format="a2_rval"
@set _ns="[ns]" _id="a3" _format="a3_rval"
[code.encode_smd(t="[<ns].a2]")] --> [[ns].a2]
[code.encode_smd(t="[<ns].a3]")] --> [[ns].a3]

@[dump] = "^a[0-9]{1,2}$"

//Okay, escaped versions are not printing escaped because the changes to markdown [] and {{}} in parameters has broken it.
// Feeble attempts to fix follow, but likely going to need to add "encode" or something to code.get_variable as a way to
// mask the \" in the string so it will print as expected. If I ever care enough that this works...
//
//@var private_esc="{{code.get_variable(v=\"invalid-attribute._private_attrs_esc_\" escape=\"True\")}}"
//PE=[private_esc]
//

// attempt to add all the reserved attributes
//TODO: should I account for _ns in the reserved list? It is now an option to @SET, but stripped out before creating the variable
@[ns] _="invalid-attribute" _private_attrs_="no" _public_attrs_="no" _private_attrs_esc_="no" _public_attrs_esc_="no" _public_keys_="no" _private_keys_="no" _all_attrs_="no" _all_attrs_esc_="no" _null_="no" _rval="no" _code="used by code ns" _params_="used by code ns" _last="used by code ns" run="code.var.run" public="yes" not_private="yes" src="print('required for code')" type="eval" _help="*{{self._}}this is line 1 help text*<br />**line2** help text." 
@[dump] = "invalid"
***public*** = [invalid-attribute._public_attrs_]
***public_esc*** = [invalid-attribute._public_attrs_esc_]
[var.in_code_namespace(true="***private*** = cannot print, has instance data" false="***private*** = [invalid-attribute._private_attrs_]")]
[var.in_code_namespace(true="***private_esc*** = cannot print, has instance data" false="***private_esc*** = [invalid-attribute._private_attrs_esc_]")]
[var.in_code_namespace(true="***all_attrs*** = cannot print, has instance data" false="***all_attrs*** = [invalid-attribute._all_attrs_]")]
[var.in_code_namespace(true="***all_attrs_esc*** = cannot print, has instance data" false="***all_attrs_esc*** = [invalid-attribute._all_attrs_esc_]")]
***public_keys*** = [invalid-attribute._public_keys_]
***private_keys*** = [invalid-attribute._private_keys_]
***null*** = [invalid-attribute._null_]
***rvalue*** = [invalid-attribute._rval]
***run*** = [invalid-attribute.run]
***_code*** = [invalid-attribute._code]
***_params_*** = [invalid-attribute._params_]
***_last*** = [invalid-attribute._last]
***_help*** = [invalid-attribute._help]
***?*** = [invalid-attribute.?]
***??*** = [invalid-attribute.??]
***_last*** = [invalid-attribute._last]
***_rval*** on legitimate variable = [a4._rval]
***No help available*** on legitimate variable = [a4.?]
***[a4._help]*** on legitimate variable = [a4._help]

[invalid-attribute._null_(not_private="YES")]
invalid-attribute.not_private = [invalid-attribute.not_private]

[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Testing creating names with invalid characters</h4>")]

Test @[ns] with no parameters
@[ns]
[code.pushline(t="@[ns]")]

These first ones will fail in AdvancedNamespace().addVariable() because the dictionary will be empty
@[ns] @="syntax"
@[ns] +="syntax"
@[ns] ^="syntax"
@[ns] $="syntax"
@[ns] ©="syntax"

These next ones will have the namespace parser  catch the errors and fail the variable creation.

[var.in_code_namespace(true="@[ns] _=\"1\" _format=\"1_rval\" src=\"test\" type=\"eval\"" false="@[ns] _=\"1\" _format=\"1_rval\"")]
[var.in_code_namespace(true="@[ns] _=\"@\" src=\"test\" type=\"eval\"" false="@[ns] _=\"@\"")]
[var.in_code_namespace(true="@[ns] _=\"a b\" _format=\"syntax\" src=\"test\" type=\"eval\"" false="@[ns] _=\"a b\" _format=\"syntax\"")]

//@[ns] _="1" _format="1_rval"
//@[ns] _id="@"
//@[ns] _="a b" _format="syntax"

@var expr="usage: var.testline(line=\"line to evaluate\")" \
     line="the line for non-code namespaces" \
     code="{{self.line}} src=\"print()\" type=\"eval\""

// This is another way I was trying to simplify and not have to specify the test line twice, but you get side affects
// because if you put variables in the expression, they expand when the macro runs due to the indirection, so not quite there...
[var.expr._null_(line="@[ns] _=\"b1\" _format=\"mix of attrs\" 123attr=\"nope\"")]
[var.in_code_namespace(true="[!var.expr.code!]" false="[!var.expr.line!]")]

@set _="code.dump" format="True" whitespace="True"
[code.dump(ns="var" name="expr")]
--> [get_variable(v="var.expr.line" ret_type="0")]
--> [get_variable(v="var.expr.code" ret_type="0")]

@[dump] = "b" help="f"

[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Testing creating variables with delayed expansion of other variables</h4>")]

These next 3 illustrate the issue described above. There is no way to get c0.a to evaluate when the test is run,
because when [bb].code=*[var.expr.code]* or [b].[ns]=*[var.expr.line]*[bb]are evaluated, they are expanded at the time, and that changes behavior
[var.expr._null_(line="@[ns] _=\"c0\" _format=\"constants\" a=\"1\" b=\"2\" c=\"3\"")]
[var.in_code_namespace(true="{{var.expr.code}}" false="{{var.expr.line}}")]
[divx.<][p.<]
[code.dump(ns="[ns]" name="c0")]

[var.expr._null_(line="@[ns] _=\"c1\" _format=\"[!c0.a!]\"")]
[var.in_code_namespace(true="{{var.expr.code}}" false="{{var.expr.line}}")]

[code.dump(ns="[ns]" name="c1")]

[var.expr._null_(line="@[ns] _=\"c2\" _format=\"{{c0.a}}\"")]
[var.in_code_namespace(true="{{var.expr.code}}" false="{{var.expr.line}}")]

[code.dump(ns="[ns]" name="c2")]
[p.>][divx.>]

[encode_smd(t="[<ns].c1]")] = [var.in_code_namespace(true="[![!ns!].c1._format!]" false="[[ns].c1]")]
[encode_smd(t="[<ns].c2]")] = [var.in_code_namespace(true="[![!ns!].c2._format!]" false="[[ns].c2]")]

[var.in_code_namespace(true="@[ns] _=\"c0\" _format=\"constants\" a=\"1\" b=\"2\" c=\"3\" src=\"print()\" type=\"eval\"" false="@[ns] _=\"c0\" _format=\"constants\" a=\"1\" b=\"2\" c=\"3\"")]
[var.in_code_namespace(true="@[ns] _=\"c1\" _format=\"[c0.a]\" src=\"print()\" type=\"eval\"" false="@[ns] _=\"c1\" _format=\"[c0.a]\"")]
[var.in_code_namespace(true="@[ns] _=\"c2\" _format=\"{{c0.a}}\" src=\"print()\" type=\"eval\"" false="@[ns] _=\"c2\" _format=\"{{c0.a}}\"")]
[encode_smd(t="[<ns].c1]")] = [[ns].c1] or [[ns].c1._format]
[encode_smd(t="[<ns].c2]")] = [[ns].c2] or [[ns].c2._format]

@[dump] = "c[0-9]{1,2}"

@set _ns="[ns]" _="c0" a="9"

@[dump] = "c[0-9]{1,2}"

@set _ns="[ns]" _="c0" a="8" _format="Constants"

//TODO: still not the behaviour I expected. c1 is 1, but now c2 is also 1. Delayed expansion fixed, but now new problem takes its place
[encode_smd(t="<c1]")] = [c1]
[encode_smd(t="<c2]")] = [c2]

@[dump] = "c[0-9]{1,2}"

[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Testing creating variables with references to instance variables</h4>")]

@set _ns="[ns]" _="c2" attr1="*attribute 1*" attr2="**attribute 2**" attr3="{{self.attr1}}--{{self.attr2}}" attr4="[self.attr2]--[self.attr1]"
[encode_smd(t="<c2.attr1]")] = [c2.attr1]
[encode_smd(t="<c2.attr2]")] = [c2.attr2]
[encode_smd(t="<c2.attr3]")] = [c2.attr3]
[encode_smd(t="<c2.attr4]")] = [c2.attr4]

@[dump] = "c[0-9]{1,2}"


[wrap_h.hash2]

This will test changing a variable's attributes using @set
@var ENC="{{code.encode_smd(t=\"&nbsp;{{self.c}}\")}}" c="[smd_markdown_here]"
Current value for [encode_smd(t="<ENC>")]=*[ENC]*

### Create new variable using @set

Make sure variable d0 doesn't exist...
@[dump] = "^d[0-9]{1,2}$"
@dump  var="ENC"

@var code_helper="{{self.attrs_code}}" attrs_code="src=\"print(12345)\" type=\"eval\"" attrs_other=""

[var.in_code_namespace(false="@set _=\"code_helper\" _format=\"{{var.code_helper.attrs_other}}\"" true="")]
@dump var="code_"
// We can change the 'c' attribute of the ENC variable and it will recompile the code for us...
// We will also change _format, because we don't want to encode the line, we want it to actually get parsed...
@set _ns="var" _="ENC" c="@set _ns=\"[ns]\" _=\"d0\" _format=\"d0_rval\"" _format="{{self.c}} {{var.code_helper}}"

**Now create the variable using [ENC]**
//The next line will actually expand to: @set _ns="[ns]" _="d0" _format="d0_rval"
[ENC]
@[dump] = "^d[0-9]{1,2}$"
@dump  var="ENC"
New value for [encode_smd(t="<ENC>")]=*[ENC]*

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

[pushline(t="@set _ns=\"[ns]\" _id=\"id1\" attr1=\"New Value\" [var.code_helper]")]

@[dump] = "^id1$"
ATTR1 should be "New Value":
[id1]

[wrap_h(t="[hash3]")]
@set _ns="[ns]" _id="id1" foo="bar"
**Added foo attribute to id1. Now id1 has values**
[id1]
@[dump] = "^id1$"

@set _ns-"[ns]" _id="id1" foo="nubar" bar="oldfu"
**Added bar attribute to id1. Now id1 is**
[id1]
@[dump] = "^id1$"

//@set _ns="[ns]" _id="id2" foo="nubar" bar="oldfu" src="print(\"test\")" type="eval"
[pushline(t="@set _ns=\"[ns]\" _id=\"id2\" foo=\"nubar\" bar=\"oldfu\" {{var.code_helper}}")]
**Created id2 with same attributes as id1 except ATTR1. *id2* =**
[[ns].id2]
@[dump] = "^id2$"

@[ns] _="id2" 01="1" 02="2" 03="3" 04="4" 05="5" 06="6" 07="7" 08="8" 09="9" 10="10"\
             11="11" 12="12" 13="13" 14="14" 15="15" 16="16" 17="17" 18="18" 19="19" 20="20" 21="21" 22="22" 23="23" 24="24" 25="25"
**Added 25 new attributes to id2. It now equals**
[[ns].id2]
@[dump] = "^id2$"

@set _ns="[ns]" _id="id2" 01="x1" 02="x2" 03="x3" 04="x4" 05="x5" 06="x6" 07="x7" 08="x8" 09="x9" 10="x10"\
                          11="x11" 12="x12" 13="x13" 14="x14" 15="x15" 16="x16" 17="x17" 18="x18" 19="x19" 20="x20"

**Changed some of the new attributes so their value has an *x* in front. It now equals**
[[ns].id2]
@[dump] = "^id2$"

