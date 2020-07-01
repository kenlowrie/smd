[link.div]
[wrap_h.chapter(t="##Divs")]

In this chapter, we will discuss the predefined **DIV**'s that are declared inside the builtin file **divs.md**. 
[rednote.wc_open]
NOTE: If you have not read the chapters on [smdvar.b], [smdset.b] and [smdhtml.b], stop right now and go read them. Otherwise, you might have trouble understanding the concepts that will be covered in this chapter...
[rednote.wc_close]

There are several types of these that are created to give several options for your content. Let's first look at a summary of the divs that are available to you:

[ulistplain.wc_open]
[e_us(t="{:.blue}**Generic Groups**")]
[e_var.b(t="section")] - Generic content
[e_var.b(t="section_pbb")] - Generic content but with the class **pbb** (i.e. page break before -- when printing)
[e_var.b(t="toc")] - Table of Contents
[e_var.b(t="syntax")] - Syntax content
[e_var.b(t="review")] - Review content
[e_var.b(t="review_pba")] - Review content with **pba** class (i.e. page break after -- when printing)
[e_var.b(t="plain")] - Plain content with class plainTitle (draws a bottom-border) after the title[bb]
[e_us(t="{:.blue}**Code Group**")]
[e_var.b(t="code")] - Code content - See notes for rendering details[bb]
[e_us(t="{:.blue}**Note Groups**")]
[e_var.b(t="note")] - Note content - See notes for rendering details on this and remaining DIVs
[e_var.b(t="vo")] - Voiceover content
[e_var.b(t="box")] - Box content
[e_var.b(t="question")] - Question content
[e_var.b(t="greyout")] - Greyout content
[e_var.b(t="important")] - Important content[bb]
[e_us(t="{:.blue}**List Groups**")]
[e_var.b(t="ulist")] - Unordered bulleted list content
[e_var.b(t="ulistplain")] - Unordered list no bullets content
[e_var.b(t="olist")] - Ordered list with decimal numbers content

[ulistplain.wc_close]

//TODO: Move these
@var e_div_ll="{{self._public_attrs_}}" s="SECTION" e="*{{self.s}}*" b="**{{self.s}}**" emb="***{{self.s}}***" il="{{self.s}}"
@var _="e_div" _inherit="e_div_ll" _format="{{self.il}}" s="section"

There are four different styles of DIVs that are predefined for you, and you can add more as well as customize these to your hearts content. Each of these has a similar interface, so let's see how what that is, and how it is used. Only one of each different type will be covered, since the interface on the others is identical! We will start with the *[e_var.b(t="section")]-style* DIVs, of which you have **section, section_pbb, toc, syntax, review, review_pba and plain**.

//TODO: Move this to the userdocs_macros.md or helpers.md...
@html _="fatmargin" _tag="div" style="margin-left:3.3em;margin-right:3.3em;border:2px solid black;background:lightgray" _open="@@{{self.<}}" _close="@@{{self.>}}"
Let's begin by taking a look at the actual definition of [e_div.b]:
[fatmargin._open] 
[var.code.wc_open(t="[e_div.s] variable definition and associated [smdhtml.b] elements")]
@dump html="^.*section_$|^_p_section_content" var="section$"
[var.code.wc_close]
[fatmargin._close]

If you examine any of other styles in the [e_us(t="{:.blue}**Generic Groups**")], you will find they have an identical set of attributes/methods. So once you are familiar with one of them, you know how to use all of them! Here is the complete syntax for these generic groups:

[syntax.wc_open(t="[E.lb]section[E.rb] attributes/methods")]
[e_us(t="[b]**[smdraw.b] Versions**")] - these issue the *[smdwrap_parms.il(parms="nop")]*[b]
[e_var.b(t="section")] - Creates a section with a title [e_var.b(t="section.t")][b]
[e_var.b(t="section.with_content")] - Creates a section with a title [e_var.b(t="section.t")] and content [e_var.b(t="section.c")][b]
[e_var.b(t="section.wc_open")] - Creates a section with a title [e_var.b(t="section.t")] and stays open for content[b]
[e_var.b(t="section.wc_close")] - Closes a previous call to [e_var.b(t="section.wc_open")][bb]
[e_us(t="**Inline Versions**")] - these do **not** issue the *[smdwrap_parms.il(parms="nop")]*[b]
[e_var.b(t="section.inline")] - Creates a section with a title [e_var.b(t="section.t")][b]
[e_var.b(t="section.wc_inline")] - Creates a section with a title [e_var.b(t="section.t")] and content [e_var.b(t="section.c")] [b]
[e_var.b(t="section.wc_open_inline")] - Creates an inline section with a title [e_var.b(t="section.t")] and stays open for content[b]
[e_var.b(t="section.wc_close_inline")] - Closes a previous call to [e_var.b(t="section.wc_open_inline")][bb]

[section.wc_close]

Now let's try each of the methods using the default values, starting with [e_var.b(t="section")]:

[section]

If we look at the HTML for it, you will see:

[syntax.wc_open(t="Raw HTML emitted by the [E.lb]section[E.rb]")]
[b]
[tab.<][escape_var(v="var.section")][tab.>]
[syntax.wc_close]

As mentioned, this is in the [smdraw.b] section, so the parser emits the double **@@** prefix, which prevents the output formatter from prefixing any [smdwrap.b] tags.

[e_var.b(t="section.with_content")] emits *[escape_var(v="var.section.with_content")]* which renders like this:
[section.with_content]

//TODO: We cannot escape_var these things that do {{pushlines}}. Look into that, is it easily fixable?

//[e_var(t="section.wc_open")] emits *[escape_var(v="var.section.wc_open")]* which renders like this:

[e_var(t="section.wc_open")] renders like this:

[section.wc_open]

//and now we have to write [e_var.b(t="section.wc_close")] to emit *[escape_var(v="var.section.wc_close")]* which will close the

and now we have to write [e_var.b(t="section.wc_close")] which will close the previous div.
We can keep typing lines, though, and they are added to this section.

[section.wc_close]



This will need to document each of the sections in the divs.md built-ins.
The complete syntax is: 

Remember, you can add your own classes in a CSS file, and then reference them using the built-in formatting of **avscript_md**.

