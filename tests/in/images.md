@import "$/testsetup.md"

[var.testdoc_nw.begin(title="image.md" desc="Testing Images in Shots support from image.md")]


@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for samples/images/images-doc.md")]

[var.toc.wc_open(t="Table of Contents - Unittest samples/images/images-inc.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/images/images-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from images-inc.md")]
@dump link="^ug_samp_images"

@import "[sys.root]/docs/samples/images/images-doc.md"

@set dump_ns_list="image=\".*\""


[var.testdoc_nw.end]
