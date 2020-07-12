[link.ug_predefined_classes]
[wrap_h.chapter(t="##Predefined classes")]

There are a number of predefined classes in the primary CSS file that can be used to quickly style your AV scripts. You can add others as required, and decorate your elements as needed. Here are a few of them, used outside the AV DIV, and then again inside an AV DIV.

{:.syntax}@@@ divTitle Predefined classes
    [SP]
    {:.indent.bigandbold}&#123;:.note} -- This is a note.
    {:.indent.bigandbold}&#123;:.question} -- This is a question.
    {:.indent.bigandbold}&#123;:.vo} -- This is a VO note
    {:.indent.bigandbold}&#123;:.important} -- This is important.
    {:.indent.bigandbold}&#123;:.greyout} -- This is grey text on grey background.

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
    {:.indent}**&#123;:.pbb}** -- Page Break Before (when printing).
    {:.indent}**&#123;:.pba}** -- Page Break After (when printing).
    {:.indent}**&#123;:.red}** -- To color text red.
    {:.indent}**&#123;:.green}** -- To color text green.
    {:.indent}**&#123;:.blue}** -- To color text blue.
    {:.indent}**&#123;:.center}** -- To center text.
    {:.indent}**&#123;:.left}** -- To left align text.
    {:.indent}**&#123;:.right}** -- To right align text.
    {:.indent}**&#123;:.bigandbold}** -- To increase text size and make it bold.
    {:.indent}**&#123;:.box}** -- To put a box around it.
    {:.indent}**&#123;:.dashed}** -- To put a dashed line around it.
    {:.indent}**&#123;:.greybg}** -- To make the background grey.
    {:.indent}**&#123;:.ignore}** -- So it won't display in the output.

You can stack multiple classes by simply stringing them together. For example, on the next line, I'll write **{:.greybg.bigandbold.blue}This is a big and bold blue note on a grey background.**

{:.greybg.bigandbold.blue}This is a big and bold blue note on a grey background.
