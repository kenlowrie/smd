
[link.ug_samp_avscript]
[wrap_h.chapter(t="##Sample A/V Script Document")]

@wrap divx,p

In this example, we will use [smd.b] to create a simple Audio/Visual (A/V) Script. AV Scripts are simple two column scripts that show the visuals i.e. shots on the left, and the audio i.e. narration or voiceover, on the right. [smd.b] has several builtins that assist with creating this type of script.

Start by including **[encode_smd(t="@import <sys.imports>")]/avs/avs.md**, and you will get everything you need to quickly create your script.

[wrap_h(t="## A/V Script Series")]

@link _="domain" _inherit="_template_" _text="https://yourdomain.com" href="https://yourdomain.com"
@link _="me" _inherit="_template_" _text="me" href="email@yourdomain.com"
@link _="feedback" _inherit="me" _text="feedback" href="DELETE_ME_mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback"

[var.cover(title="Title of Script" author="Script Author" logline="Script summary goes here and can be as long as needed. Let it wrap around if you have softwrap, or just go on forever.")]
[var.revision.plain(v="1a")]
[var.contact(cn="Contact Name" ph="Phone" em="[me]" c1="Copyright (c) 2020 by YOURNAME." c2="All Rights Reserved." c3="Don't steal my script")]
[var.review.with_content(t="Notes to Reviewers", c="\
    Please send [me] any and all [feedback], preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. ++additions are marked like this++ ~~deletions are marked like this~~\
")]

@var client="**Client Name**"

[var.plain.with_content(t="Film Pitch for [client]" c="\
    [client]:[bb]\
    Please review the proposed script for your upcoming project. We believe that it will show the type of production value that we will bring to your project, focusing primarily on ...\
")]

@import "[sys.imports]/divs.md"

@link _="article" _inherit="_template_" _text="Link to Article" href="https://domain.com/article_link/"

[var.section.wc_open(t="")]
A/V Script for [client] project entitled "Bestest Social Media Campaign for Acme Widgets, LLC"
[var.section.wc_close]

// Include the **avshot** builtin to get the support for easily formatting AV Scripts
@import "[sys.imports]/avs/avs.md"

// Inluce the avs/shotacro.md builtins file to get various shot shorthand variable declarations
@import "[sys.imports]/avs/shotacro.md"

**[encode_smd(t="<avshot.visual>")]** begins the definition of a shot. You can list one or more shots in this section, and include formatting and other markdown. When you are done listing the shots, you will use either **[encode_smd(t="<avshot.audio>")]** or **[encode_smd(t="<avshot.noaudio>")]** to either begin listing the narration or voiceover, or simply close out the shot. 

In this example, we will open with **avshot.visual**, write out shot description, and the close with **avshot.noaudio**, so there won't be anything listed in the right column.

[var.avshot.visual]
[cu] Staring out the window
[var.avshot.noaudio]

Not too exciting just yet, but we'll get there. The more common case is to use **avshot.visual**, then describe the shot, use **avshot.audio**, describe the narration or voiceover, then close with **avshot.end**. Let's do that now, and see how it looks.

[var.avshot.visual]

[ws] Busy freeway rush hour traffic at a standstill

[var.avshot.audio]
In this example, after the preceding shot declaration, we used **[encode_smd(t="<avshot.audio>")]** to close out the visuals section, and begin the narrative section. You can have as much narration and notes as you need. When you're done, close out the shot with **[encode_smd(t="<avshot.end>")]**.

There are a bunch of useful shot notation mnemonics defined in the **sys.imports/avs/shotacro.md** file, so you'll definitely want to review that to get an idea of those goodies!

[var.avshot.end]

[plain(t="Mixing AV Script builtins and other markdown")]

At any time in your AV Script, you can switch back and forth between shots and normal markdown. All you do is place the normal markdown outside the **avshot** builtins. It's that simple. When you're ready, you just start adding more shots!

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
If you want to put inline notes, questions or use any of the Simple Divs (*note, question, vo, important, greyout*), you need to use the ***no-div** version. The **no-div** version uses the suffix **_nd** on the key attribute names. For example, if I use the default and write:[bb] **[encode_smd(t="<note")][E.lp]t="this is my note")]**, this is what I will see:
[var.note(t="this is my note")]
See how the box jams up against the left margin of the right column? It also clears the floats, which will mess up the formatting for the next element in the audio section... ugh! 

This time, i'll write **note.nd**, to use the no-div variant, and let's see how that looks:
[note.nd]
Much better! Just remember to use the **nd** versions of any of the simple divs when you are using them inside the **avshot** builtins! 
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
[var.section(t="Video Segment Part 2 is next ...")]
[var.avshot.visual]
[cgi]
[var.avshot.audio]
CGI Text is here
[var.avshot.end]

[var.avshot.visual]
[ftb] *fin*
[var.avshot.audio]
The End.
[var.avshot.end]

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

[plain(t="Specialized avshot builtins")]
There are two short versions of avshot that can be used for quick shot only cases or shot with short description. They are:

[tab.<]**[encode_smd(t="<avshot.shot_only>")]** and **[encode_smd(t="<avshot.shot_with_desc>")]**[tab.>]

They are just simplified versions you can use to quickly generate a shot only or a shot with short description.

[terminal2.wc_open(t="Simplified *avshot* methods")]

**[encode_smd(t="<avshot.shot_only")](_s="shot info"[E.rp]]**
**[encode_smd(t="<avshot.shot_with_desc")](_s="shot info" _d="shot description"[E.rp]]**
[terminal2.wc_close]

[var.avshot.shot_only(_s="[cu] Hands holding phone")]

[var.avshot.shot_with_desc(_s="[ecu] text message on phone" _d="help[bb]me")]

[terminal2.wc_open(t="For reference, here is the help for **avshot**:")]
[avshot.?]
[terminal2.wc_close]

Okay, that wraps up this chapter on creating A/V scripts with [smd.b].
