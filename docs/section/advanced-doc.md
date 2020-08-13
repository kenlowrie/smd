
[link.advanced]
[wrap_h.chapter(t="##Advanced Topics: [smdraw.il] and more")]


//[docthis.open(h="Add this to advanced-doc.md")]
//[docthis.close]

[TODO] Figure out what leftovers should go here. Grep after this pass of the documentation review, and whatever doesn't fit somewhere else should go here.

The case for @raw | @@. When you use them in emitted lines (or inline), any @wrap tag will NOT be applied.

However, the parser will markdown the line, and it the contents change (i.e. markdown was there), then it will use that instead of the actual raw line.

@@ [big]

So that pretty much sums up the advanced section. Hopefully it was helpful, if not, ask questions, and I'll clarify. Or better yet, improve the docs, and submit a pull request. :)
