[link.ug_ns_code]
[wrap_h.chapter(t="## The [smdcode.il] Namespace")]

@wrap divx, p

The [smdcode.b] keyword is used to construct a very specialized type of variable for your documents. Like all the other namespaces, these variables can have names that are identical to variables in other namespaces, although it is normally recommended that you avoid doing that. 

[smdcode.b] variables are probably best described as macros, and although the other namespace variables could also be viewed this way, [smdcode.b] variables are much more powerful because they provide a way to construct emitters written in Python! [smdcode.b] macros are used heavily throughout the system builtins to achieve some of the more powerful features of [smd.b].

[bluenote(t="If you are not familiar with Python and Python programming, then you may want to skip this section; it isn't for you. You can still do quite a bit with [smd.b] without having to write extensions in Python.")]

[docthis.open(h="Add this to ns_code-doc.md")]

IDEA: @get _ns="" _id="[ns.]name" raw="true" markdown="false" escape="true"
Implementation: [get_variable_RENAME(v="varname" ret_type="0-raw,1-1st pass markdown-2normal as in full markdown" escape="True|False")]

Should [encode_smd(t="<get>")] and [encode_smd(t="<get_variable>")] be combined? Seems unnecessary to have both of them.

// If the following isn't done/documented, I should move it to a future_list or something...
Can't I also "store" an instance of a variable (like code), that has compiled something that I will use over and over?

The following doesn't work because code doesn't support _inherit (weird). As-is, because you can't _inherit from a different namespace... Actually, mk is part of @var, but there isn't a _last, because that would be part of code.repeat, and it would change. Without a way to force [] to be evaluated at declaration time, this doesn't seem doable...

[code.name.run(parms="")]
@var _="saved_code" _inherit="code.name" _format="{{self.last}}"

Document code.encode_smd

@@[code.encode_smd(t="@dump sysdef=\".\"")][b]

{:.bigandbold}If this is inline, *[code.encode_smd(t="@var name=\"value\" _format=\"# {{self.name}}\"")]*
//@dump code="encode_smd"
//@set _ns="code" _="encode_smd" b="**{{self.run}}(t={{self.t}})**"
//[encode_smd.b(t="[var]")]

document these
//@@[code.escape_var(v="var.bb")]
//@@[code.encode_smd_var(v="var.bb")]

[mk]
@code mk0="" _inherit="code.mk" _format="{{self._last}}"
@var mk1="[code.repeat._last]"
@var mk2="" _inherit="mk"

@dump var="mk" code="mk"

[mk0]
[mk1]

// be sure to test the @code thing where the only way to change attribute defaults is to use @set...

// document that you cannot use () inside parameter strings, as it breaks the parser...
**[encode_smd(t="<var.revision.plain(v=\"1.4.2\")>")]** - Doesn't work
**[encode_smd(t="<var.revision.plain[E.lp]v=\"1.4.2\"[E.rp]>")]** - Works just fine.
// I really wish I could just fix this. What a PITA...


@code _id="esc1"\
      type="eval"\
      src="print('$.url'.replace('<', '&lt;').replace('>','&gt;'))"\
      url="{{self.help}}"\
      help="Usage: {{self._}}.run(url=\"text to escape\")"
@code _id="esc2"\
      type="eval"\
      src="print('{{self.url}}'.replace('<', '&lt;').replace('>','&gt;'))"\
      url="{{self.help}}"\
      help="Usage: {{self._}}.run(url=\"text to escape\")"

[esc1]
[tab.<]-->{{self.help}}
[esc2]
[tab.<]-->Usage: esc2.run(url="text to escape")
@var fu="<cloudylogic.com>"
[esc2(url="{{var.fu}}")]
&lt;cloudylogic.com&gt;
@set _="esc2" a1="<klowrie.net>" a2="{{self.a1}}"
[esc2(url="{{self.a1}}")]
[tab.<]-->&lt;klowrie.net&gt;
[esc2(url="{{self.a2}}")]
[tab.<]-->&lt;klowrie.net&gt;
[esc2(url="$.a2")]
[tab.<]-->{{self.a1}}






[docthis.close]

[link.ug_code_syntax]
[wrap_h.section(t="### [smdcode.il] Syntax")]

[syntax.wc_open(t="[smdcode.il] command syntax")]
    [b]
    [tab.<][smdcode.b] **_id="name" src="value" type="eval | exec" [E.lb]...[E.rb][E.sp]]**[bb][tab.>]
    {:.red}[tab.<][tab.<]NOTE: either underscore [E.apos]**_**[E.apos] or [E.apos]**_id**[E.apos] can be used to name the variable.[tab.>][tab.>]
