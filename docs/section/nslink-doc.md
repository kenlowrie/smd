[link.ug_ns_link]
[wrap_h.chapter(t="##@link Namespace")]

[docthis.open(h="Add this to ns_code-doc.md")]
    [smdcomment] [E.lb]ln_factory(nm="tk" hr="https://tkdocs.com/tutorial/install.html" t="Tk")]
    [smdcomment] @set _ns="link" _="tk" tkinter="{{self.<}}tkinter{{self.>}}" target="_blank"

    Public attributes cannot refer to self.< or ns._.< because it will loop forever...

    I think this can happen anywhere, .attr1 includes .attr2 which includes .attr1, right?
    [smdcomment] @var x="{{y}}"
    [smdcomment] @var y="{{x}}"

    Solution 1: _markdown tracks recursion strings, then if the NestingError exception is raised, it will dump to console.
                requires that @debug on="markdown"
                
[docthis.close]

@wrap divx, p

The @link namespace is built atop the @html namespace, and as such, it inherits all the same characteristics of things defined in the @html space. In this chapter, we will take a closer look at the @link namespace and what it has to offer.

// links
[link.ug_links]
[wrap_h.section(t="##Link Styles")]
There are two different styles of links built-in to smd which map to standard HTML links:

@@[html.ol.<]
@wrap li2
Hyperlinks - Links created using the HTML **a** tag with the **href** attribute. e.g. *[escape(t="<a href=\"url\">content</a>")]*
Bookmarks - Links created using the HTML **a** tag with the **id** attribute. *[escape(t="<a id=\"bookmark_name\"></a>")]*
@parw
@@[html.ol.>]

As you can see, these links are both based on the HTML **a** attribute, and the distinction lies in how they are rendered within a document. The sections that follow describe how each link type is creating using the built-in factories specified in the ***sys.imports/link.md*** file.

[link.ug_hyperlinks]
[wrap_h.section(t="###Creating Hyperlinks")]

Hyperlinks are created using the @link namespace in smd, while specifying the attributes desired to describe the link. The @link namespace is a subclass of @html, and therefore it shares all the same characteristics, such as the &lt; attribute to emit the open tag HTML and &gt; to emit the close tag HTML. For more information on the @html namespace, refer to the user manual.

You can create a variable in the @link namespace using the following syntax:
@wrap divx
{:.indent}###[encode_smd(t="@link _=\"name\" href=\"http://example.com\"")]
@parw

@link _="name" href="http://example.com"

If you then specify [e_var.b(t="link.name")], the parser will emit **[escape_var(v="link.name")]**. Such a simple example isn't very useful, however, since we need the ability to insert content between the anchor tag. This can be accomplished by using the special attributes &lt; and &gt;, as follows:

@wrap divx
{:indent}###[encode_smd(t="<link.name.[E.lt]>content here<link.name.[E.gt]>")]
@parw

Now, the parser emits: **[escape_var(v="link.name.<")]content here[escape_var(v="link.name.>")]**, which is a bit more useful, but seemingly rather complex to to use in practice. In light of this, two special built-ins are provided in order to ease the creation and usage of hyperlinks. The first is a link template, [e_var.b(t="link._template_")], which can be inherited during creation of new links, and the second is a factory, [e_var.b(t="link.ln_factory")], which can be used to easily create a hyperlink with minimal input, and which has several useful attributes that can be used during rendering. Let's take a look at each of these now.

Going back to our original example, if we add **_inherit="_template_"** to the definition e.g.: 

@wrap divx
{:.indent}###[encode_smd(t="@link _=\"name\" href=\"http://example.com\" _inherit=\"_template_\"")]
@parw

@link _="name" _inherit="_template_" href="http://example.com"
We now have several new attributes available to use. For example, if we write [e_var.b(t="link.name._asurl")], the parser emits **[escape_var(v="link.name._asurl")]** which renders as [link.name._asurl]. If we use just the variable name like we did before e.g. [e_var.b(t="link.name")], we get this: [link.name]. As you can see, the default text for the link is actually a usage statement, requesting that we add the **_text=** parameter like so: **[encode_smd(t="<link.name&lpar;_text=\"my web site\"&rpar;>")]**, which then yields: [link.name(_text="my web site")]. 

