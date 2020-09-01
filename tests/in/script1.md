@import "$/testsetup.md"

[var.testdoc_nw.begin(title="script1.md" desc="Testing the AV Script support")]

[plain(t="Testing of no-Div variants for factory generated simple divs")]

@import "[sys.root]/docs/userdocs_macros.md"

@var latin="lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
@wrap nop
[note(c="[latin]")]
[note.nd]
[note.inline]
[note.inline_nd]
[note.with_content(c="wc-[E.gt][latin]")]
[note.wc_open]
this is my note, I wonder if we should maybe add that line from the unused section about I don't remember what, I just need this to be longer.
and here is another line.
[note.wc_close]
[note.nd_open]
this is my note, I wonder if we should maybe add that line from the unused section about I don't remember what, I just need this to be longer.
and here is another line.
[note.nd_close]

Moving into [smdwrap.b] **divx**
@wrap divx
Now inside [smdwrap.b] **divx**
###note and note.nd first
[note]
[note.nd]
###note.inline and note.inline_nd
[note.inline]
[note.inline_nd]
###note.with_content and note.with_content_nd
[note.with_content]
###note.wc_open and note.wc_open_nd
[note.wc_open]
this is my note, I wonder if we should maybe add that line from the unused section about I don't remember what, I just need this to be longer.
and here is another line.
[note.wc_close]

[note.nd_open]
this is my note, I wonder if we should maybe add that line from the unused section about I don't remember what, I just need this to be longer.
and here is another line.
[note.nd_close]
@parw 2
[smdwrap.b] **stack cleared - back to default of [code.wrap_stack(w="#")]: "[code.wrap_stack]"**

@import "[sys.imports]/avs/avs.md"

[var.avshot.visual]
Over in the Audio section, let's see how each of the no-div sections look when used inside avshot.audio. We will start with the *note* builtin
[var.avshot.audio]
If you don't start with content, you'll lose the light top border that appears when you use the avshot builtin
This is the standard note_div variant inside the div.av. Notice how it shifts to the left side of this column
[note]
[note.nd(c="this is an inline note. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...")]
The next note was generated with inline html.
@@<p class="note">this is an inline note. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...</p>
nd_inline
[note.nd_inline]
inline_nd
[note.inline_nd]
nd_open
[note.nd_open]
this is my open note no div
[note.nd_close]
nd_open_inline
@@[note.nd_open_inline]
@@this is my open note no div
@@[note.nd_close_inline]
[var.avshot.end]

[var.avshot.visual]
Now let's use the span class= variant of each type
[var.avshot.audio]
{: .note .left}fin. credits. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...
{: .question .left}fin. credits. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...
{: .vo .left}fin. credits. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...
{: .important .left}fin. credits. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...
{: .greyout .left}fin. credits. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...
[var.avshot.end]

[var.avshot.visual]
And now *question*...

[var.avshot.audio]
This is the standard question_div variant inside the div.av
[question(c="I wonder if we should maybe add that line from the unused section about \"...\"")]
[question.nd]
This next one is inline using raw HTML
@@<p class="question">this is an inline note. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...</p>
nd_inline
[question.nd_inline]
inline_nd
[question.inline_nd]
nd_open
[question.nd_open]
this is my open question no div
[question.nd_close]
nd_open_inline
@@[question.nd_open_inline]
@@this is my open question no div
@@[question.nd_close_inline]
[var.avshot.end]



[var.avshot.visual]
And now *vo*...

[var.avshot.audio]
This is the standard vo_div variant inside the div.av
[vo(c="I wonder if we should maybe add that line from the unused section about \"...\"")]
[vo.nd]
This next one is inline using raw HTML
@@<p class="vo">this is an inline note. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...</p>
nd_inline
[vo.nd_inline]
inline_nd
[vo.inline_nd]
nd_open
[vo.nd_open]
this is my open vo no div
[vo.nd_close]
nd_open_inline
@@[vo.nd_open_inline]
@@this is my open vo no div
@@[vo.nd_close_inline]
[var.avshot.end]


[var.avshot.visual]
And now *important*...

[var.avshot.audio]
This is the standard important_div variant inside the div.av
[important(c="I wonder if we should maybe add that line from the unused section about \"...\"")]
[important.nd]
This next one is inline using raw HTML
@@<p class="important">this is an inline note. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...</p>
nd_inline
[important.nd_inline]
inline_nd
[important.inline_nd]
nd_open
[important.nd_open]
this is my open important no div
[important.nd_close]
nd_open_inline
@@[important.nd_open_inline]
@@this is my open important no div
@@[important.nd_close_inline]
[var.avshot.end]



[var.avshot.visual]
And now *greyout*...

[var.avshot.audio]
This is the standard greyout_div variant inside the div.av
[greyout(c="I wonder if we should maybe add that line from the unused section about \"...\"")]
[greyout.nd]
This next one is inline using raw HTML
@@<p class="greyout">this is an inline note. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...</p>
nd_inline
[greyout.nd_inline]
inline_nd
[greyout.inline_nd]
nd_open
[greyout.nd_open]
this is my open greyout no div
[greyout.nd_close]
nd_open_inline
@@[greyout.nd_open_inline]
@@this is my open greyout no div
@@[greyout.nd_close_inline]
[var.avshot.end]



[var.avshot.visual]
And now *generic*...

[var.avshot.audio]
This is the standard generic_div variant inside the div.av
[generic(c="I wonder if we should maybe add that line from the unused section about \"...\"")]
[generic.nd]
This next one is inline using raw HTML
@@<p class="generic">this is an inline note. lorem ipsum. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...</p>
nd_inline
[generic.nd_inline]
inline_nd
[generic.inline_nd]
nd_open
[generic.nd_open]
this is my open generic no div
[generic.nd_close]
nd_open_inline
@@[generic.nd_open_inline]
@@this is my open generic no div
@@[generic.nd_close_inline]
[var.avshot.end]

[bluenote]
[bluenote.inline]
[bluenote.with_content]
[bluenote.nd]
[bluenote.nd_inline]
[bluenote.nd_open]
blueopen
[bluenote.nd_close]

[rednote]
[rednote.inline]
[rednote.with_content]
[rednote.nd]
[rednote.nd_inline]
[rednote.nd_open]
redopen
[rednote.nd_close]

{: .ignore}Anything with a .ignore class won't be displayed when the page is rendered by a browser, but is still part of the actual HTML document.

@exit


[var.plain(t="User manual sections for script1.md")]

[var.toc.wc_open(t="Table of Contents - Unittest script1.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/avscript/script1-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from script1-inc.md")]
@dump link="^ug_samp_avscript"

@import "[sys.root]/docs/samples/avscript/script1-doc.md"

@set dump_ns_list="var=\"note|question|greyout|important|generic|vo|avshot\" html=\".*(note|question|vo|greyout|important|generic)\"" 

[var.testdoc_nw.end]
