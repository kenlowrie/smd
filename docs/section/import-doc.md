[link.imports]
[wrap_h(t="## Importing documents")]

Content about what TEMPLATE IS USED FOR.

[docthis.open(h="Add this to import-doc.md")]

8. Document the @embed "filename" support.
40. DOCS: @import "[sys.imports]/def_head.md" twice in a row only works the first time. Intentional. stream().open()
Explain how @import '$' works when no files open i.e. reading from stdin



[docthis.close]






{:.syntax}@@@ divTitle Syntax:
    {:.indent}**@import "filename"**
    {:.indent}**@import "/abs/path/to/filename"**
    {:.indent}**@import "../relative/path/to/filename"**
    {:.indent}**@import "$/relative/to/current/filename"**

The @import statement can be used to include documents that contain commonly used contents for your scripts, such as common aliases, links, headers, sections, etc. You can use fully qualified paths, relative paths, or paths based on the current file being processed. The latter uses the symbol '$' to designate that the path to this file should begin with the path the current file being processed. For example, assume the current file being processed is: /mydir/myfile.md. The statement:

### @import "$/vars.md"

Would be the same as writing **@import "/mydir/vars.md"**. This is useful because it doesn't require that you use absolute paths for everything.

{:.note.blue.indent4}There is a gotcha when using this with BBEdit's Markup Preview. There is no context for the top level file, since it is passed to the Python script as sys.stdin. Because of that, you can't rely on avscript_md to determine the relative path of the top level file. It will work just fine when using mkavscript_md, but that won't be useful if you are using BBEdit's Markup Preview to write your documents...

The path can be specified as either **'$/path/filename'** or **'$path/filename'**. In other words, you can specify the '/' after '$' or leave it off, whatever your preference is.

