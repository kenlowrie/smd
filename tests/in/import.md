@import "[sys.imports]/builtins.md"
@import "[sys.imports]/divs.md"
@import "[sys.imports]/report.md"

@import "[sys.imports]/def_html.md"
@import "[sys.imports]/def_head.md"
@import "[sys.imports]/def_body.md"

@dump var="." html="." link="." image="."
[hash1]
### Testing built-ins from sys.imports/divs.md
{:.blue}#SMD User Manual
@var workingtitle="Script&#32;Markdown&#32;Utility"
@var storysummary="This manual describes the *Script Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create HTML documents quickly, easily and most important, efficiently. ***Enjoy!***"
@import '$/import/test_import.md'
@var a="testing"
@var bx="123"
@var c="[{{a}}][{{bx}}]"
And here's my test: [a][bx] and finally [c]

@import '$/import/test_import2.md'

@dump var=".*" link="c|d"
@import "[sys.imports]/def_bodyclose.md"
@import "[sys.imports]/def_close.md"
