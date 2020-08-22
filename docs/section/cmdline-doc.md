[link.ug_package]
[wrap_h.chapter(t="## smd Package")]

Before diving into the primary interfaces of the [smd.b] package, let's establish a little context first. 

[box(t="This chapter assumes you have successfully installed [smd.b] using one of the methods documented in the previous chapter.")]

We will start by providing an overview of the repository layout, followed by a discussion of the primary command line utilities, and finally the startup & shutdown processes of the primary command line interfaces. This will establish enough background information about [smd.b] that the discussion on the command line parameters will make more sense.

[link.ug_cl_repo_layout]
[wrap_h.section(t="### Repository Layout")]

@var _="DC" vb="&boxvr;" ra="&rtrif;" rd="&dashv;" bh="&boxh;" v="&boxv;" lc="&boxur;" return="&crarr;" cmd="&#8984;" option="&#8997;" alt="{{self.option}}" ctrl="&#8963;"\
            bh2a="{{self.sp2}}{{self.vb}}"\
            bh2ax="{{self.sp2}}{{self.lc}}"\
            bh3a="{{self.sp2}}{{self.bh2a}}"\
            bh3ax="{{self.sp2}}{{self.bh2ax}}"\
            bh4a="{{self.sp2}}{{self.bh3a}}"\
            bh4ax="{{self.sp2}}{{self.bh3ax}}"\
            sp="[sp][sp]" sp2="{{self.sp}}{{self.sp}}"\
            eol="[b][DC.sp][DC.v]"\
            1="{{self.sp}}{{self.vb}}{{self.bh}}{{self.ra}}{{sp}}"\
            1z="{{self.sp}}{{self.lc}}{{self.bh}}{{self.ra}}{{sp}}"\
            2a="{{self.sp}}{{self.v}}{{self.bh2a}}{{self.ra}}{{sp}}"\
            2z="{{self.sp}}{{self.v}}{{self.bh2ax}}{{self.ra}}{{sp}}"\
            2b="{{self.sp}}[sp]{{self.bh2a}}{{self.ra}}{{sp}}"\
            2bz="{{self.sp}}[sp]{{self.bh2ax}}{{self.ra}}{{sp}}"\
            3a="{{self.sp}}{{self.v}}{{self.bh3a}}{{self.ra}}{{sp}}"\
            3z="{{self.sp}}{{self.v}}{{self.bh3ax}}{{self.ra}}{{sp}}"\
            4a="{{self.sp}}{{self.v}}{{self.bh4a}}{{self.ra}}{{sp}}"\
            4z="{{self.sp}}{{self.v}}{{self.bh4ax}}{{self.ra}}{{sp}}"\
            9="{{self.sp}}{{self.lc}}{{self.bh2}}{{self.ra}}{{sp}}"

