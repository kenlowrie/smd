@var b="<br />"
//@var bb="[b][b]"
@var bb="{{b}}{{b}}"
@var sp="&nbsp;" 2="&nbsp;&nbsp;"
@set _="var.sp" 4="[var.sp.2][var.sp.2]" 6="[var.sp.4][var.sp.2]" 8="[var.sp.4][var.sp.4]" 10="[var.sp.8][var.sp.2]" 12="[var.sp.8][var.sp.4]"

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
    equot="\&quot;" quot="&quot;" dquot="&#34;"\
    fs="&sol;" fs2="[self.fs][self.fs]"

// Create a hex code namespace variable HEX with attrs for commonly used ASCII Character Codes
@var HEX="Entity Constants: {{self._all_attrs_}}" \
    lb="\x5b"\
    rb="\x5d"\
    lcb="\x7b"\
    lcb2="[self.lcb][self.lcb]"\
    rcb="\x7d"\
    rcb2="[self.rcb][self.rcb]"

// Create an emoji namespace variable EMOJI with attrs for commonly used emojis
@var EMOJI="Emoji Constants: {{self._public_attrs_}}" \
    mask="&#x1F637;"\
    shades="&#x1F60E;"\
    smile="&#x1F642;"\
    tonguewink="&#x1F61C;"

@html _="spanfs" _tag="span" \
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
@var e_tag="[E.lt]{{self.t}}[E.gt]" t="{{self._help}}" b="**{{self._format}}**" em="*{{self._format}}*" emb="***{{self._format}}***" _help="*{{self._}}(t=\"html_tag_to_wrap\")*"

// [e_var] will put markdown brackets [] around the text. e.g. [e_var(t="e_var")] outputs [e_var]
@var e_var="[E.lb]{{self.t}}[E.rb]" t="{{self._help}}" b="**{{self._format}}**" em="*{{self._format}}*" emb="***{{self._format}}***" _help="*{{self._}}(t=\"smd_tag_to_wrap\")*"
