@import "$/testsetup.md"

[var.testavdoc.begin(title="import.md" desc="Testing @import and @embed and @watch")]
@wrap html.divx, p

{:.blue}#Testing @import

//TODO: if this logic is tested elsewhere, lose it from here.

@var workingtitle="Script&#32;Markdown&#32;Utility"
@var storysummary="This manual describes the *Script Markdown Utility*, its features, purpose and more. I've packed it with examples too, so hopefully after you read it, you'll know all you need to know about how to use it to create HTML documents quickly, easily and most important, efficiently. ***Enjoy!***"

@import '$/import/test_import.md'
[var.plain(t="Test @import with relative $ path")]
@import '$/import/test_import2.md'

@import '[sys.imports]/code.md'
//TODO: Remove this when it's added to code.md
@code _id="encode_smd"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd('$.t'))"\
      t="Usage: code.encode_smd.run(t=\"smd markdown to encode\")"

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

@parw *
@set dump_ns_list="var=\".*\" link=\"c|d\""
[var.testavdoc.end]
