@import "[sys.imports]/builtins.md"
@import "[sys.imports]/divs.md"
@import "[sys.imports]/report.md"

@import "[sys.imports]/def_html.md"
@import "[sys.imports]/def_head.md"
@import "[sys.imports]/def_body.md"
[hash1]
{:.red}# Script Series
@link _="domain" _inherit="_template_" _text="https://yourdomain.com" href="https://yourdomain.com"
@link _="me" _inherit="_template_" _text="me" href="email@yourdomain.com"
@link _="feedback" _inherit="me" _text="feedback" href="DELETE_ME_mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback"

[var.cover(title="Title of Script" author="Script Author" logline="Script summary goes here and can be as long as needed. Let is wrap around if you have softwrap, or just go on forever.")]
[var.revision.plain(v="1a")]
[var.contact(cn="Contact Name" ph="Phone" em="[me]" c1="Copyright (c) 2018 by YOURNAME." c2="All Rights Reserved." c3="Don't steal my script")]
[var.review.with_content(t="Notes to Reviewers", c="\
    Please send [me] any and all [feedback], preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. ++additions are marked like this++ ~~deletions are marked like this~~\
")]

[var.plain.with_content(t="Film Pitch for Potential Client" c="\
    ClientName:[bb]\
    The overall purpose of this demo is to show the type of production value that we will bring to your project, focusing primarily on ...\
")]

@import "[sys.imports]/divs.md"

@link _="article" _inherit="_template_" _text="Link to Article" href="https://domain.com/article_link/"

[var.section.with_content(t="" c="\
    AV Script\
")]

@import "[sys.imports]/avs/avs.md"

// Can I use pushlines or something to make this a little nicer?
// [var.startshot] -> pushlines[ [var.avwrapper2.begin] [@wrap li]]
// [var.transition] -> pushlines [ [@parw] [var.avwrapper2.end_shots] [@wrap p]]
// [var.endshot] -> pushlines [ [@parw] [[var.avwrapper2.end] [@break] ]
// Isn't this a lot of what is going on in the music video script? Have I already solved this problem?

@var _id="avwrapper2" \
          begin="{{html._div_av_.<}}{{html.ul.<}}" \
          end_shots="{{html.ul.>}}" \
          end="{{html.div.>}}" \
          shot_only="{{self.start}}{{self._s}}{{self.endul}}{{self.enddiv}}"\
          shot_with_desc="{{self.start}}{{self._s}}{{self.endul}}{{html.p.<}}{{self._d}}{{html.p.>}}{{self.enddiv}}"\
          b1="[code.pushlines(t=\"{{var.avwrapper2.begin}}\n@wrap li\")]"\
          t1="[code.pushlines(t=\"@parw\n{{var.avwrapper2.end_shots}}\n@wrap p\")]"\
          e1="[code.pushlines(t=\"@parw\n{{var.avwrapper2.end}}\n@break\")]"\
          e2="[code.pushlines(t=\"@parw\n{{var.avwrapper2.end_shots}}\n{{var.avwrapper2.end}}\n@break\")]"\

[var.avwrapper2.begin]
@wrap li

{:.red}PART 1: Description for part 1
PART 1A
{:.blue}PART 1B

@parw
[var.avwrapper2.end_shots]
@wrap p

[link.article]

notes for the first part.
and some other notes.
And a few more.

@parw
[var.avwrapper2.end]
@break

[var.avwrapper2.begin]
@wrap li

WS:Couple watching TV
CU:Couple looking concerned

@parw
[var.avwrapper2.end_shots]
@wrap p
The narrative for the shots on the left would go here.
@parw
[var.avwrapper2.end]
@break

[var.avwrapper2.begin]
@wrap li
MS:Paranoid guy looking thru blinds[b]If you indent a line following a shot, then that text becomes part of the prior shot, allowing you to put a little more description if you need it.
@parw
[var.avwrapper2.end_shots]
@wrap p
{:.ignore}Indent by itself to put a blank line between the shot and desc
@parw
[var.avwrapper2.end]
@break

[var.avwrapper2.begin]
@wrap li
ECU:Perspective looking thru peephole.
CU:Locking door
@parw
[var.avwrapper2.end_shots]
@wrap p
More narrative here that goes with the shot on the left...
@parw
[var.avwrapper2.end]
@break




@link _="article2" _inherit="_template_"

[var.avwrapper2.b1]
PART 2: The middle section
[var.avwrapper2.t1]
This is a description for this section
[link.article2(_text="Link to Article" href="https://domain.com/another_article_link")] <-- That should have been turned into a link
[var.avwrapper2.e1]
[var.avwrapper2.b1]
{:.red}MS/CU:Clips of people angry
    You can add more information about a shot by indenting the line that follows the definition. New shots are not started if you indent, however, so don't do that. :)
[var.avwrapper2.t1]
The narration for the Clips of people angry would be here...
[var.avwrapper2.e1]
[var.avwrapper2.b1]
WS:violence
This begins a new shot, because we used the shot delimiter at the beginning of the line.
{:.green}You can, however, prefix each new indented line with a different class for formatting...
[var.avwrapper2.t1]
CGI Websites and blogs
{:.blue}CGI Use PIP to fill the screen
Words, words, words, blah, blah, blah
[var.avwrapper2.e1]
[var.section(t="section heading goes here...")]
[var.avwrapper2.b1]
CGI:
[var.avwrapper2.t1]
CGI Text is here
[var.avwrapper2.e1]

{:.pba}### Random heading
<div class="extras">
<p class="question right">
//[var.divxp(c="{: .question .right}I wonder if we should maybe add that line from the unused section about \"...\"")]
I wonder if we should maybe add that line from the unused section about "..."
</p></div>
[var.avwrapper2.b1]
F2B:fin
[var.avwrapper2.t1]
{: .question .left}fin. credits.
[var.avwrapper2.e1]

{: .ignore}Anything with a .ignore class won't be displayed when the page is rendered by a browser, but is still part of the actual HTML document.
[var.avwrapper2.b1]
WS:Stock clips of TV shows that ...
[var.avwrapper2.t1]
{:.blue}So many programs on television today ...
We should ***practice tolerance*** and ...
{:.green}It’s also crucial for people to *...* and **...**.
{:.red}We are past due for ...
[var.avwrapper2.e1]
[var.avwrapper2.b1]
TS1
[var.avwrapper2.e2]
[var.avwrapper2.b1]
TS2
[var.avwrapper2.e2]
[var.avwrapper2.b1]
TS3 
[var.avwrapper2.t1]
footage

bar
[var.avwrapper2.e1]

## heading

##    heading with leading spaces

@wrap _div_extras_
xyz

def
@parw

@dump var="revision"
@import "[sys.imports]/def_bodyclose.md"
@import "[sys.imports]/def_close.md"
