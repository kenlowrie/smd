@import "$/testsetup.md"

[var.testdoc.begin(title="stop.md" desc="Testing @stop keyword")]

[plain(t="Testing @stop keyword")]

# Testing @stop

@wrap p

This is a lot of hoopla for testing the @stop or @quit keywords, both of which just immediate exit the parser, basically pretend you hit EOF on all files.

We will include an import with the @stop keyword in, to make sure all files are closed and the parser exits.

@import "$/import/stop.md"

If this appears in out, Houston we have a problem.

[var.testdoc.end]