[syntax.wc_close]

[smdcode.b] variables require that the **[E.lb]*_* or *_id*[E.rb]** special attribute name be used to specify the variable name. In addition to that requirement, [smdcode.b] variables also require two specific public attributes: **src** and **type**. As you might expect, **src** contains the Python source code that will be executed, and **type** specifies either *eval* or *exec*, which are underlying Python concepts. Refer to the Python documentation for the specifics on *eval* vs. *exec* when writing Python code. Let's take a look at an example declaration:

[terminal.wc_open(t="Declaring an [smdcode.il] variable")]
    [sp]
    [smdcode.il] _id="echo" src="print('{{self.text}}')" type="eval" text="[E.ast]text to print[E.ast]"[b]
    [tab.<]**OR**[tab.>][b]
    [smdcode.il] _id="echo" src="print('$.text')" type="eval" text="[E.ast]text to print[E.ast]"
[terminal.wc_close]

[note(t="[smdcode.b] declarations support the shorthand notation **$.attrname** which is identical to **[E.lcb2][_self_].attrname[E.rcb2]**. They can be used interchangably on [smdcode.il] declarations within the **src** attribute only.[bb]Keep in mind, however, that there is a subtle semantic difference between the two syntaxes. In addition to only being valid in the context of the **src** attribute value, if a **$.attrname** reference value contains delayed expansion markdown i.e. [E.lcb2]var.attr[E.rcb2], it will simply be substituted, it will not be marked down.")]

[question(t="Looks like it's only attrs, and furthermore, it's a mesh between the static attrs and the jit_attrs on the markdown call. Starts with static attrs of variable, and then adds/updates those with the values from jit_attrs. Then, any references to $.attr is replaced with value from the temp dict, and then the original dict is restored, but with the side affect of any new attributes becoming sticky... Add unittests to cover all these cases. Does not markdown [E.lcb2]var.attr[E.rcb2]")]

@code _id="echo" src="print('{{self.text}}')" type="eval" text="*text to print*"
//@code _id="echo" src="print('$.text')" type="eval" text="*text to print*")*"

Let's go ahead and write that declaration now using the first style for referencing attributes **{{self.text}}**, and then we'll type **[encode_smd(t="<code.echo>")]** and it will emit: [code.echo]. So far, so good, not too terribly complicated, right? 

Okay, let's do it again, only this time, we'll pass specific text when we write the markdown, like so: **[encode_smd(t="<code.echo[E.lp]text=\"### My Inline Heading\"[E.rp]>")]**, which will give us: [code.echo(text="### My Inline Heading")]. Okay, that's weird, I was expecting an HTML level 3 heading. What happens if I write it again, only this time I'll put the macro at the start of a line:

[code.echo(text="### My Inline Heading")]

Aha! Interesting. While that might seem unique to [smdcode.b] variables, it is not. You can write the same thing as an [smdvar.b] variable, and it will behave similarly. So if it behaves like [smdvar.b] variables, then I should be able to write **[encode_smd(t="<code.echo>")]** again (at the start of the line, of course), and this time it should print the heading without me specifying it (according to the rule that parameters to markdown variables are sticky rule). Let's give that a shot:

[code.echo]

Wait what? It defaulted back to the original declaration's value for **text**. And there's another difference about [smdcode.b] variables. Parameters passed to a markdown instance do not become the new default values for the attributes associated with that variable. So how do I override it without redeclaring the variable? With [smdset.b]. Let's try that:

[terminal.wc_open(t="Changing [smdcode.il] attribute defaults")]
    [encode_smd(t="@set _=\"code.echo\" text=\"### My Inline Heading\"")]
    [encode_smd(t="<code.echo>")]
[terminal.wc_close]

This causes the following to be emitted:
 
@set _="code.echo" text="### My Inline Heading"
[code.echo]

And that's how you change the default values for [smdcode.b] variable attributes.

[wrap_h.subsect(t="###Additional attributes on [smdcode.il] variables")]

[smdcode.b] variables have several unique attributes:

[ulistplain.wc_open]
    **_code** - used by [smdcode.b] to store the compiled Python code.
    **_params_** - used by store the parameters to the current markdown instance
    **_last** - stores the result of the last time the macro was run
    **run** - used to invoke the macro. **[encode_smd(t="<code.echo.run>")]** is the same as **[encode_smd(t="<code.echo>")]**
    **src** - holds the source code in string form.
    **type** - stores the Python type used for evaluating/compiling the code.