If you want to use different content with the same link, then specifying the **_text=** parameter provides a convenient way to do that. For example, if I change the parameter to **_text="My Really Cool Website"**, I will get: [link.name(_text="My Really Cool Website")].

There is one side effect to overriding the default values for attributes on variables in all namespaces except the @code namespace. When a default attribute is overridden in a call, it changes the default value of that attribute for subsequent calls! For example, if I write **[encode_smd(t="<link.name>")]**, I will get the last value specified for _text, e.g. [link.name].

[note(t="Keep that in mind as it affects parameter passing in all of the namespaces except @code.[bb]In **@code**, default values for parameters can only be overridden when the variable is defined with **@code** or updated with **@set**. Anything passed via a call will be persisted for that call, and then revert to the original values.")]

You can also set the initial value for **_text** when the link variable is initially defined. For example, if we write:

@wrap divx
{:.indent}###[encode_smd(t="@link _=\"name\" href=\"http://example.com\" _inherit=\"_template_\" _text=\"my default title\"")]
@parw

@set _ns="link" _="name" _inherit="_template_" href="http://example.com" _text="my default title"

And I then write [e_var.b(t="link.name")], I will get the new default value for _text, i.e.: [link.name], without having to specify **_text** on the initial usage of the link.

[wrap_h.subsect(t="###Using the link factory to create hyperlinks")]

Before we leave the section on hyperlinks, let's a have a look at a better shorthand for creating links, the built-in link factory **ln_factory**. This built-in allows you to easily create a new link with minimal parameters:

@wrap divx
{:.indent}###[E.lb]ln_factory(nm="sample" hr="http://example.com" t="my default title")[E.rb]
@parw

