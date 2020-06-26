@import "$/html.md"
@import "$/code.md"
@html _="tab" _inherit="span" class="indent"
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

@var ENT="Entity Constants: {{self._all_attrs_}}" \
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
    num="&num;" hashtag="&num;

@var e_tag="[ENT.lt]{{self.t}}[ENT.gt]" t="usage: tag(t=\"text_to_wrap\")" b="**{{self._format}}**" em="*{{self._format}}*" emb="***{{self._format}}***"
@var e_var="[ENT.lb]{{self.t}}[ENT.rb]" t="usage: tag(t=\"text_to_wrap\")" b="**{{self._format}}**" em="*{{self._format}}*" emb="***{{self._format}}***"

