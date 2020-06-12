@import "$/testsetup.md"

[var.testdoc.begin(title="revision.md" desc="Testing var.revision ... again")]

[var.revision(v="1a")] 
[var.revision(v="1.0")]
[var.revision(v="28f")]

[var.testdoc.end]
@dump var="revision"
@import "[sys.imports]/def_bodyclose.md"
@import "[sys.imports]/def_close.md"
