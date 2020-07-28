@import "$/testsetup.md"

[var.testdoc.begin(title="html.md" desc="Testing @html namespace")]

@var ns="html"

@import "$/nsbasic.md"

[wrap_h.hash1]
[plain(t="Specific Namespace testing for ***@[ns]*** namespace")]

[plain(t="Testing @html builtin functions")]

[sp][get_variable(v="section", ret_type="1")]
[sp][get_variable(v="_section_div_", ret_type="0")]
[sp][get_variable(v="_section_div_", ret_type="1")]
[sp][get_variable(v="_section_div_.<", ret_type="0")]
[sp][get_variable(v="_section_div_.<", ret_type="1")]
[sp][get_variable(v="_section_div_.<+", ret_type="0")]
[sp][get_variable(v="_section_div_.<+", ret_type="1")]
[sp][get_variable(v="_section_div_.<+", ret_type="0" escape="True")]
[sp][get_variable(v="_section_div_.<+", ret_type="1", escape="True" )]


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


@set dump_ns_list="html=\".\" help=\"f\""

[var.testdoc.end]
