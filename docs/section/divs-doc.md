[link.div]
[wrap_h.chapter(t="##Divs")]

In this chapter, we will discuss the predefined **DIV**'s that are declared inside the builtin file **divs.md**. 

[rednote.wc_open]
NOTE: If you have not read the chapters on [link.ns_var._qlink(_qtext="[smdvar.b]")], [link.ns_var._qlink(_qtext="[smdset.b]")] and [link.ns_html._qlink(_qtext="[smdhtml.b]")], stop right now and go read them. Otherwise, you might have trouble understanding the concepts that will be covered in this chapter...
[rednote.wc_close]

The predefined DIVs in the **divs.md** builtin are organized into four types to give several options for your content. Let's start by looking at a summary of the divs that are available:

[ulistplain.wc_open]
[e_us(t="{:.green}**Generic DIVs**")]
[e_var.b(t="section")] - Generic content
[e_var.b(t="section_pbb")] - Generic content but with the class **pbb** (i.e. page break before -- when printing)
[e_var.b(t="toc")] - Table of Contents
[e_var.b(t="syntax")] - Syntax content
[e_var.b(t="review")] - Review content
[e_var.b(t="review_pba")] - Review content with **pba** class (i.e. page break after -- when printing)
[e_var.b(t="plain")] - Plain content with class plainTitle (draws a bottom-border) after the title[bb]
[e_us(t="{:.green}**Code DIVs**")]
[e_var.b(t="code")] - Code content - See notes for rendering details[bb]
[e_us(t="{:.green}**Note DIVs**")]
[e_var.b(t="note")] - Note content - See notes for rendering details on this and remaining DIVs
[e_var.b(t="vo")] - Voiceover content
[e_var.b(t="box")] - Box content
[e_var.b(t="question")] - Question content
[e_var.b(t="greyout")] - Greyout content
[e_var.b(t="important")] - Important content[bb]
[e_us(t="{:.green}**List DIVs**")]
[e_var.b(t="ulist")] - Unordered bulleted list content
[e_var.b(t="ulistplain")] - Unordered list no bullets content
[e_var.b(t="olist")] - Ordered list with decimal numbers content

[ulistplain.wc_close]

//TODO: Move these
@var e_div_ll="{{self._public_attrs_}}" s="SECTION" e="*{{self.s}}*" b="**{{self.s}}**" emb="***{{self.s}}***" il="{{self.s}}"
@var _="e_div" _inherit="e_div_ll" _format="{{self.il}}" s="section"

[wrap_h.section(t="###Generic DIVs")]
There four different styles of DIVs are predefined for you, and you can add more as well as customize these to your hearts content. Each of these has a similar interface, so let's see what that is, and how it is used. Only one of each different type will be covered, since the interface on the others is identical! We will start with the *[e_var.b(t="section")]-style* DIVs, of which you have **section, section_pbb, toc, syntax, review, review_pba and plain**.

Let's begin by taking a look at the actual definition of [e_div.b]:
[fatmargin._open] 
[var.code.wc_open(t="[e_div.s] variable definition and associated [smdhtml.b] elements")]
@dump html="^.*section_$|^_p_section_content" var="section$"
[var.code.wc_close]
[fatmargin._close]

If you examine any of other styles in the [e_us(t="{:.blue}**Generic Groups**")], you will find they have an identical set of attributes/methods. So once you are familiar with one of them, you know how to use all of them! Here is the complete syntax for these generic groups:

[syntax.wc_open(t="[E.lb]section[E.rb] attributes/methods")]
[e_us(t="[b]**[smdraw.b] Versions**")] - these emit the *[smdwrap_wp.il(parms="nop")]*[b]
[e_var.b(t="section")] - Creates a section with a title [e_var.b(t="section.t")][b]
[e_var.b(t="section.with_content")] - Creates a section with a title [e_var.b(t="section.t")] and content [e_var.b(t="section.c")][b]
[e_var.b(t="section.wc_open")] - Creates a section with a title [e_var.b(t="section.t")] and stays open for content[b]
[e_var.b(t="section.wc_close")] - Closes a previous call to [e_var.b(t="section.wc_open")][bb]
[e_us(t="**Inline Versions**")] - these do **not** emit the *[smdwrap_wp.il(parms="nop")]*[b]
[e_var.b(t="section.inline")] - Creates a section with a title [e_var.b(t="section.t")][b]
[e_var.b(t="section.wc_inline")] - Creates a section with a title [e_var.b(t="section.t")] and content [e_var.b(t="section.c")] [b]
[e_var.b(t="section.wc_open_inline")] - Creates an inline section with a title [e_var.b(t="section.t")] and stays open for content[b]
[e_var.b(t="section.wc_close_inline")] - Closes a previous call to [e_var.b(t="section.wc_open_inline")][bb]

[section.wc_close]

