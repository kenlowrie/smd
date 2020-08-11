[link.ug_namespaces]
[wrap_h.chapter(t="## Namespaces")]

In [smd.b], one of the primary types of markdown (specially formatted text) that you can use is the **variable**. There are several types of variables that are supported, and they are referred to as namespaces within [smd.b]. They are:

[ulist.wc_open]
[smdvar.b] - The primary namespace for creating variables
[smdhtml.b] - A namespace for creating HTML tags
[smdlink.b] - A namespace built on @html, used for creating hyperlinks and anchors (bookmarks)
[smdimage.b] - A specialized namespace specifically for creating HTML Image [e_tag.b(t="img")] elements
[smdcode.b] - A specialized namespace for creating complex macros (written in Python)
[ulist.wc_close]

[link.ug_ns_builtin_help]
[wrap_h.section(t="### Built in Help")]

There are a few things we need to cover which apply to all namespaces, and in most cases, the chapters are organized so that if you maintain the order, the concepts will be introduced as you go. However, all namespaces support the concept of built-in help, which is an optional attribute named **_help** that can be added to any variable (either at declaration time or later on via [smdset.b]). I want to cover this topic first, since accessing the builtin help, especially for some of the more advanced builtins, will likely be crucial to you learning how to effectively use [smd.b]. Let's see how it works.

[note.with_content(c="Because we haven't yet discussed any of the namespaces, this might seem a little out of place, so feel free to jump ahead to the [smdvar.b] namespace chapter, and then return here afterwards. Otherwise, stick with us, it's short, and should assist with understanding of how things work in any of the namespaces.")]

Take the following markdown which declares a variable **var1**, which takes a parameter **p** and wraps it with [e_tag.b(t="em")] and [e_tag.b(t="strong")] tags. It looks like this:

[tab.<][smdvar.il] var1="[E.ast3]{{self.p}}[E.ast3]" p="sample text"[tab.>]

Once declared, we can write markdown as follows to place the *em* and **strong** tags around text: **[E.lb]var1(p="my important text")[E.rb]**. And it would render like this:

@var var1="***{{self.p}}***" p="sample text"
[tab.<][var1(p="my important text")][tab.>]

Now that's all good (and rather simple), but down the road, when I'm trying to remember how to use it, I don't want to have to track down the file where it is declared to examine it, or even dump the variable definition to decode it's usage. Enter the **_help** attribute. If we add _help to our previous declaration like so:

[tab.<][smdvar.il] var1="[E.ast3]{{self.p}}[E.ast3]" p="sample text" _help="Usage: {{self._}}(p=\"text to wrap with [E.ast3]\")"[tab.>]

Then, when I want to use it, I can type **[E.lb]var1.?[E.rb]**, and it will generate this:

@set _="var.var1" _help="Usage: {{self._}}(p=\"text to wrap with [E.ast3]\")"
[tab.<][var1.?][tab.>]

You can also use the **_help** attribute directly and achieve the same result, but the **?** is shorter and easier to type! So what about the **??** variant? How does that fit in? 

***??*** is a specialized version of the retrieve help attribute that strips most of the HTML markup that is embedded in the help string, making it easy to read when you are running [smd.b] interactively i.e. *[smd] -nd*. If I use it in a document that is used to generate HTML, it won't look that good. For example, if I type **[E.lb]var1.??[E.rb]**, it will generate this:

[tab.<][var1.??][tab.>]

In this case, it doesn't look too bad, only causing the three inline astericks [E.ast3] to render as one red and one black, but let's see how dumping the help string for something more complex looks, and it'll be more obvious. Take the built-in macro **code.get_value**. If I type **[E.lb]code.get_value.?[E.rb]**, it will display this:

[section.wc_open(t="Results of code.get_value.?")]
    [get_value.?]
[section.wc_close]

and then if I type **[E.lb]code.get_value.??[E.rb]**, I get this:

[section.wc_open(t="Results of code.get_value.??")]
    [get_value.??]
[section.wc_close]

So obviously, if you are expecting the content to be readable inside an HTML document, you want the first option. However, if you start [smd.b] interactively, and type the same two things, you will see the the **.?** version has all sorts of HTML tags embedded making it hard to read in the text console, but **.??** is nice and simple and easy to read. Here's a screen shot to prove it:

[IMG_SIZE.medium]
@image _="ss_builtin_help" src="[sys.root]/docs/import/ss_builtin_help.png" style="[IMG_STYLE.inline_border}]"
[ss_builtin_help]

That should give you enough to use the built-in help system while you are learning [smd.b]. In the chapters that follow, we will take an indepth look at each namespace to learn it's specific syntax and semantics. With that, let's move right into the chapter on the [smdvar.b] namespace.
