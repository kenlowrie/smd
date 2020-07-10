[link.ns_code]
[wrap_h.chapter(t="## @code Namespace")]

Section on @code namespaces


[docthis.open(h="Add this to ns_code-doc.md")]

TODO: Should I encode ' before compiling to avoid syntax errors? Not sure if it's that easy, but worth a look...

_code="used by code ns"
_params_="used by code ns"
_last="used by code ns"
run="code.var.run"
src="print('required for code')"
type="eval"


Document code.encode_smd

@@[code.encode_smd(t="@dump sysdef=\".\"")][b]

{:.bigandbold}If this is inline, *[code.encode_smd(t="@var name=\"value\" _format=\"# {{self.name}}\"")]*
//@dump code="encode_smd"
//@set _ns="code" _="encode_smd" b="**{{self.run}}(t={{self.t}})**"
//[encode_smd.b(t="[var]")]

document these
//@@[code.escape_var(v="var.bb")]
//@@[code.encode_smd_var(v="var.bb")]


// be sure to test the @code thing where the only way to change attribute defaults is to use @set...


[docthis.close]
