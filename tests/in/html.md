@import "$/testsetup.md"

[var.testdoc.begin(title="html.md" desc="Testing @html namespace")]

@var ns="html"

@import "$/nsbasic.md"

[wrap_h.hash1]
[plain(t="Specific Namespace testing for ***@[ns]*** namespace")]

[plain(t="Testing @html builtin functions")]

[plain(t="Testing adding new @html builtins")]

@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for [smdhtml.b]")]

[var.toc.wc_open(t="Table of Contents - Unittest [smdhtml.b]")]
@wrap nop
[b]
@import "[sys.root]/docs/section/nshtml-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from nshtml-inc.md")]
@dump link="^ug_ns_html|ug_html_"

@import "[sys.root]/docs/section/nshtml-doc.md"


@set dump_ns_list="html=\".\""

[var.testdoc.end]
