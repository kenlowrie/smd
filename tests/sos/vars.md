@import "[sys.imports]/common.md"
[mydef]
@stop

// might have to test this with multiple Python versions (3.6 or later, cause f-strings are a 3.6 thing)
// since right now it relies on the dictionary key order
// take the re: over to the re viewer, and see if it will
// give any hints on how I can make it more reliable/version proof.
// Python 3.7+ guarantees maintaining insertion order of dict keys.
// If I require 3.7+, I should be fine, then, correct?
// this should be same as @var _="b" _format="<br />"
@debug on="ns.var|smd.4|ns.link"
@var b2="<br />"
@var x2a="rvalue" text="stuff" _fu="bar"
@var x2b="rvalue" text="stuff" _fu="bar" _format="override"
@debug off="ns.var"

// this works, but breaks how links work...
@link link1="myvalue"

@set _="x2a" xyz="123"
// set x2a="newval"
// set x2a.text="nv2"
a=[x2a]
a=[x2a.text]+++[x2a._fu]
a=[b2]

b=[basic.b]
b={[var.b]}

c=[sp]
c={[var.sp]}

d=[bb]
d={[var.bb]}

@dump var="b|sp|x" basic="b|sp|x" link="."
