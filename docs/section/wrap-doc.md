[link.wrap]
[wrap_h.chapter(t="## @wrap and @parw")]

By default, smd does not place any type of wrapper around emitted content. This is a good default, however, many times there are cases where adding wrappers can greatly assist your formatting efforts. This is where @wrap comes in handy...

[docthis.open(h="Add this to wrap-doc.md")]

Add @wrap, and probably need to clean up the docs in tests/in/script1.md; possibly xfer to shared markdown files.
99. @wrap nop and null - add tests to wrap.md
100. @parw *|all @parw -3 | 0 | 1 | 25 - add tests.
96. Add @wrap tag1 [, tag2 [...]] support
98. Should handle_header() handle @wrap lines? Code added, need to review closely.

@wrap levels are maintained across imports. so you can't leave a dangling wrap tag from an import file; it is cleared when the file is closed and reset to what it was when the file was imported. time will tell if this is an annoyance or not...

@parw will only clear as far as the top of the stack for the currently imported file...

[code.wrap_stack(w="[>|<|#]")] - document all of these...

[docthis.close]

