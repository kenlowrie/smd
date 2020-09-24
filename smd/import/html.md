@html _id="html" _tag="html"

// <head> related tags
@html _id="head"
@html _="title" _format="{{self.<}}{{self._t}}{{self.>}}" _t="Default Title"
@html _="meta" _format="{{self.<}}"
@html _="meta-charset" _inherit="meta" charset="UTF-8"
@html _="meta-viewport" _inherit="meta" \
        name="viewport"\
        content="width=device-width, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0"
@html _="link" _format="{{self.<}}"
@html _="script"
@html _="css" _inherit="link" rel="stylesheet" href="your-stylesheet.css"
@html _="js" _inherit="script" src="your-javascript.js"

// <body> related tags
@html _="body"
@html _="code"
@html _="div"
@html _="em"
@html _="h" 1="<h1>{{self.t}}</h1>"\
            2="<h2>{{self.t}}</h2>"\
            3="<h3>{{self.t}}</h3>"\
            4="<h4>{{self.t}}</h4>"\
            5="<h5>{{self.t}}</h5>"\
            6="<h6>{{self.t}}</h6>"\
            _format="{{self._help}}"\
            _help="*{{self._}}.#(t=\"your heading\")*[bb]\
[sp.4]Emit an HTML Heading[bb]\
[sp.2]**Parameters**[b]\
[sp.4]t - text for heading[bb]\
[sp.2]**Methods**[b]\
[sp.4]# - integer between 1 and 6[bb]\
[sp.2]**Examples**[b]\
[sp.4]h.1(t=\"My [E.ast]h1[E.ast] heading\")"

@html _="li"
@html _="ol"
@html _="p"
@html _="pre"
@html _="span"
@html _="strong"
@html _="table"
@html _="td"
@html _="th"
@html _="tr"
@html _="ul"

// useful list styles
@html _="ulist" _inherit="ul" class="ulist"
@html _="ulistplain" _inherit="ul" class="ulist-plain"
@html _="olist" _inherit="ol" class="olist"
@html _="olist_template" _inherit="ol"\
        _format="@@{{self._inline}}"\
        _inline="<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>"
@html _="olistAlpha" _inherit="olist_template" class="olist-Alpha"
@html _="olistalpha" _inherit="olist_template" class="olist-alpha"
@html _="olistRoman" _inherit="olist_template" class="olist-Roman"
@html _="olistroman" _inherit="olist_template" class="olist-roman"
@html _="olistGreek" _inherit="olist_template" class="olist-Greek"
@html _="olistgreek" _inherit="olist_template" class="olist-greek"
