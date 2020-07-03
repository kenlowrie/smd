[link.imports]
[wrap_h.chapter(t="## Importing files")]

In this chapter, we will cover three different keywords used in [smd.b]:

[ulistplain.wc_open]
[smdimport.b] - Used to import markdown files
[smdembed.b] - Used to embed files directly into the output stream
[smdwatch.b] - Used to manually add a file to the watch list
[ulistplain.wc_close]

The most often used of these keywords is [smdimport.b]. It begins during [smd.b] startup, when it is used to import the builtins, and continues throughout processing depending on the complexity of your markdown documents.

A few things that are import to keep in mind when using [smdimport.b]:

[ulist.wc_open]
Any given file will only be [smdimport.b]'ed one time. Subsequent attempts are ignored.
These files can and usually do contain markdown
They can be nested to any level
[smdwrap.b] tags used within any imported file are automatically cleared when EOF is reached on the imported file.
If a path begins with '$' or '$/', they are replaced with the path of the currently opened file; this allows relative importing of dependencies.
[olist.wc_close]

//[docthis.open(h="Add this to import-doc.md")]
//[docthis.close]

Here are some examples of [smdimport.b]:
[var.terminal2.wc_open(t="Example [smdimport.il] statements")]
    [var.terminal2.wc_open_content]
        @wrap code
            [sp4]@import "filename"
            [sp4]@import "/abs/path/to/filename"
            [sp4]@import "../relative/path/to/filename"
            [sp4]@import "$/relative/to/current/filename"
        @parw
    [var.terminal2.wc_close_content]
[var.terminal2.wc_close]

The [smdimport.b] statement can be used to include documents that contain commonly used contents for your scripts, such as common aliases, links, headers, sections, etc. You can use fully qualified paths, relative paths, or paths based on the current file being processed. The latter uses the symbol '$' to designate that the path to this file should begin with the path the current file being processed. For example, assume the current file being processed is: /mydir/myfile.md. The statement:

[var.terminal(t="[smdimport.il] \"$/vars.md\"")]

Would be the same as writing **@import "/mydir/vars.md"**. This is useful because it doesn't require that you use absolute paths for everything. The path can be specified as either **'$/path/filename'** or **'$path/filename'**. In other words, you can specify the '/' after '$' or leave it off, whatever your preference is.


[plain(t="{:.blue}Testing @embed")]
.@embed "this file doesn't exist"

[code.encode_smd(t="@import \"in/import/test_embed.md - 1st Time as @import\"")][b]

.@import "$/import/test_embed.md"
The reasoning behind @importing it first is because you can only @import once, but you can @embed as many times as you want. However, once you @embed, it shows up on the list of "seen" files by the tracker, so @import will fail. I am not sure if I want to change that behavior, since technically, @embed code would not likely be a candidate for @importing anyway...
[wrap_h.hash1]
[wrap_h(t="### 1st @embed of in/import/test_embed.md")]
[code.encode_smd(t="@embed \"in/import/test_embed.md - 1st Time\"")][b]
.@embed "in/import/test_embed.md"
[wrap_h(t="### 2nd @embed of in/import/test_embed.md")]
[code.encode_smd(t="@embed \"in/import/test_embed.md - 2nd Time\"")][b]
.@embed "in/import/test_embed.md"

[plain(t="{:.blue}Testing @watch")]

// Get a list of everything we've seen so far.
//@dump tracked="."

This next file doesn't exist. Should get a warning from @watch...
// Add something that doesn't exist. Will display warning in output file.
.@watch "this file doesn't exist"

// This is already there, try to watch it again - This is considered OK. Does not display warning.
//@dump tracked=".*/test_embed.md"
.@watch "in/import/test_embed.md"
//@dump tracked=".*/test_embed.md"

// Make sure stop.md is not currently watchec, then add it, then check to see if it's being watched.
//@dump tracked=".*/stop.md"
.@watch "in/stop.md"
//@dump tracked=".*/stop.md"
