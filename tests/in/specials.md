@import "$/testsetup.md"

[var.testdoc_nw.begin(title="specials.md" desc="Testing Cover, Revision and Contact section types")]

// And now let's try various versions
[hash1]
### var.cover.inline versions
[var.cover.inline(title="Title of Script" author="Script Author")]
[var.cover.inline(title="Title of Script" author="Script Author" logline="Logline")]
[var.cover.inline(author="Script Author")]
[var.cover.inline(logline="Logline")]
[var.cover.inline(author="Script Author" logline="Logline")]
[var.cover.inline(title="Title of Script" logline="Logline")]
[var.cover.inline(title="Title of Script")]
[var.cover.inline(title="" author="Script Author" logline="")]
### var.cover (@@) versions
[var.cover(title =     "Title of Script" author   =   "Script Author")]
[var.cover(title="Title of Script" author  ="Script Author" logline=  "Logline")]
[var.cover(     author    =    "Script Author"    )]
[var.cover]
[var.cover( author="author")]
[var.cover(author="author" title="title" logline="logline")]

[hash1]
[var.divxp(c="Note that we'll always use timestamp off in the unittest scripts, because otherwise the comparison will fail... The code is unit tested separately...")]

[var.revision.inline_plain(v="1.0")]
[var.revision.inline_plain(v="1.1")]
[var.revision.plain]
//[var.revision]

[hash1] 
[var.contact]  
[var.contact(cn="")]
[var.contact(ph="")]
[var.contact(em="")]
[var.contact(c1="")]
[var.contact(c2="")]
[var.contact(c3="" )]
[var.contact(cn="cn"  c2="c2")]
[var.contact(c2=""  cn="")]
[hash2]
[var.contact.inline(cn ="Contact Name"   )]   
[var.contact.inline(ph="210-555-1212"   )]  
[var.contact.inline(cn="Contact Name2" ph="210-555-1212"   )]  
[var.contact.inline(em="email@mydomain.com"    )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3")]

[var.contact( ph="210-555-5309" em="" c1="" c2="" c3=""    )]
[var.contact( ph="210-555-1212" em="email@mydomain.com"    )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2"   )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]

[var.contact.inline(  em="EMAIL@mydomain.com"    )]
[var.contact.inline(  em="email@mydomain.com" c1="Copyright  Line 1a"     )]
[var.contact.inline(  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2b"   )]
[var.contact.inline(  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3c" )]

[var.contact(   c1="Copyright  Line 1a"  )]
[var.contact(   c1="Copyright  Line 1"  c2="Copyright Line 2b" )]
[var.contact(   c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3c" )]

[var.contact(    c2="Copyright Line 2")]
[var.contact(    c2="Copyright Line 2" c3="Copyright Line 3" )]

[var.contact(     c3="Copyright Line 3" )]

[var.contact.inline( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]

[var.contact(  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]


[var.contact.inline(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" )]c3="Copyright Line 3" 
[var.contact.inline(cn="Contact Name"   c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name"  em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]

[var.contact(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact(cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2")]

[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"   c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2")]

[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1" )]

[var.contact(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact(cn="Contact Name"  em="email@mydomain.com" c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact(cn="Contact Name"   c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact(cn="Contact Name"   c1="Copyright  Line 1"  )]

[var.contact.inline(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2")]


[var.contact( ph="210-444-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212"  c1="Copyright  Line 1"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1b"  c3="Copyright Line 3" )]
[var.contact.inline( ph="210-555-1212" em="email@mydomain.com" c1="Copyright  Line 1"  c2="Copyright Line 2")]
[var.contact.inline(cn="Contact Name" ph="210-555-1212" em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name" ph="210-555-1212"   c2="Copyright Line 2c" c3="Copyright Line 3" )]
[var.contact.inline(cn="Contact Name"  em="email@mydomain.com"  c2="Copyright Line 2" c3="Copyright Line 3" )]

@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for titlepage-doc.md")]

[var.toc.wc_open(t="Table of Contents - Unittest titlepage-doc.md")]
@wrap nop
[b]
@import "[sys.root]/docs/section/titlepage-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from titlepage-inc.md")]
@dump link="^ug_title_page|ug_tp"

@import "[sys.root]/docs/section/titlepage-doc.md"

@set dump_ns_list="var=\"cover|revision|contact|defaults\" html=\"revision|contact\""


[var.testdoc_nw.end]