[terminal.wc_open(t="[smd] repository structure")]
[sp]
[e_us(t="root")]
[DC.1]debug - Python scripts used for debugging [smd.b], [smdparse.b] and [ismd.b]
[DC.2a]debug.py - Python script used for debugging [smd.b]
[DC.2a]debug-1.py - Python script used for debugging [smdparse.b]
[DC.2z]debug-2.py - Python script used for debugging [ismd.b][DC.eol]
[DC.1][e_us(t="docs")] - user guide, etc.
[DC.2a]export - a rendered version of the user documentation in HTML format
[DC.2a]import - imports used by the documentation
[DC.2a]section - chapters that make up the user documentation
[DC.2z]userdocs.md - the top level user documentation file
[DC.3z]**Parsed using *[smdparse] -f userdocs.md -c -d export* to create *docs/export/userdocs.html*** [DC.eol]
[DC.1][e_us(t="samples")] - example [smd.b] files
[DC.2z][e_us(t="obs")] - sample OBS Studio files
[DC.3a]clock - displays an updating digital clock via an OBS Browser link
[DC.3z]border - displays an opaque border via an OBS Browser link[DC.eol]
[DC.1][e_us(t="smd")] - Python [smb.b] package root
[DC.2a]smd.py - [smd.short_b] command line interface
[DC.2a]smdparse.py - [smdparse.short_b] command line interface
[DC.2a]ismd.py - [ismd.short_b] command line interface
[DC.2a]core - [smb.b] classes
[DC.2a]css - default CSS files
[DC.2z][e_us(t="import")] - [smd.b] built-ins
[DC.3a]avs - [smd.b] AV script built-ins
[DC.3a]def_html.md - default HTML open tags
[DC.3a]def_head.md - default HEAD open tags
[DC.3a]def_body.md - default BODY open tags
[DC.3a]def_bodyclose.md - default BODY closing tags
[DC.3a]def_close.md - default HTML closing tags
[DC.3z][e_us(t="builtins.md")] - main system builtins file
[DC.4a]common.md - generic builtins
[DC.4a]defaults.md - default values used in def_[E.ast].md files
[DC.4a]code.md - @code namespace builtins
[DC.4a]html.md - @html namespace builtins
[DC.4z]link.md - @link namespace builtins[DC.eol]
[DC.1]src - Miscellaneous Python Source files[DC.eol]
[DC.1z][e_us(t="tests")] - Unit tests for [smd.b]
[DC.2b]cmdline - Command Line Parameter unit tests
[DC.2b]in - individual unit test input files
[DC.2b]out - individual unit test master files (expected output)
[DC.2b]test.py - [smd.b] unittest command line interface (i.e. unit test runner)
[DC.2b]testdbg.sh - bash script that starts an interactive [smd.b] session on a unit test
[DC.2bz]test2dbg.sh - starts an interactive [smd.b] session with both chrome and hostgui windows
[sp]
[terminal.wc_close]

[link.ug_cl_components]
[wrap_h.section(t="### Primary components of [smd]")]

The primary components of [smd.b] consist of three (3) command line interfaces.

[olist.wc_open]
    [smd.b] - The [smd.short] command line interface
    [smdparse.b] - The [smdparse.short] command line interface
    [ismd.b] - The [ismd.short] command line interface[html.ol.>]
[olist.wc_close]

[box(t="NOTE: If you used [pipenv] to install [smd.b], be sure to either activate the virtual environment by typing **pipenv shell** or alternatively, type **pipenv run** in front of each [smd.b] command in the following examples.")]

[wrap_h.subsect(t="#### [smd] command line interface")]

[smd.b] is the main command line interface, and the one that you can use to experiment with this language. Since you have successfully installed [smd], go ahead and try it by entering the following command in a terminal window:

[terminal(t="$ smd -nd")]

At this point, your terminal window is waiting for input. Type **Hello, world** and press the **Return [DC.return]** key on your keyboard.

[terminal(t="$ smd -nd[b]Hello, world[DC.return][b]Hello, world[b][DC.ctrl]D")]

When you typed **Hello, world**, the parser simply echoed that input back to you. Congratulations, you have just created your first [smd.b] document! 

