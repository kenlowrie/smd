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
# h1
## h2
### h3
#### h4
##### h5
###### h6

#h1
words
##h2
words
###h3
words
####h4
words
#####h5
words
######h6
words

 # header with leading space
    ## header with leading tab (which my editor converts to spaces)

header markdown must be first thing on the line. # This will not be a header.
@@header markdown must be first thing on the line. # This will not be a header, even if you use @raw...

@set dump_ns_list="var=\".\""
[var.testdoc.end]
