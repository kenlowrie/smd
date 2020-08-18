[link.ug_setup]
[wrap_h.chapter(t="## Setting up smd")]

There are two approaches to installing [smd.B] on your system; either using **pip** or **pipenv**. This chapter will cover both methods, and you can choose which is better for you. 

*Please take note of the following caveats before continuing with the setup process.*

##### Minimum Required Python Version

[box.wc_open]
[smd.b] requires Python 3.7.3 or later! If you are running an older version, you either have to upgrade or install a virtual environment with something newer in order to run [smd.b].
[box.wc_close]

[ln_factory(nm="tk" hr="https://tkdocs.com/tutorial/install.html" t="Tk")]
@set _ns="link" _="tk" _tkinter="{{self.<}}tkinter{{self.>}}" target="_blank"
[ln_factory(nm="activestate" hr="https://www.activestate.com/products/python/" t="ActiveState")]
@set _ns="link" _="activestate" target="_blank"
[ln_factory(nm="pyenv" hr="https://github.com/pyenv/pyenv#installation" t="pyenv")]
@set _ns="link" _="pyenv" target="_blank"
[ln_factory(nm="tcl-tk", hr="https://stackoverflow.com/questions/60469202/unable-to-install-tkinter-with-pyenv-pythons-on-macos" t="tcl-tk for pyenv")]
@set _ns="link" _="tcl-tk" target="_blank"

##### Tk (tkinter) requirement for [ismd]
[box(t="If you will be using [ismd.b] [E.lp][ismd.short_b][E.rp], the version of Python you will be using must have been built with **[tk._tkinter]** [E.lp]**[tk]**[E.rp]. Versions from [activestate] will have this, but if you use some other version, for example, if you use **[pyenv]** to manage the version of Python on your system, you must set the compiler flags *prior* to doing the [pyenv] install.")]

If you did not have these flags set when you installed Python using **[pyenv]**, and you want to use [ismd.b], you will have to *uninstall* the current version, and reinstall it (with the environment variables set). Here is a link [tk._asurl] that will provide the information you need to get this done, although take a look at this [tcl-tk.<]Stackoverflow Question and Answer[tcl-tk.>] for the steps needed to solve this issue.

Okay, let's get started.

[link.ug_setup_pip]
[wrap_h.section(t="###Installing with pip")]

The easiest way to install [smd.b] on your system is to use the default package installer for Python or **pip**. From a terminal window on your machine, change to the root directory of your cloned repository and type:

[terminal(t="$ pip install .")]

[note(t="You can also install [smd.b] in *edit* mode (**pip install -e .**). This will point the installation of the [smd.b] package to the current cloned repository directory instead of copying it to your site-packages installation directory; useful if you plan on making changes and don't want to reinstall each time you make a change.")]

[terminal.wc_open(t="To install in edit mode with pip")]
$ pip install -e .
[terminal.wc_close]

[bluenote.wc_open]
HINT: If you change your mind about how [smd.b] is installed, simply run [big.120p(t="pip install ." cls=".bold.black.italic")]  or [big.120p(t="pip install -e .")] to change it. When pip detects that [smd.b] is already installed on your system, it will uninstall it first, and then install it in whatever mode you specify.
[bluenote.wc_close]

One drawback to installing [smd.b] using the **pip install** method is that the package and its dependencies will be installed globally, which could interfere with other packages installed on your system. Also, in order to minimize the number of dependencies that are installed using **pip**, three other packages that are needed by [ismd.b], namely **watchdog**, **selenium** and **bottle**, are not automatically installed. 

If you will not be using [ismd.b], then there is nothing extra required. [smd.b] and [smdparse.b] both run without these additional packages. Go ahead and skip down to the [link.ug_smd_vs_markdown._qlink(_qtext="[smd] vs markdown")] section to continue.

[wrap_h.subsect(t="####Additional pip install steps if using [ismd]")]

If you will be using [ismd.b], then you must either install these packages manually, or alternatively, you can use the **pipenv** method described in the [link.ug_setup_pipenv._qlink(_qtext="next section")], which *will* install the extra packages automatically. To install them manually using **pip**, use these commands in your terminal window:

[terminal.wc_open(t="Install additional package dependencies using pip")]
$ pip install selenium
$ pip install bottle
$ pip install watchdog
[terminal.wc_close]

After completing the pip installs for **selenium**, **bottle** and **watchdog**, the last thing you need to configure is a web driver for **selenium** for the browser you will be using. Skip down to [link.ug_setup_webdriver._qlink(_qtext="Installing a webdriver for selenium")] for the details.

[link.ug_setup_pipenv]
[wrap_h.section(t="###Installing with pipenv")]

[ln_factory(nm="pipenv" hr="https://docs.python-guide.org/dev/virtualenvs/" t="pipenv")]
@set _ns="link" _="pipenv" target="_blank"

**[pipenv]** is a much better way to install [smd.b]. It will create a virtual environment for running [smd.b] on your machine, preventing installation of the various site-packages in a global manner, the way **pip** does. This, in turn, isolates [smd.b] to a private environment for use, testing and/or evaluation. 