To close [smd.b], type **CTRL-D ([DC.ctrl]D)** (yes, macOS users, that's **CTRL-D** and not **CMD-D ([DC.cmd]D)**). **CTRL-D** will send an EOF signal on the stdin input stream, which will cause [smd.b] to perform an orderly shutdown. 

You can also terminate [smd.b] by pressing **CTRL-C ([DC.ctrl]C)**, however that results in the **SIG-INT** signal being sent, which will cause an unorderly shutdown (i.e. none of the closing tags will be written, etc.)

[wrap_h.subsect(t="#### [smdparse] command line interface")]

[smdparse.b] is a higher level command line interface that sits atop [smd.b]. It imports the direct [smd] entry point, so it's using the exact same underlying code to parse your documents, however, it adds several useful options for automation. It also provides the foundation for the final major component, [ismd.b].

Let's parse the **samples/hello/hello.md** sample file next using [smdparse.b]:

[terminal(t="$ cd samples/hello[b]$ smdparse -f hello.md -c[b]$ open html/hello.html")]

The **open html/hello.html** command opened the generated **hello.html** file in your default browser so you can review it. Close the browser window when you are done.

[wrap_h.subsect(t="#### [ismd] command line interface")]

[ismd.b] is an **interactive** version of [smd.b] that provides several different methods for viewing the output from [smd.b]. What's unique about it is that it monitors **all** of the underlying files that are processed by [smd.b] for changes, and when it detects a change, it automatically parses the document again, and updates the output monitors. 

There are several different monitors currently supported by [ismd.b]: **chrome** (the default), which displays the output in a Chrome browser window; **firefox** and **safari**, which display the output in Firefox and Safari, respectively; **hostgui**, which displays the raw HTML output in a host window and finally **endpoint**, which creates an HTTP endpoint on the localhost that can be opened by any web browser.

[link.ug_setup._null_(_qtext="Setup Chapter")]
[note(t="NOTE: The **hostgui** monitor requires that your version of Python was compiled with the **Tk [E.lp]tkinter[E.rp]** support, and the browser monitors all require an additional webdriver before they will work. Be sure to review the [link.ug_setup._qlink] for the required information for using any of the [ismd.b] monitors.")]

Let's go ahead and parse the **samples/hello/hello.md** sample file next using [ismd.b] with the **hostgui** monitor:

[terminal(t="$ cd samples/hello[b]$ ismd -f hello.md -c -m hostgui")]

When you execute the [ismd.b] command, it will parse **hello.md**, then create a **Tk** window where it will display the contents of the parsed file. It will continue to monitor all files that are parsed to generate **hello.md**, and if any of them change, it will parse again and update the **hostgui** window. Experiment with that now, by changing the contents of **hello.md**, and saving it. You should see the window update with the new content each time you make a change and save the document. Here is what it looks like when you first run it:

The terminal window:

[IMG_SIZE.large]
@image _="ss_ismd_terminal" src="[sys.root]/docs/import/ss_ismd_terminal.png" style="[IMG_STYLE.inline_border]"
[ss_ismd_terminal]

The **hostgui** window:

[IMG_SIZE.large]
@image _="ss_ismd_hostgui" src="[sys.root]/docs/import/ss_ismd_hostgui.png" style="[IMG_STYLE.inline_border]"
[ss_ismd_hostgui]

When you are done, be sure to type **CTRL-C** in the terminal window to terminate [ismd.b].

Both [smdparse.b] and [ismd.b] and their command line options will be covered in more detail later in this chapter.

[link.ug_cl_startup]
[wrap_h.section(t="### [smd] startup & shutdown overview")]

The following provides a high-level overview of the startup of [smd.b]. This is the basic flow when no command line parameters are passed to [smd.b].

@html _="smallprint" _inherit="p" style="font-size: .8em;margin:-1.5em;padding:2em;"

[bmgreybg._open]
[var.source.wc_open(t="High level overview of startup")]

[olist.wc_open]
    import builtins.md - which imports several other modules
    @@[olistAlpha.<]
        import defaults.md
        import common.md
        import code.md
        import link.md
        import html.md
    @@[olistAlpha.>]
    import opening body markup
    @@[olistAlpha.<]
        import def_html.md
        import def_head.md
        import def_body.md
    @@[olistAlpha.>]

    @@[divx.<]
    @wrap smallprint
        *[smdcomment.il] command prompt for interactive input unless -f filename or [E.lt] filename (redirection from shell)*[b]*[smdcomment.il] [e_tag(t="CTRL-D")] ends the input **(or EOF if -f filename or [E.lt] filename (redirection from shell))***
    @parw
    @@[divx.>]

    import closing body markup
    @@[olistAlpha.<]
        import def_bodyclose.md
        import def_close.md
    @@[olistAlpha.>]

[olist.wc_close]

[var.source.wc_close]
[bmgreybg._close]

By reviewing the startup process, you can see that a number of the built in markdown files are preloaded when [smd.b] is started (assuming you did not pass any command line switches preventing that behavior). In addition, the default HTML markup files are loaded and dumped to the output stream, before it begins processing your input (either from the keyboard i.e. **stdin**, or from a file if **-f** or shell redirection is used). Once EOF is reached on the input stream, the remaining HTML markup files are read and dumped to the output stream, before it cleans up and performs an orderly shutdown.

Okay, now that we've provided enough context, let's take a look at the command line parameters for each of the major [smd.b] components.

[link.ug_cl_smd]
[wrap_h.section(t="### smd command line parameters")]

The primary command line interface to [smd.b] is the Python module **smd.py**. This module contains the code to parse script markdown text files into HTML format. The command line parameters for [smd.b] are:

[terminal.wc_open(t="[smd] command line parameters")]
    [sp.4][-h] 
    [sp.4][-f FILENAME] 
    [sp.4][-ldb | -ndb] 
    [sp.4][-lub | -nub] 
    [sp.4][-nd] [-nohtml] [-nohead] [-nobody] 
    [sp.4][-html HTML_NAME] 
    [sp.4][-head HEAD_NAME] 
    [sp.4][-body BODY_NAME] 
    [sp.4][-bodyclose BODYCLOSE_NAME]
    [sp.4][-close CLOSE_NAME] 
    [sp.4][-nu] 
    [sp.4][-o [RAW_OUTPUT_FILE]]
    [sp]
[terminal.wc_close]

@var SYM="{{_public_keys_}}" \
          redir_stdin="{{big.120p(t=\"[E.lt]\" cls=\".red.bold\")}}"\
          pipe="{{big.120p(t=\"|\" cls=\".red.bold\")}}"

[wrap_h.subsect(t="#### General Parameters")]
[html.td_desc._null_(_align="left")]
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item=" -h[b]--help" desc="show help message and exit")]
        [table_2col.row_alt(item=" -f FILENAME[b]--filename FILENAME" desc="the FILENAME that you want to parse. Default is **stdin** if not specified.[bb]You can also redirect [SYM.redir_stdin] or pipe [SYM.pipe] the **stdin** stream when using [smd.b] in scripts.")]
        [table_2col.row_alt(item="-o [FILENAME][b]--output-raw-data [FILENAME]" desc="write the raw data to output file. Default is: **None**. [bb]This is useful in certain debug situations to determine how far you are getting before encountering an issue. If you do not specify the FILENAME, it will default to **smd_rawdata.out**.[bb]This option writes out each input line read and returned to the main loop starting with the declaration of the **sys** variable and the importing of **builtins.md** then continuing with the processing of the input stream.")]
        [table_2col.row_alt(item="-nu[b]--no-user-files" desc="do not load any files from ***~/.smd***. Default is: **False**.[bb]Both the **builtins** and **document defaults** support the ability to override the system provided versions with user versions that are in the logged in user's home directory. This switch, when specified, prevents [smd.b] from loading any user-provided overrides.")]
    [table_2col.close]
