@import "$/testsetup.md"

[var.testdoc.begin(title="import.md" desc="Testing @import and @embed and @watch")]

{:.blue}#Testing @import

//TODO: if this logic is tested elsewhere, lose it from here.

@var workingtitle="Script&#32;Markdown&#32;Utility"
@var storysummary="This manual describes the *Script Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create HTML documents quickly, easily and most important, efficiently. ***Enjoy!***"
@import '$/import/test_import.md'
@var a="testing"
@var bx="123"
@var c="[{{a}}][{{bx}}]"
And here's my test: [a][bx] and finally [c]

@import '$/import/test_import2.md'


[plain(t="{:.blue}Testing @embed")]

[plain(t="{:.blue}Testing @watch")]


@set dump_ns_list="var=\".*\" link=\"c|d\""
[var.testdoc.end]
