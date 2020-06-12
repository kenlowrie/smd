@import "$/testsetup.md"

[var.testdoc.begin(title="divs.md" desc="builtin DIVs from sys.imports/divs.md")]

[hash1]

### Testing var.section
[var.section]
[var.section()] <-- Intentional error, calling section with empty paramter list
[var.section(t="default format section header")]
[var.section.with_content]
[var.section.with_content()]
[var.section.with_content(t=".with_content title")]
[var.section.with_content(t="")]
[var.section.with_content(c="with content, empty title")]
[var.section.with_content(t=".with_content title" c="and content too")]

[hash2]
### Testing without the namespace prefix var.
[section]
[section()] <-- Intentional error, calling section with empty paramter list
[section(t="default format section header")]
[section.with_content]
[section.with_content()] <-- Intentional error, calling section with empty paramter list
[section.with_content(t=".with_content title")]
[section.with_content(t="")]
[section.with_content(c="with content, empty title")]
[section.with_content(t=".with_content title" c="and content too")]

[hash1]
### Testing var.section_pbb
[var.section_pbb]
[var.section_pbb.with_content]
[var.section_pbb(t="section_pbb title")]
[var.section_pbb.with_content(c="section_pbb content", t="section_pbb title2")]

[hash2]
### Testing without the namespace prefix var.

[hash1]
### Testing var.plain

[var.plain]
[var.plain.with_content]
[var.plain(t="plain non default title")]
[var.plain.with_content]
[var.plain.with_content(c="plain non default comment")]

[hash2]
### Testing without the namespace prefix var.
[plain]
[plain.with_content]
[plain(t="plain non default title")]
[plain.with_content]
[plain.with_content(c="plain non default comment")]

[hash1]
### Testing var.code

[var.code]
[var.code.with_content]
[var.code(t="code non default title")]
[var.code.with_content]
[var.code.with_content(c="code non default comment")]

[hash2]
### Testing without the namespace prefix var.

[code]
[code.with_content]
[code(t="code non default title")]
[code.with_content]
[code.with_content(c="code non default comment")]

[hash1]
### Testing var.toc
[var.toc]
[var.toc.with_content]
[var.toc(t="toc non default title")]
[var.toc.with_content]
[var.toc.with_content(c="toc non default comment")]


[hash2]
### Testing without the namespace prefix var.
[toc]
[toc.with_content]
[toc(t="toc non default title")]
[toc.with_content]
[toc.with_content(c="toc non default comment")]

[hash1]
### Testing var.review
[var.review]
[var.review.with_content]
[var.review(t="review non default title")]
[var.review.with_content]
[var.review.with_content(c="review non default comment")]

[hash2]
### Testing without the namespace prefix var.
[review]
[review.with_content]
[review(t="review non default title")]
[review.with_content]
[review.with_content(c="review non default comment")]

[hash1]
### Testing var.note
[var.note]
[var.note.with_content]
[var.note(t="note non default title")]
[var.note.with_content]
[var.note.with_content(c="note non default comment")]

[hash2]
### Testing without the namespace prefix var.
[note]
[note.with_content]
[note(t="note non default title")]
[note.with_content]
[note.with_content(c="note non default comment")]

[hash1]
### Testing var.extras and var.divxp
[var.extras]
[var.extras(c="your comment inside an extras div")]

[var.divxp]
[var.divxp(c="your content inside a p tag inside a div")]

[testdoc.end]

@dump var="." html="." link="." image="."
@import "[sys.imports]/def_bodyclose.md"
@import "[sys.imports]/def_close.md"
