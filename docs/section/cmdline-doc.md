[link.ug_cmdline]
[wrap_h.chapter(t="## smd command line parameters")]

Before diving into the command line parameters of [smd.b], [smdparse.b] and [ismd.b], we need to establish some context. 

In order to do that, we will start by providing an overview of the repository layout, followed by a discussion of the major components, and finally the startup & shutdown processes of the primary command line interfaces. This will establish enough background information about [smd.b] that the discussion on the command line parameters will make more sense.

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

[wrap_h.section(t="### major components of [smd]")]

The major components consist of three (3) command line interfaces.

[olist.wc_open]
[smd.b] - The [smd.short] command line interface
[smdparse.b] - The [smdparse.short] command line interface
[ismd.b] - The [ismd.short] command line interface[html.ol.>]
[olist.wc_close]

[smd.b] is the main command line interface, and the one that you can use to experiment with this language. If you have installed [smd], go ahead and try it by entering the following command in a terminal window:

[terminal(t="$ smd -nd")]

At this point, your terminal window is waiting for input. Type **Hello, world** and press the **Return [DC.return]** key on your keyboard.

[terminal(t="$ smd -nd[b]Hello, world[DC.return][b]Hello, world[b][DC.ctrl]D")]

When you typed **Hello, world**, the parser simply echoed that input back to you. Congratulations, you have just created your first [smd.b] document! 