[bigmargin._close]

[wrap_h.subsect(t="#### Builtin Parameters")]

The *builtin parameters* control whether or not [smd.b] will process the default builtins stored in **builtins.md** during startup. There are potentially two sets of builtins that can be loaded, the system version located in **[E.lb]sys.imports[E.rb]/builtins.md** and the optional user version located in **[E.lb]user.imports[E.rb]/builtins.md**. The following command line parameters control how the system will process them.

[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item="-ldb[b]--load-default-builtins" desc="load default builtins during startup. Default is: **True**.[bb]This switch and it's counterpart **-ndb**, **--no-default-builtins** control whether or not [smd.b] will load **[E.lb]sys.imports[E.rb]/builtins.md** during startup. Specify one or the other, but not both.")]
        [table_2col.row_alt(item="-ndb[b]--no-default-builtins" desc="do not load default builtins during startup. Default is: **False**.[bb]See **-ldb**, **--load-default-builtins** for additional information.")]
        [table_2col.row_alt(item="-lub[b]--load-user-builtins" desc="load user builtins during startup. Default is: **True**.[bb]This switch and it's counterpart **-nub**, **--no-user-builtins** control whether or not [smd.b] will load **[E.lb]user.imports[E.rb]/builtins.md** during startup. Specify one or the other, but not both. Also note that [smd.b] will load the system builtins file first, and then the user builtins, which gives you the ability to override specific system builtins by simply redefining them during startup.")]
        [table_2col.row_alt(item="-nub[b]--no-user-builtins" desc="do not load user builtins during startup. Default is: **False**.[bb]See **-lub**, **--load-user-builtins** for additional information.")]
    [table_2col.close]
