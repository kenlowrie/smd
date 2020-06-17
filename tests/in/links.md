@import "$/testsetup.md"

[var.testdoc.begin(title="links.md" desc="Testing the @link namespace")]


[wrap_h(t="###Table of Contents")]
[link.bm_factory(nm="inlinemd", t="Inline Markdown")]
[link.bm_factory(nm="links", t="Links")]
[link.bm_factory(nm="inline_links", t="Inline Links")]
[link.bm_factory(nm="ref_links", t="Reference Links")]
[link.bm_factory(nm="auto_links", t="Automatic Links")]

[link.inlinemd.link] - **Formatting content inline**
[link.links.link] - **Inline and Reference Link Styles**[b]
[link.inline_links.link] - **Creating links inline**[b]
[link.ref_links.link] - **Creating reference links**[b]
[link.auto_links.link] - **Creating automatic links**[b]

[link.inlinemd][b]


// links
[link.links]
[wrap_h(t="##Links")]
This is a section about links
[link.inline_links]
[wrap_h(t="###Inline Style:")]

//TODO: Need to update this section, no longer true about inline links and reference links
The next paragraph has inline links defined: This is **&#91;an example]:(http://example.com/ "Inline Link Sample")** of an inline link. **&#91;This inline link]:(http://example.net/)** has no title attribute.

@link _="sample1" _inherit="_template_" title="Inline Link Sample" href="http://example.com"
@link _="sample2" _inherit="_template_" href="http://example.net"

This is [link.sample1(_text="an example")] of an inline link. [link.sample2(_text="This inline link")] has no title attribute.

Inline links can occur anywhere in the text. Once an inline link has been processed the first time, the link ID, i.e. the part between the [ ], can be used over and over. e.g.: [link.sample1].

[link.ref_links]
[wrap_h(t="###Reference Style:")]
Reference links use the format [linkID]:url "optional title". Essentially, just like inline links, but without the ( ) surrounding the URL and optional title.

The reference link style **must** be placed at the beginning of a line. Unlike true Markdown, reference links *must* be defined before they are referenced in the document. Let's create a reference link for the Google Home Page.

{:.indent}####@link _="Google" _inherit="_template_" title="Google Search Page" href="https://google.com"
@link _="Google" _inherit="_template_" title="Google Search Page" href="https://google.com" _text="{{self._}}"

If I write &#91;Google], it is wrapped like so: [Google].

Now, I can go ahead and write **&#91;inline 2]**, like this: [inline 2], and it's a valid link! ***//TODO: What? This is wrong.***
[link.auto_links]
[wrap_h(t="###Automatic links")]
The final type of link format is automatic links. Automatic links are created by simply wrapping a URL with ***&lt; &gt;*** like this: <http://www.cloudylogic.com>. When you do that, the URL (everything between the angle brackets) is wrapped with an **A** tag whose **HREF** attribute is the URL. Unfortunately, this is no longer supported. However, the default template for links includes an attribute *_asurl*, which returns the href styled appropriately. For example: [link.Google._asurl]

&nbsp;


[wrap_h(t="# copied from variables.md")]


// variables
[link.bm_factory(nm="aliases" t="Aliases aka Variables")]
[link.aliases]

[wrap_h(t="## Variables")]

Variables, which is essentially text substitution, is supported using a similar syntax to reference links. **@var variable="value"**. Take the following example:
{:.indent}###@var name="Ken Lowrie"
@var name="Ken Lowrie"
Now, anywhere I write &#91;my name], it will be replaced with "Ken Lowrie". Let's do that now: [name] &lt;-- Should be Ken Lowrie.

If I instead write: &#91;name]=[&#42;Ken Lowrie*], then everywhere I write &#91;name], it will be replaced with &lt;em>Ken Lowrie&lt;/em>. Okay, let's go ahead and do that now. 
@set name="*Ken Lowrie*"
And now, [name] &lt;-- should be Ken Lowrie wrapped with &lt;em> tags.
[wrap_h(t="## Link aliases")]

