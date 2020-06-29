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
[wrap_h(t="### Testing var.code")]

[var.code]
[var.code.with_content]
[var.code(t="code non default title")]
[var.code.with_content]
[var.code.with_content(c="code non default comment")]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]

//This is intentionally ambiguous. code is also a namespace, so [code.with_content] looks for a code macro called "with_content", instead of resolving to [var.code.with_content]...

[code]
[code.with_content]
[code(t="code non default title")]
[code.with_content]
[code.with_content(c="code non default comment")]

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
[var.note(t="note non default title")]
[var.note.with_content]
[var.note.with_content(c="note non default comment")]
[var.note.wc_open(t="non-default-title-wc_open")]
some additional note content.[b]
and some more[b]
and still more
[var.note.wc_close]

[wrap_h.hash2]
[wrap_h(t="### Testing without the namespace prefix var.")]
[note]
[note.with_content]
[note(t="note non default title")]
[note.with_content]
[note.with_content(c="note non default comment")]
[note.wc_open(t="non-default-title-wc_open")]
some additional note content.[b]
and some more[b]
and still more
[note.wc_close]


[wrap_h.hash1]
[wrap_h(t="### Testing var.vo")]
[var.vo]
[var.vo.with_content]
[var.vo(t="some default text")]
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
[vo(t="some default text")]
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
[var.box(t="some default text")]
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
[box(t="some default text")]
[box.with_content(c="some default content text")]
[box.wc_open]
my content[b]
more content[b]
and a little more[b]
last line
[box.wc_close]

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

[testdoc.end]
