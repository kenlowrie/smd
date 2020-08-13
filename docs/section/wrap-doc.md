
[link.ug_wrap]
[wrap_h.chapter(t="## @wrap and @parw")]

//[docthis.open(h="Add this to wrap-doc.md")]
//[docthis.close]

By default, [smd.b] does not place any type of wrapper around emitted contE. This is a good default, however, many times adding wrappers can greatly assist your formatting efforts. This is where @wrap comes in handy...

First, let's review the complete syntax for both [smdwrap.b] and [smdparw.b]

[syntax.wc_open(t="@wrap and @parw command syntax")]
    [sp]
    [tab.<][smdwrap.b] **[E.lt]html.tag [E.lb], html.tag [E.lb], ...]] | [E.lb]nop | null][E.gt]**[bb][tab.>]
    [tab.<][smdparw.b] **[E.lb][E.ast] | all | [E.num] [E.rb]**[tab.>]
    [bb]
    [tab.<][tab.<]*NOTE: tag variables passed to [smdwrap.b] **must** be in the **@html** namespace.[tab.>][tab.>]*
[syntax.wc_close]

The concept for [smdwrap.b] is straightforward: whenever anything is written to the output stream, it will be wrapped with the specified variable from the [smdhtml.b] namespace. Let's look at an example, [smd.b] session:

[terminal.wc_open(t="@wrap demonstration")]
    *[smdcomment.il] By default, there are no wrap tags in effect*
    This line will not have any tags
    *Output -->*This line will not have any tags
    [smdwrap_wp(parms="p")]
    This line will be wrapped with HTML p tags
    *Output -->*[escape(t="<p>This line will be wrapped with HTML p tags</p>")]
    This line also...
    *Output -->*[escape(t="<p>This line also...</p>")]
    [smdparw]
    But not this line
    *Output -->*But not this line
[terminal.wc_close]

See how that works? When we issue the **@wrap p** command, subsequent output is wrapped with [escape(t="<p></p>")] tags. It remains in effect until it is cleared with the **@parw** command, or if inside an **@import**'ed file, when EOF is reached on the current file.

[note.with_content(c="It's important to note that any **@wrap** tags that are in effect during the processing of an imported file will be cleared when EOF is reached on that imported file, so that when you return to the parent file, the **@wrap** tag stack for it will be restored to what it was before the file was **@import**'ed.")]

[smdtag.b(p="@wrap")] tags can be nested as well. Consider the following example:

[terminal.wc_open(t="@wrap tag nesting")]
    [smdwrap_wp(parms="div")]
    This line will be wrapped with HTML div tags
    *Output -->*[escape(t="<div>This line will be wrapped with HTML div tags</div>")]
    [smdwrap_wp(parms="p")]
    This line, however, will be wrapped in HTML p tags
    *Output -->*[escape(t="<p>This line, however, will be wrapped in HTML p tags</p>")]
    [smdparw]
    And now we are back to being wrapped in HTML div tags again
    *Output -->*[escape(t="<div>And now we are back to being wrapped in HTML div tags again</div>")]
[terminal.wc_close]

You can nest as deeply as you wish.

In addition, you are not limited to a single HTML tag when wrapping. Take a look at this example:

[terminal.wc_open(t="@wrap tag multiples")]
    [smdwrap_wp(parms="div, p")]
    This line will be wrapped with HTML both a div and a p tag
    *Output -->*[escape(t="<div><p>This line will be wrapped with HTML both a div and a p tag</p></div>")]
[terminal.wc_close]

It is important to distinguish that if multiple tags are listed on a single **@wrap** tag, the parser considers this a single wrap tag with multiple elements. That is, when you use **@parw**, it will clear a single item from the stack, and in the case of a multiple **@wrap** tag, it clears all of the tags associated with that tag. Let's demonstrate it just to be sure:

[terminal.wc_open(t="Clearing @wrap tag multiples")]
    Begin by showing that input is not wrapped by default
    *Output -->*Begin by showing that input is not wrapped by default
    [smdwrap_wp(parms="div, p")]
    This line will be wrapped with HTML both a div and a p tag
    *Output -->*[escape(t="<div><p>This line will be wrapped with HTML both a div and a p tag</p></div>")]
    [smdparw]
    And now this line has no tags
    *Output -->*And now this line has no tags
[terminal.wc_close]

If you issue [smdparw.b] when the wrap stack is empty, the parser issues a warning:

[terminal.wc_open(t="@parw with empty wrap stack")]
    [smdparw]
    [escape(t="WARNING: wrapper stack is empty<br />")]
[terminal.wc_close]

[wrap_h.subsect(t="###Additional options")]

The [smdwrap.b] has two specialized parameters **nop** and **null** which do the same thing: they temporarily suspend wrapping of content with the previously specified [smdwrap.b] tag. Here's an example:

