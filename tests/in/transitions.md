@import "$/testsetup.md"

[var.testdoc_nw.begin(title="transitions.md" desc="Testing transitions between shots in AV scripts")]



@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for avshots.md")]

[var.toc.wc_open(t="Table of Contents - Unittest transitions.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/avshots/shots-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from shots-inc.md")]
@dump link="^ug_samp_shot"

@import "[sys.root]/docs/samples/avshots/shots-doc.md"

@set dump_ns_list="var=\"b|v|cover\" link=\"A|G|a|c\""


[var.testdoc_nw.end]
