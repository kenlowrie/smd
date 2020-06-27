@import "$/testsetup.md"

[var.testdoc_nw.begin(title="specials.md" desc="Testing Cover, Revision and Contact section types")]

@var lpar="&lpar;"
@var rpar="&rpar;"
@var obkt="&#91;"

There are three (3) predefined section types that can be defined within your document to add commonly used information in script files. They are defined in *sys.imports/report.md*:

{:.indent}###@var.cover - To add a cover section
{:.indent}###@var.revision - To add a revision section
{:.indent}###@var.contact - To add a contact section

The details for each type of section are as follows:

[var.plain(t="@var.cover")]

[hash1]

[var.syntax.with_content(t="Cover Title Syntax" c="\
     var.cover[lpar]title=\"your title\", author=\"author name\", logline=\"logline or short description\"[rpar] [bb]\
     Each element is optional, and they can appear in any order. Also note that the value of any parameter can be whatever you want. Just because it says \"author\", doesn't mean you have to put the author name there. You could instead write \"Roses are Red\", and that would be just fine...[bb]\
     var.cover.inline[lpar]title=\"your title\", author=\"author name\", logline=\"logline or short description\"[rpar] [bb]\
")]

[var.plain(t="@var.revision")]

@var rev_parms="[lpar]v=\"1.0\"[rpar]"

[var.syntax.wc_open(t="Revision Syntax")]
     [obkt]var.revision[rev_parms]][b]\
     [obkt]var.revision.plain[rev_parms]][b]\
     [obkt]var.revision.inline[rev_parms]][b]\
     [obkt]var.revision.inline_plain[rev_parms]][b]\
     [b]Specify the revision number of your document within quotes. The default rendering of the var.revision variable is to include a timestamp at the end of the string. You can request a plain revision string using the plain attribute e.g. [obkt]var.revision.plain]

[var.syntax.wc_close]

@html _id="indent" _tag="span" style="padding-left:3em" _s="mytext" _format="{{self.<}}{{self._s}}{{self.>}}"

[var.plain(t="@var.contact")]

[var.syntax.wc_open(t="Contact Syntax")]

[var.syntax.wc_p_open]
@@ var.contact[lpar]cn="name" ph="phone" em="email" c1="copyright line 1" c2="copyright line 2" c3="copyright line 3"[bb]
@@ Each element is optional, and the elements can appear in any order. By default, the system looks in the var.defaults variable for the definitions of cn, ph, em, c1, c2 & c3. As such, you can conveniently set them using a single call:[bb]
@@ [sp]**@set _id="defaults"\[b] \
     [html.indent(_s="cn=\"Ken Lowrie\"")][b]\
     [html.indent(_s="ph=\"*512-555-1234*\"")][b]\
     [html.indent(_s="em=\"[me@mycompany.com]\"")][b]\
     [html.indent(_s="c1=\"Copyright © 2020 My Company, LLC.\"")][b]\
     [html.indent(_s="c2=\"All Rights Reserved.\"")][b]\
     [html.indent(_s="c3=\"[www.cloudylogic.com]\"")][b]**
@@ [b]To see these tags in action, take a look at the userguideheading.md document in the import folder of this user guide.

@@ [html.p.>]

[var.syntax.wc_close]

@set _id="defaults"\
     cn="Ken Lowrie"\
     ph="*512-555-1234*"\
     em="[me@mycompany.com]"\
     c1="Copyright © 2020 My Company, LLC."\
     c2="All Rights Reserved."\
     c3="[www.cloudylogic.com]"

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

[var.testdoc_nw.end]
