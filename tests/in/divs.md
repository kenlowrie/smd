@import "$/testsetup.md"

[var.testdoc.begin(title="divs.md" desc="builtin DIVs from sys.imports/divs.md")]

[wrap_h(t="### Testing var.section")]
[var.section]
[var.section()] <-- Intentional error, calling section with empty paramter list
[var.section(t="default format section header")]
[var.section.with_content]
[var.section.with_content()]
[var.section.with_content(t=".with_content title")]
[var.section.with_content(t="")]
[var.section.with_content(c="with content, empty title")]
[var.section.with_content(t=".with_content title" c="and content too")]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]
[section]
[section()] <-- Intentional error, calling section with empty paramter list
[section(t="default format section header")]
[section.with_content]
[section.with_content()] <-- Intentional error, calling section with empty paramter list
[section.with_content(t=".with_content title")]
[section.with_content(t="")]
[section.with_content(c="with content, empty title")]
[section.with_content(t=".with_content title" c="and content too")]

[wrap_h.hash1]
[wrap_h(t="### Testing var.section_pbb")]
[var.section_pbb]
[var.section_pbb.with_content]
[var.section_pbb(t="section_pbb title")]
[var.section_pbb.with_content(c="section_pbb content", t="section_pbb title2")]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]
[section_pbb]
[section_pbb.with_content]
[section_pbb(t="section_pbb title")]
[section_pbb.with_content(c="section_pbb content", t="section_pbb title2")]

[wrap_h.hash1]
[wrap_h(t="### Testing var.plain")]

[var.plain]
[var.plain.with_content]
[var.plain(t="plain non default title")]
[var.plain.with_content]
[var.plain.with_content(c="plain non default comment")]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]
[plain]
[plain.with_content]
[plain(t="plain non default title")]
[plain.with_content]
[plain.with_content(c="plain non default comment")]

[wrap_h.hash1]
[wrap_h(t="### Testing var.source")]

[var.source]
[var.source.with_content]
[var.source(t="source non default title")]
[var.source.with_content]
[var.source.with_content(c="source non default comment")]

[var.source.wc_open]
[b]we are open
[var.source.wc_close]

//NOTE: The inline versions of source and probably note, etc., are not really useful, because
//      block elements as wrappers (which is likely in effect), are going to confuse the browser
//      because they will wrap other open block tags. 
//      Below is one workaround, another is how terminal2 is implemented by adding wc_open/close_content
@wrap nop
[html.divx.<]
[var.source.wc_open_inline]
[b]we are open inline
[var.source.wc_close_inline]
[html.divx.>]
@parw

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]

[source]
[source.with_content]
[source(t="source non default title")]
[source.with_content]
[source.with_content(c="source non default comment")]

[wrap_h.hash1]
[wrap_h(t="### Testing var.toc")]
[var.toc]
[var.toc.with_content]
[var.toc(t="toc non default title")]
[var.toc.with_content]
[var.toc.with_content(c="toc non default comment")]
[var.toc.wc_open]
toc content using .wc_open and .wc_close
[var.toc.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]
[toc]
[toc.with_content]
[toc(t="toc non default title")]
[toc.with_content]
[toc.with_content(c="toc non default comment")]
[toc.wc_open]
toc content using .wc_open and .wc_close
[toc.wc_close]

[wrap_h.hash1]
[wrap_h(t="### Testing var.review")]
[var.review]
[var.review.with_content]
[var.review(t="review non default title")]
[var.review.with_content]
[var.review.with_content(c="review non default comment")]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]
[review]
[review.with_content]
[review(t="review non default title")]
[review.with_content]
[review.with_content(c="review non default comment")]




[wrap_h.hash1]
[wrap_h(t="### Testing var.note")]
[var.note]
[var.note.with_content]
[var.note(c="note non default content")]
[var.note.with_content]
[var.note.with_content(c="note non default comment")]
[var.note.wc_open(c="non-default-content-ignored-on-wc_open-but-used-next-time")]
some additional note content.[b]
and some more[b]
and still more
[var.note.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]
[note]
[note.with_content]
[note(c="note non default content")]
[note.with_content]
[note.with_content(c="note non default comment")]
[note.wc_open(c="non-default-title-wc_open--this will be ignored here but used next time a **note** is used w/o a parameter override")]
some additional note content.[b]
and some more[b]
and still more
[note.wc_close]


