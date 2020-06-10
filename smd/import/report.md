@import "$/defaults.md"
// Create var.revision()
//TODO: if @@ goes away, what's the difference between plain and inline_plain?
@html _id="revision-div" class="revision" _inherit="div"
@html _id="revision-p" class="revTitle" _inherit="p"
@var _id="revision" \
     _format="@@ {{self.inline}}" \
     inline="{{html.revision-div.<}}{{html.revision-p.<}}{{self._v}} {{html.revision-p.>}}{{html.revision-div.>}}" \
     plain="@@ {{self.inline_plain}}"\
     inline_plain="{{html.revision-div.<}}{{html.revision-p.<}}{{self._vp}}{{html.revision-p.>}}{{html.revision-div.>}}" \
     _v="{{self._vp}} ({{code.datetime_stamp.run}})" \
     _vp="Revision: ***{{self.v}}***" \
     v="{{defaults.revision}}"
// Create var.contact()
@html _id="contact-div" class="contact" _tag="div"
@html _id="contact-table" style="border:none" _inherit="table"
@html _id="contact-tr" style="border:none" _inherit="tr"
@html _id="contact-td-left" class="left nowrap" style="border:none" _tag="td"
@html _id="contact-td-right" class="right nowrap" style="border:none" _tag="td"
//
@var _id="contact" \
     _format="@@ {{self.inline}}"\
     inline="{{html.contact-div.<}}{{html.contact-table.<}}{{html.contact-tr.<}}{{html.contact-td-left.<}}{{self.leftside}}{{html.contact-td-left.>}}{{html.contact-td-right.<}}{{self.rightside}}{{html.contact-td-right.>}}{{html.contact-tr.>}}{{html.contact-table.>}}{{html.contact-div.>}}" \
     rightside="{{self.cn}}<br />{{self.ph}}<br />{{self.em}}<br />" \
     leftside="{{self.c1}}<br />{{self.c2}}<br />{{self.c3}}<br />" \
     cn="{{defaults.cn}}" \
     ph="{{defaults.ph}}" \
     em="{{defaults.em}}" \
     c1="{{defaults.c1}}" \
     c2="{{defaults.c2}}" \
     c3="{{defaults.c3}}"
//
// Create var.cover()
@var _id="cover"\
     title="{{defaults.title}}" \
     author="{{defaults.author}}" \
     logline="{{defaults.logline}}" \
     _format="@@ {{self._inline_}}" \
     inline="{{self._inline_}}" \
     _inline_="<div class=\"cover\"><h3>{{self.title}}</h3><p>{{self.author}}</p><p class=\"coverSummary\">{{self.logline}}</p></div>"
//
@var _id="cover_template" \
     _inherit="cover" \
     title="{{self.t1}}" \
     author="{{self.t2}}" \
     logline="{{self.t3}}" \
     t1="Title" t2="author" t3="logline"
//
@var _id="cover_factory" \
      _format="@var _id=\"{{self.nm}}\" \
      _inherit=\"cover_template\" \
      t1=\"\" \
      t2=\"{{self.usage}}\" \
      t3=\"\"" \
     usage="Usage:[bb]**{{self.nm}}(t1=&quot;&quot; t2=&quot;text&quot; t3=&quot;&quot;)[b]{{self.nm}}.inline(same)**"