[bigmargin._close]

[wrap_h.subsect(t="#### Document Default Parameters")]
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item="-nd[b]--no-document-defaults" desc="do not load any document defaults during startup. Default is: **False**.[bb]This switch is a shorthand method of specifying **-nohtml**, **-nohead** and **-nobody** all at once. In addition, it is mutually exclusive to **-html**, **-head**, **-body**, **-bodyclose** and **-close**, so you cannot specify this along with any of those.")]
        [table_2col.row_alt(item="-nohtml[b]--no-default-html" desc="do not load default html during startup. Default is: **False**.[bb]This switch will prevent [smd.b] from loading and emitting the default document markup in **def_html.md** during startup and **def_close.md** during shutdown.[bb]Also note that precedence is given to **[E.lb]user.imports[E.rb]/def_html.md** if it exists, over the system provided **[E.lb]sys.imports[E.rb]/def_html.md**. By the way, this is true for all of the document defaults; that is, if a **user** provided version exists, it will have precedence over any **system** provided version.")]
        [table_2col.row_alt(item="-nohead[b]--no-default-head" desc="do not load default head during startup. Default is: **False**[bb]This switch will prevent [smd.b] from loading and emitting the default head markup in **def_head.md** during startup.")]
        [table_2col.row_alt(item="-nobody[b]--no-default-body" desc="do not load default body during startup. Default is: **False**[bb]This switch will prevent [smd.b] from loading and emitting the default body markup in **def_body.md** during startup and **def_bodyclose.md** during shutdown.")]
        [table_2col.row_alt(item="-html FILENAME[b]--set-html-name FILENAME" desc="set filename of document html markdown. Default is: **None**.[bb]This option allows you to specify the filename that will be used to load the default document markup that is normally contained in **def_html.md**.")]
        [table_2col.row_alt(item="-head FILENAME[b]--set-head-name FILENAME" desc="set filename of document head markdown. Default is: **None**.[bb]This option allows you to specify the filename that will be used to load the default head markup that is normally contained in **def_head.md**.")]
        [table_2col.row_alt(item="-body FILENAME[b]--set-body-name FILENAME" desc="set filename of document body markdown. Default is: **None**.[bb]This option allows you to specify the filename that will be used to load the default body markup that is normally contained in **def_body.md**.")]
        [table_2col.row_alt(item="-bodyclose FILENAME[b]--set-bodyclose-name FILENAME" desc="set filename of document body close markdown. Default is: **None**.[bb]This option allows you to specify the filename that will be used to load the default body close markup that is normally contained in **def_bodyclose.md**.")]
        [table_2col.row_alt(item="-close FILENAME[b]--set-close-name FILENAME" desc="set filename of document close markdown. Default is: **None**.[bb]This option allows you to specify the filename that will be used to load the default closing markup that is normally contained in **def_close.md**.")]
    [table_2col.close]
[bigmargin._close]

[wrap_h.subsect(t="#### Common Use Cases")]

Typically, you will use [smd.b] to interactively learn the [smd.short] syntax and semantics. Although you could technically use it to parse entire documents, it does not contain support for handling the CSS file(s), so you would have to account for that separately. It is easier to use [smdparse.b] or [ismd.b] for that, since they both handle the CSS files, and are intended for use in automation and scripting tasks.

Here are a few common use cases for [smd.b]:

[terminal.wc_open(t="Common use cases for [smd.b]")]
    [sp]
    *[smdcomment.il] Start the parser in interactive mode, do not load the document defaults*
    $ smd -nd
    [sp]
    *[smdcomment.il] Parse the file **samples/hello/hello.md***
    $ smd -f samples/hello/hello.md
    [sp]
    *[smdcomment.il] Same as the first example above i.e. **smd -nd***
    $ smd -nohtml -nohead -nobody
[terminal.wc_close]

[link.ug_cl_smdparse]
[wrap_h.section(t="### [smdparse] command line parameters")]

