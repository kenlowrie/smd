
@var smdtag="@@{{self.il}}" p="" il="[encode_smd(t=\"{{self.p}}\")]" b="**{{self.il}}**" em="*{{self.il}}*" emb="***{{self.il}}***"

@var _="smdvar" _inherit="smdtag" p="@var"
@var _="smdvar_wp" _inherit="smdtag" p="@var {{self.parms}}"
@var _="smdhtml" _inherit="smdtag" p="@html"
@var _="smdhtml_wp" _inherit="smdtag" p="@html {{self.parms}}"
@var _="smdcode" _inherit="smdtag" p="@code"
@var _="smdcode_wp" _inherit="smdtag" p="@code {{self.parms}}"
@var _="smdlink" _inherit="smdtag" p="@link"
@var _="smdlink_wp" _inherit="smdtag" p="@link {{self.parms}}"
@var _="smdimage" _inherit="smdtag" p="@image"
@var _="smdimage_wp" _inherit="smdtag" p="@image {{self.parms}}"
@var _="smdimport" _inherit="smdtag" p="@import"
@var _="smdimport_wp" _inherit="smdtag" p="@import {{self.parms}}"
@var _="smdembed" _inherit="smdtag" p="@embed"
@var _="smdembed_wp" _inherit="smdtag" p="@embed {{self.parms}}"
@var _="smdwatch" _inherit="smdtag" p="@watch"
@var _="smdwatch_wp" _inherit="smdtag" p="@watch {{self.parms}}"
@var _="smdset" _inherit="smdtag" p="@set"
@var _="smdset_wp" _inherit="smdtag" p="@set {{self.parms}}"
@var _="smddump" _inherit="smdtag" p="@dump"
@var _="smddump_wp" _inherit="smdtag" p="@dump {{self.parms}}"
@var _="smdbreak" _inherit="smdtag" p="@break"
@var _="smdbreak_wp" _inherit="smdtag" p="@break {{self.parms}}"
@var _="smdstop" _inherit="smdtag" p="@stop"
@var _="smdstop_wp" _inherit="smdtag" p="@stop {{self.parms}}"
@var _="smdexit" _inherit="smdtag" p="@exit"
@var _="smdexit_wp" _inherit="smdtag" p="@exit {{self.parms}}"
@var _="smdquit" _inherit="smdtag" p="@quit"
@var _="smdquit_wp" _inherit="smdtag" p="@quit {{self.parms}}"
@var _="smdraw" _inherit="smdtag" p="@raw"
@var _="smdraw_wp" _inherit="smdtag" p="@raw {{self.parms}}"
@var _="smddebug" _inherit="smdtag" p="@debug"
@var _="smddebug_wp" _inherit="smdtag" p="@debug {{self.parms}}"
@var _="smdcomment" _inherit="smdtag" p="//"
@var _="smdcomment_wp" _inherit="smdtag" p="// {{self.parms}}"
@var _="smdwrap" _inherit="smdtag" p="@wrap"
@var _="smdwrap_wp" _inherit="smdtag" p="@wrap {{self.parms}}"
@var _="smdparw" _inherit="smdtag" p="@parw"
@var _="smdparw_wp" _inherit="smdtag" p="@parw {{self.parms}}"


@html _="ulist" _inherit="ul" class="ulist"
@html _="ulistplain" _inherit="ul" class="ulist-plain"
@html _="olist" _inherit="ol" class="olist"
@html _="olist_template" _inherit="ol"  _format="@@{{self._inline}}" _inline="<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>"
@html _="olistAlpha" _inherit="olist_template" class="olist-Alpha"
@html _="olistalpha" _inherit="olist_template" class="olist-alpha"
@html _="olistRoman" _inherit="olist_template" class="olist-Roman"
@html _="olistroman" _inherit="olist_template" class="olist-roman"
@html _="olistGreek" _inherit="olist_template" class="olist-Greek"
@html _="olistgreek" _inherit="olist_template" class="olist-greek"

@var _="_lists_"\
      _format="@@ {{self.inline}}"\
      with_content="@@ {{self.wc_inline}}"\
      wc_inline="{{self.wc_open_inline}}{{self.c}}{{self.wc_close_inline}}"\
      wc_open="{{code.pushlines(t=\"@wrap li\n@@{{self.wc_open_inline}}\")}}"\
      wc_close="{{code.pushlines(t=\"@@{{self.wc_close_inline}}\n@parw 1\")}}"

@var _="ulist"\
    _inherit="_lists_"\
      inline="{{html._div_extras_.<}}{{html.ulist.<}}{{self.t}}{{html.ulist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.ulist.<}}"\
      wc_close_inline="{{html.ul.>}}{{html.div.>}}"\
      sID="ulist"\
      t="var.{{self.sID}} default title" \
      c="var.{{self.sID}} default content"

@var _="ulistplain" _inherit="ulist"\
      inline="{{html._div_extras_.<}}{{html.ulistplain.<}}{{self.t}}{{html.ulist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.ulistplain.<}}"\

@var _="olist"\
    _inherit="_lists_"\
      inline="{{html._div_extras_.<}}{{html.ulist.<}}{{self.t}}{{html.ulist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.olist.<}}"\
      wc_close_inline="{{html.ol.>}}{{html.div.>}}"\
      sID="olist"\
      t="var.{{self.sID}} default title" \
      c="var.{{self.sID}} default content"

@html _="spanwc" _inherit="span" class="blue"

@html _="_p_bluenote_" _inherit="_p_note_" class="{{html._p_note_.class}} blue"
@html _="_p_rednote_" _inherit="_p_note_" class="{{html._p_note_.class}} red"
@var _="bluenote" _inherit="note"
[code.attr_replace_str(s_str="_p_note_" r_str="_p_bluenote_" attr="var.bluenote.inline")]
[code.attr_replace_str(s_str="_p_note_" r_str="_p_bluenote_" attr="var.bluenote.wc_open_inline")]
@var _="rednote" _inherit="note"
[code.attr_replace_str(s_str="_p_note_" r_str="_p_rednote_" attr="var.rednote.inline")]
[code.attr_replace_str(s_str="_p_note_" r_str="_p_rednote_" attr="var.rednote.wc_open_inline")]

@html _="fatmargin" _tag="div" style="margin-left:3.3em;margin-right:3.3em;border:2px solid black;background:lightgray" _open="@@{{self.<}}" _close="@@{{self.>}}"

@var EMOJI="Emoji Constants: {{self._public_attrs_}}" \
    mask="&#x1F637;"\
    shades="&#x1F60E;"\
    smile="&#x1F642;"\
    tonguewink="&#x1F61C;"

@html _="spanfs" _inherit="span" \
      _s1="font-size:1em" \
      _s2="font-size:2em" \
      _format="<{{self._tag}} style=\"{{self._s1}}\">"\
      _big="<{{self._tag}} style=\"{{self._s2}}\">"

@var e_moji="{{html.spanfs}}{{EMOJI.{{self.e}}}}{{html.spanfs.>}}" \
      big="{{html.spanfs._big}}{{EMOJI.{{self.e}}}}{{html.spanfs.>}}"\
      e="smile"

@var sp4="[sp][sp][sp][sp]"