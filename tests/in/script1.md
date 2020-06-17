@import "$/testsetup.md"

[var.testdoc_nw.begin(title="script1.md" desc="Testing the AV Script support")]

//TODO: Remove these kludges when I enhance @wrap ...
@wrap _div_extras_

@var _="wrap_kludge" c="default content" _format="<p>{{self.c}}</p>"
@var divx_kludge="@@[html._div_extras_.<]" close="@@[html._div_extras_.>]"

[divx_kludge]
{:.red}# Script Series
[divx_kludge.close]
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

[var.avshot.visual]
{:.red}PART 1: Description for part 1
PART 1A
{:.blue}PART 1B
[var.avshot.audio]

[link.article]

notes for the first part.
and some other notes.
And a few more.
[var.avshot.end]

[var.avshot.visual]
WS:Couple watching TV
[var.avshot.noaudio]

[var.avshot.visual]
CU:Couple looking concerned
[var.avshot.audio]
The narrative for the shots on the left would go here.
[var.avshot.end]

[var.avshot.visual]
MS:Paranoid guy looking thru blinds
If you indent a line following a shot, then that text becomes part of the prior shot, allowing you to put a little more description if you need it.
[var.avshot.audio]
{:.ignore}Indent by itself to put a blank line between the shot and desc
[var.avshot.end]

[var.avshot.visual]
ECU:Perspective looking thru peephole.
[var.avshot.noaudio]

[var.avshot.visual]
CU:Locking door
[var.avshot.audio]
More narrative here that goes with the shot on the left...
[var.avshot.end]




@link _="article2" _inherit="_template_"

[var.avshot.visual]
PART 2: The middle section
[var.avshot.audio]
This is a description for this section
[link.article2(_text="Link to Article" href="https://domain.com/another_article_link")] <-- That should have been turned into a link
[var.avshot.end]

[var.avshot.visual]
{:.red}MS/CU:Clips of people angry
    You can add more information about a shot by indenting the line that follows the definition. New shots are not started if you indent, however, so don't do that. :)
[var.avshot.audio]
The narration for the Clips of people angry would be here...
[var.avshot.end]

[var.avshot.visual]
WS:violence
This begins a new shot, because we used the shot delimiter at the beginning of the line.
{:.green}You can, however, prefix each new indented line with a different class for formatting...
[var.avshot.audio]
CGI Websites and blogs
{:.blue}CGI Use PIP to fill the screen
Words, words, words, blah, blah, blah
[var.avshot.end]

[var.section(t="section heading goes here...")]
[var.avshot.visual]
CGI:
[var.avshot.audio]
CGI Text is here
[var.avshot.end]

[divx_kludge]
{:.pba}### Random heading
[divx_kludge.close]
@parw
<div class="extras">
<p class="question right">
//@@[var.divxp(c="{: .question .right}I wonder if we should maybe add that line from the unused section about \"...\"")]
I wonder if we should maybe add that line from the unused section about "..."
</p></div>

[var.avshot.visual]
F2B:fin
[var.avshot.audio]
{: .question .left}fin. credits.
[var.avshot.end]

{: .ignore}Anything with a .ignore class won't be displayed when the page is rendered by a browser, but is still part of the actual HTML document.
[var.avshot.visual]
WS:Stock clips of TV shows that ...
[var.avshot.audio]
{:.blue}So many programs on television today ...
We should ***practice tolerance*** and ...
{:.green}It’s also crucial for people to *...* and **...**.
{:.red}We are past due for ...
[var.avshot.end]

[var.avshot.visual]
TS1
[var.avshot.noaudio]

[var.avshot.visual]
TS2
[var.avshot.noaudio]

[var.avshot.visual]
TS3 
[var.avshot.audio]

footage

bar
[var.avshot.end]

[divx_kludge]
## heading
[divx_kludge.close]

[divx_kludge]
##    heading with leading spaces
[divx_kludge.close]

[divx_kludge]
@wrap p
xyz

def
@parw
[divx_kludge.close]

@set dump_ns_list="var=\"revision\""

[var.testdoc_nw.end]
