@import "$/testsetup.md"

[var.testavdoc.begin(title="dump.md" desc="Testing @dump and @debug functionality")]
@wrap html.divx, p

[plain(t="Testing @dump keyword and options")]

[wrap_h(t="# Testing @dump")]

@dump tracked="."
@dump tracked=".*/def_"


@dump sysdef="."
@dump sysdef="_load"

@dump tracked=".*/builtins.md" sysdef="_config"

@dump tracked=".*/builtins.md" sysdef="_config" var="b" code="push"

@dump

[wrap_h(t="# Testing @debug")]

[plain(t="Testing @debug keyword and options")]

@debug
@debug
@debug on="."
@debug off="."
@debug enabled="."
@debug toggle="."
@debug tags="."

@parw *

[var.testavdoc.end]
