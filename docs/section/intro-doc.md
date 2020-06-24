[link.intro]
[wrap_h(t="# Introduction to SMD")]

In this chapter, we will discuss the basics of SMD: what it is, and some of the things you can do with it. It's a fairly versatile script parser, that you can use to easily create HTML documents on the fly, and turn them into a static page, or serve them via an endpoint. Let's get started with an overview of what SMD is.

[var.plain(t="What is SMD?")]

SMD is a Python command line utility that takes plain text files loosely, *oh, so loosely*, based on Markdown as input, and generates an HTML document. A CSS file can be used to style the output, making it super easy to customize the final render to your liking.

In the beginning, it started as a utility for generating AV (Audio/Video) style scripts for filmmakers. Essentially:

{:.note.indent}**Markdown** list item tags ***([ENT.ast], -, +)*** were used to identify ***visuals*** (shots), and regular paragraphs are the ***audio/narration*** that go along with the visuals.

At least that's how it started out. It's grown quite a bit since the early days, and while some markdown span elements are still supported, generating AV Scripts is now done using specialized ***macros*** that are provided as part of the built-ins that come with SMD. The remainder of this document will attempt to provide an in-depth overview of most of the capabilities of SMD, but you are encouraged to look thru all of the samples provided to get a better idea of what it can do.

[link.inlinemd]
[wrap_h(t="###Inline Markdown")]

A few of the standard markdown span elements are supported, as are a couple of specialized span elements. These include (in order of precedence, that is the order they are parsed when scanning input lines):

@@[html.ol.<]
@wrap li2
Variables - These are smd namespace variables accessed with this type of markdown: **[encode_smd(t="[variable]")]**
Strong - Double [ENT.ast2] placed around content will apply the [e_tag.b(t="strong")] tag: **[encode_smd(t="**wrap text in a single asterisk for bold**")]**
Emphasis - Single &ast; placed around content will apply the [e_tag.b(t="em")] tag: *[encode_smd(t="*wrap text in single asterisks for emphasis*")]*
Insertion - Double &plus; placed around content will apply the [e_tag.b(t="ins")] tag: ++[encode_smd(t="++wrap text in double plus signs for &lt;ins&gt; tag++")]++
Deletion - Double &sim; placed around content will apply the [e_tag.b(t="del")] tag: ~~[encode_smd(t="~~wrap text in double tilde for &lt;del&gt; tag~~")]~~
@parw
@@[html.ol.>]

Here are a few examples:

When I write [ENT.ast]text[ENT.ast], it becomes *text*, and when I write [ENT.ast2]text[ENT.ast2], it becomes **text**

You can stack them too, so that [ENT.ast3]text[ENT.ast3] becomes ***text***

When you want to wrap text with [e_tag(t="ins")], use the double plus ([ENT.ins]), and it will render like this: ++Stuff that's been added++. 

Similarly, when you want to wrap text with [e_tag(t="del")], use the double tilde ([ENT.del]), and it will render like this: ~~Stuff that's been removed~~.

So far, this is similar to using regular markdown, so that part, at least, probably isn't new or exciting. When we start mixing in macros, however, things will get much more interesting. We will see that in the chapters that cover the namespaces: **var**, **html**, **link**, **image**, and **code**.


