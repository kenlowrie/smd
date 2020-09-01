[link.ug_div]
[wrap_h.chapter(t="##Divs")]

In this chapter, we will discuss the predefined **DIV**'s that are declared inside the builtin file **divs.md**. 

[rednote.wc_open]
NOTE: If you have not read the chapters on [link.ug_ns_var._qlink(_qtext="[smdvar.b]")], [link.ug_set_keyword._qlink(_qtext="[smdset.b]")] and [link.ug_ns_html._qlink(_qtext="[smdhtml.b]")], stop right now and go read them. Otherwise, you might have trouble understanding the concepts that will be covered in this chapter...
[rednote.wc_close]

The predefined DIVs in the **divs.md** builtin are organized into four types to provide several options for your content. Let's start with a summary of the divs that are available:

[ulistplain.wc_open]
[e_us(t="{:.green}**Generic DIVs**")]
[e_var.b(t="section")] - Generic content
[e_var.b(t="section_pbb")] - Generic content but with the class **pbb** (i.e. page break before -- when printing)
[e_var.b(t="toc")] - Table of Contents
[e_var.b(t="syntax")] - Syntax content
[e_var.b(t="review")] - Review content
[e_var.b(t="review_pba")] - Review content with **pba** class (i.e. page break after -- when printing)
[e_var.b(t="plain")] - Plain content with class plainTitle (draws a bottom-border) after the title[bb]
[e_us(t="{:.green}**Source DIVs**")]
[e_var.b(t="code")] - Source content - See notes for rendering details[bb]
[e_us(t="{:.green}**Note DIVs**")]
[e_var.b(t="note")] - Note content - See notes for rendering details on this and remaining DIVs
[e_var.b(t="box")] - Box content
[e_var.b(t="generic")] - Generic content
[e_var.b(t="greyout")] - Greyout content
[e_var.b(t="important")] - Important content
[e_var.b(t="question")] - Question content
[e_var.b(t="vo")] - Voiceover content[bb]
[e_us(t="{:.green}**List DIVs**")]
[e_var.b(t="ulist")] - Unordered bulleted list content
[e_var.b(t="ulistplain")] - Unordered list no bullets content
[e_var.b(t="olist")] - Ordered list with decimal numbers content

[ulistplain.wc_close]

@var e_div_ll="{{self._public_attrs_}}" s="SECTION" e="*{{self.s}}*" b="**{{self.s}}**" emb="***{{self.s}}***" il="{{self.s}}"
@var _="e_div" _inherit="e_div_ll" _format="{{self.il}}" s="section"

[wrap_h.section(t="###Generic DIVs")]
There are four different styles of DIVs that are predefined for you, and you can add more as well as customize these to your hearts content. Each of these has a similar interface, so let's see what that is, and how it is used. Only one of each different type will be covered, since the interface on the others is identical! We will start with the *[e_div.b]-style* DIVs, of which you have **section, section_pbb, toc, syntax, review, review_pba and plain**.

First, let's take a look at the actual definition of [e_div.b] and it's associated [smdhtml.b] and [smdvar.b] variables:

[code.pushlist(attrlist="var.dumpit" \
               nsvar="html" \
               nsname="^_section_div_$|^_section_p" \
               title="[smdhtml.il] Support for *section*")]

// Give t,c reasonable defaults instead of whatever the last [section] block was ...
[section._null_(t="section default title string" c="section default content data")]
[code.pushlist(attrlist="var.dumpit" \
               nsvar="var" \
               nsname="section$" \
               title="[smdvar.il] definition for *section*")]

If you examine any of other styles in the [e_us(t="{:.blue}**Generic Groups**")], you will find they have an identical set of attributes/methods. So once you are familiar with one of them, you know how to use all of them! Here is the help string for the [e_div.b] var, which applies to all of the generic groups:

[syntax.wc_open(t="Built-in help string for ***section*** DIV")]
    [section.?]
[syntax.wc_close]

[wrap_h.subsect(t="###[smdraw.il] Versions")]
The [smdraw.b] versions will emit using **@@**, which signals the output formatter to suppress any [smdwrap.b] tags in effect. This is done to prevent any unintentional formatting from changing how the browser will render the markup. Let's try each of the methods using the default values, starting with [e_var.b(t="section")]:

[section]

If we look at the HTML for it, you will see:

