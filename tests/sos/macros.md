//@code _id="encode_smd" type="exec" src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd('$.t'))" t="Usage: code.encode_smd.run(t=\"smd markdown to encode\")"

//[code.encode_smd(t="simple")]
//[code.encode_smd(t="si\"mp\"le")]
//[code.encode_smd(t="[myfunc(\"bar\")]")]

@import "[sys.imports]/helpers.md"

@code _="echo" type="eval" src="print('$.e')" e="hello, world"
[echo(e="ain't that grand")]
//[code.encode_smd(t="[echo(e=\"hello, world\"&rpar;]")]
