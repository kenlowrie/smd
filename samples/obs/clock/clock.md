@import "[sys.imports]/def_html.md"

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

@watch "[sys.basepath]/../samples/obs/clock/css/style.css"

