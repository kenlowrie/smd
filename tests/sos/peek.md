@import "[sys.imports]/link.md"
@link _id="cls" _inherit="_template_" _text="Cloudy Logic Studios" href="https://cloudylogic.com"
@var _id="cloudylogic.com" _format="{{link.cls._qlink(_qtext=\"cloudylogic.com\")}}"
@var cloudylogic2com="{{link.cls._qlink(_qtext=\"cloudylogic.com\")}}"

@import "[sys.imports]/divs.md"
[var.plain(t="hello, world!!!")]

@var cl3.com="foobar"
@var cl42="fubar"

[cloudylogic.com]
[cloudylogic2com]
[cl3.com]
{:.green}[cl42]

@dump var="c"
