@import "$/testsetup.md"

[var.testdoc_nw.begin(title="script1.md" desc="Testing the AV Script support")]



@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for script1.md")]

[var.toc.wc_open(t="Table of Contents - Unittest script1.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/avscript/script1-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from script1-inc.md")]
@dump link="^ug_samp_avscript"

@import "[sys.root]/docs/samples/avscript/script1-doc.md"

@set dump_ns_list="var=\"revision\""

[var.testdoc_nw.end]
