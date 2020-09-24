@import "$/testsetup.md"

[var.testdoc_nw.begin(title="misc.md" desc="Testing miscellaneous stuff")]



@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for misc.md")]

[var.toc.wc_open(t="Table of Contents - Unittest misc.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/proposal/misc-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from misc-inc.md")]
@dump link="^ug_samp_proposal"

@import "[sys.root]/docs/samples/proposal/misc-doc.md"

@set dump_ns_list="var=\".*\""






[var.testdoc_nw.end]
