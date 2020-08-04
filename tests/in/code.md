@import "$/testsetup.md"

[var.testdoc_nw.begin(title="code.md" desc="Testing @code namespace")]

@var ns="code"

//TODO: What is _raw attribute for? Look at all the _element_partials. Need to make sure everything is covered in testing...

@wrap divx,p
@import "$/nsbasic.md"
@parw

[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Re-Testing creating names with invalid characters</h4>")]

Test @[ns] with no parameters[b]
@[ns]
[code.pushline(t="@[ns] src=\"print()\" type=\"eval\"")]

These first ones will fail in AdvancedNamespace().addVariable() because the dictionary will be empty[b]

@[ns] @="syntax" src="print()" type="eval"
@[ns] +="syntax" src="print()" type="eval"
@[ns] ^="syntax" src="print()" type="eval"
@[ns] $="syntax" src="print()" type="eval"
@[ns] ©="syntax" src="print()" type="eval"

Now create a new variable with 25 attributes (by redefining an existing variable)

@[ns] _="id2" 01="1" 02="2" 03="3" 04="4" 05="5" 06="6" 07="7" 08="8" 09="9" 10="10"\
             11="11" 12="12" 13="13" 14="14" 15="15" 16="16" 17="17" 18="18" 19="19" 20="20" 21="21" 22="22" 23="23" 24="24" 25="25" src="print(\"test\")" type="eval"
**Added 25 new attributes to id2. It now equals**[b]
[code.dump(ns="[ns]" name="id2" format="True" whitespace="True")] 

[plain(t="Testing @code builtin functions")]

### In this section, add tests to exercise all macros in the **code.md** built-ins.

@var div_helper="{{self._all_keys_}}"\
    macro="macro.name"

// You have to use [!!] to set macro so it will expand before {{div_helper._null}} is processed, resulting in [code.pushlist.name] being what macro is set to...
@var dividers="{{self._all_keys_}}"\
    1="{{wrap_h.hash2}}"\
    2="@wrap divx,p"\
    3="{{div_helper._null_(macro=\"[!code.pushlist.name!]\")}}"\
    4="Testing {{var.div_helper.macro}}"\
    5="{{var.div_helper.macro}} testing complete"\
    6="@parw"\
    7="{{wrap_h.hash3}}"\
    start="1,2,3,4"\
    end="5,6,7"

//[code.dump(ns="var", name="div_helper" format="True" whitespace="True")]

[code.pushlist(name="code.esc_angles" attrlist="var.dividers.start")]

[ln_factory(nm="ln_esc_angles" hr="https://www.test.com" t="Test Site")]
[ln_esc_angles] = [ln_esc_angles._asurl]
[esc_angles(url="<this is just text with angle brackets>")]
[esc_angles(url="<https://test.domain.com?parameter1>")]
[pushlist(attrlist="var.dividers.end")]

[code.pushlist(name="code.escape" attrlist="var.dividers.start")]
**escape** and **escape_var** get used quite a bit in the **wrap-doc.md** user guide chapter, which is included by the **tests/in/wrap.md**, so they both get good coverage.[b]
[escape(t="<https://test.domain.com?parameter1&parameter2>")]
[pushlist(attrlist="var.dividers.end")]


@html _="blockquote" cite="url-goes-here"
[code.pushlist(name="code.escape_var" attrlist="var.dividers.start")]
    [terminal.wc_open(t="Examples")]
        [e_var.b(t="html.blockquote")] *=* [escape_var(v="html.blockquote")]
        [e_var.b(t="html.blockquote.<")] *=* [escape_var(v="html.blockquote.<")]
        [e_var.b(t="html.blockquote.>")] *=* [escape_var(v="html.blockquote.>")]
        [e_var.b(t="html.blockquote.<+")] *=* [escape_var(v="html.blockquote.<+")]
    [terminal.wc_close]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.encodeURL" attrlist="var.dividers.start")]
**encodeURL** is thoroughly tested already. The underlying Python function is used by variable.py when returning _public_attrs_ and it detects *href* in an @link request.[bb]It is also tested in **tests/mailto.md** encoding URLs with spaces, and two mailto: samples, one with just an email address, and another with a parameter with spaces.
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.encode_smd" attrlist="var.dividers.start")]
**encode_smd** is used throughout the documentation and unit tests, so only minimal testing is needed for it. The main thing to capture here is how you cannot use inline markdown in the string to encode, because it will be marked down before being passed to the macro, which will then proceed to encode the HTML as SMD...

@var A="answers" y="- **right**" n="- *wrong*"
[encode_smd(t="@wrap **is**")] [A.n]
[encode_smd(t="@wrap [E.ast2]is[E.ast2]")] [A.y]

[encode_smd(t="++wrong++ : ~~wrong~~ : *wrong* : ***wrong***")] [A.n]
[encode_smd(t="[E.ins]right[E.ins] : [E.del]right[E.del] : [E.ast]right[E.ast] : [E.ast3]right[E.ast3]")] [A.y]

[encode_smd(t="<var.attr(p1=\"v1\")>")] [A.n]
[encode_smd(t="<var.attr[E.lp]p1=\"v1\"[E.rp]>")] [A.y]

[encode_smd(t="< > 2{ 2} * @ 2+ 2~")] [A.y]

[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.encode_smd_var" attrlist="var.dividers.start")]

@var encode_var_tests="public keys - {{self._public_keys_}}"\
    1="<var.attr(p1=\"v1\")>"\
    2="@wrap **is**"\
    3="< > 2{ 2} * @ 2+ 2~"\
    4="[E.ins]right[E.ins] : [E.del]right[E.del] : [E.ast]right[E.ast] : [E.ast3]right[E.ast3]"\
    5="++wrong++ : ~~wrong~~ : *wrong* : ***wrong***"

[encode_var_tests]
[encode_smd_var(v="encode_var_tests.1")] [A.y]
[encode_smd_var(v="encode_var_tests.2")] [A.n]
[encode_smd_var(v="encode_var_tests.3")] [A.y]
[encode_smd_var(v="encode_var_tests.4")] [A.y]
[encode_smd_var(v="encode_var_tests.5")] [A.n]

[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.datetime_stamp" attrlist="var.dividers.start")]
**datetime_stamp** is already unit tested in multiple places.
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.repeat" attrlist="var.dividers.start")]
**repeat** is already unit tested in multiple places.
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.get" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.get_value" attrlist="var.dividers.start")]

[b]Get **section** variable[b]
0=[get_value(v="section", ret_type="0")]
1=[get_value(v="section", ret_type="1")]
2=[get_value(v="section", ret_type="2")]
3=[get_value(v="section", ret_type="3" esc_smd="True")]
9=[get_value(v="section", ret_type="9" escape="True")]

[b]Get **_section_div_** variable[b]
0=[get_value(v="_section_div_", ret_type="0")]
1=[get_value(v="_section_div_", ret_type="1")]
2=[get_value(v="_section_div_", ret_type="2")]
3=[get_value(v="_section_div_", ret_type="3" escape="True")]
9=[get_value(v="_section_div_", ret_type="9" escape="True")]

[b]Get **_section_div_.[E.lt]** variable[b]
0=[get_value(v="_section_div_.<", ret_type="0")]
1=[get_value(v="_section_div_.<", ret_type="1")]
2=[get_value(v="_section_div_.<", ret_type="2")]
3=[get_value(v="_section_div_.<", ret_type="3" escape="True")]
9=[get_value(v="_section_div_.<", ret_type="9" escape="True")]

[b]Get **_section_div_.[E.lt]+** variable[b]
0=[get_value(v="_section_div_.<+", ret_type="0")]
1=[get_value(v="_section_div_.<+", ret_type="1")]
2=[get_value(v="_section_div_.<+", ret_type="2")]
3=[get_value(v="_section_div_.<+", ret_type="3" escape="True")]
9=[get_value(v="_section_div_.<+", ret_type="9", escape="True" )]

[b]Get **dividers** variable[b]
0=[get_value(v="dividers", ret_type="0")]
1=[get_value(v="dividers", ret_type="1")]
2=[get_value(v="dividers", ret_type="2")]
3=[get_value(v="dividers", ret_type="3")]
9=[get_value(v="dividers", ret_type="9")]

//[code.dump(ns="var" name="dividers" format="True" whitespace="True")]
[b]Get **dividers.4** variable[b]
0=[get_value(v="dividers.4", ret_type="0")]
1=[get_value(v="dividers.4", ret_type="1")]
2=[get_value(v="dividers.4", ret_type="2" esc_smd="True")]
3=[get_value(v="dividers.4", ret_type="3" esc_smd="True")]
9=[get_value(v="dividers.4", ret_type="9")]

[b]Get **dividers.4** variable with escape="True"[b]
0=[get_value(v="dividers.4", ret_type="0" escape="True")]
1=[get_value(v="dividers.4", ret_type="1" escape="True")]
2=[get_value(v="dividers.4", ret_type="2" esc_smd="True")]
3=[get_value(v="dividers.4", ret_type="3" esc_smd="True")]
9=[get_value(v="dividers.4", ret_type="9" escape="True")]

[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.get_default" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.pushline" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.pushlines" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.pushvar" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[pushlist(name="code.ln_alias" attrlist="var.dividers.start")]

//@dump link="ln_factory" code="ln_alias"
@dump link="lntest"
[ln_factory(nm="lntest" hr="https://google.com" t="Google")]
@dump link="lntest"
[lntest]
[ln_alias(nm="lntest" attr="_alt" lt="Alternate Google Attribute")]
@dump link="lntest"
[lntest._alt]

[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.append" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.equals" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[pushlist(name="code.wrap_stack" attrlist="var.dividers.start")]

// Change the default encoding of output from wrap_stack to True so the HTML tags are not interpreted by the browser
@set _id="code.wrap_stack" encode="True"

[divxp.open]
Initially, the wrap_stack should be empty: "[code.wrap_stack]"
[divxp.close]

@wrap divx, p
And now we are changing it to the more traditional "@wrap divx, p": "[code.wrap_stack]"

Next up, we will turn off @wrap, and see that we are clear.

@wrap nop
This should not be wrapped.
@parw

@@[code.wrap_stack(w="<", encode="False")]
@@And this should be wrapped, even though we said it was raw, because previously, we emitted the open tag via code.wrap_stack(w="<")...
@@[code.wrap_stack(w=">", encode="False")]

And now we are back to normal, as we emitted the close tag via code.wrap_stack(w=">")

@@[code.wrap_stack(w="*", encode="False")]
There should be an empty div before this because we emitted the entire wrap tag sequence with code.wrap_stack(w="*")

@parw

[pushlist(attrlist="var.dividers.end")]

[code.pushlist(name="code.replace" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.attr_replace" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.attr_replace_str" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.dump" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.pushlist" attrlist="var.dividers.start")]
[pushlist(attrlist="var.dividers.end")]


[code.pushlist(name="code.split_as" attrlist="var.dividers.start")]
**Is this even used any more?**
[pushlist(attrlist="var.dividers.end")]


// ------------------------------------

[code.pushlist(name="code.NEXT" attrlist="var.dividers.start")]

[pushlist(attrlist="var.dividers.end")]


[plain(t="Testing adding new @code builtins")]


[var.plain(t="User manual sections for @code")]

@import "[sys.root]/docs/userdocs_macros.md"

[var.toc.wc_open(t="Table of Contents - Unittest [smdcode.il]")]
@wrap nop
[b]
@import "[sys.root]/docs/section/nscode-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from nscode-inc.md")]
@dump link="^ug_ns_code|ug_code_"

@import "[sys.root]/docs/section/nscode-doc.md"

@set dump_ns_list="[ns]=\".\" help=\"f\""

[var.testdoc_nw.end]
