[link.avs]

[wrap_h.chapter(t="##Audio/Visual [E.lp]AV[E.rp] Script Formatting")]

//[docthis.open(h="Add this to av-doc.md")]
//[docthis.close]

In the prior incarnation of [smd.b], the primary purpose of the application was to create Audio/Visual (AV) style scripts from plain text markdown files. In fact, the name of the prior version was **AVScript**, and it consisted of two Python command line utilities: **avscript.py** and **mkavscript.py**. You may recall that this version relied on the **BBEdit** text editor in order to provide the WYSIWYG preview support while building your markdown documents.

As it morphed into the current version where no reliance on a specific text editor was required, it also shed some of the syntax and semantics of the prior version which limited it to being useful only for creating AV Script documents. This led the way to it being useful for creating many other types of content, from simple web pages to dynamic pages and new monitoring features including endpoints for direct HTTP service.

But the roots of being useful for generating A/V Scripts remains through the use of specialized built-ins provided as part of the distribution package. This support is contained within the **[E.lb]sys.imports[E.rb]/avs** directory.

[wrap_h.section(t="### The **AVS** builtin library")]

The **AVS** builtins provide everything you need to create A/V-style scripts, from the simple, mostly text based scripts, to complex shot-breakdown documents that help you communicate your vision to everyone, be it your Executive Producers or the all important Crew Members!

Although there are a number of markdown files in the **avs** directory, the two you will use primarily are:

[ulistplain.wc_tag_open]
    **[E.lb]sys.imports[E.rb]/avs/avshot.md** - for simple A/V scripts
    **[E.lb]sys.imports[E.rb]/avs/avs.md** - for access to the shot breakdown builtins.
[ulistplain.wc_tag_close]

Let's see a quick example now. Consider the following markdown:

[terminal.wc_open(t="Generate a simple AV shot")]
    [encode_smd(t="@import \"[E.lb]sys.imports[E.rb]/avs/avshot.md\"")]
    [sp]
    [E.lb]avshot.shot_with_desc(_s="WS:Sunrise", _d="\[sp]
        [sp.4]There is just something about a sunrise that gets the blood flowing...\[sp]
        [sp.4]And here is some additional narration.[E.lb]bb[E.rb]\[sp]
        [sp.4]and here are some additional shot notes.\[sp]
    ")] 
[terminal.wc_close]

This is what will be rendered by the browser:

[avshot.shot_with_desc(_s="WS:Sunrise", _d="\
    There is just something about a sunrise that gets the blood flowing...\
    And here is some additional narration.[bb]\
    and here are some additional shot notes.\
")]

And here is the actual HTML code that the parser emits:

[terminal.wc_open(t="Raw HTML Output from prior *avshot.shot_with_desc* markdown")]

    [escape(t="<div class=\"av\"><ul>")]
    [escape(t="<li>WS:Sunrise</li>")]
    [escape(t="</ul>")]
    [escape(t="<p>There is just something about a sunrise that gets the blood flowing...    And here is some additional narration.<br><br>    and here are some additional shot notes.</p>")]
    [escape(t="</div>")]

[terminal.wc_close]

While this is useful for simple A/V Shot generation, many times it might be easier and clearer to write things in a more free-from style. As it turns out, **avshot** has builtin methods for that as well. Take a look at this:

[terminal.wc_open(t="Generate a simple AV shot using the section methods")]
    [E.lb]avshot.visual[E.rb]
        [sp.4]There is nothing like waking up to the smell of coffee percolating in the outdoors.
    [E.lb]avshot.audio[E.rb]
        [sp.4][E.ast]After we fade into the early morning wide-shot of the camp-site, we will cut to this close-up, making sure the client's product logo is visible in the shot.[E.ast]
    [E.lb]avshot.end[E.rb]
[terminal.wc_close]

And here is how the browser will render this markdown:

[avshot.visual]
    CU:Coffee pot heating on wire rack of fire pit
[avshot.audio]
    There is nothing like waking up to the smell of coffee percolating in the outdoors.
    *After we fade into the early morning wide-shot of the camp-site, we will cut to this close-up, making sure the client's product logo is visible in the shot.*
[avshot.end]

In both the **.visual** and **.audio** sections, you can have as much information as required, just keep writing, even starting new regular paragraphs. You can insert any markdown as well, to aid your reader in understanding what you want. When you're done, close out the one shot, and start another. You know, lather, rinse, repeat...

In the upcoming [link.examples._qlink(_qtext="Samples")] chapters, we will cover **avshot** in much more detail as well as the entire set of **avs** builtins... For now, this hopefully provided a quick introduction to what's in store!

[wrap_h.section(t="### Guide to the Sample Documents")]

Before we leave this chapter, here's a summary of the examples provided in the upcoming chapters. This should point you to which specific sample(s) you may want to review to jump start your project, although it's probably best that you read them in the order listed, since each one builds upon concepts covered in a predecessor.

[ulistplain.wc_tag_open]
     Sample 1 - [link.ug_samp_proposal._qlink(_qtext="Creating a Project Proposal")]
     Sample 2 - [link.ug_samp_avscript._qlink(_qtext="How to use the *avshot* builtin")]
     Sample 3 - [link.ug_samp_shots._qlink(_qtext="Real World Example - AAT A/V script using *avshot*")]
     Sample 4 - [link.ug_samp_film._qlink(_qtext="A Music Video Treatment")]
     Sample 5 - [link.ug_samp_images._qlink(_qtext="Using the Advanced Image and Shot Support")]
[ulistplain.wc_tag_close]