[wrap_h.subsect(t="###[smdraw.il] Versions")]
Now let's try each of the methods using the default values, starting with [e_var.b(t="section")]:

[section]

If we look at the HTML for it, you will see:

[syntax.wc_open(t="Raw HTML emitted by the [E.lb]section[E.rb]")]
[b]
[tab.<][escape_var(v="var.section")][tab.>]
[syntax.wc_close]

As mentioned, this is in the [smdraw.b] section, so the parser emits the double **@@** prefix, which prevents the output formatter from prefixing any [smdwrap.b] tags. Let's take a look at the remaining built-in attributes and how they render.

[e_var.b(t="section.with_content")] like this:
[section.with_content]

//TODO: We cannot escape_var these things that do {{pushlines}}. 
//TODO: Not easily fixable. getValue() does a markdown, which does the pushline,...

[e_var(t="section.wc_open")] renders like this:
[section.wc_open]

and now we have to write [e_var.b(t="section.wc_close")] which will close the previous div.
We can keep typing lines, though, and they are added to this section until you close it with [e_var.b(t="section.wc_close")].

[section.wc_close]

You can also next them, let's look at an example of that. Here I will just write [e_var(t="section.wc_open")] three times in a row, followed by three [e_var.b(t="section.wc_close")] tags.

[section.wc_open]
[section.wc_open]
[section.wc_open]
[section.wc_close]
[section.wc_close]
[section.wc_close]

As we previously mentioned, all of the variables within a group contain the exact same attributes/methods. Given that, we can next them within each other too:

[section.wc_open]
[syntax.wc_open]
[toc.wc_open]
[plain.wc_open]
[plain.wc_close]
[toc.wc_close]
[syntax.wc_close]
[section.wc_close]

When you look at this last example, you'll notice that some of the interior divs have non-default headings. This goes back to the side effect discussed in the [link.ns_var.link] chapter that discussed when attribute values are updated they stay updated. So in this last example, the default values used were those from the previous update, in this user guide!

That is a good segue into changing the default values for these examples.

All of these attributes (across all of the different div types) use the same attribute names for parameters. **t** for the title and **c** for the content. So, if we [e_var.b(t="section.with_content[E.lp]t=\"my title\" c=\"my content\"")], we will see this:

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

See how it used the "last" values for **t** and **c**? That's an important concept to remember, as it applies throughout [smd.b]. If we use the **.with_content** instead, we get:

[section.with_content]

See how that works?

Good, now let's look at the **inline** versions of the [e_var.b(t="section")] variable.

[wrap_h.subsect(t="###Inline Versions")]

Now, let's take a look at the **_inline** versions of the attributes. The only difference between these versions and their *non-_inline* counterparts is that they do not prefix the output with the [smdraw.b] tag. Here are some examples of how the output looks when using them:

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

Now they are identical to using the **non-_inline** versions, since [smdwrap_wp.b] is essentially telling the output formatter to write in raw mode! The final two inline modes will be covered in the next section on nesting DIVs, but there isn't any real magic to them. They match up to their counterparts exactly like the two we just reviewed...

[wrap_h.subsect(t="###Final notes on nesting DIVS")]
Before we leave Generic DIVs, let's look at a few more examples of nesting. You can get into some precarious formatting issues if you aren't careful, due to how most modern browsers treat block elements, as you'll see below.

In the first example, we are using wc_open_inline followed by content, then another wc_open_inline, etc. We are using the [smdraw.b] tag on each of the wc* calls, to prevent the output formatter from wrapping the divs with the current wrap tags...

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

@@[section.wc_open_inline] Here is some content. [section.wc_open_inline] Here is different content. [section.wc_open_inline] And here's the last nested content. [section.wc_close_inline] But here is some additional written after closing the innermost div. [section.wc_close_inline] And some final content just before closing the outmost div... [section.wc_close_inline]

In this final example on nesting, we are using the raw attributes again, just writing the content on separate lines. This behaves exactly like the first version above, just perhaps a bit more readable since you don't need the [smdraw.b] tags.

[section.wc_open] 
    Here is some content.<br/>
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

The remaining Generic DIVs have all the same behaviour and attributes as [e_div.b(s="section")]. The only difference in how they look goes back to how they are styled in the **smd.css** file. Try a few out, and/or take a look at the **tests/in/divs.md** unittest file to see them in action!

[wrap_h.section(t="###Code DIVs")]

Code divs here

[wrap_h.section(t="###Note DIVs")]

Note divs here

[wrap_h.section(t="###List DIVs")]

List divs here

[wrap_h.section(t="###DIVs Summary")]

DIVs are one of the fundemental building blocks for styling HTML pages. Play around with the builtins, and create your own. Remember, you can add your own classes in the **smd.css** CSS file, and then reference them by building your own custom divs using the div factory **_dfactory**.

