[link.helpers]
[wrap_h.chapter(t="## Helper built-ins")]

There are tons of helper built-ins that are provided in the different namespaces to make it easy to create content.

[docthis.open(h="Add this to helpers-doc.md")]

Document code.encode_smd

@@[code.encode_smd(t="@dump sysdef=\".\"")][b]

{:.bigandbold}If this is inline, *[code.encode_smd(t="@var name=\"value\" _format=\"# {{self.name}}\"")]*
//@dump code="encode_smd"
//@set _ns="code" _="encode_smd" b="**{{self.run}}(t={{self.t}})**"
//[encode_smd.b(t="[var]")]

document these
//@@[code.escape_var(v="var.bb")]
//@@[code.encode_smd_var(v="var.bb")]



[docthis.close]

[link.toc.link]