[syntax.wc_open(t="Raw HTML emitted by the [E.lb]section[E.rb] variable")]
[b]
[tab.<][escape_var(v="var.section")][tab.>]
[syntax.wc_close]

As mentioned, this is in the [smdraw.b] section, so the parser emits the double **@@** prefix, which prevents the output formatter from prefixing any [smdwrap.b] tags. Let's take a look at the remaining built-in attributes and how they render.

[e_var.b(t="section.with_content")] renders like this:
[section.with_content]

If you examine the built-in help, you will see that these two versions rely on the parameters **t** and **c** to override default values. Thus, if we were to write the following:

[terminal.wc_open(t="Passing parameters to *section* methods")]
[E.lb]section(t="My heading")[E.rb]
[E.lb]section(t="My with_content heading" c="My important content")[E.rb]
[terminal.wc_close]

The parser emits the following:

[section(t="My heading")]
[section.with_content(t="My with_content heading" c="My important content")]

// Reset t,c reasonable defaults instead of whatever the last [section] block was ...
[section._null_(t="section default title string" c="section default content data")]

So in any of the methods that take either [big.120p(t="t" cls=".bold.black")] and/or [big.120p(t="c")], you can easily specify your own values when you invoke the method in your markdown. Moving on, let's take a look at the **wc_open** method, which allows you to create a section but leave the **DIV** open to accept the content up until it encounters the **wc_close** method.

Consider the following markdown:

[terminal.wc_open(t="Using section.wc_open")]
    [E.lb]section.wc_open[E.rb]

    and now we have to write [e_var.b(t="section.wc_close")] which will close the previous div.
    We can keep typing lines, though, and they are added to this section until you close it with [e_var.b(t="section.wc_close")].

    Okay, the next line in the user docs will contain: [e_var.b(t="section.wc_close")]
    [E.lb]section.wc_close[E.rb]
[terminal.wc_close]

The parser emits the following:

//TODO.md: We cannot escape_var these things that do {{pushlines}}. 
//TODO.md: Not easily fixable. getValue() does a markdown, which does the pushline,...

[section.wc_open]

and now we have to write [e_var.b(t="section.wc_close")] which will close the previous div.
We can keep typing lines, though, and they are added to this section until you close it with [e_var.b(t="section.wc_close")].

Okay, the next line in the user docs will contain: [e_var.b(t="section.wc_close")]
[section.wc_close]

You can also nest them, let's look at an example of that. Here I will just write [e_var.b(t="section.wc_open")] three times in a row, followed by three [e_var.b(t="section.wc_close")] tags.

[section.wc_open]
[section.wc_open]
[section.wc_open]
[section.wc_close]
[section.wc_close]
[section.wc_close]

As we previously mentioned, all of the variables within a group contain the exact same attributes/methods. Given that, we can nest them within each other. For example:

[terminal.wc_open(t="Nesting other general DIVs")]
    [E.lb]section.wc_open(t="This is the section.wc_open markdown")[E.rb]
    [sp.2][E.lb]syntax.wc_open(t="This is the syntax.wc_open markdown")[E.rb]
    [sp.4][E.lb]toc.wc_open(t="This is the toc.wc_open markdown")[E.rb]
    [sp.6][E.lb]plain.wc_open(t="This is the plain.wc_open markdown")[E.rb]
    [sp.6][E.lb]plain.wc_close[E.rb]
    [sp.4][E.lb]toc.wc_close[E.rb]
    [sp.2][E.lb]syntax.wc_close[E.rb]
    [E.lb]section.wc_close[E.rb]
[terminal.wc_close]


[section.wc_open(t="This is the section.wc_open markdown")]
    [syntax.wc_open(t="This is the syntax.wc_open markdown")]
        [toc.wc_open(t="This is the toc.wc_open markdown")]
            [plain.wc_open(t="This is the plain.wc_open markdown")]
            [plain.wc_close]
        [toc.wc_close]
    [syntax.wc_close]
[section.wc_close]

That is a good segue into changing the default values for these examples, as we touched on briefly earlier.

All of these attributes (across all of the different div types) use the same attribute names for parameters. [big.120p(t="t" cls=".bold.black")] for the title and [big.120p(t="c")] for the content. 

So, when we write [e_var.b(t="section.with_content[E.lp]t=\"my title\" c=\"my content\"")], we will see this:

