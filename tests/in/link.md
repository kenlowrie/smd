@import "$/testsetup.md"

[var.testdoc.begin(title="links.md" desc="Testing the @link namespace")]

@var ns="link"

@import "$/nsbasic.md"

[plain(t="Testing @link builtin functions")]

@wrap nop
[var.toc.wc_open(t="Table of Contents - Unittest [ns]")]
[b]
@import "[sys.basepath]/../docs/section/nslink-inc.md"
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from link-inc.md")]
@dump link="inlinemd|^links$|hyperlinks|bookmarks"
@parw

@import "[sys.basepath]/../docs/section/nslink-doc.md"

[plain(t="Testing adding new @link builtins")]

This seems unnecessary at this time.

[plain(t="Testing generic @link support")]

[link.ln_factory(nm="google", hr="https://google.com" t="Google home page")]
[link.google._null_(target="_blank" title="click on me to search on google.com")]

[link.google]
[link.google._asurl]
[link.google._qlink]

@set dump_ns_list="var=\".\" link=\".\""
[var.testdoc.end]
