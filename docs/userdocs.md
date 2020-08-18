{:.blue.center}#Script Markdown User Manual
@var workingtitle="Script Markdown Utility"
@var storysummary="This manual describes the *Script Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create script markdown documents quickly, easily and most important, efficiently. **Enjoy!**[bb]***NOTE:*** Additional samples that might be worth reviewing are those in the unit test code located here: ***(../tests/in/&ast;.md)***. Keep in mind that the unit test code is meant to stress test the parser as well as the limits and edges of the syntax of smd, so in some cases it might be confusing or even contradictory to what the user guide covers!"

@import '[sys.imports]/divs.md'
@import '[sys.imports]/report.md'
@import '[sys.imports]/helpers.md'
@import '[sys.imports]/avs/avs.md'
@import '$/userdocs_macros.md'
@import '$/import/userguideheading.md'

// More helpers for the user manual. Add anything useful to built-ins once completed.

@html _="codeblk" _inherit="code" style="display:block;color:purple"

@var TODO="{:.bigandbold.red}TODO:[sp]"

@var docthis="usage: docthis.open(), then content, then docthis.close()"\
    open="{{code.pushlines(t=\"@wrap null\n{{self._start}}\n{{html.prewrap.<}}\n{{html.codeblk.<}}\n@parw 1\n@wrap divx\")}}"\
    close="{{code.pushlines(t=\"@parw 1\n@wrap null\n{{html.codeblk.>}}\n{{html.prewrap.>}}\n@parw 1\")}}"\
     _start="{{wrap_h(t=\"## {{self.h}}\")}}"\
     h="Things to document"

// Override some of the default helpers

[link.bm_factory(nm="toc" t="Table of Contents")]
[link.bm_factory(nm="summary" t="Summary")]
[link.bm_factory(nm="building" t="Building Documents")]
[link.bm_factory(nm="examples" t="Sample Documents")]

[link.toc]
[var.toc.wc_open(t="Table of Contents - SMD User Guide[bb]")]
@import "$/section/setup-inc.md"
@import "$/section/cmdline-inc.md"
@import "$/section/intro-inc.md"
@import "$/section/heading-inc.md"
@import "$/section/builtins-inc.md"
@import "$/section/helpers-inc.md"
@import "$/section/ns-inc.md"
@import "$/section/nsvar-inc.md"
@import "$/section/nshtml-inc.md"
@import "$/section/nslink-inc.md"
@import "$/section/mailto-inc.md"
@import "$/section/nsimage-inc.md"
@import "$/section/nscode-inc.md"
[link.building.link] - **Creating sophisticated layouts**[b]
@import "$/section/import-inc.md"
@import "$/section/wrap-inc.md"
@import "$/section/divs-inc.md"
@import "$/section/titlepage-inc.md"
@import "$/section/advanced-inc.md"
@import "$/section/predefcss-inc.md"
@import "$/section/av-inc.md"
@import "$/section/debug-inc.md"
[link.examples.link] - **Specialized examples built with [smd]**[b]
@import "$/samples/proposal/misc-inc.md"
@import "$/samples/avscript/script1-inc.md"
@import "$/samples/avshots/shots-inc.md"
@import "$/samples/film/film-inc.md"
@import "$/samples/images/images-inc.md"
[link.summary.link] - **So long, and thanks for all the fish**[b]
[var.toc.wc_close]

//[docthis.open(h="Add this to ????.md")]
//Holding tank for adding things that need to be covered somewhere...
//[docthis.close]

@wrap divx, p

[wrap_h.chapter(t="# [smd] - The [smd.short] Processor")]

Welcome to the user manual for [smd.b], the [smd.short_b] Processor that can take plain text files written in a specialized markdown syntax and turn them into rich HTML documents. This guide will take you through installation and setup of [smd.b], and then show you how you can use it to create all sorts of interesting and cool HTML projects. So let's get going!

[TODO] The release process should smdparse -f userdocs.md -c -d export so the rendered version of the documentation is part of the repository. This is required because the instructions in the README.md say "open this file with your browser" to read the docs current with the release you are looking at...