[section.with_content(t="mytitle" c="my content")]

Similarly, if we write [e_var.b(t="section[E.lp]t=\"my different title\"")], we get:

[section(t="my different title")]

And now if we got back and use that same nested sequence from before, we would get:

[section.wc_open]
[section.wc_open]
[section.wc_open]
[section.wc_close]
[section.wc_close]
[section.wc_close]

Recall how specifying a new value for any parameter in namespace variables (other than the [smdcode.b] namespace) is sticky. That is, when you override a value on a method call, that value will continue to be used until it is overridden again. That's an important concept to remember, as it applies throughout [smd.b]. If we use the **.with_content** instead, we get:

[section.with_content]

See how that works? Remember, this goes back to the side effect discussed in the [link.ug_ns_var.link] chapter that discussed when attribute values are updated they stay updated. So in this last example, the default values used were those from the previous time we used [e_div.b] in this chapter (I was going to say *section*, but it seems like I've worn that out already).

Okay, now let's look at the **inline** versions of the [e_var.b(t="section")] variable.

[wrap_h.subsect(t="###Inline Versions")]

The **_inline** versions of the attribute methods match up to their [smdraw.b] cousins just about identically. The only difference between these versions and their *non-_inline* counterparts is that they do not prefix the output with the [smdraw.b] tag. Here are some examples of how the output looks when using them:

First, here's [e_var.b(t="section.inline")]:

[section.inline]

And now, [e_var.b(t="section.wc_inline")]:

[section.wc_inline]

Essentially what you get when using them is output wrapped with whatever the current [smdwrap.b] tag happens to be. This gives you plenty of flexibility to style the output by only controlling the block elements that contain the **_inline** versions of each.

Currently, the [smdwrap.b] tag is set to: ***[escape_var(v="code.wrap_stack")]***. Let's set it to [smdwrap_wp.b(parms="nop")], and then add the same two previous markdown elements:
@wrap nop
[section.inline]
[section.wc_inline]
@parw

Now they are identical to using the **non-*_inline*** versions, since [smdwrap_wp.b] is essentially telling the output formatter to write in raw mode! The final two inline modes will be covered in the next section on nesting DIVs, but there isn't any real magic to them. They match up to their counterparts exactly like the two we just reviewed...

[wrap_h.subsect(t="###Final notes on nesting DIVS")]
Before we leave Generic DIVs, let's look at a few more examples of nesting. You can get into some precarious formatting issues if you aren't careful, due to how most modern browsers treat block elements, as you'll see below.

In the first example, we are using **wc_open_inline** followed by content, then another **wc_open_inline**, etc. We are also using the [smdraw.b] tag on each of the [big.110p(t="wc_[E.ast]" cls=".blue")] calls, to prevent the output formatter from wrapping the divs with the current wrap tags. Let's take a look at the markdown, and then what the parser emits:

[terminal.wc_open(t="Nesting wc_open_inline with content")]
    [E.at][E.at][E.lb]section.wc_open_inline[E.rb]
    [sp.2]Here is some content.
    [sp.2][E.at][E.at][E.lb]section.wc_open_inline[E.rb]
    [sp.4]Here is different content.
    [sp.4][E.at][E.at][E.lb]section.wc_open_inline[E.rb]
    [sp.6]And here's the last nested content.
    [sp.4][E.at][E.at][E.lb]section.wc_close_inline[E.rb]
    [sp.4]But here is some additional written after closing the innermost div.
    [sp.2][E.at][E.at][E.lb]section.wc_close_inline[E.rb]
    [sp.2]And some final content just before closing the outmost div...
    [E.at][E.at][E.lb]section.wc_close_inline[E.rb]
[terminal.wc_close]

And here's how the browser will render that:

@@[section.wc_open_inline]
    Here is some content.
    @@[section.wc_open_inline]
        Here is different content.
        @@[section.wc_open_inline]
            And here's the last nested content.
        @@[section.wc_close_inline]
        But here is some additional written after closing the innermost div.
    @@[section.wc_close_inline]
    And some final content just before closing the outmost div...
@@[section.wc_close_inline]

This works okay (as long as you use the [smdraw.b] tag when emitting the inline divs, because [smdwrap.b] is set to [e_tag.emb(t="p")], so each line is wrapped as a paragraph.

In this next example, we will do the same thing, but without any line breaks. It looks similar, except that most modern browsers will close an open block tag if a new block tag is encountered. Unfortunately, there isn't any simple way to address this because you can't rely on the output formatter of [smd.b] to solve the issue (like we did above), because there is only a single line being output...

[terminal.wc_open(t="Nesting wc_open_inline with content on a single line")]
    [E.at][E.at][E.lb]section.wc_open_inline[E.rb] Here is some content. [E.lb]section.wc_open_inline[E.rb] Here is different content. [E.lb]section.wc_open_inline[E.rb] And here's the last nested content. [E.lb]section.wc_close_inline[E.rb] But here is some additional written after closing the innermost div. [E.lb]section.wc_close_inline[E.rb] And some final content just before closing the outmost div... [E.lb]section.wc_close_inline[E.rb]
[terminal.wc_close]

Which will render like this:

@@[section.wc_open_inline] Here is some content. [section.wc_open_inline] Here is different content. [section.wc_open_inline] And here's the last nested content. [section.wc_close_inline] But here is some additional written after closing the innermost div. [section.wc_close_inline] And some final content just before closing the outmost div... [section.wc_close_inline]

In this final example on nesting, we will use the raw attribute methods again, just writing the content on separate lines. This behaves exactly like the first version above, just perhaps a bit more readable since you don't need the [smdraw.b] tags. First, let's look at the markdown:

[terminal.wc_open(t="Nesting [smdraw.il] wc_open with content")]
    [E.lb]section.wc_open[E.rb]
        [sp.2]Here is some content.[E.lb]b[E.rb]
        [sp.2]and more content
        [sp.2][E.lb]section.wc_open[E.rb]
            [sp.4]Here is different content.
            [sp.4][E.lb]section.wc_open[E.rb]
                [sp.6]And here's the last nested content.
            [sp.4][E.lb]section.wc_close[E.rb]
            [sp.4]But here is some additional written after closing the innermost div.
            [sp.4]what about this?
        [sp.2][E.lb]section.wc_close[E.rb]
        [sp.2]And some final content just before closing the outmost div...
        [sp.2]and more
        [sp.2]and more
    [E.lb]section.wc_close[E.rb]
[terminal.wc_close]

And now here's what the browser renders.

[section.wc_open] 
    Here is some content.[b]
    and more content
    [section.wc_open] 
        Here is different content.
        [section.wc_open] 
            And here's the last nested content.
        [section.wc_close] 
        But here is some additional written after closing the innermost div.
        what about this?
    [section.wc_close] 
    And some final content just before closing the outmost div...
    and more
    and more
[section.wc_close]

[wrap_h.subsect(t="###Other Generic DIVs")]

The remaining Generic DIVs have all the same behaviour and attributes as [e_div.b(s="section")]. The only difference in how they look goes back to how they are styled in the **smd.css** file. Try a few out, and/or take a look at the **tests/in/divs.md** unittest file to see them in action! Here is the online help for each of the remaining divs, **toc**, **syntax**, **review** and **plain**.

@var WHICH="{{self.l}}" l="toc" u="TOC" b="**{{self.l}}**" B="**{{self.u}}**" em="*{{self.l}}*" EM="*{{self.u}}*" emb="***{{self.l}}***" EMB="***{{self.u}}***"

#### [WHICH.em] Generic DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l].with_content example
**[E.lb][WHICH.l].with_content(t="My [WHICH.u] heading" c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l].with_content(t="My [WHICH.u] Heading" c="My [WHICH.u] content")]

[WHICH._null_(l="syntax" u="SYNTAX")]
#### [WHICH.em] Generic DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l].with_content example
**[E.lb][WHICH.l].with_content(t="My [WHICH.u] heading" c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l].with_content(t="My [WHICH.u] Heading" c="My [WHICH.u] content")]


