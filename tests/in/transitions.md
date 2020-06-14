@import "$/testsetup.md"

[var.testavdoc.begin(title="transitions.md" desc="Testing transitions between shots in AV scripts")]

[var.plain.with_content(t="{:.blue}Transitions", c="{:.blue}This test document is used to test the transitions from A/V sections")]

//TODO: Update this to use the newer avshot support

@import "[sys.imports]/avs/avs.md"

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

[var.plain(t="This should be a new section")]

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

[var.plain(t="{:.green}This should be a new section")]

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

@var variable="VALUE"

[var.avwrapper2.b1]
Shot - [variable] <-- should be the word VALUE
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

@link _="cls" _inherit="_template_" href="https://www.cloudylogic.com" _text="{{self._}}"

[var.avwrapper2.b1]
Shot - [cls] <-- should be a link to www.cloudylogic.com
Shot 2 - [cls]
{:.red}Shot 3 - [cls]
Shot 4 - [cls] - Working good..
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

@link _="Google" _inherit="_template_" href="https://www.google.com" _text="{{self._}}"

[var.avwrapper2.b1]
Shot - [Google] <-- Should be link to google.com
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]
@link _="amazon" _inherit="_template_" title="amazon website" href="https://www.amazon.com" _text="{{self._}}"

[var.avwrapper2.b1]
Shot - [amazon] <-- Should be link to amazon.com with title "amazon website"
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

@link _="Amazon" _inherit="_template_" title="Amazon website" href="https://www.amazon.com" _text="{{self._}}"

[var.avwrapper2.b1]
Shot - [Amazon] <-- Should be link to amazon.com with title "Amazon website"
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

//$$revision$$:<<1b>>

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

@break
[var.cover(title="A" author="B" logline="C")]

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]
@break

[var.contact(c1="D" c2="E"  c3="F"  cn = "A"  ph  =  "B"    em   ="C")]

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

@dump var="b|v|cover"

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

@dump link="A|G|a|c"

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

# Header

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description
[var.avwrapper2.e1]

{:.red}##Header2a

[var.avwrapper2.b1]
Shot
[var.avwrapper2.t1]
Description

{:.red}$$revision$$:<<1 This should not be a new div, class prefixes are not allowed here.>>
{:.blue}$$cover$$:<<.NOT>>:<<.HERE>>:<<.EITHER>>
{:.green}$$contact$$:<<.NOT>>:<<.HERE>>:<<.EITHER>>:<<1>>:<<2>>:<<3>>
{:.red}[variable]=NO NOT HERE EITHER
{:.blue}[link]:not_in_links_either_
[var.avwrapper2.e1]

@break
[link.bm_factory(nm="myanchor" t="*This is my text*")]
[link.myanchor]
[link.myanchor.link]

[var.testavdoc.end]
