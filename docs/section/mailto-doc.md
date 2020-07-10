[link.ug_mailto_links]
[wrap_h.chapter(t="###mailto links")]

//[docthis.open(h="Add this to mailto-doc.md")]
//[docthis.close]

You can create mailto: links in your document too, which enables users to click on a link to automatically compose an email addressed to the specified email address. [smd.b] will encode the entire mailto: link URL using a mix of decimal and hexadecimal HTML entities as a deterrent to spam bots that mine email addresses from HTML documents. Here's the syntax for a *mailto:* link:
[syntax.wc_open(t="mailto Link Syntax")]
    [generic.wc_open_inline]
        [smdlink.b] _id="name" href="*mailto:*you@yourdomain.com"[bb]
        [smdcomment.b] or use the link factory
        [encode_smd(t="[link.ln_factory(nm=\"sample\" hr=\"mailto://example.com\" t=\"my default title\") ]")]
    [generic.wc_close_inline]
[syntax.wc_close]

Let's create two sample links using each method and see how they are then used in your markdown:

@link _="email_me" href="mailto:me@domain.com"
[ln_factory(nm="feedback" hr="mailto:user@mydomain.com?subject=feature%20feedback" t="Send feedback")]

[terminal.wc_open(t="using the mailto: prefix on [smdlink.il] declarations")]
    [tab.<]@link _="email_me" href="mailto:me@domain.com"[tab.>]
    [tab.<][E.lb]ln_factory(nm="feedback" hr="mailto:user@mydomain.com?subject=feature%20feedback" t="Send feedback")[E.rb][tab.>]
[terminal.wc_close]

I've defined the previous examples inline in the user docs, so now we can use them by using either of these methods:

**[encode_smd(t="[link.email_me.<]email_me[link.email_me.>")]** emits this:[b]
[tab.<]*[escape_var(v="link.email_me.<")]*email_me*[escape_var(v="link.email_me.>")]*[tab.>]

which the browser renders like this: [email_me.<]email me[email_me.>].

[bluenote.wc_open]
**Wait, what the ... happened to the href?**
[bb]
[tab.<]*[escape_var(v="link.email_me.<")]*[tab.>]
[bb]
How come the **href** on the link is all jacked up? Actually, this is intentional! It encodes the email address in a way that makes it a bit more challenging for **spambots** and other web scraper tools to detect an email address. Not impossible, but definitely more challenging! In addition, every time the parser runs the output will be slightly different, yet the link and the behavior remain consistent and correct! Just a cool side benefit to how [smd.b] parses and encodes links that use a **mailto** prefix on the **href**.
[bluenote.wc_close]

Getting back to **mailto** links, let's take a look at the other example, the one created with the link factory. The variable name for it is **feedback**, and to use the link, all we need to write is **[encode_smd(t="[feedback]")]**, which is much easier and cleaner than having to use the link open and close tags as before.

When we do that, the browser will display [feedback], which is exactly what we need. If you'll recall from the discussion on the link factory before, you also have access to the **_qlink** attribute, so we can create custom alternate text on the fly. 

For example, if we write **[encode_smd(t="[feedback._qlink")](_qtext="I would love to get your feedback!")]**, then this is what the browser would display: [feedback._qlink(_qtext="I would love to get your feedback!")]

And so we come to the end of the [smdlink.b] chapter. Built upon the [smdhtml.b] namespace, [smdlink.b] offers some cool features for creating and using hyperlinks if your markdown documents. Next up, is the [smdimage.b] namespace.
