[link.imports]
[wrap_h.chapter(t="## Importing, Embedding and Watching files")]

//[docthis.open(h="Add this to import-doc.md")]
//[docthis.close]


In this chapter, we will cover three different keywords used in [smd.b]:

[ulistplain.wc_open]
[smdimport.b] - Used to import markdown files
[smdembed.b] - Used to embed files directly into the output stream
[smdwatch.b] - Used to manually add a file to the watch list
[ulistplain.wc_close]

[wrap_h.section(t="###The [smdimport.il] keyword")]

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

[link.embed]
[wrap_h.section(t="###The [smdembed.il] keyword")]

The [smdembed.b] keyword is used to embed files directly into the output stream. It's a bit like [smdimport.b], except that the files are **not** parsed. The contents are embedded directly into the output stream. In most cases, you will use [smdembed.b] to embed HTML markdown directly into your output stream, but technically, it can be used to embed anything. Just make sure that whatever you embed is properly formatted for the context, as there isn't any way to modify it. Here are few fun facts about [smdembed.b]: 

[ulist.wc_open]
Any given file can be [smdembed.b]'ed as many times as you want.
These files usually do **not** contain [smd.b] markdown, although it's okay if they do, the content just won't be parsed...
Like [smdimport.b], [smdembed.b] files can be nested to any level
Also like [smdimport.b], [smdembed.b] supports the relative import prefix of '$' or '$/'
[olist.wc_close]

[syntax.wc_open(t="[smdembed.il] Syntax")]
[b]
[smdembed.il] [E.lb] [E.lt]escape | esc[E.gt] = "True" | "Yes" [E.rb]
[syntax.wc_close]

The [smdembed.il] keyword supports an option **escape** or **esc** that allows you to specify that the output should be encoded HTML: *[E.lt]* becomes *[E.amp]lt;*, *[E.gt]* becomes *[E.amp]gt;*, etc. This allows you to display HTML encoded files as text, otherwise the browser would interpret and render it as HTML. The default is **False**.

[var.terminal(t="**Example [smdembed.il] statements**[bb][sp4][smdembed.il] \"myembedfile.html\"[b][sp4][smdembed.il] \"myembedfile.html\" escape=\"true\"")]

[link.watch]
[wrap_h.section(t="###The [smdwatch.il] keyword")]

[smdwatch.b] isn't used very often, since most files that are either imported, embedded or otherwise handled via one of the command line interfaces are automatically added to the watch list.

[wrap_h.subsect(t="###What is the watch list?")]

The watch list is simply a list of all the files that the [smd.b] parser has encountered while performing markdown on your content. The higher level command line utilities such as [smdparse.b] and [ismd.b] also add files to the watch list, but for the most part, it's the underlying [smd.b] parser that is responsible for keeping track. 

Interestingly enough, as far as [smd.b] is concerned, the watch list isn't very important. It doesn't act on it in any way, but it's useful for other programs and utilities, such as [ismd.b], as a way to detect changes occurring to files that are directly involved with the current document being processed, and act on it. In the case of [ismd.b], for example, when changes to the files that make up a document are detected, it will invoke the parser again to refresh the content, and then notify all the output monitors that they need to update their output windows. This is extremely useful while developing new content, because it gives you a sort of WYSIWYG always updating view of the changes as you make them!

So why do we need [smdwatch.b] then? I mean, if [smd.b] and other command line utilities already track everything, why do I need it? Good question, grasshopper. The most common reason ties back to the [smdembed.b] command. Since the content of embedded files is not parsed or scanned in any way, there isn't a way for the parser to know if that content references something that needs to be monitored. Enter [smdwatch.b]. Using this keyword, you can add files to the watch list, and then if they are changed, and one of the underlying utilities that monitors the watch list detects it, it will reparse the content and update the output monitors. Pretty cool, huh?

The usage is simple, identical to [smdembed.b] as a matter of fact (except that the **escape** option isn't supported -- nor does it make sense here):

[var.terminal(t="**Example [smdwatch.il] statement**[bb][sp4][smdwatch.il] \"mywatchfile.html\"")]

You can use the [smddump.b] keyword with option **tracked=** to review the files that are currently being watched. This is a good way to just make sure that your watch command is working as expected during the creation process. For example, let's say you [smdembed.b] the file "myscript.html" which includes a [e_tag.b(t="script")] tag that references **myjavascript.js**. We could make sure that our [smdwatch.b] markdown is correct by using the following markdown:

[fatmargin._open]
[var.source.wc_open(t="Debug hack for making sure my [smdwatch.il] file is monitored")]
[bb]
[smdcomment.il] first let's dump the embed file inline escaped[b]
**[smdembed.il] '$/../import/myscript.html' escape="true"[b]**
@embed '$/../import/myscript.html' escape="true"
[bb]
[smdcomment.il] now embed it again, but this time don't escape it[b]
**[smdembed.il] '$/../import/myscript.html'[b]**
@embed '$/../import/myscript.html'
[b]
[smdcomment.il] now let's see which files are being watched[b]
**[smddump.il] tracked=".*(myjavascript.js|myscript.html)"**
@dump tracked=".*(myjavascript.js|myscript.html)"
[b]
[smdcomment.il] okay, so only the *myscript.html* was picked up, as expected. Let's add a watch for the JS file...[b]
**[smdwatch.il] '$/../import/myjavascipt.js'**
@watch "$/../import/myjavascript.js"
[bb]
[smdcomment.il] Let's check again to see what's being monitored...[b]
**[smddump.il] tracked=".*(myjavascript.js|myscript.html)"**
@dump tracked=".*(myjavascript.js|myscript.html)"
[b]
[smdcomment.il] Cool! Now both files are being watched ...[b]
[var.source.wc_close]
[fatmargin._close]

When you review the preceding section in the docs, you will notice a lot more than is actually needed in practice. This is because I wanted to show the steps and the actual content to help you understand all the steps. In reality, all you needed was:

[terminal.wc_open(t="Just the needed steps for the debug hack...")]
[smdembed.b] 'path/to/myscript.html'
[smdwatch.b] 'path/to/myjavascript.js'
[smddump.b] tracked=".*(myjavascript.js|myscript.html)"
[terminal.wc_close]

[wrap_h.section(t="###Summary of [smdimport.il], [smdembed.il] and [smdwatch.il]")]

That wraps up the section on importing, embedding and watching files. Onward!
