@import "$/testsetup.md"

[var.testdoc_nw.begin(title="code.md" desc="Testing @code namespace")]

@var ns="code"


//TODO: What is _raw attribute for? Look at all the _element_partials. Need to make sure everything is covered in testing...

@wrap divx,p
@import "$/nsbasic.md"
@parw

TODO: Need to add some code specific testing pulling cases from the nsbasic.md, because much of that doesn't test due to missing src and type attributes.

[plain(t="Testing @code builtin functions")]

[wrap_h.hash2]
Testing code.wrap_stack

// Change the default encoding of output from wrap_stack to True so the HTML tags are not interpreted by the browser
@set _id="code.wrap_stack" encode="True"

[divxp.open]
Initially, the wrap_stack should be empty: "[code.wrap_stack]"
[divxp.close]

@wrap divx, p
And now we are changing it to the more traditional "@wrap divx, p": "[code.wrap_stack]"

Next up, we will turn off @wrap, and see that we are clear.

@wrap nop
This should not be wrapped.
@parw

@@[code.wrap_stack(w="<", encode="False")]
@@And this should be wrapped, even though we said it was raw, because previously, we emitted the open tag via code.wrap_stack(w="<")...
@@[code.wrap_stack(w=">", encode="False")]

And now we are back to normal, as we emitted the close tag via code.wrap_stack(w=">")

@@[code.wrap_stack(w="*", encode="False")]
There should be an empty div before this because we emitted the entire wrap tag sequence with code.wrap_stack(w="*")

This concludes the testing of code.wrap_stack
[wrap_h.hash2]

[plain(t="Testing adding new @code builtins")]

@parw

@set dump_ns_list="code=\".\""
[var.testdoc_nw.end]
