[link.ug_builtins]
[wrap_h.chapter(t="## The builtins")]

This chapter will cover the builtins that are automatically loaded (unless the -ndb and -nub command line switches are specified).

[wrap_h.section(t="### builtins.md")]
All of the system provided builtins are located [e_var.b(t="sys.imports")] directory. When [smd.b] is initializing, just before it loads the default document sections, it **@import**'s the file **builtins.md**. If you examine this file, you will see it just imports several other files:

[terminal.wc_open(t="[E.lb]**sys.imports/builtins.md**[E.rb]")]
[sp]
[E.at]import "[E.lb]sys.imports[E.rb]/defaults.md"
[E.at]import "[E.lb]sys.imports[E.rb]/common.md"
[E.at]import "[E.lb]sys.imports[E.rb]/code.md"
[E.at]import "[E.lb]sys.imports[E.rb]/link.md"
[E.at]import "[E.lb]sys.imports[E.rb]/html.md"
[terminal.wc_close]

Each of these imports, in turn, then defines things specific to the namespace they represent. Although they are technically variables, it might be easier to think of them as macros, because when they are encountered while parsing, they expand to something else. In some cases, it's just a direct text replacement, e.g. [e_var.b(t="E.ast")] expands to **[E.amp]ast;**, but in other cases, they might push several lines of other content, including [smd.b] commands onto the input stream!

If you directly examine the contents in these files, you will see how the many things that they define for you to use in your own markdown files.

[note.wc_open]
Some of the content in these files will look rather foreign at first glance, especially those in **code.md**. However, once you understand the syntax for each of the namespaces, it will become much easier to decipher these system provided builtins.
[note.wc_close]

[wrap_h.section(t="### System vs. User builtins")]

[smd.b] supports the concept of both system and user defined builtins. The system builtins are located in the [e_var.b(t="sys.basepath")]**/import** directory. User builtins, on the other hand, are located in the **~/.smd/import** directory. On Linux based operating systems (of which macOS is a derivative), the tilde [E.tilde] character refers to the base of the currently logged in user directory: **/Users/[e_tag(t="username")]**.

Whenever the system is ready to load the builtins, it will look in both places for a file named **builtins.md**. It looks in the system directory first, and once finished processing those, it then looks in the user directory (if it exists). This allows you to **override** the system defaults with your own variables.


[wrap_h.section(t="### The @var sys builtin")]

There is a special built-in in the @var namespace called sys that contains several attributes that are useful in your script markdown files.

[terminal.wc_open(t="@var sys default attributes")]
[sp]
*basepath=*The location of the [smd.b] package. This directory is where [smd.b], [smdparse.b] & [ismd.b] are stored.
*imports=*The location of the import directory. This directory is located here: [e_var.b(t="sys.basepath")]**/import**
*root=*The root of the [smd.b] installation. This directory is located here: [e_var.b(t="sys.basepath")]**/..**
*user_basepath=*The location of the user [smd] directory for the currently logged in user.
*user_imports=*The location of the user [smd] import directory for the currently logged in user.
*user_root=*The home directory for the currently logged in user.
[sp]
[terminal.wc_close]

The most commonly used of the sys attributes is import. Anytime you want to load one of the system defined import files. For example, **@import "[e_var(t="sys.imports")]/divs.md"** would import the *divs.md* markdown script.

//[docthis.open(h="Add this to builtins-doc.md")]
//[docthis.close]
