
[link.div]
{:.plain}@@@ plainTitle
##Divs
You can create a new DIV using ***---*** or ***@@@*** at the start of a new line. The complete syntax is: 

###&#91;{:.class}&lt;***---*** | ***@@@***&gt; &lt;***title_className | .***&gt; &#91;optional title&#93;

The class prefix is optional, but handy if you want your DIV to be styled in a unique way. You can list one or more classes in dotted notation. E.g.: **{:.myclass}** or **{:.myclass1.myclass2}**. Then an optional class for the title, or '.' to indicate no title class, and finally, the optional title. Let's take a look at an example:

When I write ***{:.section}@@@ divTitle This is my new DIV section*** at the start of a new line, I get this:
{:.section}--- divTitle This is my new DIV section

If I indent subsequent lines immediately following the DIV declaration, they become part of the DIV as a regular paragraph. For example, I'll add four (4) indented lines immediately after the previous DIV declaration and I get this:

{:.section}--- divTitle This is my new DIV section
    This is line 1
    This is line 2
    This is line 3
    This is line 4

There are a several built-in CSS classes that are defined in the accompanying **avscript_md.css** file, and you can add your own to get new DIVs formatted to your liking.

{:.syntax}@@@ divTitle Predefined DIVs
    [SP]
    {:.indent.bigandbold}&#123;:.toc} -- For Table of Contents sections.
    {:.indent.bigandbold}&#123;:.section} -- Generic section.
    {:.indent.bigandbold}&#123;:.unused} -- Unused section.
    {:.indent.bigandbold}&#123;:.syntax} -- Syntax section.
    {:.indent.bigandbold}&#123;:.review} -- Review section.
    {:.indent.bigandbold}&#123;:.plain} -- Plain section.

Remember, you can add your own classes in a CSS file, and then reference them using the built-in formatting of **avscript_md**.

