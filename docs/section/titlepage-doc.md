[link.ug_title_pages]
[wrap_h.chapter(t="##Cover, Revision & Contact Sections")]

@var bmo="{{html.bigmargin._open}}"
@var bmc="{{html.bigmargin._close}}"

@wrap divx, p

There are three (3) builtins that can be used in your document to add commonly used sections in script files. They are defined in *sys.imports/report.md*:

[ulistplain.wc_open]
**var.cover** - To add a cover section
**var.revision** - To add a revision section
**var.contact** - To add a contact section
[ulistplain.wc_close]

The details for each type of section are discussed below.

[link.ug_tp_cover]
[wrap_h.section(t="### @var.cover")]
[var.syntax.wc_open(t="Cover Title Syntax")]
     @wrap divx,_syntax_p_content_
          [encode_smd(t="<var.cover")](title="your title", author="author name", logline="logline or short description")][b]
          [encode_smd(t="<var.cover.inline")](title="your title", author="author name", logline="logline or short description")][b]
     @parw
     [b]
     Each attribute is optional, and they can appear in any order. Also note that the value of any parameter can be whatever you want. Just because it says "author", doesn't mean you have to put the author name there. You could instead write "Roses are Red", and that would be just fine...

[var.syntax.wc_close]

Let's see how **[encode_smd(t="<var.cover>")]** renders out:

[bmo]
[var.cover.inline]
[bmc]

Interesting. Looks like it relies on several ***default*** values from the [smd.b] variable **var.default**. That gives us two options to proceed: Either set the defaults (which you might opt to do in  your enviroment, giving them better default values for your own markdown projects), or you can pass them on the fly, using the syntax above. Let's try again, only this time, we'll use the parameters from above:

[bmo]
[var.cover.inline(title="your title" author="author name" logline="logline or short description")]
[bmc]

That's better! So that's pretty much all there is to **var.cover**. It's used in a few of the samples provided in the docs, and you might find it useful for your own projects, along with its companions, **var.revision** and **var.contact**. Let's take a look at them.

[link.ug_tp_revision]
[wrap_h.section(t="### @var.revision")]

@var rev_parms="[E.lp]v=\"1.0\"[E.rp]"

[var.syntax.wc_open(t="Revision Syntax")]
     @wrap divx,_syntax_p_content_
          [E.lb]var.revision[rev_parms]][b]
          [E.lb]var.revision.plain[rev_parms]][b]
          [E.lb]var.revision.inline[rev_parms]][b]
          [E.lb]var.revision.inline_plain[rev_parms]][b]
     @parw
     [b]
     Specify the revision number of your document within quotes. The default rendering of the **var.revision** variable is to include a timestamp at the end of the string. You can request a plain revision string using the plain attribute e.g. [encode_smd(t="<var.revision.plain>")]. In our example below, we are going to use the **plain** version, because this file is included as part of the unittests, and timestamping would cause the test to fail every time. :)

[var.syntax.wc_close]

Let's see how **[encode_smd(t="<var.revision.plain>")]** renders out:
[bmo]
[var.revision.plain]
[bmc]

And once again, we see that the default revision if not specified, looks to **var.default** for the **revision** attribute. Let's go ahead and specify the revision in the markdown using the following syntax: **[encode_smd(t="<var.revision.plain[E.lp]v=\"1.4.2\"[E.rp]>")]**

[bmo]
[var.revision.plain(v="1.4.2")]
[bmc]

Now that you've seen both **var.cover** and **var.revision**, you can probably guess how **var.contact** works just by reviewing the syntax. Let's take a look!

[link.ug_tp_contact]
[wrap_h.section(t="### @var.contact")]

@var contact_parms="(cn=\"name\" ph=\"phone\" em=\"email\" c1=\"copyright line 1\" c2=\"copyright line 2\" c3=\"copyright line 3\")"

[var.syntax.wc_open(t="Contact Syntax")]
     @wrap divx,_syntax_p_content_

     [encode_smd(t="<var.contact")][var.contact_parms]]
     [encode_smd(t="<var.contact.inline")][var.contact_parms]]
     @parw
     [b]
     Each element is optional, and the elements can appear in any order. By default, the system looks in the *var.defaults* variable for the definitions of *cn, ph, em, c1, c2 & c3*.
[var.syntax.wc_close]

For this example, let's look at an alternative of editing defaults.md to specify the defaults for a markdown document, since it's likely you would vary these on a per-project basis. As it turns out, you can conveniently set them using a single call:

[ulistplain.wc_open(t="Set defaults for var.contact")]
     [sp]@set _id="defaults" [E.bs]
          [tab.<]cn="Ken Lowrie" [E.bs][tab.>]
          [tab.<]ph="*512-555-1234*" [E.bs][tab.>]
          [tab.<]em="me@mycompany.com" [E.bs][tab.>]
          [tab.<]c1="Copyright © 2020 My Company, LLC." [E.bs][tab.>]
          [tab.<]c2="All Rights Reserved." [E.bs][tab.>]
          [tab.<]c3="www.mydomain.com"[tab.>]
     [ulistplain.>]
[ulistplain.wc_close]

So, I'm going to do that now, and then we'll write the **[encode_smd(t="<var.contact>")]** markdown and see what we get.
@set _id="defaults"\
     cn="Ken Lowrie"\
     ph="*512-555-1234*"\
     em="me@mycompany.com"\
     c1="Copyright © 2020 My Company, LLC."\
     c2="All Rights Reserved."\
     c3="www.mydomain.com"

[bmo]
[var.contact.inline]
[bmc]

Pretty cool, huh? Of course you would likely create [smdlink.b] variables for the email address and the website so you could make them hyperlinks, but I'm going to leave that up to you to do.

So that's it for these special section divs. Let's move on!
