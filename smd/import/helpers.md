@import "$/html.md"
@import "$/code.md"
@import "$/divs.md"
@html _="tab" _inherit="span" class="indent"
@html _="us" _inherit="span" style="text-decoration:underline"
@html _="spanwc" _inherit="span" class="blue"
@html _="divx" _inherit="_div_extras_"
@html _="divx1" _inherit="divx" style="border-bottom:5px solid green;color:green"
@html _="divx2" _inherit="divx" style="border-bottom:3px solid black;color:green"
@html _="divx3" _inherit="divx" style="border-bottom:2px solid black"
@html _="li2" _tag="li" _inherit="li" style="font-size:1.3em;margin-left:2em"

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

// Create an entity namespace variable E with attrs for commonly used HTML entities
@var E="Entity Constants: {{self._all_attrs_}}" \
    ast="&ast;"\
    ast2="[self.ast][self.ast]"\
    ast3="[self.ast][self.ast][self.ast]"\
    lb="&lsqb;"\
    rb="&rsqb;"\
    lcb="&lcub;"\
    lcb2="[self.lcb][self.lcb]"\
    rcb="&rcub;"\
    rcb2="[self.rcb][self.rcb]"\
    lt="&lt;"\
    gt="&gt;"\
    at="&commat;"\
    lp="&lpar;"\
    rp="&rpar;"\
    plus="&plus;"\
    ins="[self.plus][self.plus]"\
    minus="&minus;"\
    tilde="&sim;"\
    del="[self.tilde][self.tilde]"\
    sp="&nbsp;"\
    sp2="[self.sp][self.sp]"\
    apos="&apos;"\
    num="&num;" hashtag="&num;"\
    amp="&amp;"\
    bs="&bsol;"\
    fs="&sol;" fs2="[self.fs][self.fs]"

// Create an emoji namespace variable EMOJI with attrs for commonly used emojis
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

// Create a builtin that outputs two different sizes of emojis
// [e_moji] for 1em sized emoji
// [e_moji.big] for 2em sized emoji
@var e_moji="{{html.spanfs}}{{EMOJI.{{self.e}}}}{{html.spanfs.>}}" \
      big="{{html.spanfs._big}}{{EMOJI.{{self.e}}}}{{html.spanfs.>}}"\
      e="smile"

// [e_tag] will create an HTML tag (encoded) for printing. e.g. [e_tag(t="div")] outputs <div>
@var e_tag="[E.lt]{{self.t}}[E.gt]" t="usage: tag(t=\"text_to_wrap\")" b="**{{self._format}}**" em="*{{self._format}}*" emb="***{{self._format}}***"

// [e_var] will put markdown brackets [] around the text. e.g. [e_var(t="e_var")] outputs [e_var]
@var e_var="[E.lb]{{self.t}}[E.rb]" t="usage: tag(t=\"text_to_wrap\")" b="**{{self._format}}**" em="*{{self._format}}*" emb="***{{self._format}}***"

@var e_us="{{html.us.<}}{{self.t}}{{html.us.>}}" t="text_to_underscore"

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

