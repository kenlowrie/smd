@import "$/testsetup.md"

[var.testdoc.begin(title="html.md" desc="Testing @html namespace")]

@var ns="html"

@import "$/nsbasic.md"

[wrap_h.hash1]
[plain(t="Specific Namespace testing for ***@[ns]*** namespace")]

[plain(t="Testing @html builtin functions")]

[plain(t="Testing adding new @html builtins")]

@set dump_ns_list="html=\".\""

[var.testdoc.end]
