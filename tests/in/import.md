@import "$/testsetup.md"

[var.testdoc.begin(title="import.md" desc="Testing @import and @embed and @watch")]

{:.blue}#Testing @import

//TODO: if this logic is tested elsewhere, lose it from here.

@var workingtitle="Script&#32;Markdown&#32;Utility"
@var storysummary="This manual describes the *Script Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create HTML documents quickly, easily and most important, efficiently. ***Enjoy!***"

@import '$/import/test_import.md'
[var.plain(t="Test @import with relative $ path")]
@import '$/import/test_import2.md'

@import '[sys.imports]/code.md'

@import "this file doesn't exist"


[plain(t="{:.blue}Testing @embed")]
@embed "this file doesn't exist"

[code.encode_smd(t="@import \"in/import/test_embed.md - 1st Time as @import\"")][b]

@import "$/import/test_embed.md"
The reasoning behind @importing it first is because you can only @import once, but you can @embed as many times as you want. However, once you @embed, it shows up on the list of "seen" files by the tracker, so @import will fail. I am not sure if I want to change that behavior, since technically, @embed code would not likely be a candidate for @importing anyway...
[wrap_h.hash1]
[wrap_h(t="### 1st @embed of in/import/test_embed.md")]
[code.encode_smd(t="@embed \"in/import/test_embed.md - 1st Time\"")][b]
@embed "in/import/test_embed.md"
[wrap_h(t="### 2nd @embed of in/import/test_embed.md")]
[code.encode_smd(t="@embed \"in/import/test_embed.md - 2nd Time\"")][b]
@embed "in/import/test_embed.md"

@embed esc="true"
@embed escape="true"

[plain(t="{:.blue}Testing @watch")]

// Get a list of everything we've seen so far.
@dump tracked="."

This next file doesn't exist. Should get a warning from @watch...
// Add something that doesn't exist. Will display warning in output file.
@watch "this file doesn't exist"

// This is already there, try to watch it again - This is considered OK. Does not display warning.
@dump tracked=".*/test_embed.md"
@watch "in/import/test_embed.md"
@dump tracked=".*/test_embed.md"

// Make sure stop.md is not currently watchec, then add it, then check to see if it's being watched.
@dump tracked=".*/stop.md"
@watch "in/stop.md"
@dump tracked=".*/stop.md"

@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for [smdimport.b], [smdembed.b] & [smdwatch.b]")]

[var.toc.wc_open(t="Table of Contents - Unittest [smdimport.b], [smdembed.b] & [smdwatch.b]")]
@wrap nop
[b]
@import "[sys.root]/docs/section/import-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from import-inc.md")]
@dump link="^imports|embed|watch"

@import "[sys.root]/docs/section/import-doc.md"




@set dump_ns_list="var=\".*\" link=\"c|d\""
[var.testdoc.end]
