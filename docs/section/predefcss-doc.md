[link.ug_predefined_classes]
[wrap_h.chapter(t="##Predefined classes")]

[TODO] When we document the DIV versions of the these, we can decide to document their use inline like this or not... If not, then we can make that call here, or just delete all of this... The support for this type of thing is a bit odd, so we may not want to do it...

There are a number of predefined classes in the primary CSS file that can be used to quickly style your AV scripts. You can add others as required, and decorate your elements as needed. Here are a few of them, used outside the AV DIV, and then again inside an AV DIV.

[syntax.wc_open(t="Predefined classes")]
    {:.indent.bigandbold}[E.lcb]:.note[E.rcb] -- This is a note.
    {:.indent.bigandbold}[E.lcb]:.question[E.rcb] -- This is a question.
    {:.indent.bigandbold}[E.lcb]:.vo[E.rcb] -- This is a VO note
    {:.indent.bigandbold}[E.lcb]:.important[E.rcb] -- This is important.
    {:.indent.bigandbold}[E.lcb]:.greyout[E.rcb] -- This is grey text on grey background.
[syntax.wc_close]

Here they are used outside an AV DIV Section.

{:.note}This is a note.
{:.question}This is a question.
{:.vo}This is a VO note
{:.important}This is important.
{:.greyout}This is grey text on grey background.

*CU: Predefined Classes used inside AV section
Here they are again, used inside an AV DIV section

{:.note}This is a note.
{:.question}This is a question.
{:.vo}This is a VO note
{:.important}This is important.
{:.greyout}This is grey text on grey background.

@exit
Here are a few more of the predefined classes available, and remember, you can tailor these or add more as required for your particular purpose.

{:.syntax.width70}@@@ divTitle More predefined classes
    [SP]
    {:.indent}**[E.lcb]:.pbb[E.rcb]**-- Page Break Before (when printing).
    {:.indent}**[E.lcb]:.pba[E.rcb]**-- Page Break After (when printing).
    {:.indent}**[E.lcb]:.red[E.rcb]**-- To color text red.
    {:.indent}**[E.lcb]:.green[E.rcb]**-- To color text green.
    {:.indent}**[E.lcb]:.blue[E.rcb]**-- To color text blue.
    {:.indent}**[E.lcb]:.center[E.rcb]**-- To center text.
    {:.indent}**[E.lcb]:.left[E.rcb]**-- To left align text.
    {:.indent}**[E.lcb]:.right[E.rcb]**-- To right align text.
    {:.indent}**[E.lcb]:.bigandbold[E.rcb]**-- To increase text size and make it bold.
    {:.indent}**[E.lcb]:.box[E.rcb]**-- To put a box around it.
    {:.indent}**[E.lcb]:.dashed[E.rcb]**-- To put a dashed line around it.
    {:.indent}**[E.lcb]:.greybg[E.rcb]**-- To make the background grey.
    {:.indent}**[E.lcb]:.ignore[E.rcb]**-- So it won't display in the output.

You can stack multiple classes by simply stringing them together. For example, on the next line, I'll write **{:.greybg.bigandbold.blue}This is a big and bold blue note on a grey background.**

{:.greybg.bigandbold.blue}This is a big and bold blue note on a grey background.
