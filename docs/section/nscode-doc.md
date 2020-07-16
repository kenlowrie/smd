[link.ug_ns_code]
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

IDEA: @get _ns="" _id="[ns.]name" raw="true" markdown="false" escape="true"
Implementation: [get_variable_RENAME(v="varname" ret_type="0-raw,1-1st pass markdown-2normal as in full markdown" escape="True|False")]

Should [encode_smd(t="[get]")] and [encode_smd(t="[get_variable]")] be combined? Seems unnecessary to have both of them.

// If the following isn't done/documented, I should move it to a future_list or something...
Can't I also "store" an instance of a variable (like code), that has compiled something that I will use over and over?

The following doesn't work because code doesn't support _inherit (weird). As-is, because you can't _inherit from a different namespace... Actually, mk is part of @var, but there isn't a _last, because that would be part of code.repeat, and it would change. Without a way to force [] to be evaluated at declaration time, this doesn't seem doable...

[code.name.run(parms="")]
@var _="saved_code" _inherit="code.name" _format="{{self.last}}"

Document code.encode_smd

@@[code.encode_smd(t="@dump sysdef=\".\"")][b]

{:.bigandbold}If this is inline, *[code.encode_smd(t="@var name=\"value\" _format=\"# {{self.name}}\"")]*
//@dump code="encode_smd"
//@set _ns="code" _="encode_smd" b="**{{self.run}}(t={{self.t}})**"
//[encode_smd.b(t="[var]")]

document these
//@@[code.escape_var(v="var.bb")]
//@@[code.encode_smd_var(v="var.bb")]

[mk]
@code mk0="" _inherit="code.mk" _format="{{self._last}}"
@var mk1="[code.repeat._last]"
@var mk2="" _inherit="mk"

@dump var="mk" code="mk"

[mk0]
[mk1]

// be sure to test the @code thing where the only way to change attribute defaults is to use @set...


[docthis.close]
