
// Set the defaults for code.dump so I don't have to specify them every time...
@set _id="code.dump" help="False" ns="code" whitespace="True" format="True"

//@var test="{{code.pushlines(t=\"{{self.1}}\n{{self.2}}\n{{self.3}}\n{{self.4}}\")}}"\
    1="{{generic(t=\"**Dump of code.[!code.pushlist.name!]**:\")}}"\
    2="{{box.wc_open}}"\
    3="{{code.dump(name=\"[!code.pushlist.name!]\")}}"\
    4="{{box.wc_close}}"\
    al="1,2,3,4"

@var macrohelp=""\
    1="{{bigmargin._open}}"\
    2="{{section.wc_open(t=\"Macro: code.[!code.pushlist.name!]\")}}"\
    3="{{code.[!code.pushlist.name!].?}}"\
    4="{{generic(t=\"**Dump of code.[!code.pushlist.name!]**:\")}}"\
    5="{{box.wc_open}}"\
    6="{{code.dump(name=\"[!code.pushlist.name!]$\")}}"\
    7="{{box.wc_close}}"\
    8="{{section.wc_close}}"\
    9="{{bigmargin._close}}"\
    attrlist="1,2,3,4,5,6,7,8,9"

@set _="code.pushlist" attrlist="var.macrohelp"

//    name="esc_angles"
//@debug toggle="utility"
[pushlist(name="esc_angles")]
[pushlist(name="get")]
//@debug toggle="utility"
@dump var="test$"
//[test]

[wrap_h.subsect(t="### Escaping and Encoding")]
[bigmargin._open] 
    [section.wc_open(t="Macro: code.esc_angles")]
        [code.esc_angles.?]
        [generic(t="**Dump of code.esc_angles**:")]
        [box.wc_open]
            [code.dump(name="esc_angles")]
        [box.wc_close]
    [section.wc_close]
[bigmargin._close]

[bigmargin._open] 
    [section.wc_open(t="Macro: code.escape")]
        [code.escape.?]
        [code.dump(name="escape")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.escape_var")]
        [code.escape_var.?]
        [code.dump(name="escape_var")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.encodeURL")]
        [code.encodeURL.?]
        [code.dump(name="encodeURL")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.encode_smd")]
        [code.encode_smd.?]
        [code.dump(name="encode_smd")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.encode_smd_var")]
        [code.encode_smd_var.?]
        [code.dump(name="encode_smd_var")]
    [section.wc_close]
[bigmargin._close] 

[wrap_h.subsect(t="### Miscellaneous Helpers")]

[bigmargin._open] 
    [section.wc_open(t="Macro: code.datetime_stamp")]
        [code.datetime_stamp.?]
        [code.dump(name="datetime_stamp")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.dump")]
        [code.dump.?]
        [code.dump(name="dump")]
        **NOTE:** The values for **format**, **whitespace** and **help** above are what is being used for generating the user documentation, and are not necessarily the defaults. Refer to the docs above for the actual defaults.
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.ln_alias")]
        [code.ln_alias.?]
        [code.dump(name="ln_alias")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.repeat")]
        [code.repeat.?]
        [code.dump(name="repeat")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.wrap_stack")]
        [code.wrap_stack.?]
        [code.dump(name="wrap_stack")]
    [section.wc_close]
[bigmargin._close] 

[wrap_h.subsect(t="### Pushing lines onto input stream")]

[bigmargin._open] 
    [section.wc_open(t="Macro: code.equals")]
        [code.equals.?]
        [code.dump(name="equals")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.pushline")]
        [code.pushline.?]
        [code.dump(name="pushline")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.pushlines")]
        [code.pushlines.?]
        [code.dump(name="pushlines")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.pushlist")]
        [code.pushlist.?]
        [code.dump(name="pushlist")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.pushvar")]
        [code.pushvar.?]
        [code.dump(name="pushvar")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.replace")]
        [code.replace.?]
        [code.dump(name="replace")]
    [section.wc_close]
[bigmargin._close] 

[wrap_h.subsect(t="### Specialized get & set variable / attribute values")]

[bigmargin._open] 
    [section.wc_open(t="Macro: code.append")]
        [code.append.?]
        [code.dump(name="append")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.attr_replace")]
        [code.attr_replace.?]
        [code.dump(name="attr_replace")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.attr_replace_str")]
        [code.attr_replace_str.?]
        [code.dump(name="get")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.get")]
        [code.get.?]
        [code.dump(name="get")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.get_value")]
        [code.get_value.?]
        [code.dump(name="get_value")]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="Macro: code.get_default")]
        [code.get_default.?]
        [code.dump(name="get_default")]
    [section.wc_close]
[bigmargin._close] 

[wrap_h.subsect(t="### Specialized get variable / attribute values")]


The import file **[encode_smd(t="<sys.imports>/code.md")]** is where the majority of the [smdcode.b] built-in macros are documented, so we will just embed the file here to review them.

[terminal.wc_open(t="Contents of code.md builtins")]
    @embed "[sys.imports]/code.md" esc="y"
[terminal.wc_close]