The [smdparse.b] command line interface is in the Python module **smdparse.py**. This module contains the code to generate an HTML file from a text file written in script markdown ([smd.b]) format. [smdparse.b] utility exits after parsing the input file.

[smdparse.b] accepts the same parameters as [smd.b], plus a few additional parameters useful for scripting and automation (the most common use case for [smdparse.b]):

[terminal.wc_open(t="[smdparse] command line parameters")]
    [sp.4][-h] 
    [sp.4]-f FILENAME 
    [sp.4][-c [CSSFILELIST [CSSFILELIST ...]]] 
    [sp.4][-d [PATH]] 
    [sp.4][-i [IMPORTFILELIST [IMPORTFILELIST ...]]] 
    [sp.4][-sph HEAD_FILE_NAME] 
    [sp.4][-dbg] 
    [sp.4][-notid]
    [sp]
    [sp.4]*Plus all the options supported by [smd]*
    [sp]
[terminal.wc_close]

[wrap_h.subsect(t="#### [smdparse] Common Parameters")]
This first group of options applies to both [smdparse.b] and [ismd.b].

[html.td_desc._null_(_align="left")]
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item=" -h[b]--help" desc="show help message and exit")]
        [table_2col.row_alt(item=" -f FILENAME[b]--filename FILENAME" desc="the FILENAME that you want to parse. Unlike [smd.b], there is no default, this parameter must be specified.")]
        [table_2col.row_alt(item="-c [FILE1 [FILE2 ...]][b]--cssfile [FILE1 [FILE2 ...]]" desc="the CSS file[E.lp]s[E.rp] you want used for the styling. If you specify **-c** by itself, the default CSS file **smd.css** will be used, and it will also be copied to the output directory **-d**. Otherwise, you can specify one or more CSS files, and each of them will be copied to the output directory, and a **link** tag will be added for each in the **[E.lt]head[E.gt]** section of the generated HTML output.")]
        [table_2col.row_alt(item="-d [PATH][b]--path [PATH]" desc="the directory that you want the HTML file written to. If you either do not specify this option, or if you specify **-d** by itself, the default output directory will be **./html**, otherwise, the specified **PATH** will be used. Also, if the output directory does not exist, it will be created.")]
        [table_2col.row_alt(item="-i [FILE1 [FILE2 ...]][b]--import [FILE1 [FILE2 ...]]" desc="list of file(s) to import after **builtins.md** loaded. If you specify **-i** without a filename, then *import_**--filename*** will be used. For example .... Default loaded. Default is **None**. If **-i/--import** is specified without a filename, ")]
        [table_2col.row_alt(item="-sph FILENAME[b]--smdparse-head-name FILENAME" desc="the filename to use for the head HTML markdown. Default is **smdparse_head.md**")]
    [table_2col.close]
[bigmargin._close]

[wrap_h.subsect(t="#### [smdparse]-Only Parameters")]
These options are specific to [smdparse.b].
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item="-dbg[b]--debug" desc="display additional debug information. Default is: **False**.[bb]This option will cause [smdparse.b] to dump the **ScriptParser** object instance variables as well as the **SystemDefaults** object instance variables, either or both of which you might find helpful when debugging script processing.")]
        [table_2col.row_alt(item="-notid[b]--no-tid-in-output" desc="do not display the thread id in the output messages. Default is: **False**.[bb]This option is used during the unit testing of [smdparse.b] to prevent the thread ID from being output in log messages, making it easier to validate the output against expected results. Most likely you won't use this option, unless you are unit testing changes made to [smdparse.b].")]
    [table_2col.close]
[bigmargin._close]

[wrap_h.subsect(t="#### Common Use Cases")]

Here are a few common use cases for [smdparse.b].

[terminal.wc_open(t="Common use cases for [smdparse]")]
    [sp]
    *[smdcomment.il] Parse samples/hello/hello.md write to ./html directory*
    $ smdparse -f samples/hello/hello.md
    [sp]
    *[smdcomment.il] Parse **samples/hello/hello.md**, include default CSS file in output folder*
    $ smdparse -c -f samples/hello/hello.md
    [sp]
    *[smdcomment.il] Parse **samples/hello/hello.md**, include default CSS file, export to **export** folder*
    $ smdparse -c -f samples/hello/hello.md -d export
