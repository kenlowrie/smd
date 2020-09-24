
[link.advanced]
[wrap_h.chapter(t="##Advanced Topics: [smdraw.il] and more")]

We've been using [smdraw.b] (which can also be written as **@@**) throughout this documentation, and when and if you ever peer into the builtins that come with [smd.b], you'll see it used quite often. Essentially, beginning a line with [smdraw.b] will suppress any [smdwrap.b] formatting that is currently in effect, making it so you can control exactly what the parser will emit.

There is one thing to keep in mind about this if markdown is written after the [smdraw.b] qualifier: since the markdown could effectively change the line to something else completely, say if a line is pushed onto the input stream, you may not get the results you were expecting!

[wrap_h.subsect(t="#### @break and @exit")]
In the precursor to [smd.b], a formatter called **avscript**, [smdbreak.b] and [smdexit.b] were used quite heavily to control the formatting, primarily as a means to clear the floats in effect when formatting **AV script**.

In [smd.b], however, they are only used sparingly, but as you might have guessed, it will be in **AV Script** markdown documents. In order to avoid unnecessary blank space between elements, the **avs** macros do not automatically emit a block element that will clear the floats, since in most cases, an **AV** script will simply begin a new shot which avoids the issue. However, if you have a need to insert other information between shots, then you'll likely have to use [smdbreak.b]/[smdexit.b] in order to forcibly clear the floats.

So that pretty much sums up the advanced section. Apparently there aren't too many advanced topics after all... Hopefully it was helpful, if not, ask questions, and I'll clarify. Or better yet, improve the docs, and submit a pull request. :)
