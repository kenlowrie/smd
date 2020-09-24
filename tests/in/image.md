@import "$/testsetup.md"

[var.testdoc.begin(title="image.md" desc="Testing @image namespace")]

@var ns="image"

@import "$/nsbasic.md"

@import "[sys.imports]/image.md"

[plain(t="Testing @image builtin functions")]
[IMG_SIZE.thumb]

// 1st time use brackets around style
@image _="shot1" src="[sys.root]/docs/import/shot1.jpg" style="[var.IMG_STYLE.inline_border]"
[shot1]
@dump image="shot1"

//2nd time use curly braces around style
@image _="shot1" src="[sys.root]/docs/import/shot1.jpg" style="{{var.IMG_STYLE.inline_border}}"
[shot1]
@dump image="shot1"

[plain(t="Testing adding new @image builtins")]


@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for nsimage-doc.md")]

[var.toc.wc_open(t="Table of Contents - Unittest nsimage-doc.md")]
@wrap nop
[b]
@import "[sys.root]/docs/section/nsimage-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from nsimage-inc.md")]
@dump link="^ug_ns_image|^ug_image"

@import "[sys.root]/docs/section/nsimage-doc.md"

@set dump_ns_list="[ns]=\".\" help=\"f\""

[var.testdoc.end]