[terminal.wc_close]


[link.ug_cl_ismd]
[wrap_h.section(t="### [ismd] command line parameters")]

[ismd.b] is an interactive version of [smd.b] that monitors all of the files that were processed when the specified input file is parsed, and whenever changes are made to any of them, it will re-parse the input file and update all of the output monitors. 

By default, [ismd.b] creates a **Google Chrome** output monitor, so you can see the results of the parse displayed in the window, and when you update & save one of the files that went into creating it, it will automatically refresh the output window. This is extremely useful when you are developing new content, as you can see the results of your changes in real-time.

[ismd.b] accepts the same parameters as [smd.b], along with the common parameters for [smdparse.b] reviewed in the previous section, plus these additional parameters:

[terminal.wc_open(t="[ismd]-specific command line parameters")]
    [sp.4][-m MONITOR [MONITOR ...]]
    [sp.4][-ipf]
    [sp]
    [sp.4]*Plus all the options supported by [smd] and the [smdparse] common options.*
    [sp]
[terminal.wc_close]


[wrap_h.subsect(t="#### [smdparse]-only Parameters")]
These options are specific to [smdparse.b].
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item="-m MONITOR [MONITOR ...][b]--monitor MONITOR [MONITOR ...]" desc="Specify the monitor [one ore more of the following: **chrome**, **safari**, **firefox**, **hostgui**, **endpoint**] you want used to display changes. The default is **chrome**.[bb]You can specify more than one output monitor, which allows you to review the ouput in any/all of the monitors you are interested in deploying on.[bb]**hostgui** is a specialized monitor that displays the raw HTML in a platform-specific window, so that you can review the actual HTML being generated by [smd.b].[bb]**endpoint** is another specialized monitor that will create an endpoint on **localhost** at the following URL:[bb][tab.<]**localhost:8080/smd/*FILEBASE*/html/*FILEBASE*.html.**[tab.>][bb]***FILEBASE*** is the basename of the filename specified in the **-f** parameter. For example, if you specified **-f path/mydoc.md -m endpoint**, then ***FILEBASE*** will be **mydoc** in the URL string.")]
        [table_2col.row_alt(item="-ipf[b]--ignore-parse-fail" desc="Ignore failure of initial parse. Default is: False.[bb]By default, when [ismd.b] encounters a failure during the initial parse, it exits with an error code. In some cases, however, you might prefer to continue on and enter the monitor loop, knowing that you will fix whatever issue is causing the failure [E.lp]assuming it's a scripting/markdown error and not an error in the Python code[E.rp]. In this case, specify the **-ipf** option, to ignore the error, and continue with the monitoring.")]
    [table_2col.close]
[bigmargin._close]

[wrap_h.subsect(t="#### Common Use Cases")]

Here are a few common use cases for [ismd.b].

[terminal.wc_open(t="Common use cases for [ismd]")]
    [sp]
    *[smdcomment.il] Parse samples/hello/hello.md and launch a Chrome monitor window*
    $ ismd -f samples/hello/hello.md
    [sp]
    *[smdcomment.il] Parse **samples/hello/hello.md**, include default CSS file, monitor using **hostgui** window*
    $ ismd -c -f samples/hello/hello.md -m hostgui
    [sp]
    *[smdcomment.il] Parse **samples/hello/hello.md**, include default CSS file, monitor with firefox and create an endpoint*
    $ ismd -c -f samples/hello/hello.md -m firefox endpoint
[terminal.wc_close]


[ismd.b] monitors changes and keeps all monitor windows updated until CTRL-C is pressed in the terminal window where you launch [ismd.b].

[wrap_h.section(t="### Summary of Command Line Parameters Chapter")]

Okay, at this point, we've covered the setup of [smd.b] and the major components that make up the package and we also discussed the various command line options for those major components. It's time to get down to business, and learn how to use [smd.b] for generating HTML content from your markdown files.

//[docthis.open(h="Add this to cmdline-doc.md")]
//[docthis.close]
