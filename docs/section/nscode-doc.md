[link.ug_ns_code]
[wrap_h.chapter(t="## The [smdcode.il] Namespace")]

@wrap divx, p

The [smdcode.b] keyword is used to construct a very specialized type of variable for your documents. Like all the other namespaces, these variables can have names that are identical to variables in other namespaces, although it is normally recommended that you avoid doing that. 

[smdcode.b] variables are probably best described as macros, and although the other namespace variables could also be viewed this way, [smdcode.b] variables are much more powerful because they provide a way to construct emitters written in Python! [smdcode.b] macros are used heavily throughout the system builtins to achieve some of the more powerful features of [smd.b].

[bluenote(t="If you are not familiar with Python and Python programming, then you may want to skip this section; it isn't for you. You can still do quite a bit with [smd.b] without having to write extensions in Python.")]

[link.ug_code_syntax]
[wrap_h.section(t="### [smdcode.il] Syntax")]

[syntax.wc_open(t="[smdcode.il] command syntax")]
    [b]
    [tab.<][smdcode.b] **_id="name" src="value" type="eval | exec" [E.lb]...[E.rb][E.sp]]**[bb][tab.>]
    {:.red}[tab.<][tab.<]NOTE: either underscore [E.apos]**_**[E.apos] or [E.apos]**_id**[E.apos] can be used to name the variable.[tab.>][tab.>]
[syntax.wc_close]

[smdcode.b] variables require that the [big.multi(t="_" cls=".green.bold.italic")] or [big.multi(t="_id")] special attribute name be used to specify the variable name. In addition to that requirement, [smdcode.b] variables also require two specific public attributes: [big.multi(t="src")] and [big.multi(t="type")]. As you might expect, [big.multi(t="src")] contains the Python source code that will be executed, and [big.multi(t="type")] specifies either *eval* or *exec*, which are underlying Python concepts. Refer to the Python documentation for the specifics on *eval* vs. *exec* when writing Python code. Let's take a look at an example declaration:

[terminal.wc_open(t="Declaring an [smdcode.il] variable")]
    [sp]
    [smdcode.il] _id="echo" src="print('{{self.text}}')" type="eval" text="[E.ast]text to print[E.ast]"[b]
    [tab.<]**OR**[tab.>][b]
    [smdcode.il] _id="echo" src="print('$.text')" type="eval" text="[E.ast]text to print[E.ast]"
[terminal.wc_close]

[note(t="[smdcode.b] declarations support the shorthand notation **$.attrname** which is identical to **[E.lcb2][_self_].attrname[E.rcb2]**. They can be used interchangably on [smdcode.il] declarations within the **src** attribute only.[bb]Keep in mind, however, that there is a subtle semantic difference between the two syntaxes. In addition to only being valid in the context of the **src** attribute value, if a **$.attrname** reference value contains delayed expansion markdown i.e. [E.lcb2]var.attr[E.rcb2], it will simply be substituted, it will not be marked down.")]

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

[code.pushlist(attrlist="var.dumpit" \
               nsvar="code" \
               nsname="echo$" \
               title="Definition for **code.echo**")]

Accessing these attributes is done the same way as any other namespace. For example:

**[encode_smd(t="<code.echo.src>")]** contains *[code.get_value(v="code.echo.src" ret_type="0")]* which emits *[code.echo.src]*.
**[encode_smd(t="<code.echo._last>")]** contains *[code.get_value(v="code.echo._last" ret_type="0")]* which emits *[code.echo._last]*.

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
    *[smdcomment.b] Because **url** has not been set yet, it will default to the built-in help string*
    [sp]
    [e_var.b(t="code.esc_angles")] emits *[code.esc_angles]*[b]
    **[E.lb]code.esc_angles(url="[E.lt]https://google.com[E.gt]")]** emits *[code.esc_angles(url="<https://google.com>")]*.
[terminal.wc_close]

As it turns out, **code.esc_angles** is actually one of the built-in [smdcode.b] macros provided by [smd.b]. 

[code.pushlist(attrlist="var.dumpit" \
               nsvar="code" \
               nsname="esc_angles$" \
               title="Definition for **code.esc_angles**")]

[terminal.wc_open(t="Reviewing the builtin help for **esc_angles**")]
    *[smdcomment.il] Value of **_help** has been suppressed from the dump above. It follows:*[b]
    **_help=**[get_value(v="code.esc_angles._help" ret_type="0" escape="True" esc_smd="True")][b]
    **[encode_smd(t="<esc_angles._help>")]** emits [b][esc_angles._help][b]
    **[encode_smd(t="<esc_angles.?>")]** emits [b][esc_angles.?]
[terminal.wc_close]

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
[wrap_h.section(t="### [smdcode.il] Built-in Macros Help Section")]

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
[pushlist(name="attr_replace_value")]
[pushlist(name="get")]
[pushlist(name="get_value")]
[pushlist(name="get_default")]

[wrap_h.subsect(t="### Contents of the code.md builtins file")]


The import file **[encode_smd(t="<sys.imports>/code.md")]** is where the majority of the [smdcode.b] built-in macros are documented, so we will just embed the file here to review them.

[terminal.wc_open(t="Contents of code.md builtins")]
    @embed "[sys.imports]/code.md" esc="y"
[terminal.wc_close]

[link.ug_code_misc]
[wrap_h.subsect(t="### A few more things about [smdcode.il]")]

[TODO] FINISH THIS SECTION

Here are just a few more things about the [smdcode.b] namespace to help drive home your understanding of the declaration and usage of variables within it.

[smdcode.b] attributes cannot be changed via _null_ or when markdown is applied. You must use [smdset.b] to do that

Not specific to [smdcode.b], but you'll likely encounter it here: You cannot use () inside parameter strings, as it breaks the parser... Workaround using the **E.lp/E.rp** constants.

Which leads to this issue: you cannot nest markdown variables that require parameters... they require that you use () inside parameter strings... no workaround for this right now.

Here's an example:

**[encode_smd(t="<var.revision.plain(v=\"1.4.2\")>")]** - Doesn't work
**[encode_smd(t="<var.revision.plain[E.lp]v=\"1.4.2\"[E.rp]>")]** - Works just fine.

//[docthis.open(h="Add this to ns_code-doc.md")]
//[docthis.close]