[WHICH._null_(l="review" u="REVIEW")]
#### [WHICH.em] Generic DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l].with_content example
**[E.lb][WHICH.l].with_content(t="My [WHICH.u] heading" c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l].with_content(t="My [WHICH.u] Heading" c="My [WHICH.u] content")]

[WHICH._null_(l="plain" u="PLAIN")]
#### [WHICH.em] Generic DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l].with_content example
**[E.lb][WHICH.l].with_content(t="My [WHICH.u] heading" c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l].with_content(t="My [WHICH.u] Heading" c="My [WHICH.u] content")]


[wrap_h.section(t="###Source DIVs")]

[e_div._null_(s="source")]
The **source** DIV provides formatting for inline source code, using the [e_tag.b(t="code")] HTML tag. It is used throughout the user manual displaying sample [smd.b] markdown as well as variable definitions. 

Here is the definition of [e_div.b] (displayed with **source**, of course) and it's associated [smdhtml.b] and [smdvar.b] variables:

[code.pushlist(attrlist="var.dumpit" \
               nsvar="html" \
               nsname="^_source_" \
               title="[smdhtml.il] Support for ***source***")]

// Give t,c reasonable defaults instead of whatever the last [source] block was ...
[source._null_(t="source default title string" c="source default content data")]
[code.pushlist(attrlist="var.dumpit" \
               nsvar="var" \
               nsname="source$" \
               title="[smdvar.il] definition for ***source***")]

