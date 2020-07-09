// Things that need to be figured out / fixed if needed should be placed in here. Choose an empty spot below...

// ID: 0002-20
//Here is a difference between {{ }} and [ ]
//TODO: Study this, and understand why it happens, and when it's useful to rely on it when writing macros and expansions.
// It's an order of precedence thing. When it doesn't work, it's because [] is evaluated during the markdown of the entire
//      line, whereas the t="{{self.c}}" doesn't evaluate until the JIT attrs are marked down. Or so is my theory. Need to
//      verify by running in debugger, and looking at the line while it is being processed.
@var ENC="{{code.encode_smd(t=\"&nbsp;{{self.c}}\")}}" c="[smd_markdown_here]"
I expect to get **smd_markdown_here**, but instead I get *[ENC]*
@dump var="ENC"

@var ENC="[code.encode_smd(t=\"&nbsp;[self.c]\")]" c="[smd_markdown_here]"
So put [] around self.c to get **smd_markdown_here**, but instead I get *[ENC]*
@dump var="ENC"

@var ENC="[code.encode_smd(t=\"&nbsp;{{self.c}}\")]" c="[smd_markdown_here]"
So finally, I put the [] around the code.encode_smd, and {{}} around self.c, and I get *[ENC]*
@dump var="ENC"

***[ENC]***


----------------------
// ID: 0005-20
Two different ways to do indented boxes
[fatmargin._open]
[var.code.wc_open(t="High level overview of startup")]

Uses courier font and formatting

[var.code.wc_close]
[fatmargin._close]



[fatmargin._open]
[wrap_h(t="###High level overview of startup")]

... data here - uses standard font and formatting...

[fatmargin._close]

----------------------
// ID: 0007-20

var.terminal vs var.terminal2. Is one better over the other? Should I fix the output of terminal?
----------------------
// ID: 0008-20
// Is this what I was trying to get at with _c _r item in the punchlist.txt?
@html _="spanwc" _inherit="span" class="blue" _c="" _content("{{self.<}}{{self._c}}{{self.>}}"

----------------------
// ID: 0009-20
you can't use escape_var... if the variable has a {{code.pushlines}} in it. I think because it expands, not sure. It would be nice to figure out why this is, because several of the builtin code macros fail when attempting to use them with variables that use pushlines... Not just code.pushlines either. I think it has to do with get_value() in the namespace xface actually causing code to run??? figure it out!



----------------------
// ID: 0011-20
----------------------
// ID: 0012-20


----------------------
// Move these to the Fixed section below after the test is represented in the unit tests...
FIXED THINGS AWAITING ADDITION TO UNIT TESTS ARE BELOW HERE
----------------------








----------------------
FIXED THINGS REPRESENTED IN UNIT TESTS ARE BELOW HERE
----------------------
// no need to keep executing things that are fixed -- don't move them here until they are represented in the unittests.
@stop

----------------------
// ID: 0003-20

//If you use @wrap nop
@wrap nop
//and a line follows like
TEST::: [code.escape_var(v="code.wrap_stack")]
// Does the parser fall thru and match @wrap nop twice? seems like it did, but maybe I was dreaming...

----------------------
// ID: 0004-20
// Just add unittests for these cases
@var fu="1"
@var fu1="abc" attr="xyz"
@var _="fu2" _format="23" attr2="bc"
@var fu3="boo" _format="32" attr2="cb"
@dump var="fu"
@var fu="2"
@var fu1="xyz"
@var fu2="32"
@var _="fu3"
@dump var="fu"
// these show that if you redeclare a variable, the redeclaration wins...

----------------------
// ID: 0006-20
[var.code.wc_open] does not work correctly. leaves open <code> tag... 
Added code to divs.md to test wc_open/wc_open_inline, but didn't actually find a bug...
----------------------
// ID: 0001-20
Fixed this on 7/2/2020 @ 8:18pm
@break
x [code.wrap_stack]
//@wrap nop
@break

@import "[sys.imports]/code.md"

// if @wrap nop in effect, you can't use this line, even with prefix! 
[b]1st try[b]
TEST::: [code.escape_var(v="code.wrap_stack")]
[b]2nd try[b]
[esc_html(url="The wrap stack=<[code.wrap_stack]>")]
[b]3rd try[b]
[code.wrap_stack]
IMPORT HERE
[b]

@import "[sys.imports]/divs.md"
@import "[sys.imports]/helpers.md"

@wrap divx,p
[bb]

----------------------
// ID: 0010-20
If you are using any non-block elements as your current [smdwrap.b] tag, and you are using any of the **avshot** builtins, you need to reset the floating element CSS that is used by the **AV** div. In this example, I've set the [smdwrap.b] tag to [encode_tag(t="p")], so you can see what happens.

[smd.b] has a built keyword, two actually, that you can use to clear the floats and begin normal markdown. They are: [smdbreak.b] or [smdexit.b]. They do exactly the same thing, so it doesn't matter which one you use. Once you insert that command, the floats will be cleared, and you can continue with normal markdown.

I need to fix this once and for all. **p** needs to be the plain p with 1.2em size, so you have a better default. And then AV shot (and any other built-ins for shots), can be modified to use the "special p" that has the float right CSS associated.



----------------------


