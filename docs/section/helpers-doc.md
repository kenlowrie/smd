[link.ug_helpers]
[wrap_h.chapter(t="## **helpers.md** built-ins")]

**helpers.md** contains a set of built-ins that declare a set of commonly used tags, constants and other useful things to help with creating content. 

[rednote(t="This chapter might get into some information that seems a bit complex because we haven't discussed the namespaces yet. You can either skip ahead and read up on namespaces first, then come back, or just follow along as best you can, and when you get to namespaces, it will probabnly seem like old hat by then.")]

Let's start by taking a look at what's contained in **helpers.md**:

//[docthis.open(h="Add this to helpers-doc.md")]
//[docthis.close]

[terminal.wc_open(t="Contents of helpers.md builtins")]
@embed "[sys.imports]/helpers.md" esc="y"
[terminal.wc_close]

It starts by importing the files that contain things that are being extended or are used to create the macros it is declaring. In most cases, these would already be imported, so they are ignored, but in the rare case where they haven't been, it will prevent a bunch of errors when it tries to parse the contents of this file.

A few useful [smdhtml.b] variables are created, including **tab** and **us**. **tab** just indents content by wrapping it with a [e_tag.b(t="span")] tag, and **us** can be used to [e_us(t="underline")] content inline. It would be a little clumbsy to write [e_var.b(t="html.us.<")][us.<]underline[us.>][e_var.b(t="html.us.>")], so a little later on the variable **e_us** is created, that makes it easier.

The **wrap_h** variable contains several useful attributes to simply creating headings. They are:
[ulistplain.wc_open]
    hash1 - create [e_tag(t="h1")] header of dashes
    hash2 - create [e_tag(t="h2")] header of dashes
    hash3 - create [e_tag(t="h3")] header of dashes
    chapter - create a chapter heading with a thick green bottom border
    section - create a section heading with a smaller green bottom border
    subsect - create a sub-section heading with a thin black bottom border
[ulistplain.wc_close]

These are used throughout the user manual to create the headings you see in the documentation. For example, if I write **[e_var(t="wrap_h.hash3")]**, the parser will emit (and your browser will render):

[wrap_h.hash3]

If instead I write **[e_var(t="wrap_h.subsect[E.lp]t=\"###E and EMOJI\"[E.rp]")]**, this is what I get:

[wrap_h.subsect(t="###E and EMOJI")]

**E** and **EMOJI** create namespace wrappers for commonly used HTML Entities and Emojis. Another helper builtin, **e_moji**, makes it easy to create two different sizes of emojis. For example, **[e_var(t="e_moji[E.lp]e=\"mask\"[E.rp]")]** emits [e_moji(e="mask")], and **[e_var(t="e_moji.big[E.lp]e=\"mask\"[E.rp]")]** emits [e_moji.big(e="mask")].

The variables **e_tag** and **e_var** are used quite a bit in the documentation to encode the entities and markdown so that it can be shown inline instead of having either the parser or the browser process it.

Finally, a commonly used trick of extending an underlying macro is used to create two custom versions of the **note** [e_tag.b(t="div")], **bluenote** and **rednote**. This is done by creating a new variable using the *color*note name, inheriting from the underlying **note** variable, and then one of the attributes within that variable is modified to use the newly created color class in the [smdhtml.b] namespace. Let's use all three of them (note, bluenote and rednote) to see how they render:

[note(c="This is my inline note using the default **note** builtin.")]
[bluenote(t="This is my inline note using the **bluenote** builtin created in helpers.md.")]
[rednote(t="This is my inline note using the **rednote** builtin created in helpers.md.")]

Taking an underlying builtin and just **tweaking** it makes it easy to extend the builtins, without having to spend a lot of time recreating the wheel so to speak... [e_moji.big(e="tonguewink")]

The last things (at the time of writing this chapter) are the **bigmargin** and **bmgreybg** [smdhtml.b] variables that are also used in the documentation to render content with bigger than the default margins. They can both be nested, which makes it easy to do things like this:

[bigmargin._open]
    *Here is some content with 3.3em right and left margins. See how it's been indented on the left?*
[bigmargin._close]
Now let's nest them:
[bigmargin._open]
    [bigmargin._open]
        *Here is some content with 3.3em right and left margins. Now it's got double margins or 6.6em.*
    [bigmargin._close]
[bigmargin._close]
Let's try the **bmgreybg** with the same thing:

[bmgreybg._open]
    *Here is some content with 3.3em right and left margins. See how it's been indented on the left?*
[bmgreybg._close]
Now let's nest them:
[bmgreybg._open]
    [sp]
    [bmgreybg._open]
        *Here is some content with 3.3em right and left margins. Now it's got double margins or 6.6em.*
    [bmgreybg._close]
    [sp]
[bmgreybg._close]
That's kind of interesting with the double boxes. Let's use the **bigmargin** first, then the **bmgreybg** inside:

[bigmargin._open]
    [sp]
    [bmgreybg._open]
        *Here is some content with 3.3em right and left margins. Now it's got double margins or 6.6em.*
    [bmgreybg._close]
    [sp]
[bigmargin._close]


Now let's use the **bluenote** to render the middle text and **bigmargin** for the two nests:
[bigmargin._open]
    [bigmargin._open]
        [bluenote(c="Here is some **blue** content with 3.3em right and left margins. Now it's got double margins or 6.6em.")]
    [bigmargin._close]
[bigmargin._close]

Anyway, I think you get the point. There's a lot you can do with the markdown and building custom variables or macros or whatever you want to call them. Let's move on.
