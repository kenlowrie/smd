@import "[sys.imports]/link.md"
@link _="me" _inherit="_template_" href="mailto:myemail@mydomain.com" _text="{{self._}}"
@link _="you" _inherit="_template_" href="mailto:your.email_address@your-domain.com" _text="{{self._}}"
@link _="feedback" _inherit="_template_" href="mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback" _text="{{self._}}"

@import "[sys.imports]/common.md"

I'm using the variable [link.me].[bb]

And I can also email [link.you].[bb]

Now I'm using the [link.feedback] variable.[bb]

@import "[sys.imports]/code.md"
[code.encodeURL(t="https://www.google.com?s=\"testing stuff\"")][bb]
[code.encodeURL(t="mailto:info@domain.com")][bb]
[code.encodeURL(t="mailto:info@www.testdomain.net?a=\"this is a test\"")][bb]
