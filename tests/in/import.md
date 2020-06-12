@import "$/testsetup.md"

[var.testdoc.begin(title="import.md" desc="Testing built-ins from sys.imports/divs.md")]

{:.blue}#SMD User Manual
@var workingtitle="Script&#32;Markdown&#32;Utility"
@var storysummary="This manual describes the *Script Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create HTML documents quickly, easily and most important, efficiently. ***Enjoy!***"
@import '$/import/test_import.md'
@var a="testing"
@var bx="123"
@var c="[{{a}}][{{bx}}]"
And here's my test: [a][bx] and finally [c]

@import '$/import/test_import2.md'

[var.testdoc.end]

@dump var=".*" link="c|d"
@import "[sys.imports]/def_bodyclose.md"
@import "[sys.imports]/def_close.md"
