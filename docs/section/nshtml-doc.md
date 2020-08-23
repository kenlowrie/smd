[link.ug_ns_html]
[wrap_h.chapter(t="## [smdhtml.il] Namespace")]

The [smdhtml.b] keyword is used to construct variables that represent HTML elements for your documents. These variables are stored in the [smdhtml.b] namespace, and can have names that are identical to variables in other namespaces, although it is normally recommended that you avoid doing that. 

Most of the features and concepts just discussed for [link.ug_ns_var._qlink(_qtext="[smdvar.b]")] variables also applies to [smdhtml.b] variables. If you haven't read that chapter yet, you should, as this one assumes that you have read and understand those concepts, and will build upon them.

[link.ug_html_syntax]
[wrap_h.section(t="### [smdhtml.il] Syntax")]

[syntax.wc_open(t="[smdhtml.il] command syntax")]
    [b]
    [tab.<][smdhtml.b] **_id="name" [E.lb]_tag="tagname" [E.lb]...[E.rb][E.sp][E.sp][E.rb]**[bb][tab.>]
[syntax.wc_close]

All of the built-in attributes previously documented for [smdvar.b] are supported for [smdhtml.b] variables, and a new one **_tag** has been introduced. _tag is used to set the HTML element name for the variable. If _tag is not specified, it will be set to the same value as _id. Let's define a few variables, and then examine them.

[terminal.wc_open(t="Defining an [smdhtml.il] variable")]
[sp]
[smdhtml_wp(parms="_=\"blockquote\" cite=\"url-goes-here\"")]
[smdhtml_wp(parms="_id=\"bquote\" _tag=\"blockquote\"")]
[smdhtml_wp(parms="_id=\"bq\" _inherit=\"blockquote\"")]
[terminal.wc_close]

In the preceding example, we've defined  three [smdhtml.b] variables: **blockquote**, **bquote** and **bq**. Let's use **[E.lb]code.dump[E.rb]** to take a look at their declarations.

@html _="blockquote" cite="url-goes-here"
@html _id="bquote" _tag="blockquote"
@html _id="bq" _inherit="blockquote"

[code.pushlist(attrlist="var.dumpit" \
               nsvar="html" \
               nsname="^blockquote$|bq.*" \
               title="Definition of *blockquote*, *bquote* & *bq* variables")]

First, take a look at **blockquote**. **_tag**, although we didn't specify it, has been set to **blockquote**. In many cases, this is what you want, so not having to specify it is a nice shortcut when declaring variables. Also, notice how **_format** has been set to *[E.lt]{{self._tag}}{{self._public_attrs_}}[E.gt][E.lt]{{self._tag}}[E.gt]*. 

Given that, if we write [e_var.em(t="blockquote")] it will emit ***[escape_var(v="blockquote")]***. 

The first thing you'll notice is that there isn't a way to get content between the opening and closing tags, so on the surface, this doesn't look very useful. Enter the special attributes **[E.lt]** and **[E.gt]**, supported by all [smdhtml.b]-based namespaces.

Now, if we write [e_var.b(t="blockquote*.[E.lt]*")] it will emit [escape_var(v="blockquote.<")]. Conversely, if we write [e_var.b(t="blockquote*.[E.gt]*")], it will emit [escape_var(v="blockquote.>")]. So now all we need is to specify a value for the **cite** attribute when we declare the open tag, add some content, and specify the closing tag. Let's see how it all comes together.

[terminal.wc_open(t="Adding content to the blockquote HTML variable")]
[e_var.b(t="blockquote.[E.lt][E.lp]cite=\"https://google.com\"[E.rp]")]
Google has always had the "I'm Feeling Lucky" button just below it's search input box, which can be used to automatically follow the first returned link in your search.
[e_var.b(t="blockquote.[E.gt]")]

[terminal.wc_close]

This is what will be rendered by the browser:
[blockquote.<(cite="https://google.com")]Google has always had the "I'm Feeling Lucky" button just below it's search input box, which can be used to automatically follow the first returned link in your search.[blockquote.>]

[note.with_content(c="Keep in mind that the formatting of the **blockquote** tag is defined by your Browser, or the CSS specified for you document.")]

Let's return to looking at the **bquote** and **bq** variables. With **bquote**, notice it doesn't have the **cite** attribute, because it wasn't specified. Attributes can always be added to an [smdhtml.b] variable on the fly, it isn't required that they be added when the variables are defined. And remember, most HTML elements support the global attributes (e.g. class, style, id, etc.), and if any of these are declared as public attributes on an [smdhtml.b] variable, they will automatically be output whenever the opening tag of an element is emitted by the parser.

**bq** is identical to **blockquote**, because the **_inherit** attribute was specified at declaration time. Recall from the [smdvar.b] section, **_inherit** is used to add all attributes of the named variable to this new declaration. And, any of the underlying attributes can be overridden in the new declaration by simply specifying them again.  For example, if we wrote:

