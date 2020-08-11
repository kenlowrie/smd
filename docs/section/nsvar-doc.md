
[link.ug_ns_var]
[wrap_h.chapter(t="## The [smdvar.il] Namespace")]

The [smdvar.il] keyword is used to construct a more flexible type of variable for your documents. These variables are stored in the [smdvar.b] namespace, and can have names that are identical to variables in other namespaces, although it is normally recommended that you avoid doing that. 

We will discuss this namespace first, because it is the basis for all namespaces, and most of the features, syntax and semantics apply to the others. Given that, it is a great starting point for our discussion on creating variables for use in [smd.b] documents.

[link.ug_var_syntax]
[wrap_h.section(t="### [smdvar.il] Syntax")]

[syntax.wc_open(t="[smdvar.il] command syntax")]
    [b]
    [tab.<][smdvar.b] **name="value" [E.lb] attr="value" [E.lb]...]&nbsp;]**[bb][tab.>]
    [tab.<][smdvar.b] **_id="name" [E.lb]_format="value" [E.lb]...[E.rb][E.sp]]**[bb][tab.>]
    {:.red}[tab.<][tab.<]NOTE: either underscore [E.apos]**_**[E.apos] or [E.apos]**_id**[E.apos] can be used to name the variable.[tab.>][tab.>]
[syntax.wc_close]

[smdvar.b] variables are the only ones that can use the shorthand **name="value"** notation when defining a variable. All the other namespaces require that the **[E.lb]*_* or *_id*[E.rb]** special attribute name be used to specify the variable name.  Note that when the shorthand notation is used, it is the first **name="value"** pair that will be used to name the variable. Each of the following examples does exactly the same thing:

[terminal.wc_open(t="Declaring a variable")]
[sp]
[smdvar_wp(parms="fu=\"bar\"")]
[smdvar_wp(parms="_=\"fu\" _format=\"bar\"")]
[smdvar_wp(parms="_id=\"fu\" _format=\"bar\"")]
[sp]
[terminal.wc_close]

Essentially, declaring a variable in *any* of the namespaces is done in exactly this fashion. ***@ns*** followed by a series of attribute="value" pairs. Remember, only [smdvar.b] allows the shorthand **fu="bar"** format for naming the variable and setting the **_format** attribute value. All other namespaces require the alternate format. In addition, namespaces based on [smdhtml.b] and [smdcode.b] normally do not specify **_format**, since that attribute is constructed on the fly during the declaration ([smdhtml.b]) or is not used ([smdcode.b]). More on that later.

[note.wc_open]
NOTE: If you redeclare a variable, it will be overwritten with the new declaration. If you want to add attributes to an existing variable, use [smdset.b]
[note.wc_close]

[terminal.wc_open(t="Declaring variables in other namespaces")]
[sp]
[smdvar_wp(parms="_id=\"fu\" _format=\"bar\"")]
[smdhtml_wp(parms="_id=\"fu\"")]
[smdlink_wp(parms="_id=\"fu\"")]
[sp]
[terminal.wc_close]

Notice that in the [smdhtml.b] and [smdlink.b] declarations we didn't specify the _format attribute. You'll see why when we get to the chapters on those namespaces, but for now, just realize that if you did specify the _format="bar" on those, then they would result in the exact same behavior as the [smdvar.il] variable. That is, when you write [e_var.b(t="var.fu")], [e_var.b(t="html.fu")], [e_var.b(t="link.fu")] in your markdown document, each would simply emit **bar**. Let's try that now.

[terminal.wc_open(t="Using _format on [smdhtml.il] and [smdlink.il]")]
*[smdcomment.il] declare [E.apos]fu[E.apos] in [smdvar.il], [smdhtml.il] & [smdlink.il]*
[smdvar_wp(parms="_id=\"fu\" _format=\"bar\"")]
[smdhtml_wp(parms="_id=\"fu\" _format=\"bar\"")]
[smdlink_wp(parms="_id=\"fu\" _format=\"bar\"")]
[sp]
@var _id="fu" _format="bar"
@html _id="fu" _format="bar"
@link _id="fu" _format="bar"
*[smdcomment.il] now print each one*
[e_var(t="var.fu")] emits *[var.fu]*
[e_var(t="html.fu")] emits *[html.fu]*
[e_var(t="link.fu")] emits *[link.fu]*
[sp]
*[smdcomment.il] Redefine html.fu and link.fu*
[smdhtml_wp(parms="_id=\"fu\"")]
[smdlink_wp(parms="_id=\"fu\"")]
@html _id="fu"
@link _id="fu"
[sp]
*[smdcomment.il] now print each one*
[e_var(t="var.fu")] emits *[var.fu]*
[e_var(t="html.fu")] emits *[escape_var(v="html.fu")]*
[e_var(t="link.fu")] emits *[escape_var(v="link.fu")]*