@import "$/section/setup-doc.md"
[link.toc.link]
@import "$/section/cmdline-doc.md"
[link.toc.link]
@import "$/section/intro-doc.md"
[link.toc.link]
@import "$/section/heading-doc.md"
[link.toc.link]
@import "$/section/builtins-doc.md"
[link.toc.link]
@import "$/section/helpers-doc.md"
[link.toc.link]

@import "$/section/ns-doc.md"
[link.toc.link]
@import "$/section/nsvar-doc.md"
[link.toc.link]
@import "$/section/nshtml-doc.md"
[link.toc.link]
@import "$/section/nslink-doc.md"
[link.toc.link]
@import "$/section/mailto-doc.md"
[link.toc.link]
@import "$/section/nsimage-doc.md"
[link.toc.link]
@import "$/section/nscode-doc.md"
[link.toc.link]

[link.building]
[wrap_h.chapter(t="## Creating Sophisticated Layouts")]

Now that you've got the basics out of the way, it's time to dig in a little deeper and look at the tools available to create bigger and more sophisticated layouts for your documents. In the chapters that follow, we will look at importing files in order to create reusable building blocks, managing the default block tags emitted when no specific HTML markdown is specified, and a set of common **div**'s that you can use and/or customize to your specific needs.
[link.toc.link]

@import "$/section/import-doc.md"
[link.toc.link]
@import "$/section/wrap-doc.md"
[link.toc.link]
@import "$/section/divs-doc.md"

// Reset the cover, contact and revision info so the docs make sense. :)
@set _id="var.cover"\
     title="{{defaults.title}}" \
     author="{{defaults.author}}" \
     logline="{{defaults.logline}}"
@set _id="var.contact" \
     cn="{{defaults.cn}}" \
     ph="{{defaults.ph}}" \
     em="{{defaults.em}}" \
     c1="{{defaults.c1}}" \
     c2="{{defaults.c2}}" \
     c3="{{defaults.c3}}"
@set _id="var.revision" v="{{defaults.revision}}"

[link.toc.link]
@import "$/section/titlepage-doc.md"
[link.toc.link]
@import "$/section/advanced-doc.md"
[link.toc.link]
@import "$/section/predefcss-doc.md"
[link.toc.link]
// av-doc might fit better in the examples? unless it's just documenting avshot.visual, audio, etc.
@import "$/section/av-doc.md"
[link.toc.link]

@import "$/section/debug-doc.md"
[link.toc.link]

[link.examples]
[wrap_h.chapter(t="## Sample Projects built with [smd]")]

We will now look at several different examples created with [smd.b] that show some of what you can do with this app. Most of these samples were taken from actual projects I did, with just some minor cleanup to hopefully give you ideas and/or a starting point for creating your own content.

[ulistplain.wc_open]
     Sample 1 - [link.ug_samp_proposal._qlink(_qtext="Creating a Project Proposal")]
     Sample 2 - [link.ug_samp_avscript._qlink(_qtext="How to use the *avshot* builtin")]
     Sample 3 - [link.ug_samp_shots._qlink(_qtext="Real World Example - AAT A/V script using *avshot*")]
     Sample 4 - [link.ug_samp_film._qlink(_qtext="A Music Video Treatment")]
     Sample 5 - [link.ug_samp_images._qlink(_qtext="Using the Advanced Image and Shot Support")]
[ulistplain.wc_close]

I recommend reading them in order, since each builds upon concepts covered in one or more of the prior examples. 

[link.toc.link]

@import "$/samples/proposal/misc-doc.md"
[link.toc.link]
@import "$/samples/avscript/script1-doc.md"
[link.toc.link]
@import "$/samples/avshots/shots-doc.md"
[link.toc.link]
@import "$/samples/film/film-doc.md"
[link.toc.link]
@import "$/samples/images/images-doc.md"
[link.toc.link]


[link.summary]
[wrap_h.chapter(t="## Summary")]

Well that's it! Hope you've enjoyed reading the docs for the smd utility. More importantly, I hope that you can use this app to streamline your html document and audio/visual script development!

[link.toc.link]
