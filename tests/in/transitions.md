@import "$/testsetup.md"

[var.testdoc_nw.begin(title="transitions.md" desc="Testing transitions between shots in AV scripts")]

[var.plain.with_content(t="{:.blue}Transitions", c="{:.blue}This test document tests the transitions from A/V sections")]

@import "[sys.imports]/avs/avs.md"

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.plain(t="This should be a new section")]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.plain(t="{:.green}This should be a new section")]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

@var variable="VALUE"

[var.avshot.visual]
    Shot - [variable] <-- should be the word VALUE
[var.avshot.audio]
    Description
[var.avshot.end]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

@link _="cls" _inherit="_template_" href="https://www.cloudylogic.com" _text="{{self._}}"

[var.avshot.visual]
    Shot - [cls] <-- should be a link to www.cloudylogic.com
    Shot 2 - [cls]
    {:.red}Shot 3 - [cls]
    Shot 4 - [cls] - Working good..
[var.avshot.audio]
    Description
[var.avshot.end]

@link _="Google" _inherit="_template_" href="https://www.google.com" _text="{{self._}}"

[var.avshot.visual]
    Shot - [Google] <-- Should be link to google.com
[var.avshot.audio]
    Description
[var.avshot.end]
@link _="amazon" _inherit="_template_" title="amazon website" href="https://www.amazon.com" _text="{{self._}}"

[var.avshot.visual]
    Shot - [amazon] <-- Should be link to amazon.com with title "amazon website"
[var.avshot.audio]
    Description
[var.avshot.end]

@link _="Amazon" _inherit="_template_" title="Amazon website" href="https://www.amazon.com" _text="{{self._}}"

[var.avshot.visual]
    Shot - [Amazon] <-- Should be link to amazon.com with title "Amazon website"
[var.avshot.audio]
    Description
[var.avshot.end]

//$$revision$$:<<1b>>

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.cover(title="A" author="B" logline="C")]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.contact(c1="D" c2="E"  c3="F"  cn = "A"  ph  =  "B"    em   ="C")]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

# Header

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description
[var.avshot.end]

{:.red}##Header2a

[var.avshot.visual]
    Shot
[var.avshot.audio]
    Description

    This is the old syntax for revision, cover, contact, basic vars and links
    {:.red}$$revision$$:1 This should not be a new div.
    {:.blue}$$cover$$:.NOT:.HERE:.EITHER
    {:.green}$$contact$$:.NOT:.HERE:.EITHER:1:2:3
    {:.red}[variable]=NO NOT HERE EITHER
    {:.blue}[var.link]:not_in_links_either_
[var.avshot.end]

[link.bm_factory(nm="myanchor" t="*This is my text*")]
[link.myanchor]
[link.myanchor.link]


@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for avshots.md")]

[var.toc.wc_open(t="Table of Contents - Unittest transitions.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/avshots/shots-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from shots-inc.md")]
@dump link="^ug_samp_shot"

@import "[sys.root]/docs/samples/avshots/shots-doc.md"

@set dump_ns_list="var=\"b|v|cover\" link=\"A|G|a|c\""


[var.testdoc_nw.end]