[note(t="NOTE: If you do not have [pipenv] installed on your machine, navigate to [pipenv._asurl] to get information on it.")]

The **Pipfile** and **Pipfile.lock** files are provided in the root directory of your cloned repository. Simply navigate to that directory on your local machine and type:

[terminal(t="$ pipenv install")]

to create the runtime environment for launching smd on your machine. Once it finishes, type:

[terminal.wc_open(t="Starting [ismd] after pipenv install")]
$ pipenv shell
[sp]
*# Launch [ismd.b]*
$ smd -h
[sp]
*# or Launch [smdparse.b]*
$ smdparse - h
[sp]
*# or Launch [ismd.b]*
$ ismd - h
[terminal.wc_close]

And then invoke [smd.b], [smdparse.b] and/or [ismd.b] within the virtual environment that was created. Alternatively, you can use **pipenv run ...** to execute the code inside the virtual environment created by **pipenv install**:

[terminal.wc_open(t="Using pipenv run to execute Python code in virtual environment")]
*# Launch [ismd.b]*
$ pipenv run smd -h
[sp]
*# or Launch [smdparse.b]*
$ pipenv run smdparse - h
[sp]
*# or Launch [ismd.b]*
$ pipenv run ismd - h
[terminal.wc_close]

By default, [smd.b] is installed *edit* mode (**pipenv install -e .**). This points the installation of the [smd.b] package to the current cloned repository directory instead of copying it to your site-packages installation directory; useful if you plan on making changes and don't want to reinstall each time you make a change. 

If you don't want [smd.b] installed in *edit* mode, you can:

[terminal(t="$ pipenv uninstall smd")]

Followed by:

[terminal(t="$ pipenv install .")]

From the root directory of your cloned repository to change how it is installed.

[link.ug_setup_webdriver]
[wrap_h.section(t="###Installing a webdriver for *selenium*")]

[ln_factory(nm="wd_chrome" hr="https://sites.google.com/a/chromium.org/chromedriver/downloads" t="Chrome Webdriver")]
@set _="link.wd_chrome" _thelink="{{self.<}}Chrome Webdriver{{self.>}}" target="_blank"

[ln_factory(nm="wd_firefox" hr="https://github.com/mozilla/geckodriver/releases" t="Firefox Webdriver")]
@set _="link.wd_firefox" _thelink="{{self.<}}Firefox Webdriver{{self.>}}" target="_blank"

[ln_factory(nm="wd_safari" hr="https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari" t="Safari Webdriver")]
@set _="link.wd_safari" _thelink="{{self.<}}enabling the Safari Webdriver{{self.>}}" target="_blank"

[ln_factory(nm="ug_about_selenium" hr="https://selenium-python.readthedocs.io/" t="About Selenium")]
[ln_factory(nm="ug_selenium_webdrivers" hr="https://selenium-python.readthedocs.io/installation.html#drivers" t="Selenium Webdrivers")]

In order for **selenium** to be able to control your browser, it requires a special driver called a **webdriver**. You can read more about [link.ug_about_selenium._qlink(_qtext="Selenium with Python" target="_blank")] here, and specifically about [link.ug_selenium_webdrivers._qlink(_qtext="Selenium drivers" target="_blank")] here.

Each browser driver should provide any required setup steps on their site. For the most part, however, it's just a matter of copying the driver into the PATH, so that **selenium** can find it. So, navigate to one of the following links and get the driver for your browser.

If you are using Google Chrome, you will need to get the [link.wd_chrome._thelink] version.

If you are using Mozilla Firefox, you need to get the [link.wd_firefox._thelink] version.

If you are using Apple Safari, the driver ships with **macOS**. Navigate to [link.wd_safari._thelink] where you can read about setting up and configuring the Safari driver.

[note(t="At the time of writing this documentation, the **Safari** webdriver has a feature called the **glass pane** which makes it not very useful for being an [ismd.b] monitor. I've been unable to figure out a way to disable the glass pane without stopping the automation, which prevents you from interacting with the browser window to do simple things such as scrolling down... DOH! Gee, thanks Apple. Good news though, both Chrome and Firefox work GREAT! So you might want to use one of them instead, at least when using the monitor feature of [ismd.b]. If and when I find a solution, I will fix the code and update the documentation.")]

Here are a few notes that might help you get things working if you have never used **selenium** before.

First, on newer versions of **macOS**, the driver may require that you grant it the appropriate rights to run the driver on the platform, depending on whether or not the driver has been notarized. Usually, this can be accomplished by simply running the driver once. For both the [link.wd_chrome] and the [link.wd_firefox] versions, I simply ran the executable in a terminal window, and when I got the prompt from **macOS**, I allowed it to run. Fortunately, this is only required one time.

On Safari, you need to:

[terminal(t="$ safaridriver --enable")]

You may also need to **Show Develop Menu**:

[IMG_SIZE.medium]
@image _="ss_safari_show_develop" src="[sys.root]/docs/import/ss_safari_show_develop.png" style="[IMG_STYLE.inline_border}]"
[ss_safari_show_develop]


