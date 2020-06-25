[link.headings]
[wrap_h(t="##Headers")]

Just like in standard Markdown, you can use the # symbol at the beginning of a line to designate an HTML [e_tag.b(t="h1")] element. ## symbols designate an [e_tag.b(t="h2")] element, and so on, up to ###### for [e_tag.b(t="h6")]. Here are examples of each.

@wrap divx
{:.indent}### # Heading h1
{:.indent}### ## Heading h2
{:.indent}### ### Heading h3
{:.indent}### #### Heading h4
{:.indent}### ##### Heading h5
{:.indent}### ###### Heading h6

[divxp(c="And this is how they will look in the document when it's formatted:")]

# Heading h1
## Heading h2
### Heading h3
#### Heading h4
##### Heading h5
###### Heading h6
@parw

You may want to style the headers to your liking in the smd.css file.

[note(t="IMPORTANT! Using the # to create headings ***requires*** that the hashtag start in column 1 of the line. If you start it anywhere else, it will be interepreted simply as an inline hashtag.")]

For example:

[wrap_h(t="# this works")]

But **#this works**, clearly does not work.