If you compare the declaration of **source** to any of the **generic** DIVs, the first thing you'll notice is that both the *_source_p_* and *_source_p_content_* [smdhtml.b] variables have been replaced with *_source_* and *_source_content_*. This minor difference essentially causes content to be wrapped with the [e_tag.b(t="code")] [smdhtml.b] tag instead of the [e_tag.b(t="p")] tag, like all of the **generic** DIVs.

Besides that, it's pretty much identical to the **generic** DIVs we discussed in the previous section.

[WHICH._null_(l="source" u="SOURCE")]
#### [WHICH.em] DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l].with_content example
**[E.lb][WHICH.l].with_content(t="My [WHICH.u] heading" c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l].with_content(t="My [WHICH.u] Heading" c="My [WHICH.u] content")]

As you can see by reviewing the output, the [e_tag.b(t="code")] [smdhtml.b] tag does not apply any formatting to the provided content, so when you use it, adding the appropriate formatting and line breaks is quite important. Let's try that again:

#### [WHICH.l].with_content example
**[E.lb][WHICH.l].with_content(t="My [WHICH.u] heading" c="[E.lb]bb[E.rb]My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l].with_content(t="My [WHICH.u] Heading" c="[bb]My [WHICH.u] content")]

When using **source**, you will likely want nest the output inside another DIV in order to prevent it from smashing into the left margin of the browser window. There are many different ways to accomplish this; in the user manual, this is normally done by wrapping the **source** DIV with either the **bmgreybg** or **bigmargin** [smdhtml.b] tag like this:

#### *[WHICH.l].with_content* example wrapped with *bigmargin* tag
**[E.lb]*bigmargin*._open[E.rb]**
[sp.4]**[E.lb]*[WHICH.l].with_content*(t="My [WHICH.u] heading" c="[E.lb]bb[E.rb]My [WHICH.u] content")[E.rb]**
**[E.lb]*bigmargin*._close[E.rb]**
#### renders like this:
[bigmargin._open]
[[WHICH.l].with_content(t="My [WHICH.u] Heading" c="[bb]My [WHICH.u] content")]
[bigmargin._close]



[wrap_h.section(t="###Note DIVs")]

[e_div._null_(s="note")]

**Note** DIVs provide formatting for inline notes. They are similar to the **generic** DIVs, but instead of having a dedicated class for their containing DIV, they all use the **extras** class for their DIV container, and then have styling specific to the content contained within. In addition, they do not support the concept of **title/content**, i.e. the variables [big.120p(t="t,c" cls=".bold.blue")]. Instead, only [big.120p(t="c")] is used to specify the content.

Not surprisingly, one of the builtins for the **Note** DIVs is called simply **note**. We will start our examination of this class of DIVs by taking a look at the actual definition of [e_div.b] and it's associated [smdhtml.b] and [smdvar.b] variables:

[code.pushlist(attrlist="var.dumpit" \
               nsvar="html" \
               nsname="^_note_div_$|^_note_p" \
               title="[smdhtml.il] Support for ***note***")]

// Give t,c reasonable defaults instead of whatever the last [note] block was ...
[note._null_(c="note default content data")]
[code.pushlist(attrlist="var.dumpit" \
               nsvar="var" \
               nsname="note$" \
               title="[smdvar.il] definition for ***note***")]

Just like how all the attributes/methods of the [e_us(t="{:.blue}**Generic Groups**")] are similar to the those in **section** DIV, if you examine any of other styles in the [e_us(t="{:.blue}**Note Groups**")], you will find they have an identical set of attributes/methods. So once you are familiar with those in the **note** DIV, you know how to use all of them! Here is the help string for the [e_div.b] var, which applies to all of the note groups:

[WHICH._null_(l="note" u="note")]
#### [WHICH.em] Note DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

Like we mentioned above, the **Note** DIVs have a similar set of attribute and methods, just like the other DIVs we've covered so far. The real difference is the addition of the ***nd, _nd*** variants to the methods. **ND**, in this context, stands for **no div**, which, as you might guess, are variants that do not emit **DIV** wrappers around the content. These are most useful when combined with the **AV Shot** support, as you will see later in the chapters that cover the examples. Here are a few examples to illustrate how these look.


[wrap_h.subsect(t="###[smdraw.il] Versions")]
The [smdraw.b] versions will emit using **@@**, which signals the output formatter to suppress any [smdwrap.b] tags in effect. This is done to prevent any unintentional formatting from changing how the browser will render the markup. Let's try each of the methods using the default values, starting with [e_var.b(t="note")]:

[note]

If we look at the HTML for it, you will see:

[syntax.wc_open(t="Raw HTML emitted by the [E.lb]note[E.rb] variable")]
[b]
[tab.<][escape_var(v="var.note")][tab.>]
[syntax.wc_close]

As mentioned, this is in the [smdraw.b] section, so the parser emits the double **@@** prefix, which prevents the output formatter from prefixing any [smdwrap.b] tags. Let's take a look at the remaining built-in attributes and how they render.

[e_var.b(t="note.with_content")] renders like this:
[note.with_content]

If you examine the built-in help, you will see that these two versions rely on the parameter **c** to override default values. Thus, if we were to write the following:

[terminal.wc_open(t="Passing a parameter to *note* methods")]
[E.lb]note(c="My content with no method specified")[E.rb]
[E.lb]note.with_content(c="My content using the [E.ast]with_content[E.ast]")[E.rb]
[terminal.wc_close]

The parser emits the following:

[note(c="My content with no method specified")]
[note.with_content(c="My content using the *with_content*")]

// Reset c to a reasonable default instead of whatever the last [note] block was ...
[note._null_(c="note default content data")]

So in any of the methods that take either [big.120p(t="t" cls=".bold.black")] and/or [big.120p(t="c")], you can easily specify your own values when you invoke the method in your markdown. Moving on, let's take a look at the **wc_open** method, which allows you to create a section but leave the **DIV** open to accept the content up until it encounters the **wc_close** method.

Consider the following markdown:

[terminal.wc_open(t="Using note.wc_open")]
    [E.lb]note.wc_open[E.rb]

    and now we have to write [e_var.b(t="note.wc_close")] which will close the previous div.
    We can keep typing lines, though, and they are added to this note until you close it with [e_var.b(t="note.wc_close")].

    Okay, the next line in the user docs will contain: [e_var.b(t="note.wc_close")]
    [E.lb]note.wc_close[E.rb]
[terminal.wc_close]

The parser emits the following:

//TODO.md: We cannot escape_var these things that do {{pushlines}}. 
//TODO.md: Not easily fixable. getValue() does a markdown, which does the pushline,...

[note.wc_open]

and now we have to write [e_var.b(t="note.wc_close")] which will close the previous div.
We can keep typing lines, though, and they are added to this section until you close it with [e_var.b(t="note.wc_close")].

Okay, the next line in the user docs will contain: [e_var.b(t="note.wc_close")]
[note.wc_close]

Unlike the **Generic Group**, the **Note Group** doesn't support nesting.

Okay, now let's look at the **inline** versions of the [e_var.b(t="note")] variable.

[wrap_h.subsect(t="###Inline Versions")]

The **_inline** versions of the attribute methods match up to their [smdraw.b] cousins just about identically. The only difference between these versions and their *non-_inline* counterparts is that they do not prefix the output with the [smdraw.b] tag. Here are some examples of how the output looks when using them:

First, here's [e_var.b(t="note.inline")]:

[note.inline]

And now, [e_var.b(t="note.wc_inline")]:

[note.wc_inline]

As is readily evident, the *wc_[E.ast]* variants of the **Note DIVs** are somewhat redundant, given the output is identical as just shown. However, they have been maintained in order to keep consistency between the **Generic** and **Source** DIVs.

Just like the **Generic DIVs**, what you get when using them is output wrapped with whatever the current [smdwrap.b] tag happens to be. This gives you plenty of flexibility to style the output by only controlling the block elements that contain the **_inline** versions of each.

As we eluded to earlier, the **Note DIVs** do have an additional set of methods referred to as the *No-DIV* or *nd* variants, which emit the content without using a DIV tag. This can be useful in many different situations, including when using in combination with the **A/V and avshot** builtins. This allows notes to be inserted in either the left or right hand columns inline without affecting the floats in effect to format the AV script.

For example, [e_var.b(t="note.nd_inline")] emits [escape_var(v="var.note.nd_inline")] which renders as:

[note.nd_inline]

Currently, the [smdwrap.b] tag is set to: ***[escape_var(v="code.wrap_stack")]***. Let's set it to [smdwrap_wp.b(parms="nop")], and then write all three inline markdown methods (**note.inline**, **note.wc_inline** and **note.nd_inline**):

@wrap nop
[note.inline]
[note.wc_inline]
[note.nd_inline]
@parw

Here you can see that the *nd_* version will be styled according to it's context within the HTML document (in addition to the styling defined as part of the **note** CSS class in **smd.css**.)

[wrap_h.subsect(t="###Other Note DIVs")]

The remaining **Note DIVs** have all the same behavior and attributes as [e_div.b(s="note")]. The only difference in how they look goes back to how they are styled in the **smd.css** file. Try a few out, and/or take a look at the **tests/in/divs.md** unittest file to see them in action! Here is the online help for each of the remaining **Note DIVs**: **box**, **generic**, **greyout**, **important**, **question** and **vo**.

[WHICH._null_(l="box" u="BOX")]
#### [WHICH.em] Note DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l] example
**[E.lb][WHICH.l](c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l](c="My [WHICH.u] content")]