[terminal.wc_close]

The reason that [e_var.b(t="html.fu")] emits *[escape_var(v="html.fu")]* will be explained in the [smdhtml.b] chapter on variable declarations. For now, just go with it. [e_moji.big(e="tonguewink")]

One other caveat to the shorthand notation: if you specify also specify the **_format= attribute**, whatever you attempt to assign as part of the declaration will be ignored, and the value specified with _format will win. For example:

@var fu="bar" _format="123"
[terminal.wc_open(t="Using shorthand notation and specifiying _format")]
[smdvar_wp(parms="fu=\"bar\" _format=\"123\"")]
[sp]
Then [e_var(t="fu")] will emit **[fu]** instead of *bar*
[sp]
[terminal.wc_close]

If you fail to specify the **_format** attribute when you declare an [smdvar.b] variable, and you do not use the short-hand notation to create it, then referencing the variable will result in all attributes being dumped. Let's see how that works. Take the following markdown:

[tab.<][encode_smd(t="@var _=\"myvar\" attr1=\"value1\" attr2=\"value2\"")][tab.>]

Then, if we write **[E.lb]myvar[E.rb]** the parser will emit:

@var _="myvar" attr1="value1" attr2="value2"

[bigmargin._open]
    [myvar]
[bigmargin._close]

There isn't much usefulness in this side affect since there is no way to control the formatting, however, you may find it handy as a way of checking the current definition of a variable without having to dump it. i.e. [e_var.b(t="myvar")] is shorter than **[E.lb]code.dump(ns="var" name="myvar")[E.rb]** or even **[encode_smd(t="@dump var=\"^myvar$\"")]**.

[wrap_h.subsect(t="### Inheriting attributes")]

One last concept to discuss about declaring variables is the attribute **_inherit**. This attribute can be used at declaration time only, and it's purpose is to avoid having to redefine common attributes. This is used throughout the builtin files that come with [smd.b], so you'll see it used quite often. Let's look at an example of how it is used.

[terminal.wc_open(t="Using _inherit to streamline declarations")]
*[smdcomment.il] declare [E.apos]smdtag[E.apos] variable*
[smdvar.b] smdtag="@@[_self.il(p="il")]" il="[E.lcb2]encode_smd[E.lp]t=\"[_self.il]\"[E.rp][E.rcb2]" b="[E.ast2][_self.il][E.ast2]" em="[E.ast][_self.il][E.ast]" emb="[E.ast3][_self.il][E.ast3]"
[sp]
*[smdcomment.il] now declare several variables based on **smdtag***
[smdvar_wp(parms="_id=\"smdvar\" _inherit=\"smdtag\" p=\"@var\"")]
[smdvar_wp(parms="_id=\"smdhtml\" _inherit=\"smdtag\" p=\"@html\"")]
[smdvar_wp(parms="_id=\"smdlink\" _inherit=\"smdtag\" p=\"@link\"")]
[sp]
*[smdcomment.il] now we have three new variables that all contain similar attributes*
[e_var(t="smdvar")] = [smdvar.il], [e_var(t="smdvar.b")] = [smdvar.b], [e_var(t="smdvar.em")] = [smdvar.em], [e_var(t="smdvar.emb")] = [smdvar.emb]
[e_var(t="smdhtml")] = [smdhtml.il], [e_var(t="smdhtml.b")] = [smdhtml.b], [e_var(t="smdhtml.em")] = [smdhtml.em], [e_var(t="smdhtml.emb")] = [smdhtml.emb]
[e_var(t="smdlink")] = [smdlink.il], [e_var(t="smdlink.b")] = [smdlink.b], [e_var(t="smdlink.em")] = [smdlink.em], [e_var(t="smdlink.emb")] = [smdlink.emb]
[terminal.wc_close]

