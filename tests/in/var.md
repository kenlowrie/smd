@import "$/testsetup.md"

[var.testdoc.begin(title="var.md" desc="Testing @var and @set namespaces")]

//TODO: move this to code.md!
@code _id="encode_smd"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd('$.t'))"\
      t="Usage: code.encode_smd.run(t=\"smd markdown to encode\")"

//[code.encode_smd(t="[echo(e=\"hello, world\"&rpar;]")]

@var ns="var"

@import "$/nsbasic.md"

[wrap_h.hash1]
[plain(t="Specific Namespace testing for ***@[ns]*** namespace")]

@var a1="a1_rval"
@var _a4="a4_rval"
[code.encode_smd(t="[a1]")] --> [a1]
[code.encode_smd(t="[_a4]")] --> [_a4]
Setting default rvalue for a2 and a3
@set a2="a2_rval"
@set a3="a3_rval"
[code.encode_smd(t="[a2]")] --> [a2]
[code.encode_smd(t="[a3]")] --> [a3]

@dump var="^a[0-9]{1,2}$"

This next one will work, sort of, because another attribute will become the new "1st attribute", hence the var has a name. Probably not what you wanted though...
{:.blue}&nbsp;@var $="syntax" b_unexpected="attribute ends up becoming the name of the variable..."

@var $="syntax" b_unexpected="attribute ends up becoming the name of the variable..."
***[code.encode_smd(t="[b_unexpected]")]*** = **[b_unexpected]**
These next ones will have the namespace parser  catch the errors and fail the variable creation.

@var 1="1_rval"
@var _id="@"
@var _="a b" _format="syntax"

// Should I force attribute names to conform to the variable naming convention? start with [a-zA-Z_] and then only contain [-\w]?

@var b1="mix of attrs" 123attr="nope"
@dump var="b"

[wrap_h.hash3]
[wrap_h(t="{:.blue}<h4>Testing creating variables with delayed expansion of other variables</h4>")]

@var c0="constants" a="1" b="2" c="3"
@var c1="[c0.a]"
@var c2="{{c0.a}}"

[encode_smd(t="[c1]")] = [c1]
[encode_smd(t="[c2]")] = [c2]

@dump var="c[0-9]{1,2}"

//TODO the next line will crash the parser. Fix that.
@set c0="" a="9"

@dump var="c[0-9]{1,2}"

@set _="c0" a="8" _fmt="Constants"

//TODO: not the behaviour I expected. Thought c1 would have still been 1. Looks like delayed expansion may be the default behavior...
[encode_smd(t="[c1]")] = [c1]
[encode_smd(t="[c2]")] = [c2]

@dump var="c[0-9]{1,2}"


[wrap_h.hash1]

[var.plain(t="{:.blue}Variables")]
We can define variables using the syntax: ***@var name="value"***. Here's an example. The next line will define the variable *whoami* and set it to *Ken Lowrie*.
@var whoami="Ken Lowrie"
Now, whenever I write whoami inside square brackets **[ ]**, it will replace it with *Ken Lowrie*. Let's try that now. Hello, my name is *[whoami]*. That's pretty straightforward...

// be sure to test the @code thing where the only way to change attribute defaults is to use @set...

#### Starting with using @set to change compiled code in @code macros
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
[plain(t="Specific Testing of @set namespace with @var variables")]



//TODO: Why if I try to put [ns] in here does it not expand when the code is compiled over in testdoc.end???
// this relates back to there not being a reliable way to cause variables to evaluate markdown when the variable is created.
@set dump_ns_list="var=\".\""

[var.testdoc.end]