[WHICH._null_(l="generic" u="GENERIC")]
#### [WHICH.em] Note DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l] example
**[E.lb][WHICH.l](c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l](c="My [WHICH.u] content")]



[WHICH._null_(l="greyout" u="GREYOUT")]
#### [WHICH.em] Note DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l] example
**[E.lb][WHICH.l](c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l](c="My [WHICH.u] content")]


[WHICH._null_(l="important" u="IMPORTANT")]
#### [WHICH.em] Note DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l] example
**[E.lb][WHICH.l](c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l](c="My [WHICH.u] content")]


[WHICH._null_(l="question" u="QUESTION")]
#### [WHICH.em] Note DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l] example
**[E.lb][WHICH.l](c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l](c="My [WHICH.u] content")]


[WHICH._null_(l="vo" u="VO")]
#### [WHICH.em] Note DIV
[syntax.wc_open(t="Built-in help string for [WHICH.emb] DIV")]
    [[WHICH.l].?]
[syntax.wc_close]

#### [WHICH.l] example
**[E.lb][WHICH.l](c="My [WHICH.u] content")[E.rb]** renders like this:
[[WHICH.l](c="My [WHICH.u] content")]



Other misc examples...











<hr />

[note]
[note(c="1c")]
[note(c="1ac")]
[note.with_content]
[note.wc_inline]
nd variants
[note.nd]
[note.inline_nd]
[note.nd_inline]
[note._null_(c="2ac")]
here comes wc_open
[note.wc_open]
2ac-inline
[note.wc_close]
[note]
[note.with_content]
[note.nd_open]
2ac-inline variant
[note.nd_close]
<hr />
@wrap null
[note.wc_open_inline]
2ac-inline with null wrap
[note.wc_close_inline]
[mk]
[note.nd_open_inline]
2ac-inline_nd with null wrap
[note.nd_close_inline]
@parw
<hr />


[wrap_h.section(t="###List DIVs")]

[TODO] List divs here


[wrap_h.section(t="###Terminal DIVs")]

[TODO] Terminal divs here

[wrap_h.section(t="###DIVs Summary")]

DIVs are one of the fundemental building blocks for styling HTML pages. Play around with the builtins, and create your own. Remember, you can add your own classes in the **smd.css** CSS file, and then reference them by building your own custom divs using the div factory **_dfactory**.

