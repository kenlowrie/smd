@import "$/testsetup.md"

[var.testdoc.begin(title="variables.md" desc="Testing the @var namespace")]

Variables provide a convenient means for text substitution. The syntax for defining a variable is: **@var variable="value"**. Take the following example:
[wrap_h(t="####<span class=\"indent\">@var name=\"Ken Lowrie\"</span>")]
@var name="Ken Lowrie"
Now, anywhere I write &#91;name], it will be replaced with "Ken Lowrie". Let's do that now: [name] &lt;-- Should be Ken Lowrie.

If I instead write: &#91;name]=[&#42;Ken Lowrie*], then everywhere I write &#91;name], it will be replaced with &lt;em>Ken Lowrie&lt;/em>. Okay, let's go ahead and do that now. 
@set name="*Ken Lowrie*"
And now, [name] &lt;-- should be Ken Lowrie wrapped with &lt;em> tags.


@var abc="123"
@var def="456"
@var xyz="?={{abc}}%20{{def}}]"
@link _="jitlinkvar" _inherit="_template_" _text="{{self._}}" href="https://mydomain.com?a=[abc]%20[def]"
@link _="jitlinkvar2" _inherit="jitlinkvar" href="https://mydomain.com[xyz]"
Here is my [jitlinkvar]
Here is my [jitlinkvar2]

[var.plain(t="{:.blue}Variables")]
We can define variables using the syntax: ***[name]=value***. Here's an example. The next line will define the variable *whoami* and set it to *Ken Lowrie*.
@var whoami="Ken Lowrie"
Now, whenever I write whoami inside square brackets **[ ]**, it will replace it with *Ken Lowrie*. Let's try that now. Hello, my name is *[whoami]*. That's pretty straightforward...

@@[html.divx.<]
@wrap p
Here are a couple more examples:

Remember, variable definitions and reference link definitions must be declared on a line by themself. If you put more stuff, it will just process the first one. If it isn't at the beginning of the line, it'll be ignored. For example:

@var varName="varValue is okay."
But @var varName="varValue" is not, because this line begins with "But " ...

@var _noid="noid"
@var id="alsonoid"
@var _id="id0" attr1="attribute 1"
@var _="id1" attr1="attribute 1"
[_noid]
[id]
[id0]
[id0.attr1]
[var.id0]
[var.id0.attr1]
id0._id=[id0._id][b]id0._=[id0._]
[var]
[var.]
[var.nothing]
@dump var="id"  

[var.plain(t="{:blue}Changing attribute values in a variable using @set")]

@set foo="bar"
@set _id="id1" attr1="New Value"
ATTR1 should be "New Value":
[id1]
[wrap_h(t="[hash3]")]
@set _id="id1" foo="bar"
[id1]
@set _id="id1" foo="nubar" bar="oldfu"
[id1]
@set _id="id2" foo="nubar" bar="oldfu"
[id2]
@var _="id2" 1="1" 2="2" 3="3" 4="4" 5="5" 6="6" 7="7" 8="8" 9="9" 10="10"\
               11="11" 12="12" 13="13" 14="14" 15="15" 16="16" 17="17" 18="18" 19="19" 20="20" 21="21"
[id2]
@set _id="id2" 1="x1" 2="x2" 3="x3" 4="x4" 5="x5" 6="x6" 7="x7" 8="x8" 9="x9" 10="x10"\
               11="x11" 12="x12" 13="x13" 14="x14" 15="x15" 16="x16" 17="x17" 18="x18" 19="x19" 20="x20" 21="x21"

[id2]
@parw
@@[html.divx.>]

@set dump_ns_list="var=\"id\""
[testdoc.end]
