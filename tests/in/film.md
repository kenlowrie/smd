@import "$/testsetup.md"

[var.testdoc.begin(title="film.md" desc="Testing film related items")]



@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for film.md")]

[var.toc.wc_open(t="Table of Contents - Unittest film.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/film/film-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from film-inc.md")]
@dump link="^ug_samp_film"

@import "[sys.root]/docs/samples/film/film-doc.md"

@var dump_ns_list="image=\".\" var=\".\" link=\".\" html=\".\""
[var.testdoc.end]