[ulistplain.wc_close]

Let's take a quick look at the definition for **code.echo**:

[bmgreybg._open]
@dump code="echo"
[bmgreybg._close]

Accessing these attributes is done the same way as any other namespace. For example:

**[encode_smd(t="<code.echo.src>")]** contains *[code.get_variable(v="code.echo.src" ret_type="0")]* which emits *[code.echo.src]*.
**[encode_smd(t="<code.echo._last>")]** contains *[code.get_variable(v="code.echo._last" ret_type="0")]* which emits *[code.echo._last]*.

**_last** just provides a convenient way to access the value output of the last time the code was run by the Python interpreter, avoiding having to run it again to get the same value. You might find this useful at times.

Let's update our **echo** variable by adding the following **help** attribute and changing the default for **text** to reference it (by the way, this is how most of the [smdcode.b] system built-ins are declared):

@set _="code.echo" text="{{self._help}}" _help="{{self._}}(text=\"*text to print*\")"
[terminal.wc_open(t="Adding a default help string to an [smdcode.il] variable")]
    [encode_smd(t="@set _=\"code.echo\" text=\"[E.lcb2][_self_]._help[E.rcb2]\" _help=\"[E.lcb2][_self_]._[E.rcb2][E.lp]\\\"[E.ast]text to print[E.ast]\\\"[E.rp]\"")][b]
    [encode_smd(t="<code.echo._help>")] emits [code.echo._help]
    [encode_smd(t="<code.echo.?>")] emits [code.echo.?]
[terminal.wc_close]

If you create your own [smdcode.b] macros, it's a good idea to create a default help string for it so that anyone trying to use it will see how it works. That someone might just be you, and you'll be glad you did!

Let's take a look at one more declaration: 

[tab.<]**[smdcode.il] _id="esc_angles" type="eval" src="print('{{self.url}}'.replace('<', '[E.amp]lt;').replace('>', '[E.amp]gt;'))" url="{{self._help}}" _help="Usage: code.esc_angles.run(url="text to escape"**[tab.>]

And now we write the following markdown:
[terminal.wc_open(t="")]
    [smdcomment.b] Because **url** has not been set yet, it will default to the built-in help string
    [e_var.b(t="code.esc_angles")] emits *[code.esc_angles]*[b]
    **[E.lb]code.esc_angles(url="[E.lt]https://google.com[E.gt]")]** emits *[code.esc_angles(url="<https://google.com>")]*.
[terminal.wc_close]

As it turns out, **code.esc_angles** is actually one of the built-in [smdcode.b] macros provided by [smd.b]. 

[bmgreybg._open]
@dump code="esc_angles"
[encode_smd(t="<esc_angles._help>")] emits [b][esc_angles._help]
[encode_smd(t="<esc_angles.?>")] emits [b][esc_angles.?]
[bmgreybg._close]

We will see the rest of built-in macros later in the chapter.

[wrap_h.subsect(t="### Inheriting attributes")]

[smdcode.b] variables do **not** support the **_inherit** attribute when declaring new variables.

[link.ug_code_names]
[wrap_h.section(t="### [smdcode.il] Variable names")]

Variable names in the [smdcode.b] namespace are restricted to the same requirements as the other namespaces, e.g. [link.ug_var_names.link].

[link.ug_code_attrs]
[wrap_h.section(t="### [smdcode.il] Built-in Attributes")]

In addition to the specific attributes covered above, [smdcode.b] variables support the underlying built-in attributes of all namespaces. They can be useful to assist in debugging complex declarations. Refer to the [link.ug_var_attrs.link] section for all of the details of the built-in attributes.

[link.ug_code_builtins]
[wrap_h.section(t="### [smdcode.il] Built-in Macros")]

[smdcode.b] provides a number of useful builtins to assist with creating more complex markdown documents. In this section, we'll take a closer look at what's available, and see how they can be used in your own documents.

// Set the defaults for code.dump so I don't have to specify them every time...
@set _id="code.dump" help="False" ns="code" whitespace="True" format="True"

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
    attrlist="1,2,3,4,5,6,7,8,9"\
    al_part1="1,2,3"\
    al_part2="4,5,6,7"\
    al_part3="8,9"

@set _="code.pushlist" attrlist="var.macrohelp"

[wrap_h.subsect(t="### Escaping and Encoding")]

[pushlist(name="esc_angles")]
[pushlist(name="escape")]
[pushlist(name="escape_var")]
[pushlist(name="encodeURL")]
[pushlist(name="encode_smd")]
[pushlist(name="encode_smd_var")]

