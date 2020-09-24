[link.ug_predefined_classes]
[wrap_h.chapter(t="##Predefined classes")]

When you examine the default CSS provided with [smd.b] (located in **css/smd.css**), you will see quite a few predefined classes that have been provided to style the various types of documents you can create with [smd.b]. Of course you can add more, and/or change the existing ones to your hearts content, and get things styled the way you want them.

@var var="{:.red}This text will be RED"

In many cases, these different styles are referenced via the **class=** attribute on HTML variables. But there's also another way you access them in your inline markdown by using a special span syntax: e.g.: [var]. There are two ways you can use this:

[olist.wc_tag_open]
Add it to the beginning of any line in your markdown
Add it to the start of an attribute value
[olist.wc_tag_close]

Let's have a look at the syntax.

[var.syntax.wc_open(t="Span Syntax a.k.a. Variable Decorators")]

[b]
{:.bigandbold.indent}&nbsp;@var variable="{:.class}value"
[b]
So, if you declared this: **@var mynewvar="{:.bigandbold.red}My new big bold value"**, and then write &#91;mynewvar], you'd get this:[bb]
@var mynewvar="{:.bigandbold.red}My new big bold value"
[mynewvar]
[var.syntax.wc_close]

There are a number of predefined classes in the primary CSS file that can be used to quickly style your AV scripts. You can add others as required, and decorate your elements as needed. Here are a few of them, used outside the AV DIV, and then again inside an AV DIV.

[syntax.wc_open(t="Predefined classes")]
    {:.indent.bigandbold}[E.lcb]:.note[E.rcb] -- This is a note.
    {:.indent.bigandbold}[E.lcb]:.question[E.rcb] -- This is a question.
    {:.indent.bigandbold}[E.lcb]:.vo[E.rcb] -- This is a VO note
    {:.indent.bigandbold}[E.lcb]:.important[E.rcb] -- This is important.
    {:.indent.bigandbold}[E.lcb]:.greyout[E.rcb] -- This is grey text on grey background.
[syntax.wc_close]

Here they are used outside an AV Section.

{:.note}This is a note.
{:.question}This is a question.
{:.vo}This is a VO note
{:.important}This is important.
{:.greyout}This is grey text on grey background.

Here they are again, used inside an AV DIV section

[avshot.visual]
    CU: Predefined Classes used inside AV section
[avshot.audio]
    {:.note}This is a note.
    {:.question}This is a question.
    {:.vo}This is a VO note
    {:.important}This is important.
    {:.greyout}This is grey text on grey background.
[avshot.end]
@exit

Here are a few more of the predefined classes available, and remember, you can tailor these or add more as required for your particular purpose.

[wrap_h.section(t="#### More predefined classes")]

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

If you have text you want included in the HTML document, but do not want it rendered by the browser, use the **{:.ignore}** class prefix. For example, on the next line, we'll write *{:.ignore}You won't see this.*

{:.ignore}You won't see this.

When you examine the HTML, you'll see the prior text wrapped in **[E.lt]p[E.gt]** tags, inside **[E.lt]div class="extras"[E.gt]** markup. However, it will not be rendered by the browser, unless you modify the CSS rule for the ignore class.

Lines that begin with a double forward slash ***[E.fs2]*** are treated as comments, and are discarded by [smd.b]. They will not appear in the HTML at all. As another example, we'll write *//This will not appear in the HTML* on the next line.

//This will not appear in the HTML

Once again, if you examine the HTML output, you will not see the previous line in the output.

