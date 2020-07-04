[link.debug]
[wrap_h.chapter(t="##Debugging your markdown files")]

Okay, most of you will never need any of the things we are going to discuss here. Why would you? Your markdown will be flawless and perfect the first time. That's good for you, unfortunately for me, that's not the case. Because of that, two special keywords were added to assist with the markdown debugging process: [smddebug.b] and [smddump.b]. This chapter is going to go over both of them in detail, and show how they can be used to assist in the debugging process.



[wrap_h.section(t="###The [smddebug.il] keyword")]

We will start with the [smddebug.b] keyword, as this is useful for getting debug messages written into the output stream, so that you can see what is happening in real-time.

[syntax.wc_open(t="Debug Keyword Syntax")]
[b]
[tab.<][smddebug.b] [E.lb]*tag*="*regex*" [E.lb]*tag*="*regex*" [E.lb] ... [E.rb] [E.rb] [E.rb][tab.>]
[bb]
[tab.<][tab.<]***tag*** is one of [E.lt]**on | off | toggle | enabled | tags**[E.gt][tab.>][tab.>]
[tab.<][tab.<]***regex*** is any Python-compliant regular expression[tab.>][tab.>]
[syntax.wc_close]

Okay, to start, you can see that the parameters to [smddebug.b] are optional. So, if we type [smddebug.em], this is what happens:

[terminal2.wc_open(t="[smddebug.il] keyword")]
[terminal2.wc_open_content]
[smdcomment.b] Toggle everything on
[smddebug.b]
Toggling Debug Mode<br />
<span class="debug green"><strong>Method(toggle): _SYSTEM is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): bookmarks is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): cache is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): cache.import is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): markdown is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): ns is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): ns.add is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): ns.code is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): ns.html is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): ns.image is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): ns.link is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): ns.var is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): smd is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): smd.line is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): smd.raw is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): stdinput is now enabled</strong></span>
<span class="debug green"><strong>Method(toggle): utility is now enabled</strong></span>
[smdcomment.b] Toggle everything back off
[smddebug.b]
Toggling Debug Mode<br />
<span class="debug green"><em>Method(toggle): _SYSTEM is now disabled</em></span>
<span class="debug green"><em>Method(toggle): bookmarks is now disabled</em></span>
<span class="debug green"><em>Method(toggle): cache is now disabled</em></span>
<span class="debug green"><em>Method(toggle): cache.import is now disabled</em></span>
<span class="debug green"><em>Method(toggle): markdown is now disabled</em></span>
<span class="debug green"><em>Method(toggle): ns is now disabled</em></span>
<span class="debug green"><em>Method(toggle): ns.add is now disabled</em></span>
<span class="debug green"><em>Method(toggle): ns.code is now disabled</em></span>
<span class="debug green"><em>Method(toggle): ns.html is now disabled</em></span>
<span class="debug green"><em>Method(toggle): ns.image is now disabled</em></span>
<span class="debug green"><em>Method(toggle): ns.link is now disabled</em></span>
<span class="debug green"><em>Method(toggle): ns.var is now disabled</em></span>
<span class="debug green"><em>Method(toggle): smd is now disabled</em></span>
<span class="debug green"><em>Method(toggle): smd.line is now disabled</em></span>
<span class="debug green"><em>Method(toggle): smd.raw is now disabled</em></span>
<span class="debug green"><em>Method(toggle): stdinput is now disabled</em></span>
<span class="debug green"><em>Method(toggle): utility is now disabled</em></span>

[terminal2.wc_close_content]
[terminal.wc_close]

Okay, awesome, you can see that [smddebug.b] on it's own, simply toggles the state of each registered debug handler. In our case, everything was off, and so the first time [smddebug.b] was used, it toggled everything on. Then, the second time, everything was toggled back off. 

However, if one or more of the registered handlers was **on**, then the first time we issued the [smddebug.b] it would have toggled those off, and everything else on! It's a toggle, so that should be self explanatory. If you aren't sure, open up an [smd.b] session and try it, and see how it works.

[wrap_h.subsect(t="###The [smddebug.il] parameters")]

The parameters to [smddebug.b] are:

[ulistplain.wc_open]
**on** - turn the registered debug handler(s) on
**off** - turn the registered debug handler(s) off
**toggle** - toggle the state of the registered debug handler(s)
**enabled** - dumps the current registered debug handler(s) and their state, without changing it
**tags** - dumps the registered debug handler(s) names, either *em* or **strong** so you know the current state
[ulistplain.wc_close]


[wrap_h.section(t="###The [smddump.il] keyword")]

Dumping variables and links

[smddump.b] ...

.@dump link="."

.@dump html="."

.@dump link="."

.@dump var="."

[docthis.open(h="Add this to debug-doc.md")]

17. Document @debug, @debug tags="" on="", off="", toggle="", enabled=""
18. Document @dump, @dump sysdef="." tracked="." [var|html|link|image|code]="."



[docthis.close]

[link.toc.link]
