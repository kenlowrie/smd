@import "$/testsetup.md"
[var.testavdoc.begin(title="stop.md" desc="Testing @stop keyword")]
@wrap html.divx, p

[plain(t="Testing @stop keyword")]

[wrap_h(t="# Testing @stop")]

This is a lot of hoopla for testing the @stop or @quit keywords, both of which just immediate exit the parser, basically pretend you hit EOF on all files.

We will include an import with the @stop keyword in, to make sure all files are closed and the parser exits.

@import "$/import/stop.md"

If this appears in out, Houston we have a problem.
@parw *
[var.testavdoc.end]
