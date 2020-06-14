@import "$/testsetup.md"

[var.testdoc.begin(title="revision.md" desc="Testing var.revision ... again")]

[var.revision(v="1a")] 
[var.revision(v="1.0")]
[var.revision(v="28f")]

@set dump_ns_list="var=\"revision\""
[var.testdoc.end]