[link.ln_factory(nm="sample" hr="http://example.com" t="my default title"")]

And now, if I write **[encode_smd(t="<sample>")]**, I will get: [sample]. Notice how in this example, we left off the namespace **link.**. Namespaces allow identifiers to be reused, and the value of a duplicated identifier in different namespaces will be unique. This ambiguity can lead to unexpected expansion since the if no namespace is supplied, the different namespaces are searched attempting to resolve the identifier. If the parser finds a match before it searches the intended namespace, then that is what it will use. Given that, it's always a good idea to specify the namespace except in the most simple of documents, to avoid incorrect expansion down the road. Thus, if I write **[encode_smd(t="<link.sample>")]**, I will get the value as before: [link.sample].

As you might expect, **ln_factory** inherits from **link._template**, and as such, it inherits attributes including **_asurl**. For example, [e_var.emb(t="link.sample._asurl")] which expands to **[escape_var(v="link.sample._asurl")]** and renders as: [link.sample._asurl]. 

[link.sample._null_(_qtext="alternative link text")]
One other feature of the **link._template_** is the **_qlink** and **_qtext** attributes. These allow you to specify alternative link text to the same **href**. For example, if I add **_qtext="alternative link text"** when the variable is declared, and then write **[encode_smd(t="<link.sample._qlink>")]**, I will get: [link.sample._qlink].

[link.sample._null_(_qtext="alt2 link text")]
You can also specify the **_qtext** using the special **_null_** syntax:  **[encode_smd(t="<link.sample._null_&lpar;_qtext=\"alt2 link text\"&rpar;>")]**. Doing so then cause **_qlink** to emit: [link.sample._qlink].

As in the @html namespace, any valid HTML attribute can be specified when creating link variables. Like @html, attributes that begin with an underscore ***_*** are considered *private* and attributes that begin with a letter are considered *public*. When HTML tags are emitted as part of variable expansion, all public attributes are written as part of the opening tag. Let's see how this works.

If we add **title="my link title here"** when we define the link variable **link.sample** we were just using, and then emit the code using any of the emitters **(link.sample, link.sample._asurl, link.sample._qlink)**, the HTML code includes a **title=** attribute every time the anchor opening tag is written. Let's see how that looks, first, we'll declare it:

@wrap divx
{:.indent}###[E.lb]ln_factory(nm="sample" hr="http://example.com" t="my default title" title="my link title here")[E.rb]
@parw

[link.sample._null_(title="my link title here")]

And now, let's take a look at what the parser emits and what the browser renders:

[e_var.b(t="link.sample")] emits *[code.escape_var(v="link.sample")]* which renders as: [link.sample]
[e_var.b(t="link.sample._asurl")] emits *[code.escape_var(v="link.sample._asurl")]* which renders as: [link.sample._asurl]
[e_var.b(t="link.sample._qlink")] emits *[code.escape_var(v="link.sample._qlink")]* which renders as: [link.sample._qlink]

If you hover over any of the preceding links, the browser will show "**my link title here**" after a couple of seconds. By using this feature, you can add custom CSS styling via **style=** along with other valid HTML attributes to any *@link, @image or @html* namespace tag.. As one last example, we will add **style="font-size:2em"** to the link.sample variable, and then emit the same 3 links as before:

[link.sample._null_(style="font-size:2em")]

[e_var.b(t="link.sample")] emits *[code.escape_var(v="link.sample")]* which renders as: [link.sample]

Similarly, [e_var.b(t="link.sample._asurl")]  and [e_var.b(t="link.sample._qlink")] render as:

[link.sample._asurl]
[link.sample._qlink]

This should give you a pretty good idea of how you can use hyperlinks in your smd documents, and so this wraps up the section on creating them using the built-ins provided in ***sys.imports/link.md***.



[link.ug_bookmarks]
[wrap_h.section(t="###Creating Bookmarks")]

Bookmarks are a special type of link used within an HTML document. There are two logical parts to a bookmark, the ***ID*** and the actual reference to the ID, which is done by writing ***#ID***. Within smd, bookmarks are implemented with the @link namespace, and are usually created using the Bookmark factory, **bm_factory**, which is a built-in link variable. **bm_factory** uses the **bm_template** variable in order to provide a simple abstraction for creating and using bookmarks within an HTML document.

[note(t="***NOTE***: Because the **bm_template** isn't useful outside the context of the **bm_factory**, we are going to focus on the latter only, since it is what you will use to create and use bookmarks.")]

Similar to it's counterpart **ln_factory**, has the following syntax:

@wrap divx
{:.indent}###[E.lb]bm_factory(nm="bookmark1" t="my bookmark text")[E.rb]
@parw

The **bm_factory** does not need the **hr=** parameter, however, because the href is constructed using only the bookmark name, since it refers to a location within the current document.

[link.bm_factory(nm="bookmark1", t="my bookmark text")]

Once the bookmark is created using the syntax above, hyperlinks within the current document are created by using the **.link** attribute, and the anchor location is emitted using simply the variable name. Let's look at an example.

Within your document, use the **[encode_smd(t="[link.bookmark1]")]** to place the anchor at the appropriate location. In our case, I've placed the anchor just below the variable dump below, so that it's easy to test.  To create a hyperlink to that location, use the syntax: **[encode_smd(t="[link.bookmark1.link]")]**, as I have done right here: [link.bookmark1.link]. &lt;-- Click on that link and see that it takes you to the location below.

I'm going to dump the various @link variables we've been creating to create some space between the bookmark link I just emitted above and the location where the heading is that I dropped the anchor.

[bmgreybg._open] 
[var.source.wc_open(t="[e_div.s] variable definition and associated [smdhtml.b] elements")]
@dump link="name$|sample|bookmark1"
[var.source.wc_close]
[bmgreybg._close]

[link.bookmark1]
[wrap_h(t="### This is where I dropped the anchor for **bookmark1**")]

Before we leave bookmarks, it is worth mentioning that this factory also supports the **_qlink** and **_qtext** attributes, just like standard links do. So, using our prior bookmark, here is the output when using them:

[e_var.b(t="link.bookmark1._qlink[E.lp]\"my alternate bookmark name\"[E.rp]")] --[E.gt] [link.bookmark1._qlink(_qtext="my alternate bookmark name")]

That's about all there is to using the smd built-ins for creating HTML bookmarks within a document.

@parw 1
