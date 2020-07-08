@import "$/testsetup.md"

[var.testdoc.begin(title="var.md" desc="Testing @var and @set namespaces")]

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

[plain(t="Specific Testing of @set namespace with @var variables")]

This might be added in the future, if there are things I specifically need to unittest that are not already covered.

[plain(t="Test redeclaring variables")]

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



[var.plain(t="User manual sections for @var and @set")]

@import "[sys.root]/docs/userdocs_macros.md"

[var.toc.wc_open(t="Table of Contents - Unittest [smdvar.il]")]
@wrap nop
[b]
@import "[sys.root]/docs/section/nsvar-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from nsvar-inc.md")]
@dump link="^ns_var|var_|^set_.*$"

@import "[sys.root]/docs/section/nsvar-doc.md"

//TODO: Why if I try to put [ns] in here does it not expand when the code is compiled over in testdoc.end???
// this relates back to there not being a reliable way to cause variables to evaluate markdown when the variable is created.
@set dump_ns_list="var=\".\""

[var.testdoc.end]
