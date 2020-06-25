{:.blue.center}#Script Markdown User Manual
@var workingtitle="Script Markdown Utility"
@var storysummary="This manual describes the *Script Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create script markdown documents quickly, easily and most important, efficiently. **Enjoy!**[bb]***NOTE:*** Additional samples that might be worth reviewing are those in the unit test code located here: ***(../tests/in/&ast;.md)***. Keep in mind that the unit test code is meant to stress test the parser as well as the limits and edges of the syntax of smd, so in some cases it might be confusing or even contradictory to what the user guide covers."

@import "[sys.imports]/divs.md"
@import '[sys.imports]/report.md'
@import '[sys.imports]/helpers.md'
@import '[sys.imports]/avs/avs.md'
@import '$/import/userguideheading.md'


[link.bm_factory(nm="summary" t="Summary")]

@wrap nop
[var.toc.wc_open(t="Table of Contents - SMD User Guide[bb]")]
@import "$/section/intro-inc.md"
@import "$/section/heading-inc.md"
@import "$/section/ns-inc.md"
@import "$/section/nsvar-inc.md"
@import "$/section/nshtml-inc.md"
@import "$/section/nslink-inc.md"
@import "$/section/mailto-inc.md"
@import "$/section/nsimage-inc.md"
@import "$/section/nscode-inc.md"
@import "$/section/divs-inc.md"
@import "$/section/titlepage-inc.md"
@import "$/section/import-inc.md"
@import "$/section/advanced-inc.md"
@import "$/section/predefcss-inc.md"
@import "$/section/debug-inc.md"
[link.summary.link] - **Summary of the User Guide**[b]
[var.toc.wc_close]
@parw

//TODO: What if we wrapped the entire document in an Extras Div?

@wrap divx

## Things to document
<pre style="white-space:pre-wrap">
<code style="display:block>">
var.code.with_content(t="Things to document", c="code ...")]

.@var fu=\"bar\" i.e. short notation
.@var fu=\"bar\" _format=\"wins\" i.e. assignment to fu ignored if _format present
.@set fu=\"bar2\" a1=\"val\" i.e. you can add attrs during a set operation
.@set _=\"defaults\" revision=\"0.4.2\" - that you can add an attr while keeping the rest...
.{:.bigandbold}you can add a span prefix
all the new command line switches. distinguish between smd, ismd, smdparse, smdlive
defaults variable:[b] [defaults]
@ defaults keyword - currently no parameters, but perhaps extend? @defaults [flags | raw | imports ...]

8. Document the @embed "filename" support.
9. Inline links and Reference links do not work. I think it's because you have to use @link to define links... Fix the docs.
10. Mailto links and Automatic links also do not seem to work. Fix the docs.
11. Link aliases don't work. Fix the docs.
12. Bookmark syntax is wrong. Fix the docs.
13. Cover, Revision & Contact are wrong. These are "builtins". Fix the docs.
15. Is varv2 a thing? Fix the docs. I think it is basic. and var., where basic. refers to aliases, and var refers to @var ...
17. Document @debug, @debug key="re", @debug tags=""
[b]
40. DOCS: @import "[sys.imports]/def_head.md" twice in a row only works the first time. Intentional. stream().open()
41. Document all the new command line switches (smd, smdparse, ismd and smdlive)
[b]
If I put a div extras at top, then gotta watch using it inline, otherwise we get double margins, etc.
Document @defaults, @watch "filename"
The custom file data logic in cache.py no longer works due to how stream.py handles imports.
The anatomy of a complex variable definition. Passing parameters, self, why _ is important. How link and html work. How code works.
Add @wrap, and probably need to clean up the docs in tests/in/script1.md; possibly xfer to shared markdown files.
Explain how @import '$' works when no files open i.e. reading from stdin
Document @dump sysdef="." tracked="." and @debug.
Document code.encode_smd
96. Add @wrap tag1 [, tag2 [...]] support
98. Should handle_header() handle @wrap lines? Code added, need to review closely.
99. @wrap nop and null - add tests to wrap.md
100. @parw *|all @parw -3 | 0 | 1 | 25 - add tests.
mailto: hyperlinks must be discussed here, we cannot do that in the unittest for link.md because output changes between runs.

@@[code.encode_smd(t="@dump sysdef=\".\"")][b]

{:.bigandbold}If this is inline, *[code.encode_smd(t="@var name=\"value\" _format=\"# {{self.name}}\"")]*
//@dump code="encode_smd"
//@set _ns="code" _="encode_smd" b="**{{self.run}}(t={{self.t}})**"
//[encode_smd.b(t="[var]")]

</code>
</pre>

@var mk="{{self.s}}" s="@@<br/>{{code.repeat(t=\"&\" c=\"100\")}}<br />" e="@@<br/>{{code.repeat(t=\"%\" c=\"100\")}}<br />"

//#Check this out!
//TODO: Move this to code.md
@code _id="escape_var" type="exec" src="from .utility import HtmlUtils;print(HtmlUtils.escape_html_var('$.v'))" v="Usage: code.escape.run(v=\"var_to_esc\")"
//Is this useful for anything? Right off I don't think so...
@code _id="encode_smd_var" type="exec" src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd_var('$.v'))" v="Usage: code.encode_smd_var.run(v=\"var_to_encode\")"

//[mk]
//@@[code.escape_var(v="var.bb")]
//@@[code.encode_smd_var(v="var.bb")]
//[mk]

@parw
@wrap divx, p

@import "$/section/intro-doc.md"

@import "$/section/ns-doc.md"

@import "$/section/nsvar-doc.md"

@import "$/section/nshtml-doc.md"

@import "$/section/nslink-doc.md"
 
@import "$/section/mailto-doc.md"

@import "$/section/nsimage-doc.md"

@import "$/section/nscode-doc.md"

@import "$/section/divs-doc.md"

@import "$/section/heading-doc.md"

@import "$/section/titlepage-doc.md"

@import "$/section/import-doc.md"

@import "$/section/advanced-doc.md"

@import "$/section/predefcss-doc.md"

@import "$/section/debug-doc.md"




[link.summary]
[wrap_h(t="## Summary")]

Well that's it! Hope you've enjoyed reading the docs for the smd utility. More importantly, I hope that you can use this app to streamline your html document and audio/visual script development!
