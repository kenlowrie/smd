[link.setup]
[wrap_h.chapter(t="## Setting up smd")]

There are two approaches to installing [smd.B] on your system; either using **pip** or **pipenv**. This chapter will cover both methods, and you can choose which is better for you.

[box.wc_open]
NOTE: [smd.b] requires Python 3.7.3 or later! If you are running an older version, you either have to upgrade or install a virtual environment with something newer in order to run [smd.b].
[box.wc_close]

[wrap_h.section(t="###Installing with pip")]

The easiest way to install [smd] on your system is to use the default package installer for Python or **pip**. From a terminal window on your machine, change to the root directory of your cloned repository and type:

[terminal(t="$ pip install .")]

One drawback to this method is that the package and its dependencies will be installed globally, which could interfere with other packages installed on your system. In addition to that, you

In order to minimize the number of dependencies that are installed using **pip**, two other packages that are needed by [ismd.b], namely **selenium** and **bottle**, are not automatically installed. If you will not be using [ismd.b], then there is nothing extra required. [smd.b] and [smdparse.b] will both run just fine without these additional packages. On the other hand, if you will be using [ismd.b], then you must either install these packages manually, or alternatively, you can use the **pipenv** method described next, which *will* install the extra packages. To install them manually, use these commands in your terminal window:

[terminal.wc_open(t="Install additional package dependencies")]
[sp]
$ pip install selenium
$ pip install bottle
[terminal.wc_close]

[question.wc_open]
Need to document downloading a driver for selenium.[bb]
*download from here: [escape(t="https://sites.google.com/a/chromium.org/chromedriver/downloads")]*
[question.wc_close]

You can also install the package in developer mode with the -e flag. This will point the installation of the package to the current cloned repository directory instead of copying it over to your site-packages installation directory; useful if you plan on making changes and don't want to reinstall each time you make a change. Use the following command in your terminal window to install [smd.b] in developer mode:

[terminal.wc_open(t="Install in developer mode with pip")]
[sp]
$ pip install -e .
[terminal.wc_close]

[bluenote.wc_open]
HINT: If you later decide you want to install [smd.b] in developer mode, you can issue the above command to accomplish that. If it detects that [smd.b] is already installed on your system, it will uninstall it first, and then install it in developer mode.
[bluenote.wc_close]

[wrap_h.section(t="###Installing with pipenv")]

[ln_factory(nm="pipenv" hr="https://docs.python-guide.org/dev/virtualenvs/" t="pipenv")]
@set _ns="link" _="pipenv" target="_blank"

[question.wc_open]
I think the Pipfile/Pipfile.lock belong in the root directory, like where they were before. And then pipenv gets renamed to samples...
[question.wc_close]

**[pipenv]** is a much better way to setup a virtual environment for running SMD on a local machine. Doing so prevents installing site-packages in a global manner, the way **pip** does, thus isolating [smd.b] to a private environment for use, testing and/or evaluation. The Pipfile and Pipfile.lock files are provided in the **[encode_smd(t="<sys.root>/pipenv")]** directory, which is located at the root of your cloned repository. Simply navigate to that directory on your local machine and type:

[terminal(t="$ pipenv install")]

to create the runtime environment for launching smd on your machine. Once it finishes, type:

[terminal(t="$ pipenv shell")]

And then invoke [smd.b], [smdparse.b] and/or [ismd.b] within the virtual environment that was created.

[note(t="NOTE: If you do not have [pipenv] installed on your machine, you can navigate to [pipenv._asurl] to get information on it.")]

[ln_factory(nm="tk" hr="https://tkdocs.com/tutorial/install.html" t="Tk")]
@set _ns="link" _="tk" _tkinter="{{self.<}}tkinter{{self.>}}" target="_blank"
[ln_factory(nm="activestate" hr="https://www.activestate.com/products/python/" t="ActiveState")]
@set _ns="link" _="activestate" target="_blank"
[ln_factory(nm="pyenv" hr="https://github.com/pyenv/pyenv#installation" t="pyenv")]
@set _ns="link" _="pyenv" target="_blank"
[ln_factory(nm="tcl-tk", hr="https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos" t="tcl-tk for pyenv")]
@set _ns="link" _="tcl-tk" target="_blank"

[note(t="NOTE2: If you will be using [ismd.b] [E.lp][ismd.short_b][E.rp], the version of Python you will be using must have been built with **[tk._tkinter]** [E.lp]**[tk]**[E.rp]. Versions from [activestate] will have this, but if you use some other version, for example, if you use **[pyenv]** to manage the version of Python on your system, you must set the compiler flags *prior* to doing the [pyenv] install.")]

If you did not have these flags set when you did the install of Python using **[pyenv]**, and you want to use ismd, you will have to *uninstall* the current version, and reinstall it (with the propery environment variables set). Here is a link [tk._asurl] that will provide the information you need to get this done, although take a look at this [tcl-tk.<]Stackoverflow Question and Answer[tcl-tk.>] for the steps needed to solve this issue.

[wrap_h.section(t="### Creating a virtual environment for running **OBS Studio** browser endpoints")]

[terminal.wc_open(t="Running virtual environment for OBS Studio browser endpoints")]
[sp]
[E.num] TODO: need a better folder name
$ cd pipenv
pipenv install  - this will install what's referred to in Pipfile.lock
pipenv shell
ismd -nd -f clock.md -m endpoint hostgui
[terminal.wc_close]

If the code is not changing, you can also load it is a static local file in OBS. Describe that here...
[terminal(t="$ smdparse -nd -f clock.md")]

[wrap_h.section(t="## inside OBS")]

Add a Browser to a scene
Use localhost:8080/smd/clock/html/clock.html

[wrap_h.section(t="## Create the pipenv/*.lock files first time")]

[terminal.wc_open(t="Creating the Pipfile and Pipfile.lock")]
[sp]
$ pipenv install selenium
$ pipenv install watchdog
$ pipenv install bottle
$ cd root_of_smd_cloned_repo
$ pipenv install -e /path/2/smd
[terminal.wc_close]




[docthis.open(h="Add this to setup-doc.md")]

The release process should smdparse -f userdocs.md -c -d export so the rendered version of the documentation is part of the repository. This is required because the instructions in the README.md say "open this file with your browser" to read the docs current with the release you are looking at...

Need to move the additional useful variable definitions from this chapter to the builtins...

[docthis.close]

[wrap_h.section(t="### README.md from repository root")]
Just below, I will import the README.md from the root directory of this repository. That file uses a more standard markdown syntax, and if you review the rendered output, you will see where certain things do not expand as the syntax is not supported by [smd.b]. The most obvious are the inline and reference links, although this is a rather simple example, not intended to show all differences between **markdown** and [smd.b].

@html _="divxplus" _inherit="divx" style="margin-left:7em;margin-right:7em;background-color:lightgray;padding:0 1em .5em;font-size:1.3em"
@wrap divx
@@[divxplus.<]
@import "[sys.root]/README.md"
@@[divxplus.>]
@parw 1

As you can see, the simple markdown including headings e.g. **[E.num]**, bold face [e_tag.b(t="strong")] and italics [e_tag.b(t="em")] are parsed and render the same with [smd.b] as they do with standard **markdown**. As you will soon see, however, [smd.b] will do much, much more.
