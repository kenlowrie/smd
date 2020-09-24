@import "$/testsetup.md"

[var.testdoc.begin(title="quit.md" desc="Testing @quit keyword")]

[plain(t="Testing @quit keyword")]

[wrap_h(t="# Testing @quit")]

This is a lot of hoopla for testing the @stop or @quit keywords, both of which just immediate exit the parser, basically pretend you hit EOF on all files.

We will include an import with the @quit keyword in, to make sure all files are closed and the parser exits.

@import "$/import/quit.md"

If this appears in out, Houston we have a problem.

[var.testdoc.end]