[terminal.wc_open(t="Temporarily suspend wrapping of content")]
    [smdwrap_wp(parms="div, p")]
    This line will be wrapped with HTML both a div and a p tag
    *Output -->*[escape(t="<div><p>This line will be wrapped with HTML both a div and a p tag</p></div>")]
    [smdwrap_wp(parms="null")]
    And now this line has no tags
    *Output -->*And now this line has no tags
    [smdparw]
    And now this line will have the previously specified wrap tags of div, p
    *Output -->*[escape(t="<div><p>And now this line will have the previously specified wrap tags of div, p</p></div>")]
[terminal.wc_close]

The [smdparw.b] also accepts parameters: [big.120p(t="[E.ast] | all" cls=".bold")] or alternatively a [big.120p(t="[E.num]")] specified how many tags to clear from the stack. By default, [smdparw.b] will clear a single item from the wrap stack. If you pass an integer [big.120p(t="n")], then it will attempt to clear [big.120p(t="n")] items from the wrap stack. If you pass either [big.120p(t="[E.ast]")] or [big.120p(t="all")], then it will clear all items from the wrap stack, but only those that were added within the current scope. The current scope just means the current [smdimport.b] file, and it goes back to the note we made up front about remove items from the wrap stack. Here are a couple of examples of the parameters to [smdparw.b]:

[terminal.wc_open(t="Clearing the wrap stack")]
    [smdwrap_wp(parms="div, p")]
    This line will be wrapped with HTML both a div and a p tag
    *Output -->*[escape(t="<div><p>This line will be wrapped with HTML both a div and a p tag</p></div>")]
    [smdwrap_wp(parms="li")]
    And now this line a list item tag
    *Output -->*[escape(t="<li>And now this line a list item tag</li>")]
    [smdparw_wp(parms="*")]
    And now this line has no tags
    *Output -->*And now this line has no tags
    [sp]
    [smdwrap_wp(parms="div")]
    This line will be wrapped with HTML div tags
    *Output -->*[escape(t="<div>This line will be wrapped with HTML div tags</div>")]
    [smdwrap_wp(parms="p")]
    This line, however, will be wrapped in HTML p tags
    *Output -->*[escape(t="<p>This line, however, will be wrapped in HTML p tags</p>")]
    [smdparw_wp(parms="25")]
    [escape(t="WARNING: only 2 items found on the stack that were cleared<br />")]
[terminal.wc_close]

The final thing we'll cover is a specialized [smdcode.b] macro called **wrap_stack**. This macro gives you some additional options to use with [smdwrap.b] tags for a few specialized cases. Here are the details on this macro.

The first thing is the macro itself, here's the builtin help string for it:

[syntax.wc_open(t="code.wrap_stack help string")]
    [code.wrap_stack.?]
[syntax.wc_close]

If you invoke it with no parameters *[E.lb]code.wrap_stack[E.rb]*, it will return the complete starting and ending tags for the current wrap tag. 

If you pass [big.red(t="[E.lt]")], it returns the opening tag(s) sequence, and conversely, [big.red(t="[E.gt]")] returns the closing tag(s).

If you pass [big.red(t="[E.num]")], it returns the current stack size, which is really only useful for debugging purposes. 

Finally, are the options [big.120p(t="tag.<" cls=".red")] and [big.120p(t="tag.>" cls=".red")]. These are similar to the [big.120p(t="[E.lt][sp][E.gt]")] options, but they return the tags in text form instead of as the actual HTML markup. [big.120p(t="tag.<")] is the most useful, because you can use it to maintain the current [smdwrap.b] tags, while adding one or more additional tags.

Here are some examples:

[terminal.wc_open(t="Viewing the wrap stack")]
    [smdwrap_wp(parms="div, p")]
    [encode_smd(t="<code.wrap_stack>")]
    [escape(t="<div><p><div><p></p></div></p></div>")]
    [sp]
    [encode_smd(t="@@<code.wrap_stack>")]
    [escape(t="<div><p></p></div>")]
    [sp]
    [encode_smd(t="@@<code.wrap_stack")](w="[E.lt]")]
    [escape(t="<div><p>")]
    [sp]
    [encode_smd(t="@@<code.wrap_stack")](w="[E.gt]")]
    [escape(t="</p></div>")]
    [sp]
    [encode_smd(t="@@<code.wrap_stack")](w="[E.num]")]
    1
    [sp]
    [encode_smd(t="@@<code.wrap_stack")](w="tag.<")]
    div,p
[terminal.wc_close]

At first glance, the initial call to **[E.lb]code.wrap_stack[E.rb]** might look like a bug, because the tag appears twice. However, this is behaving properly, since technically, a wrap tag of **div,p** is currently in effect, and thus the output from the call to **code.wrap_stack** is being wrapped in the tags! On the subsequent calls, you'll notice we prefix each line with ***[E.at][E.at]***, something we haven't discussed yet. This is the **raw** prefix, and when used at the start of any line, any wrap tags in effect are ignored.

This concludes the chapter on [smdwrap.b] and [smdparw.b].