[wrap_h.subsect(t="### Miscellaneous Helpers")]

[pushlist(name="datetime_stamp")]
[pushlist(name="dump" attrlist="var.macrohelp.al_part1")]
[pushlist(name="dump" attrlist="var.macrohelp.al_part2")]
**NOTE:** The values for **format**, **whitespace** and **help** above are what is being used for generating the user documentation, and are not necessarily the defaults. Refer to the docs above for the actual defaults.
[pushlist(name="dump" attrlist="var.macrohelp.al_part3")]

[pushlist(name="ln_alias")]
[pushlist(name="repeat")]
[pushlist(name="wrap_stack")]

[wrap_h.subsect(t="### Pushing lines onto input stream")]

[pushlist(name="equals")]
[pushlist(name="pushline")]
[pushlist(name="pushlines")]
[pushlist(name="pushlist")]
[pushlist(name="pushvar")]
[pushlist(name="replace")]

[wrap_h.subsect(t="### Specialized get & set variable / attribute values")]

[pushlist(name="append")]
[pushlist(name="attr_replace")]
[pushlist(name="attr_replace_str")]
[pushlist(name="get")]
[pushlist(name="get_variable")]
[pushlist(name="get_default")]

[wrap_h.subsect(t="### Specialized get variable / attribute values")]


The import file **[encode_smd(t="<sys.imports>/code.md")]** is where the majority of the [smdcode.b] built-in macros are documented, so we will just embed the file here to review them.

[terminal.wc_open(t="Contents of code.md builtins")]
    @embed "[sys.imports]/code.md" esc="y"
[terminal.wc_close]



[link.ug_code_misc]
[wrap_h.subsect(t="### [smdcode.il] Miscellaneous Examples")]

Here are just a few examples to help drive home your understanding of the declaration and usage of variables in the [smdcode.b] namespace.


This can let you build some really cool automation in your documents. But you need one more thing before you get started. A way to change one or more attributes of an existing variable in any namespace. Enter [smdset.b] and the **_null_** attribute.

[repeat(t="%" c="42")]



[terminal.wc_open(t="Using _format on [smdhtml.il] and [smdlink.il]")]
    [sp]
    [smdcomment] declare [E.apos]fu[E.apos] in [smdcode.il], [smdhtml.il] & [smdlink.il]
    [smdcode_wp(parms="_id=\"fu\" _format=\"bar\"")]
    [smdhtml_wp(parms="_id=\"fu\" _format=\"bar\"")]
    [smdlink_wp(parms="_id=\"fu\" _format=\"bar\"")]
    [sp]
    @var _id="fu" _format="bar"
    @html _id="fu" _format="bar"
    @link _id="fu" _format="bar"
    [smdcomment] now print each one
    [e_var(t="var.fu")] emits *[var.fu]*
    [e_var(t="html.fu")] emits *[html.fu]*
    [e_var(t="link.fu")] emits *[link.fu]*
    [smdcomment] Redefine html.fu and link.fu
    @html _id="fu"
    @link _id="fu"
    [smdcomment] now print each one
    [e_var(t="var.fu")] emits *[var.fu]*
    [e_var(t="html.fu")] emits *[escape_var(v="html.fu")]*
    [e_var(t="link.fu")] emits *[escape_var(v="link.fu")]*

[terminal.wc_close]


[terminal.wc_open(t="Updating attribute values with [smdset.il]")]
    [smdcomment_wp(parms="First, let[E.apos]s declare a new variable called [E.apos]fu[E.apos]")]
    [smdcode_wp.b(parms="fu=\"bar\" attr1=\"value1\"")]
    @var fu="bar" attr1="value1"
    [e_var.b(t="fu.attr1")] emits **[fu.attr1]**

    [sp]
    [smdcomment_wp(parms="using [smdset.il], change the value of attr1 to [E.apos]value2[E.apos]")]
    [smdset_wp.b(parms="_=\"fu\" attr1=\"value2\"")]
    @set _="fu" attr1="value2"
    [e_var.b(t="fu.attr1")] emits **[fu.attr1]**

    [sp]
    [smdcomment_wp(parms="using the _null_ attribute, change the value of attr1 to [E.apos]value3[E.apos]")]
    [e_var.b(t="fu._null_[E.lp]attr1=\"value3\"[E.rp]")]
    [fu._null_(attr1="value3")]
    [e_var.b(t="fu.attr1")] emits **[fu.attr1]**

[terminal.wc_close]