As well as **Develop | Allow Remote Automation**:

[IMG_SIZE.medium]
@image _="ss_safari_allow_remote_automation" src="[sys.root]/docs/import/ss_safari_allow_remote_automation.png" style="[IMG_STYLE.inline_border}]"
[ss_safari_allow_remote_automation]

In order to get the [link.wd_safari] to work. And by "*to work*", I mean "show the first part of your markdown document only". [e_moji.big(e="tonguewink")].

[wrap_h.section(t="### Using [smd] with OBS Studio")]

[smd.b] can be used to create dynamic content for use in **OBS Studio**. You will likely use either [smdparse.b] to generate a static file, or [ismd.b] to create an endpoint on the **localhost** that you can use with **OBS Studio**. Let's see how this can be done.

[box(t="**NOTE:** This section is jumping ahead just a bit, so if it seems confusing, don't worry. It does assume you are familiar with **OBS**, so if that isn't the case, then you may want to skip it for now.[bb]In addition, it assumes you have successfully installed and configured [smd.b] with either **pip** or **pipenv**.")]

Consider the following:

[link.ug_setup_use_obs]
[terminal.wc_open(t="Creating content for OBS Studio")]
*# If you installed [smd.b] with **pipenv**, start with:*
$ cd [E.lt]root_of_your_smd_repo[E.gt]
$ pipenv shell
[sp]
*# Now move to the samples/obs/clock directory*
$ cd samples/obs/clock
[sp]
*# this next command will create the virtual env and run ismd*
$ ismd -nd -f clock.md -m endpoint hostgui 
[sp]
*# [ismd.b] will parse clock.md, create an endpoint, and keep it live until you press **CTRL-C (&#8963;C)***
[terminal.wc_close]

Alternatively, if the code is not changing (i.e. you've completed development/debugging), you can simply generate a static local file using [smdparse.b] and load that inside OBS. Assuming you are in the **samples/obs/clock** directory **AND** you are in a **pipenv** shell if you installed with **pipenv**:

[terminal(t="$ smdparse -nd -f clock.md")]

[wrap_h.subsect(t="#### Loading the *clock* HTML inside OBS")]

To access the **clock** sample inside OBS, you can add a **browser** to a **scene**, and use one of the following URLs:

[terminal.wc_open(t="URL syntax for accessing the clock sample")]
*If you are running using the [ismd.b] endpoint then use:*
localhost:8080/smd/clock/html/clock.html
[sp]
*If you used [smdparse.b] to generate the raw HTML then use:*
file://<path_to_your_cloned_smd_repo>/samples/obs/clock/html/clock.html
[terminal.wc_close]

Once again, I realize we jumped ahead a bit with this sample on using [ismd.b] and [smdparse.b] since we have yet to cover them, but I figured showing a somewhat more real-world example would help illustrate the kind of things you can do with [smd.b]! One last thing to cover before we move on is how you can customize the **[pipenv]** **Pipfile** to add additional packages you want to use inside your [smd.b] virtual environment.

[wrap_h.section(t="### Creating the Pipenv/Pipenv.lock files the first time")]

If you want to create your own custom configuration for **pipenv**, you can do that with the following commands:

[terminal.wc_open(t="Creating the Pipfile and Pipfile.lock")]
$ pipenv install selenium
$ pipenv install watchdog
$ pipenv install bottle
$ cd [E.lt]root_of_smd_cloned_repo[E.gt]
$ pipenv install -e .
[sp]
*# Now add more **pipenv install** commands for your other packages*
[terminal.wc_close]

Technically, you don't need the first four steps above, since the **Pipenv** file already has everything you need for [smd.b]. You could just **pipenv install** your own packages while sitting in the root directory of your cloned repository, and they will be added to the existing configuration file. Subsequently, whenever you create a new virtual environment using **pipenv install** or **pipenv run**, it will add any additional packages automatically.

//[docthis.open(h="Add this to setup-doc.md")]
//[docthis.close]

[link.ug_smd_vs_markdown]
[wrap_h.section(t="### [smd] vs markdown - Repository README.md")]
Just below, I will import the README.md from the root directory of this repository. That file uses a more standard markdown syntax, and if you review the rendered output, you will see where certain things do not expand as the syntax is not supported by [smd.b]. The most obvious are the inline and reference links, although this is a rather simple example, not intended to show all differences between **markdown** and [smd.b].

@html _="divxplus" _inherit="divx" style="margin-left:7em;margin-right:7em;background-color:lightgray;padding:0 1em .5em;font-size:1.3em"
@wrap divx
@@[divxplus.<]
@import "[sys.root]/README.md"
@@[divxplus.>]
@parw 1

As you can see, the simple markdown including headings e.g. **[E.num]**, bold face [e_tag.b(t="strong")] and italics [e_tag.b(t="em")] are parsed and render the same with [smd.b] as they do with standard **markdown**. As you will soon see, however, [smd.b] will do much, much more.