If you specify an attribute that is defined in the underlying inherited variable, it will override the underlying value. Otherwise, the new variable will contain all of the same attributes, plus any new ones added at the time of declaration (or later using [smdset.b]).

[link.ug_var_names]
[wrap_h.section(t="### [smdvar.il] Variable names")]
Variable names in the [smdvar.b] namespace, well actually, in **any** namespace are restricted to these requirements:

[ulist.wc_open]
Must begin with a letter or the underscore character
Must contain only letters, numbers or underscores
Are case sensitive. That is, abc and ABC are different variable names
[ulist.wc_close]

Here are some examples of variable names:

@html _id="td_item" _inherit="td" class="item" style="padding:5px;width:auto;font-size:1.3em;text-align:{{self._align}}" _align="center"
@html _id="td_desc" _inherit="td" class="item" style="padding:5px;width:auto;font-size:1.3em;text-align:{{self._align}}" _align="center"
@html _id="th_item" _tag="th"     _inherit="td_item"
@html _id="th_desc" _tag="th"     _inherit="td_desc" 
@html _id="table_2" _inherit="table" style="margin-left:auto;margin-right:auto"

@var table_2col="Macro for emitting 2 column table"\
    open="{{code.pushlines(t=\"@wrap null\n[_div_extras_.<+][table_2.<+]\")}}"\
    close="{{code.pushlines(t=\"[table.>][_div_extras_.>]\n@parw 1\")}}"\
    row="[tr.<]{{td_item.<}}{{self.item}}[td.>]{{td_desc.<}}{{self.desc}}[td.>][tr.>]"\
    row_alt="[tr.<]{{td_item.<}}*{{self.item}}*[td.>]{{td_desc.<}}{{self.desc}}[td.>][tr.>]"\
    header="[tr.<]{{th_item.<}}{{self.item}}[td.>]{{th_desc.<}}{{self.desc}}[td.>][tr.>]"\