[note(t="The **_null_** attribute illustrates an important concept with the attributes of variables in [smd.b]. That is, any time an attribute value is changed by specifying a new value when a method is invoked, that value becomes the new value for that attribute. This is true with all namespaces except [smdcode.b]; in the [smdcode.b] namespace, attribute values overridden via a method invocation are temporary. Once the method returns, the original attribute values are restored.[bb]As previously mentioned, the only way to change the value of a variable in the [smdcode.b] namespace is by using [smdset.b]. When this is done, the code behind the variable (Python source code) is recompiled, which essentially updates their usage in the compiled code stored as part of the variable.")]

You can also add new attributes to an existing variable with [smdset.b]. And, if you [smdset.b] a variable that does not exist, [smdset.b] will create it. Let[E.apos]s see both of these things in action now.

[terminal2.wc_open(t="Adding attributes with [smdset.il]")]
    [terminal2.wc_open_content]
        [smdcomment_wp.il(parms="add a new attribute to [E.apos]fu[E.apos] using [smdset.il]")]
        [smdset_wp.b(parms="_=\"fu\" attr2=\"value42\"")]
        @set _="fu" attr2="value42"
        [e_var.b(t="fu.attr2")] emits **[fu.attr2]**
        [sp]
        [smdcomment_wp.il(parms="adding a new attribute doesn[E.apos]t affect existing attributes in [E.apos]fu[E.apos]")]
        [e_var.b(t="fu.attr1")] still emits **[fu.attr1]**

        [sp]
        [smdcomment_wp.il(parms="using the _null_ attribute, add attr3 to [E.apos]fu[E.apos]")]
        [e_var.b(t="fu._null_[E.lp]attr3=\"many ways to add attributes\"[E.rp]")]
        [fu._null_(attr3="many ways to add attributes")]
        [e_var.b(t="fu.attr3")] emits **[fu.attr3]**

        [sp]
        [smdcomment_wp.il(parms="We can also add and update variables at the same time")]
        [e_var.b(t="fu._null_[E.lp]attr3=\"update 3rd attribute\" attr4=\"add 4th attribute\"[E.rp]")]
        [fu._null_(attr3="update 3rd attribute" attr4="add 4th attribute")]
        [e_var.b(t="fu.attr3")] emits **[fu.attr3]** and [e_var.b(t="fu.attr4")] emits **[fu.attr4]**

        [sp]
        [smdcomment_wp.il(parms="We can also add and update variables at the same time using [smdset.b]")]
        [smdset_wp.b(parms="_=\"fu\" attr2=\"update attr2\" attr6=\"6th attribute\"")]
        @set _="fu" attr2="update attr2" attr6="6th attribute"
        [e_var.b(t="fu.attr2")] emits **[fu.attr2]** and [e_var.b(t="fu.attr6")] emits **[fu.attr6]**
    [terminal2.wc_close_content]
[terminal2.wc_close]

Let's dump the variable 'fu' to see all the attributes and their values.


[bmgreybg._open] 
[var.source.wc_open(t="Current definition of [E.apos]fu[E.apos] variable")]
@dump var="fu$"
[var.source.wc_close]
[bmgreybg._close]

And finally, you can also specify the namespace two different ways with [smdset.b]. Witness:

[terminal.wc_open(t="Specifying the namespace")]

    [smdcomment_wp(parms="Specify the namespace with @set; don[E.apos]t leave it to chance!")]
    [smdset_wp.b(parms="*_ns=\"var\"* _=\"fu\" attr6=\"update attr6\"")]
    @set _ns="var" _="fu" attr6="update attr6"
    [e_var.b(t="fu.attr6")] emits **[fu.attr6]**
    [sp]
    [smdcomment_wp(parms="Alternate method to set namespace")]
    [smdset_wp.b(parms="_=\"*var.*fu\" attr6=\"update attr6 again!\"")]
    @set _="var.fu" attr6="update attr6 again!"
    [e_var.b(t="fu.attr6")] emits **[fu.attr6]**

[terminal.wc_close]

One last time let's dump the variable 'fu' to see all the attributes and their values.

[bmgreybg._open] 
[var.source.wc_open(t="Current definition of [E.apos]fu[E.apos] variable")]
@dump var="fu$"
[var.source.wc_close]
[bmgreybg._close]

Here are just a few examples to help drive home your understanding of the declaration and usage of variables in the [smdcode.b] namespace.

[note(t="[smdcode.b] attributes cannot be changed via _null_ or when markdown is applied. You must use [smdset.b] to do that")]