To close [smd.b], type **CTRL-D ([DC.ctrl]D)** (yes, macOS users, that's **CTRL-D** and not **CMD-D ([DC.cmd]D)**). **CTRL-D** will send an EOF signal on the stdin input stream, which will cause [smd.b] to perform an orderly shutdown. 

You can also terminate [smd.b] by pressing **CTRL-C ([DC.ctrl]C)**, however that results in the **SIG-INT** signal being sent, which will cause an unorderly shutdown (i.e. none of the closing tags will be written, etc.)

[smdparse.b] is a higher level command line interface that sits atop [smd.b]. It imports the direct [smd] entry point, so it's using the exact same underlying code to parse your documents, however, it adds several useful options for automation. It also provides the foundation for the final major component, [ismd.b].

[ismd.b] is an **interactive** version of [smd.b] that provides several different methods for viewing the output from [smd.b]. What's unique about it is that it monitors **all** of the underlying files that are processed by [smd.b] for changes, and when it detects a change, it automatically parses the document again, and updates the output monitors. 

There are several different monitors currently supported by [ismd.b]: **chrome** (the default), which displays the output in a Chrome browser window; **firefox** and **safari**, which display the output in Firefox and Safari, respectively; **hostgui**, which displays the raw HTML output in a host window and finally **endpoint**, which creates an HTTP endpoint on the localhost that can be opened by any web browser.

[link.ug_setup._null_(_qtext="Setup Chapter")]
[note(t="NOTE: The browser monitors all require additional setup before they will work. Be sure to review the [link.ug_setup._qlink] for the information on installing **selenium** and the **web drivers** before trying to use them with [ismd.b]")]

Both [smdparse.b] and [ismd.b] will be covered later in this chapter when we review the specific command line parameters.

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

[wrap_h.section(t="## smd command line parameters")]

The command line parameters for [smd.b] are:

[terminal.wc_open(t="smd command line parameters")]
[sp]
usage: smd [-h] [-f FILENAME] [-ldb | -ndb] [-lub | -nub] [-nd] [-nohtml] [-nohead] [-nobody] 
                [-html HTML_NAME] [-head HEAD_NAME] [-body BODY_NAME] [-bodyclose BODYCLOSE_NAME] 
                [-close CLOSE_NAME] [-nu] [-o [RAW_OUTPUT_FILE]]
[sp]
Parse Script Markdown text files into HTML format.
[sp]
optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME - the file that you want to parse. Default is stdin if not specified
  -ldb, --load-default-builtins - load default builtins during startup. Default is: True
  -ndb, --no-default-builtins - do not load default builtins during startup. Default is: False
  -lub, --load-user-builtins - load user builtins during startup. Default is: True
  -nub, --no-user-builtins - do not load user builtins during startup. Default is: False
  -nd, --no-document-defaults - do not load any document defaults during startup. Default is: False
  -nohtml, --no-default-html - do not load default html during startup. Default is: False
  -nohead, --no-default-head - do not load default head during startup. Default is: False
  -nobody, --no-default-body - do not load default body during startup. Default is: False
  -html HTML_NAME, --set-html-name HTML_NAME - set filename of document html markdown. Default is: None
  -head HEAD_NAME, --set-head-name HEAD_NAME - set filename of document head markdown. Default is: None
  -body BODY_NAME, --set-body-name BODY_NAME - set filename of document body markdown. Default is: None
  -bodyclose BODYCLOSE_NAME, --set-bodyclose-name BODYCLOSE_NAME - set filename of document body close markdown. Default is: None
  -close CLOSE_NAME, --set-close-name CLOSE_NAME - set filename of document close markdown. Default is: None
  -nu, --no-user-files  do not load any files from ~/.smd. Default is: False
  -o [RAW_OUTPUT_FILE], --output-raw-data [RAW_OUTPUT_FILE] - write the raw data to output file. Default is: None


[sp]
[terminal.wc_close]

[terminal.wc_open(t="smdparse command line parameters")]
[sp]
[smdparse.b] accepts the same parameters as [smd.b], plus these additional parameters:
[sp]
usage: smdparse [-h] -f FILENAME [-c [CSSFILELIST [CSSFILELIST ...]]] [-sph HEAD_FILE_NAME] [-i [IMPORTFILELIST [IMPORTFILELIST ...]]] [-d [PATH]] [-dbg]
                [-notid] [-ldb | -ndb] [-lub | -nub] [-nd] [-nohtml] [-nohead] [-nobody] [-html HTML_NAME] [-head HEAD_NAME] [-body BODY_NAME]
                [-bodyclose BODYCLOSE_NAME] [-close CLOSE_NAME] [-nu] [-o [RAW_OUTPUT_FILE]]
[sp]
Generate HTML file from a text file in Script Markdown format.
[sp]
optional arguments:
  -h, --help show this help message and exit
  -f FILENAME, --filename FILENAME the file that you want to parse
  -c [CSSFILELIST [CSSFILELIST ...]], --cssfile [CSSFILELIST [CSSFILELIST ...]] the CSS file you want used for the styling. Default is smd.css
  -sph HEAD_FILE_NAME, --smdparse-head-name HEAD_FILE_NAME the filename to use for the head HTML markdown. Default is smdparse_head.md
  -i [IMPORTFILELIST [IMPORTFILELIST ...]], --import [IMPORTFILELIST [IMPORTFILELIST ...]] list of file(s) to import after builtins.md loaded. Default is None
  -d [PATH], --path [PATH] the directory that you want the HTML file written to. Default is ./html
  -dbg, --debug display additional debug information. Default is: False
  -notid, --no-tid-in-output do not display the thread id in the output messages. Default is: False
[sp]
  *command line options for [smd.b] ...*
[sp]
This utility exits after parsing the input file.

[sp]
[terminal.wc_close]


[ismd.b] accepts the same parameters as [smd.b], plus these additional parameters:

[terminal.wc_open(t="ismd command line parameters")]
[sp]
usage: ismd [-h] -f FILENAME [-c [CSSFILELIST [CSSFILELIST ...]]] [-sph HEAD_FILE_NAME] [-d [PATH]] [-i [IMPORTFILELIST [IMPORTFILELIST ...]]]
            [-m MONITOR [MONITOR ...]] [-ldb | -ndb] [-lub | -nub] [-nd] [-nohtml] [-nohead] [-nobody] [-html HTML_NAME] [-head HEAD_NAME] [-body BODY_NAME]
            [-bodyclose BODYCLOSE_NAME] [-close CLOSE_NAME] [-nu] [-o [RAW_OUTPUT_FILE]]
[sp]
Generate HTML file from a text file in Script Markdown format.
[sp]
optional arguments:
  -h, --help show this help message and exit
  -f FILENAME, --filename FILENAME the file that you want to parse
  -c [CSSFILELIST [CSSFILELIST ...]], --cssfile [CSSFILELIST [CSSFILELIST ...]] the CSS file you want used for the styling. Default is smd.css
  -sph HEAD_FILE_NAME, --smdparse-head-name HEAD_FILE_NAME the filename to use for the head HTML markdown. Default is smdparse_head.md
  -d [PATH], --path [PATH] the directory that you want the HTML file written to. Default is ./html
  -i [IMPORTFILELIST [IMPORTFILELIST ...]], --import [IMPORTFILELIST [IMPORTFILELIST ...]] list of file(s) to import after builtins.md loaded. Default is None
  -m MONITOR [MONITOR ...], --monitor MONITOR [MONITOR ...] the monitor [browser, hostgui, endpoint] you want used to display changes. Default is browser
[sp]
  *command line options for [smd.b] ...*
[sp]
The program monitors changes and keeps window updated until CTRL-C is pressed.
[sp]
[terminal.wc_close]



[docthis.open(h="Add this to cmdline-doc.md")]

41. Document all the new command line switches (smd, smdparse, ismd and smdlive)


[docthis.close]