[tab.<][smdhtml_wp.b(parms="_id=\"bq\" _inherit=\"blockquote\" cite=\"different-default-citation\"")][tab.>]

@html _id="bq" _inherit="blockquote" cite="different-default-citation"

Then this is what the definition of **bq** looks like in memory:

[code.pushlist(attrlist="var.dumpit" \
               nsvar="html" \
               nsname="bq$" \
               title="New definition of *bq* variable")]

[link.ug_html_names]
[wrap_h.section(t="### [smdhtml.il] Variable names")]

Variable names in the [smdhtml.b] namespace are restricted to the same requires as the [smdvar.b] namespace.

[link.ug_html_attrs]
[wrap_h.section(t="### [smdhtml.il] Built-in Attributes")]

In addition to all of the built-in attributes supported by [smdvar.b], [smdhtml.b] variables have several built-ins that are unique to it:

[html.td_desc._null_(_align="left")]
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Attribute Name" desc="Description")]
        [table_2col.row_alt(item="_tag" desc="The HTML element name of the variable")]
        [table_2col.row_alt(item="[E.lt]" desc="The opening tag for this variable")]
        [table_2col.row_alt(item="[E.gt]" desc="The closing tag for this variable")]
        [table_2col.row_alt(item="[E.lt]+" desc="The opening tag with embedded quotes escaped.")]
    [table_2col.close]
[bigmargin._close]

We've already seen these in action above, so no need to discuss further with the exception of the **[E.lt]+**, which will output the opening tag with escaped quotes in the public variable definitions.

[terminal.wc_open(t="Examples")]
[e_var.b(t="html.blockquote")] *=* [escape_var(v="html.blockquote")]
[e_var.b(t="html.blockquote.<")] *=* [escape_var(v="html.blockquote.<")]
[e_var.b(t="html.blockquote.>")] *=* [escape_var(v="html.blockquote.>")]
[e_var.b(t="html.blockquote.<+")] *=* [escape_var(v="html.blockquote.<+")]
[e_var.b(t="html.blockquote._id")] *=* [html.blockquote._id]
[e_var.b(t="html.blockquote._tag")] *=* [html.blockquote._tag]
[e_var.b(t="html.blockquote._public_keys_")] *=* [blockquote._public_keys_]
[e_var.b(t="html.blockquote._private_keys_")] *=* [blockquote._private_keys_]
[terminal.wc_close]

[link.ug_html_misc]
[wrap_h.subsect(t="### [smdhtml.il] Miscellaneous Examples")]

Here are just a few more examples to help drive home your understanding of the declaration and usage of variables in the [smdhtml.b] namespace. Let's start by examining the contents of the **[e_var(t="sys.imports")]/html.md** file:

[terminal.wc_open(t="Contents of html.md builtins")]
    @embed "[sys.imports]/html.md" esc="y"
[terminal.wc_close]

You can see a combination of syntaxes used in declaring the builtins for [smdhtml.b]. Most are very simple, just the name and tag (when necessary), others have a few have additional options. If you begin to examine other system builtin files, you will see more complex declarations. Remember **helpers.md** from the earlier chapter [link.ug_helpers.link]?

Many times, you may find that taking a system provided builtin as a starting point, using **_inherit** to pick up all of its attributes, and then extending it by adding additional attributes or even changing the behavior by modifying an existing attribute is a great way to get exactly what you need. And this brings us to the end of [smdhtml.b]. From here, spend some time experimenting with this namespace, and maybe try modifying existing or extending something to get a better feel for how they work.

One last thing before we take a look at the [smdlink.b] namespace. Do not use [big.120p(t="[_self_].&lt;" cls=".bold.black")] or [big.120p(t="[_self_].&lt;+")] in any public attributes that are declared on [smdhtml.b] variables. Doing so will cause an infinite loop in the **Markdown** class, because when it attempts to markdown [big.120p(t="&lt;")] or [big.120p(t="&lt;+")], it will enumerate the public attributes, expanding any markdown in those attributes before rendering the content. However, in this case, the public attribute contains the [big.120p(t="[_self_].&lt;")] builtin, and it recurses to process that, only to find itself repeating the same thing. Long story short, it will throw an exception after twenty-five recursive calls to attempt to evaluate the expression. Here's a really short example that you can run in the interactive shell:

[terminal.wc_open(t="Sample infinite recursion using *[_self_].&lt;* in public attribute")]
    $ [smd] -nd
    [smdlink.il] _="fu" boom="{{[_self_].<}}"
    [E.lb]fu.boom[E.rb]
[terminal.wc_close]

If you try the two statements above in an interactive [smd.b] session, you will quickly see the issue. You may want to add **[smddebug.il] toggle="markdown"** just before the **[E.lb]fu.boom[E.rb]** so you scroll up to get a dump of markdown recursion loop (a trick discussed in the [link.ug_debug._qlink(_qtext="chapter on debugging")].)
//[docthis.open(h="Add this to nsvar-doc.md")]
//[docthis.close]