//TODO: This link format text is wrong. Fix the description/syntax in the docs. Inline, it's correct.
Building on that, we can create aliases for inline links. Say I define a reference link like this: 
{:.indent}###&#91;cls]:https://cloudylogic.com
[link.ln_factory(nm="cls", hr="https://cloudylogic.com", t="{{self.nm}}")]
Now, when I write **&#91;cls]**, it is replaced with a link to https://cloudylogic.com. For example: [cls].
And that's all good. It's concise, I only have to write *cls* in [ ] and it is wrapped with an HTML link. Saves a lot of typing and potential mistakes. But what if I want to have other, more descriptive names for that URL? Good news, we can do that using a special form of aliases: [Descriptive Text]=[id], where *id* is the name of a previously described reference link. Let me go ahead and create an alias for the *cls* link so the descriptive name is Cloudy Logic. THIS TEXT IS ALL WRONG. DOESN'T WORK THIS WAY ANYMORE...
{:.indent}###&#91;Cloudy Logic]=cls
@link _="cls2" _inherit="cls" _text="Cloudy Logic"
Now, when I write [cls2], it is wrapped with the link for *cls*. Cool!

@var abc="123"
@var def="456"
@var xyz="?={{abc}}%20{{def}}]"
@link _="jitlinkvar" _inherit="_template_" _text="{{self._}}" href="https://mydomain.com?a=[abc]%20[def]"
@link _="jitlinkvar2" _inherit="jitlinkvar" href="https://mydomain.com[xyz]"
Here is my [jitlinkvar]
Here is my [jitlinkvar2]

{:.red.center}### avscript tester doc
[var.cover(title="User Manual" author="Ken Lowrie" logline="This is a user manual for the AVScript utility.")]
// $$revision$$:<<*1b*>>

[var.plain(t="{:.blue}Variables")]
We can define variables using the syntax: ***[name]=value***. Here's an example. The next line will define the variable *whoami* and set it to *Ken Lowrie*.
@var whoami="Ken Lowrie"
Now, whenever I write whoami inside square brackets **[ ]**, it will replace it with *Ken Lowrie*. Let's try that now. Hello, my name is *[whoami]*. That's pretty straightforward...

[var.plain(t="Links")]
We can also define hyperlinks using a similar syntax: [linkID]:linkurl. Let's go ahead and define a few links now...
I've defined two new links, one called *cls* which is a standard HTTPS link for my website, and another called *me*, which is a mailto: link that will compose a new email to myself. I use these just like variables, just write the ID inside square brackets.

Visit my domain [cls] or send [me] an email. If you click on either *cls* or *me*, they should behave accordingly.

[wrap_h(t="#### Aliases")]

So far so good. Typing [cls] is certainly better than typing out the entire URL, but it's not very descriptive... Sometimes, maybe I want to have more text, or even the URL as the hyperlink. In those cases, you can create variables whose value matches the name of a linkID, and when you use that variable, it will wrap the variable name with the link tag. Kind of like creating an alias for the link description.
So let's try that. The next line is ***defining the variable*** called "My Email Address" and setting its value to "me". 
@var MyEmailAddress="{{me}}"
By defining a variable's value such that the value is a valid linkID, when you use the variable's name in the document, it will be wrapped in the linkIDs hyperlink. So now when I write [MyEmailAddress], it is more friendly than [me], even though they evaluate to the same link.

You can create more than one "alias" to the same underlying link. The new variable design requires that you add a new format string and specific private variable to support that. Here's an example of it:

In the previous 2 lines, I created two new variables and set both of their values to the linkID called *cls*. So now when I write [link.cls._qlink(_qtext="My Production Website")] and [link.cls._qlink(_qtext="Cloudy Logic Studios, LLC")], both of them are links to my website. 

Most of the time, you'll just add normal links with the regular link syntax, but sometimes it's cool to have these other options.

Here are a couple more examples:

[link.ln_factory(nm="article1", hr="https://wordpress.org/news/2018/05/the-month-in-wordpress-april-2018/", t="Link to Article")]
@link _="article2" _inherit="_template_" _text="Link to Article2" href="https://domain.com/another_article_link"
@var domain="cls"
[article1] <-- That should have been turned into a link
@link _="withtitle" _inherit="_template_" _text="One with Title" href="https://www.cloudylogic.com" title="This is a link title..."

You can send [feedback]. Or you can just email [me]. Or go to my [domain]. But don't do that if [Cloudy Logic]:(cls) is not defined. Finally, [withtitle]

Remember, variable definitions and reference link definitions must be declared on a line by themself. If you put more stuff, it will just process the first one. If it isn't at the beginning of the line, it'll be ignored. For example:

@set dump_ns_list="var=\".\" link=\".\""
[var.testdoc.end]