[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Variable Name" desc="Valid / Invalid")]
        [table_2col.row(item="a" desc="valid")]
        [table_2col.row(item="a1" desc="valid")]
        [table_2col.row(item="a_1" desc="valid")]
        [table_2col.row(item="_a1" desc="valid")]
        [table_2col.row(item="A" desc="valid")]

        [table_2col.row(item="1a" desc="{:.red}invalid")]
        [table_2col.row(item="a-b" desc="{:.red}invalid")]
        [table_2col.row(item="1+" desc="{:.red}invalid")]
        [table_2col.row(item="%a" desc="{:.red}invalid")]
    [table_2col.close]
[bigmargin._close]

Attribute names, on the other hand, are restricted to these requirements:

[ulist.wc_open]
Must contain only letters, numbers, underscores or dashes
Are case sensitive. That is, abc and ABC are different variable names
[ulist.wc_close]

Here are some examples of attribute names:

[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Attribute Name" desc="Valid / Invalid")]
        [table_2col.row(item="a" desc="valid")]
        [table_2col.row(item="a1" desc="valid")]
        [table_2col.row(item="a_1" desc="valid")]
        [table_2col.row(item="_a1" desc="valid")]
        [table_2col.row(item="A" desc="valid")]
        [table_2col.row(item="1a" desc="valid")]
        [table_2col.row(item="a-b" desc="valid")]
        [table_2col.row(item="1+" desc="{:.red}invalid")]
        [table_2col.row(item="%a" desc="{:.red}invalid")]
    [table_2col.close]
[bigmargin._close]

As you can see, attribute names are not quite as restrictive in their naming as variable names, allowing dashes to be used, and also allowing names to begin with numbers.

[link.ug_var_attrs]
[wrap_h.section(t="### [smdvar.il] Built-in Attributes")]

[smdvar.b] variables have a number of built-in attributes to extract common components. In fact, all namespaces share these built-in attributes, and in the case of variables based on the [smdhtml.b] namespace, they are relied on much more, but nonetheless, they can be useful in any of the namespaces, if for no other reason to assist in debugging complex declarations.

Here is the full list of built-in attributes supported across all namespaces:

[html.td_desc._null_(_align="left")]
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Attribute Name" desc="Description")]
        [table_2col.row_alt(item="_" desc="The name of the variable")]
        [table_2col.row_alt(item="_id" desc="The name of the variable")]
        [table_2col.row_alt(item="?" desc="Returns **_help** if present otherwise **No help available**")]
        [table_2col.row_alt(item="??" desc="Same as *?*, but strips most HTML tags. Useful when running [smd.b] interactively.")]
        [table_2col.row_alt(item="_private_attrs_" desc="All of the private attributes [E.lp]those that begin with underscore [E.apos]_[E.apos][E.rp]")]
        [table_2col.row_alt(item="_public_attrs_" desc="All of the public attributes [E.lp]those that do not begin with underscore[E.rp]")]
        [table_2col.row_alt(item="_private_attrs_esc_" desc="Same as private attributes, but quotes are escaped.")]
        [table_2col.row_alt(item="_public_attrs_esc_" desc="Same as public attributes, but quotes are escaped.")]
        [table_2col.row_alt(item="_public_keys_" desc="The public attribute names")]
        [table_2col.row_alt(item="_private_keys_" desc="The private attribute names")]
        [table_2col.row_alt(item="_all_attrs_" desc="All attributes")]
        [table_2col.row_alt(item="_all_attrs_esc_" desc="Same as all attributes, but quotes are escaped.")]
        [table_2col.row_alt(item="_null_" desc="A null attribute - emits nothing, used to set default values of any public/private attribute")]
    [table_2col.close]
[bigmargin._close]

[terminal.wc_open(t="Examples")]
[e_var.b(t="var.fu._")] *=* [fu._]
[e_var.b(t="var.fu._id")] *=* [fu._id]
[e_var.b(t="var.fu._all_attrs_")] *=*[fu._all_attrs_]
[e_var.b(t="var.fu._private_keys_")] *=*[fu._private_keys_]
[e_var.b(t="var.fu.?")] *=*[fu.?]
[sp]
[e_var.b(t="html.divx._all_attrs_")] *=*[get_value(v="html.divx._all_attrs_" ret_type="0" escape="True")]
[e_var.b(t="html.divx._private_attrs_")] *=*[get_value(v="html.divx._private_attrs_" ret_type="0" escape="True")]
[e_var.b(t="html.divx._public_attrs_")] *=*[html.divx._public_attrs_]
[terminal.wc_close]

[link.ug_var_misc]
[wrap_h.subsect(t="#### [smdvar.il] Miscellaneous Examples")]

Here are just a few more examples to help drive home your understanding of the declaration and usage of variables in the [smdvar.b] namespace.

Consider this declaration: 

[tab.<][smdvar_wp.b(parms="_id=\"varname\" attr1=\"value1\" _format=\"format string\"")][tab.>]

@var _id="varname" attr1="value1" _format="format string"

And now we write the following markdown:

[terminal.wc_open(t="")]

[e_var.b(t="varname.attr1")] would emit ***[varname.attr1]***.
[e_var.b(t="varname._id")] would emit ***[varname._id]***.
[e_var.b(t="varname._format")] would emit ***[varname._format]***.

[terminal.wc_close]

So that's pretty cool, but there's a bit more to the _format attribute. You can reference the attributes contained within the variable by using **{{self}}.attrname**. Given that, if we write the following:

[tab.<][smdvar_wp.b(parms="_id=\"fullname\" first=\"ken\" last=\"lowrie\" _format=\"[E.lcb2][_self_].first[E.rcb2] [E.lcb2][_self_].last[E.rcb2]\"")][tab.>]

@var _id="fullname" first="ken" last="lowrie" _format="{{self.first}} {{self.last}}"

[terminal.wc_open(t="")]
[e_var.b(t="fullname")] would emit ***[fullname]***.
[terminal.wc_close]

Using that, you can build some pretty powerful tools for automating frequently used tasks in your documents. Take a look at the **film.md**, **image.md** and **avs.md** tests to get an idea of what you can do.

Before we leave this, take note of the difference between {{first}} and {{self.first}}. Both syntaxes are valid, but the first one references the normal variable first, while the second one (self.first) references the attribute named *first* defined within the *varname* variable. Also take note that you can reference the attributes of other [smdvar.b] variables as long as you qualify them. Let me show you a quick example of that. Take this:

[tab.<][smdvar_wp.b(parms="_id=\"var1\" first=\"ken\" last=\"lowrie\"")][tab.>]
[tab.<][smdvar_wp.b(parms="_id=\"var2\" prefix=\"mr.\" _format=\"{{{{_self_}}.prefix}} {{var1.first}} {{var1.last}}\"")][tab.>]

@var _id="var1" first="ken" last="lowrie"
@var _id="var2" prefix="mr." _format="{{self.prefix}} {{var1.first}} {{var1.last}}"

Then, if you write this:

[terminal.wc_open(t="")]
[e_var.b(t="var2")] would emit ***[var2]***.
[terminal.wc_close]

One last thing, remember how we discussed that sometimes you need a way to resolve ambiguities of variables across the different variable types? **image.** can be used to resolve a variable inside the [smdimage.b] namespace, and **var.** can be used to resolve a variable inside the [smdvar.b] namespace. Given that:

[terminal.wc_open(t="")]
[e_var.b(t="var2")] and [e_var.b(t="*var*.var2")] resolve to the same thing.
[terminal.wc_close]

Did you notice that in the first example, we used **[E.lcb2]** and **[E.rcb2]** around the variable/attribute name, and in the second, we used square brackes i.e. **[E.lb]** and **[E.rb]**? What's the difference (if there is one), and why use one over the other? Good question. Now is a good time to talk about the concept of attribute markdown expansion, and how it works.

[link.ug_attr_exp]
[wrap_h.subsect(t="#### Attribute Expansion")]

You are going to see this over and over in the coming chapters, and even more once you start examining the built-ins and this user guide, however, we need to cover it now, so it won't seem overly complex later on. What I'm talking about is the concept of attribute expansion, in the context of [smd.b]'s markdown variables and attributes. 

As you have seen, variables can have one or more attributes, and those attributes can be anything from plain text, to specialized markdown such as [E.ast], [E.ast2], [E.ins] and [E.del], to the referencing of other attributes, both within the same definition, as well as in entirely other variables and yes, even other namespaces! Let's review a few examples to get started.

@var prefix="[smdvar.il] var1=\"\"" encoded="[b]**[E.lb]var1.attr1[E.rb]=**" value="[var1.attr1]"

[terminal.wc_open(t="Attribute expansion - simple and inline markdown")]
@var var1="" attr1="plain text"
[prefix] attr1="plain text" [prefix.encoded][prefix.value]
[sp]
@var var1="" attr1="*text with markdown*"
[prefix] attr1="[E.ast]text with markdown[E.ast]" [prefix.encoded][prefix.value]
[sp]
@var var1="" attr1="<strong>text with html markup</strong>"
[prefix] attr1="[E.lt]strong[E.gt]text with html markup[E.lt]/strong[E.gt]" [prefix.encoded][prefix.value]
[terminal.wc_close]

With simple markdown, you are providing the values directly, and possibly adding the inline markdown elements to it for decoration. 

Next up, let's take a look at referencing values stored in attributes within the same variable. This can be done using either square brackets **[E.lb][sp][E.rb]** or curly brackets **[E.lcb2][sp][E.rcb2]**. Before looking at the examples, though, let's get aquainted with the semantic differences between the two variations.

Anytime you use square brackets during the declaration of new variables and/or attributes, they will be evaluated at the time the variable declaration is parsed. Curly braces, on the on the other hand, are not evaluated until the attribute value is referenced later in the document. This is a very important distinction, because sometimes, you want some parts of your declaration to evaluate during the parsing stage, and other times, you need them to evaluate later, when a given attibute is being referenced.

@var prefix="[smdvar.il] var1=\"\"" encoded="[b]**[E.lb]var1.attr1[E.rb]=**" value="[!var1.attr2!]"

[terminal.wc_open(t="Attribute expansion - referencing attributes within the same variable")]
@var var1="" attr1="[self.attr2]" attr2="*from var1.attr2*"
    [prefix] attr1="[E.lb]self.attr1[E.rb]" attr2="[E.ast]from var1.attr2[E.ast]" [prefix.encoded][prefix.value]
@var var1="" attr1="{{self.attr2}}" attr2="*from var1.attr2*"
    [sp]
    [prefix] attr1="[E.lcb2]self.attr1[E.rcb2]" attr2="[E.ast]from var1.attr2[E.ast]" [prefix.encoded][prefix.value]
[terminal.wc_close]

Couple of notes on the prior example. First, notice the use of **self.** as a shorthand notation for **var.var1**. This is a frequently used notation, because if you change the variable name, you don't have to change any of the **self.** references. The parser will take care of that for you. 

Second, notice that both the square brackets and the curly braces produced the same results. This happens due to a side effect of referencing attributes during the declaration of a new variable. Since at the time of parsing, **var1** does not exist, the lookup for **var1.attr1** fails, and thus the markdown fails to expand. However, later, when we access the attribute again, it will resolve, and thus both variations work the same way. Keep in mind that relying on this side effect isn't a great idea; it will often lead to pesky bugs in your markdown documents, so it is highly recommended that you use the appropriate syntax when it's called for to avoid it!

Okay, now let's add a new twist. Having the attributes in one declaration reference the attributes in another declaration. This will demonstrate the issue we were just talking about, the semantic differences between square brackets and curly braces in [smd.b] markdown.

[terminal.wc_open(t="Attribute expansion - referencing attributes in a different variable")]
    *[smdcomment.il] Declare a second variable with an attribute we can reference from var1*
@var extvar="" attr2="*from {{self._}}.attr2*"
    [encode_smd(t="@var")] extvar="" attr2="[E.ast]from extvar.attr2[E.ast]"
    [sp]
    *[smdcomment.il] Declare var1 and var2*
@var var1="" attr1="[extvar.attr2]"
    [smdvar.il] var1="" attr1="[E.lb]extvar.attr2[E.rb]" [prefix.encoded][var1.attr1]
    [sp]
@var var2="" attr1="{{extvar.attr2}}"
    [smdvar.il] var2="" attr1="[E.lcb2]extvar.attr2[E.rcb2]" [b]**[E.lb]var2.attr1[E.rb]=**[var2.attr1]
    [sp]
    *[smdcomment.il] Now, let's change the value of extvar.attr2 and then reference both variables **attr1** again*
@set _="extvar" attr2="***A new value!***"
    [encode_smd(t="@set")] _="extvar" attr2="[E.ast3]A new value![E.ast3]"
    [sp]
    *[smdcomment.il] Review current values of **var1.attr1** and **var2.attr1***
    [prefix.encoded][var1.attr1][b]**[E.lb]var2.attr1[E.rb]=**[var2.attr1]
[terminal.wc_close]

See the difference? In **var1.attr1**, it's value was set to **extvar.attr2** when it was defined, but **var2.attr1**, was told to wait to markdown its value until someone asks for it. This is what is normally referred to as *deferred expansion* in the user manual, and you will see it used all the time throughout the builtins. 

Because of the deferred expansion, once we changed the value of **extvar.attr2** to something else, only **var2.attr1** reflected the new value. **var1.attr1** is still the same as what it was when it was declared. Usually, the curly braces are preferred, but there are some cases where using the square brackets are what you need. Before we leave this example, let's dump the current declarations of **var1**, **var2** and **extvar**, so you can see their current state.

[code.pushlist(attrlist="var.dumpit" nsvar="var" nsname="var1$|var2$|extvar$" title="Current definition of [E.apos]var1/2[E.apos] and [E.apos]extvar[E.apos] variables")]

So that leaves us with one more variation of delayed expansion support, the ***[!!]*** syntax. Essentially, it's a way to tell the parser's variable declaration API that you want to the variable or attribute to use square brackets, but you don't want to expand it at declaration time. In this case, the ***[!*** will be replaced with ***[*** and ***!]*** will be replaced with ***]***, just before the variable definition is written to memory. This will make more sense with an example. Let's use the exact one we just saw, but changing on the declaration of var1. Take a look:

[terminal.wc_open(t="Attribute expansion - referencing attributes using [E.lb]!![E.rb] syntax")]
    *[smdcomment.il] Declare a second variable with an attribute we can reference from var1*
@var extvar="" attr2="*from {{self._}}.attr2*"
    [encode_smd(t="@var")] extvar="" attr2="[E.ast]from extvar.attr2[E.ast]"
    [sp]
    *[smdcomment.il] Declare var1 and var2*
@var var1="" attr1="[!extvar.attr2!]"
    [smdvar.il] var1="" attr1="[E.lb]!extvar.attr2![E.rb]" [prefix.encoded][var1.attr1]
    [sp]
@var var2="" attr1="{{extvar.attr2}}"
    [smdvar.il] var2="" attr1="[E.lcb2]extvar.attr2[E.rcb2]" [b]**[E.lb]var2.attr1[E.rb]=**[var2.attr1]
    [sp]
*[smdcomment.il] Now, let's change the value of extvar.attr2 and then reference both variables **attr1** again*
@set _="extvar" attr2="***A new value!***"
    [encode_smd(t="@set")] _="extvar" attr2="[E.ast3]A new value![E.ast3]"
    [sp]
    *[smdcomment.il] Review current values of **var1.attr1** and **var2.attr1***
    [prefix.encoded][var1.attr1][b]**[E.lb]var2.attr1[E.rb]=**[var2.attr1]
[terminal.wc_close]

See how it worked this time? Let's look at the current declarations of the variables again:

[code.pushlist(attrlist="var.dumpit" nsvar="var" nsname="var1$|var2$|extvar$" title="Current definition of [E.apos]var1/2[E.apos] and [E.apos]extvar[E.apos] variables")]

 Now, in **var1.attr1**, it's value is set to **[E.lb]extvar.attr2[E.rb]**, which makes it behave like **var2.attr1**. In this case, we have applied *deferred expansion* using ***[!!]*** instead of the usual curly brackets **[E.lcb2][sp][E.rcb2]**.

This can help you build some really cool automation in your documents. But you need one more thing before you get started. A way to change one or more attributes of an existing variable in any namespace. Enter [smdset.b] and the **_null_** attribute. We've already been using it in our examples, so it may be old hat by now, but let's take a closer look at it just to be thorough.

[link.ug_set_keyword]
[wrap_h.subsect(t="### The [smdset.il] Keyword")]

Attributes in any variable in any namespace can be added or updated at any time. There are two (perhaps three depending on semantics) ways this can be done in all namespaces except [smdcode.b]. In [smdcode.il], there is only one way to update an attribute value, and that is with [smdset.b]. Let's see how it's done.

[terminal.wc_open(t="Updating attribute values with [smdset.il]")]
    *[smdcomment_wp.il(parms="First, let[E.apos]s declare a new variable called [E.apos]fu[E.apos]")]*
    [smdvar_wp.b(parms="fu=\"bar\" attr1=\"value1\"")]
@var fu="bar" attr1="value1"
    [e_var.b(t="fu.attr1")] emits **[fu.attr1]**

    [sp]
    *[smdcomment_wp.il(parms="using [smdset.il], change the value of attr1 to [E.apos]value2[E.apos]")]*
    [smdset_wp.b(parms="_=\"fu\" attr1=\"value2\"")]
@set _="fu" attr1="value2"
    [e_var.b(t="fu.attr1")] emits **[fu.attr1]**

    [sp]
    *[smdcomment_wp.il(parms="using the _null_ attribute, change the value of attr1 to [E.apos]value3[E.apos]")]*
    [e_var.b(t="fu._null_[E.lp]attr1=\"value3\"[E.rp]")]
[fu._null_(attr1="value3")]
    [e_var.b(t="fu.attr1")] emits **[fu.attr1]**
[terminal.wc_close]

[note(t="The **_null_** attribute illustrates an important concept with the attributes of variables in [smd.b]. That is, any time an attribute value is changed by specifying a new value when a method is invoked, that value becomes the new value for that attribute. This is true with all namespaces except [smdcode.b]; in the [smdcode.b] namespace, attribute values overridden via a method invocation are temporary. Once the method returns, the original attribute values are restored.[bb]As previously mentioned, the only way to change the value of a variable in the [smdcode.b] namespace is by using [smdset.b]. When this is done, the code behind the variable (Python source code) is recompiled, which essentially updates their usage in the compiled code stored as part of the variable.")]

You can also add new attributes to an existing variable with [smdset.b]. And, if you [smdset.b] a variable that does not exist, [smdset.b] will create it. Let[E.apos]s see both of these things in action now.

[terminal2.wc_open(t="Adding attributes with [smdset.il]")]
    [terminal2.wc_open_content]
        *[smdcomment_wp.il(parms="add a new attribute to [E.apos]fu[E.apos] using [smdset.il]")]*
        [smdset_wp.b(parms="_=\"fu\" attr2=\"value42\"")]
@set _="fu" attr2="value42"
        [e_var.b(t="fu.attr2")] emits **[fu.attr2]**
        [sp]
        *[smdcomment_wp.il(parms="adding a new attribute doesn[E.apos]t affect existing attributes in [E.apos]fu[E.apos]")]*
        [e_var.b(t="fu.attr1")] still emits **[fu.attr1]**

        [sp]
        *[smdcomment_wp.il(parms="using the _null_ attribute, add attr3 to [E.apos]fu[E.apos]")]*
        [e_var.b(t="fu._null_[E.lp]attr3=\"many ways to add attributes\"[E.rp]")]
[fu._null_(attr3="many ways to add attributes")]
        [e_var.b(t="fu.attr3")] emits **[fu.attr3]**

        [sp]
        *[smdcomment_wp.il(parms="We can also add and update variables at the same time")]*
        [e_var.b(t="fu._null_[E.lp]attr3=\"update 3rd attribute\" attr4=\"add 4th attribute\"[E.rp]")]
[fu._null_(attr3="update 3rd attribute" attr4="add 4th attribute")]
        [e_var.b(t="fu.attr3")] emits **[fu.attr3]** and [e_var.b(t="fu.attr4")] emits **[fu.attr4]**

        [sp]
        *[smdcomment_wp.il(parms="We can also add and update variables at the same time using")] [smdset.b]*
        [smdset_wp.b(parms="_=\"fu\" attr2=\"update attr2\" attr6=\"6th attribute\"")]
@set _="fu" attr2="update attr2" attr6="6th attribute"
        [e_var.b(t="fu.attr2")] emits **[fu.attr2]** and [e_var.b(t="fu.attr6")] emits **[fu.attr6]**
    [terminal2.wc_close_content]
[terminal2.wc_close]

Let's dump the variable 'fu' to see all the attributes and their values. xxx
[code.pushlist(attrlist="var.dumpit" nsvar="var" nsname="fu$" title="Current definition of [E.apos]fu[E.apos] variable")]

And finally, you can also specify the namespace two different ways with [smdset.b]. Witness:

[terminal.wc_open(t="Specifying the namespace")]
    *[smdcomment_wp.il(parms="Specify the namespace with @set; don[E.apos]t leave it to chance!")]*
    [smdset_wp.b(parms="*_ns=\"var\"* _=\"fu\" attr6=\"update attr6\"")]
@set _ns="var" _="fu" attr6="update attr6"
    [e_var.b(t="fu.attr6")] emits **[fu.attr6]**
    [sp]
    *[smdcomment_wp.il(parms="Alternate method to set namespace")]*
    [smdset_wp.b(parms="_=\"*var.*fu\" attr6=\"update attr6 again!\"")]
@set _="var.fu" attr6="update attr6 again!"
    [e_var.b(t="fu.attr6")] emits **[fu.attr6]**
[terminal.wc_close]

One last time let's dump the variable 'fu' to see all the attributes and their values.

[code.pushlist(attrlist="var.dumpit" nsvar="var" nsname="fu$" title="Current definition of [E.apos]fu[E.apos] variable")]

Here are just a few more examples to help drive home your understanding of the declaration and usage of variables in the [smdvar.b] namespace.

Given the following markdown:
[bmgreybg._open] 
    [var.source.wc_open(t="Create a new [smd] variable *c2*")]
        [bb]
        [encode_smd(t="@var ns=\"var\"")][b]
        [encode_smd(t="@set")] _ns="[E.lb]ns[E.rb]" _="c2" attr1="[E.ast]value 1[E.ast]" attr2="[E.ast2]value 2[E.ast2]" attr3="{{self.attr1}}--{{self.attr2}}" attr4="[E.lb]self.attr2[E.rb]--[E.lb]self.attr1[E.rb]"
    [var.source.wc_close]
[bmgreybg._close]

Then the following markdown sometime later will produce:

@var ns="var"
@set _ns="[ns]" _="c2" attr1="*value 1*" attr2="**value 2**" attr3="{{self.attr1}}--{{self.attr2}}" attr4="[self.attr2]--[self.attr1]"
[bmgreybg._open]
    [encode_smd(t="<c2.attr1>")] = [c2.attr1]
    [encode_smd(t="<c2.attr2>")] = [c2.attr2]
    [encode_smd(t="<c2.attr3>")] = [c2.attr3]
    [encode_smd(t="<c2.attr4>")] = [c2.attr4]
[bmgreybg._close]

//[docthis.open(h="Add this to nsvar-doc.md")]
//[docthis.close]