[wrap_h.hash1]
[wrap_h(t="### Testing var.vo")]
[var.vo]
[var.vo.with_content]
[var.vo(c="some default text")]
[var.vo.with_content(c="some default content text")]
[var.vo.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[var.vo.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing vo without prefix var.")]
[vo]
[vo.with_content]
[vo(c="some default text")]
[vo.with_content(c="some default content text")]
[vo.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[vo.wc_close]

[wrap_h.hash1]
[wrap_h(t="### Testing var.box")]
[var.box]
[var.box.with_content]
[var.box(c="some default text")]
[var.box.with_content(c="some default content text")]
[var.box.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[var.box.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing box without prefix var.")]
[box]
[box.with_content]
[box(c="some default text")]
[box.with_content(c="some default content text")]
[box.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[box.wc_close]

[wrap_h.hash1]
[wrap_h(t="### Testing var.generic")]
[var.generic]
[var.generic.with_content]
[var.generic(c="some default text")]
[var.generic.with_content(c="some default content text")]
[var.generic.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[var.generic.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing generic without prefix var.")]
[generic]
[generic.with_content]
[generic(c="some default text")]
[generic.with_content(c="some default content text")]
[generic.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[generic.wc_close]


[wrap_h.hash1]
[wrap_h(t="### Testing var.greyout")]
[var.greyout]
[var.greyout.with_content]
[var.greyout(c="some default text")]
[var.greyout.with_content(c="some default content text")]
[var.greyout.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[var.greyout.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing greyout without prefix var.")]
[greyout]
[greyout.with_content]
[greyout(c="some default text")]
[greyout.with_content(c="some default content text")]
[greyout.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[greyout.wc_close]


[wrap_h.hash1]
[wrap_h(t="### Testing var.important")]
[var.important]
[var.important.with_content]
[var.important(c="some default text")]
[var.important.with_content(c="some default content text")]
[var.important.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[var.important.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing important without prefix var.")]
[important]
[important.with_content]
[important(c="some default text")]
[important.with_content(c="some default content text")]
[important.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[important.wc_close]


[wrap_h.hash1]
[wrap_h(t="### Testing var.question")]
[var.question]
[var.question.with_content]
[var.question(c="some default text")]
[var.question.with_content(c="some default content text")]
[var.question.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[var.question.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing question without prefix var.")]
[question]
[question.with_content]
[question(c="some default text")]
[question.with_content(c="some default content text")]
[question.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[question.wc_close]







[wrap_h.hash1]
[wrap_h(t="### Testing var.extras and var.divxp")]
[var.extras]
[var.extras(c="your comment inside an extras div")]

[var.divxp]
[var.divxp(c="your content inside a p tag inside a div")]

[wrap_h.hash1]
[wrap_h(t="### Testing var.specials")]

[var.syntax]
[syntax]
[syntax.inline]

[var.syntax()] <-- Intentional error, calling section with empty paramter list
[syntax()] <-- Intentional error, calling section with empty paramter list

[var.syntax(t="My new title")]
[syntax]

[var.syntax.with_content]
[syntax.with_content]
[syntax.wc_inline(t="syntax.wc_inline")]

[var.syntax._null_(t="RESET TITLE" c="RESET CONTENT")]
[syntax.with_content]

[var.syntax.with_content(c="Just some new content")]
[var.syntax.with_content(t="And now the title too")]

[var.syntax._null_(t="RESET TITLE" c="RESET CONTENT")]
[var.syntax.wc_open]
[var.syntax.wc_close]

[var.syntax.wc_open(t="syntax.wc_open")]
Some content here
And some additional
And one last thing
[var.syntax.wc_close]

[var.syntax._null_(t="RESET TITLE" c="RESET CONTENT")]
[var.syntax.wc_open(t="syntax.wc_open")]
    Some content here[b]\
    And some additional[b]\
    And one last thing[b]\
[var.syntax.wc_close]

[var.syntax._null_(t="RESET TITLE" c="RESET CONTENT")]
@@[var.syntax.wc_open_inline(t="syntax.wc_open")]
    Some content here[b]\
    And some additional[b]\
    And one last thing[b]
[var.syntax.wc_close_inline]

[wrap_h(t="### Testing help")]

[bigmargin._open] 
    [section.wc_open(t="DIV: var.section")]
        [section.?]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="DIV: var.source")]
        [source.?]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="DIV: var.note")]
        [note.?]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="DIV: var.terminal")]
        [terminal.?]
    [section.wc_close]
[bigmargin._close] 

[bigmargin._open] 
    [section.wc_open(t="DIV: var.terminal2")]
        [terminal2.?]
    [section.wc_close]
[bigmargin._close] 


[var.plain(t="User manual sections for DIVs")]

@import "[sys.root]/docs/userdocs_macros.md"

[var.toc.wc_open(t="Table of Contents - Unittest DIVs Builtins")]
@wrap nop
[b]
@import "[sys.root]/docs/section/divs-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from divs-inc.md")]
@dump link="^ug_div|ug_div_"

@import "[sys.root]/docs/section/divs-doc.md"

@set dump_ns_list="var=\".\" html=\".\" help=\"f\""

[var.testdoc.end]
