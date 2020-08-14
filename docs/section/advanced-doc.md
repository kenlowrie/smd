
[link.advanced]
[wrap_h.chapter(t="##Advanced Topics: [smdraw.il] and more")]


//[docthis.open(h="Add this to advanced-doc.md")]
//[docthis.close]

[TODO] Figure out what leftovers should go here. Grep after this pass of the documentation review, and whatever doesn't fit somewhere else should go here.

The case for @raw | @@. When you use them in emitted lines (or inline), any @wrap tag will NOT be applied.

However, the parser will markdown the line, and it the contents change (i.e. markdown was there), then it will use that instead of the actual raw line.

@@ [big]

Seems like @break is essentially a way of doing a "clear:both" thru the use of a display:block element such as headers...

The @break/@exit are not really needed, because the avshot macro properly handles the closure... grep for this and then see if they are still used then decide it we need to document them...

[var.note(t="When you want to force the document out of shot mode, use ***@break*** or ***@exit*** on an empty line. That will reset the floats which are controlling the AV formatting, and start a new section. See how the document leaves the narration mode of the prior shot, and starts this new block paragraph?")]
@break

**[at]break** [lt]--Use @break or @exit to close a shot DIV."



So that pretty much sums up the advanced section. Hopefully it was helpful, if not, ask questions, and I'll clarify. Or better yet, improve the docs, and submit a pull request. :)
