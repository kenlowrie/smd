@import "[sys.imports]/def_html.md"

//TODO: This needs to move to the html.md built-ins file...

//@html _="title" _tag="title" _format="{{self.<}}{{self._t}}{{self.>}}" _t="Default Title"
//@html _="meta" _tag="meta" _format="{{self.<}}"
//@html _="meta-charset" _inherit="meta" charset="UTF-8"
//@html _="meta-viewport" _inherit="meta" name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0"
//@html _="link" _tag="link" _format="{{self.<}}"
//@html _="css" _inherit="link" rel="stylesheet" href="your-stylesheet.css"
//@html _="script" _tag="script"
//@html _="js" _inherit="script" src="your-javascript.js"

[html.head.<]
    [html.meta-charset]
    [html.meta-viewport]
    [html.title(_t="Clock")]
    [html.css(href="../css/style.css")]
    [html.js(src="../js/script.js")]
[html.head.>]

@html _="clockbody" _inherit="body" onload="startTime()"
@html _="wrapper" _inherit="div" class="wrapper"

[clockbody.<]
[wrapper.<]

<div id="clock-div"></div>

@import "[sys.imports]/def_bodyclose.md"
@import "[sys.imports]/def_close.md"

@watch "[sys.basepath]/../pipenv/obs/clock/css/style.css"

