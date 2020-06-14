@import "$/testsetup.md"

[var.testdoc.begin(title="dump.md" desc="Testing @dump and @debug functionality")]

[plain(t="Testing @dump keyword and options")]

# Testing @dump

@dump tracked="."
@dump tracked=".*/def_"


@dump sysdef="."
@dump sysdef="_load"

@dump tracked=".*/builtins.md" sysdef="_config"

@dump tracked=".*/builtins.md" sysdef="_config" var="b" code="push"

@dump

# Testing @debug

[plain(t="Testing @debug keyword and options")]

@debug
@debug
@debug on="."
@debug off="."
@debug enabled="."
@debug toggle="."
@debug tags="."

[var.testdoc.end]
