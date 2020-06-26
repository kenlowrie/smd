[link.setup]
[wrap_h.chapter(t="## Setting up smd")]

@html _id="_div_terminal_" \
      _tag="div" \
      class="plain" style="padding-left:3em;padding-right:3em"
 
@html _id="_prewrap_terminal_" \
      _inherit="prewrap" \
      class="divTitle"\
      style="background-color:lightgray;font-style:italic"
@html _id="_prewrap_terminal_content_" \
      _inherit="prewrap" \
      class="divTitle"\
      style="background-color:lightgray;font-weight:100" 


@var _id="terminal" \
          _format="@@ {{self.inline}}" \
          inline="{{html._div_terminal_.<}}{{html._prewrap_terminal_content_.<}}{{self.t}}{{html._prewrap_terminal_content_.>}}{{html._div_terminal_.>}}"\
          with_content="@@ {{self.wc_inline}}" \
          wc_inline="{{self.wc_open_inline}}{{self.c}}{{self.wc_close_inline}}"\
          wc_open="{{code.pushlines(t=\"@wrap nop\n{{self.wc_open_inline}}\")}}"\
          wc_close="{{code.pushlines(t=\"{{self.wc_close_inline}}\n@parw 1\")}}"\
          wc_open_inline="{{html._div_terminal_.<}}{{html._prewrap_terminal_.<}}{{self.t}}{{html._prewrap_terminal_.>}}{{html._prewrap_terminal_content_.<}}"\
          wc_close_inline="{{html.prewrap.>}}{{html.div.>}}"\
          t="This is your terminal title" \
          c="This is your terminal content"

//@dump var="terminal" html=".*terminal"

There are two approaches to installing [smd.B] on your system; either using **pip** or **pipenv**. The remainder of this chapter will cover both methods, and you can choose which is better for you.

[wrap_h.section(t="###Installing with pip")]

Is pip optional or built-in? Need to address that.

The easiest way to install [smd] on your system is to use the package installer for Python or **pip**. From a terminal window on your machine, change to the root directory of your cloned repository and type:

[terminal(t="$ pip install .")]

One drawback to this method is that the package and its dependencies will be installed globally, which could interfere with other packages installed on your system. In addition to that, you

TODO: Mention that this will not install bottle and selenium which are required by [ismd.b]..., but pipenv will...

You can also install the package in developer mode with the -e flag. This will point the installation of the package to the current cloned repository directory instead of copying it over to your site-packages installation directory; useful if you plan on making changes and don't want to reinstall each time you make a change.

[terminal.wc_open(t="Install in developer mode with pip")]
[sp]
$ pip install -e .
[terminal.wc_close]


[docthis.open(h="Add this to setup-doc.md")]

Make the build process create a "compiled" version of the documentation as a part of the build tree, so the instructions in the README.md can say to just "open this file with your browser" to read the docs current with the release you are looking at... Doesn't need to be a build thing, just needs to be a "release" thing.

[docthis.close]

[wrap_h.section(t="### README.md from root of this tree")]
@wrap divx
@html _="divxplus" _inherit="divx" style="margin:5em;margin-right:250px;background-color:lightgray;padding:2em"
@@[divxplus.<]
@import "[sys.basepath]/../README.md"
@@[divxplus.>]
@parw 1
