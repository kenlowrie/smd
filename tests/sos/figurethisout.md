//Here is a difference between {{ }} and [ ]
//TODO: Study this, and understand why it happens, and when it's useful to rely on it when writing macros and expansions.
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


@wrap nop
// if @wrap nop in effect, you can't use this line, even with prefix! 
TEST::: [escape_var(v="code.wrap_stack")]



----------------------

you can't use escape_var... if the variable has a {{code.pushlines}} in it. I think because it expands, not sure. It would be nice to figure out why this is, because several of the builtin code macros fail when attempting to use them with variables that use pushlines... Not just code.pushlines either. I think it has to do with get_value() in the namespace xface actually causing code to run??? figure it out!
----------------------

----------------------

----------------------

----------------------

----------------------

----------------------

----------------------


