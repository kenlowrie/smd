@import "$/testsetup.md"

[var.testdoc.begin(title="markdown.md" desc="Testing markdown")]

// markdown tests
*emphasis*[b]
**strong**[b]
***emphasis and strong***[b]
++this is added++[b]
~~this is deleted~~[b]
// blank lines

    

// multiple markdowns
*emphasis* and regular and **strong** and regular and ***both***[b]
not at start *emphasis* and regular and **strong** and regular and ***both***[b]
not or start *emphasis* and regular and **strong** and regular and ***both*** or end[b]
++this is added++ and ~~this is deleted~~[b]
n o s ++this is added++ and ~~this is deleted~~[b]
nos ++this is added++ and ~~this is deleted~~ or end[b]

// nested
*emphasis and **strong** and ++new stuff++ and ~~old stuff~~*[b]
*emphasis and **strong** and ~~old ++new stuff inside++ stuff~~ and ~~old stuff~~*[b]

// headers
@wrap html.divx
# h1
## h2
### h3
#### h4
##### h5
###### h6
@parw

[wrap_h(t="#h1")]
words
[wrap_h(t="##h2")]
words
[wrap_h(t="###h3")]
words
[wrap_h(t="####h4")]
words
[wrap_h(t="#####h5")]
words
[wrap_h(t="######h6")]
words

[wrap_h(t="# header with leading space")]
[wrap_h(t="## header with leading tab &lpar;which my editor converts to spaces&rpar;")]

header markdown must be first thing on the line. # This will not be a header.
@@header markdown must be first thing on the line. # This will not be a header, even if you use @raw...

@set dump_ns_list="var=\".\""
[var.testdoc.end]
