@import "$/testsetup.md"

[var.testdoc_nw.begin(title="transitions.md" desc="Testing transitions between shots in AV scripts")]

[var.plain.with_content(t="{:.blue}Transitions", c="{:.blue}This test document is used to test the transitions from A/V sections")]

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

@break
[var.cover(title="A" author="B" logline="C")]

[var.avshot.visual]
Shot
[var.avshot.audio]
Description
[var.avshot.end]
@break

[var.contact(c1="D" c2="E"  c3="F"  cn = "A"  ph  =  "B"    em   ="C")]

[var.avshot.visual]
Shot
[var.avshot.audio]
Description
[var.avshot.end]

@dump var="b|v|cover"

[var.avshot.visual]
Shot
[var.avshot.audio]
Description
[var.avshot.end]

@dump link="A|G|a|c"

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

{:.red}$$revision$$:<<1 This should not be a new div, class prefixes are not allowed here.>>
{:.blue}$$cover$$:<<.NOT>>:<<.HERE>>:<<.EITHER>>
{:.green}$$contact$$:<<.NOT>>:<<.HERE>>:<<.EITHER>>:<<1>>:<<2>>:<<3>>
{:.red}[variable]=NO NOT HERE EITHER
{:.blue}[link]:not_in_links_either_
[var.avshot.end]

@break
[link.bm_factory(nm="myanchor" t="*This is my text*")]
[link.myanchor]
[link.myanchor.link]

[var.testdoc_nw.end]
