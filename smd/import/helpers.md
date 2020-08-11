@import "$/html.md"
@import "$/code.md"
@import "$/divs.md"
@html _="tab" _inherit="span" class="indent"
@var _="tab2" o="[tab.<][tab.<]" c="[tab.>][tab.>]" o3="[tab.<][tab.<][tab.<]"  c3="[tab.>][tab.>][tab.>]"
@html _="us" _inherit="span" style="text-decoration:underline"
@html _="spanwc" _inherit="span" class="blue"
@html _="divx" _inherit="_div_extras_"
@html _="divx1" _inherit="divx" style="border-bottom:5px solid green;color:green"
@html _="divx2" _inherit="divx" style="border-bottom:3px solid black;color:green"
@html _="divx3" _inherit="divx" style="border-bottom:2px solid black"
@html _="li2" _tag="li" _inherit="li" style="font-size:1.3em;margin-left:2em"

@var e_us="{{html.us.<}}{{self.t}}{{html.us.>}}" t="{{self._help}}" _help="*{{self._}}(t=\"text_to_underscore\")*"
@var hash1="# [code.repeat.run(t=\"-\", c=\"42\")]"
@var hash2="## [code.repeat.run(t=\"-\", c=\"42\")]"
@var hash3="### [code.repeat.run(t=\"-\", c=\"42\")]"
@var wrap_h="{{code.pushlines(t=\"@wrap html.divx\n{{self.t}}\n@parw 1\")}}"\
    hash1="{{code.pushlines(t=\"@wrap html.divx\n{{var.hash1}}\n@parw 1\")}}"\
    hash2="{{code.pushlines(t=\"@wrap html.divx\n{{var.hash2}}\n@parw 1\")}}"\
    hash3="{{code.pushlines(t=\"@wrap html.divx\n{{var.hash3}}\n@parw 1\")}}"\
    chapter="{{code.pushlines(t=\"@wrap html.divx1\n{{self.t}}\n@parw 1\")}}"\
    section="{{code.pushlines(t=\"@wrap html.divx2\n{{self.t}}\n@parw 1\")}}"\
    subsect="{{code.pushlines(t=\"@wrap html.divx3\n{{self.t}}\n@parw 1\")}}"

// Make a couple of specialized Simple DIV **note** types where the font color is blue or red
@html _="_bluenote_p_" _inherit="_note_p_" class="[html._note_p_.class] blue"
@html _="_rednote_p_" _inherit="_note_p_" class="[html._note_p_.class] red"
// create var.bluenote, inherit note attributes, and then just change the p class in the _inline attrs
@var _="bluenote" _inherit="note"
[code.attr_replace_str(s_str="_note_p_" r_str="_bluenote_p_" attr="var.bluenote.inline_nd")]
[code.attr_replace_str(s_str="_note_p_" r_str="_bluenote_p_" attr="var.bluenote.wc_open_inline_nd")]
@var _="rednote" _inherit="note"
[code.attr_replace_str(s_str="_note_p_" r_str="_rednote_p_" attr="var.rednote.inline_nd")]
[code.attr_replace_str(s_str="_note_p_" r_str="_rednote_p_" attr="var.rednote.wc_open_inline_nd")]

@html _="bigmargin" _tag="div" style="margin-left:3.3em;margin-right:3.3em" _open="@@{{self.<}}" _close="@@{{self.>}}"

@html _="bmgreybg" _inherit="bigmargin" style="[html.bigmargin.style];border:2px solid black;background:lightgray"

