[link.ug_debug]
[wrap_h.chapter(t="##Debugging your markdown files")]

Okay, most of you will never need any of the things we are going to discuss here. Why would you? Your markdown will be flawless and perfect the first time. That's good for you, unfortunately for me, that's not the case. Because of that, two special keywords were added to assist with the markdown debugging process: [smddebug.b] and [smddump.b]. This chapter is going to go over both of them in detail, and show how they can be used to assist in the debugging process.

[link.ug_debug_cmd]
[wrap_h.section(t="###The [smddebug.il] keyword")]

We will start with the [smddebug.b] keyword, as this is useful for getting debug messages written into the output stream, so that you can see what is happening in real-time.

[syntax.wc_open(t="[smddebug.il] Keyword Syntax")]
    [b]
    [tab.<][smddebug.b] [E.lb]*tag*="*regex*" [E.lb]*tag*="*regex*" [E.lb] ... [E.rb] [E.rb] [E.rb][tab.>]
    [b]
    [tab.<][tab.<]***tag*** is one of [E.lt]**on | off | toggle | enabled | tags**[E.gt][tab.>][tab.>]
    [tab.<][tab.<]***regex*** is any Python-compliant regular expression[tab.>][tab.>]
[syntax.wc_close]

Okay, to start, you can see that the parameters to [smddebug.b] are *all* optional. So, if we type [smddebug.em], this is what happens:

[terminal2.wc_open(t="[smddebug.il] keyword")]
    [terminal2.wc_open_content]
        *[smdcomment.b] Toggle everything on*
        [smddebug.b]
        Toggling Debug Mode<br />
        <span class="debug green"><strong>Method(toggle): _SYSTEM is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): bookmarks is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): cache is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): cache.import is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): markdown is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): ns is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): ns.add is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): ns.code is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): ns.html is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): ns.image is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): ns.link is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): ns.var is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): smd is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): smd.line is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): smd.raw is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): stdinput is now enabled</strong></span>
        <span class="debug green"><strong>Method(toggle): utility is now enabled</strong></span>
        [sp]
        *[smdcomment.b] Toggle everything back off*
        [smddebug.b]
        Toggling Debug Mode<br />
        <span class="debug green"><em>Method(toggle): _SYSTEM is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): bookmarks is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): cache is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): cache.import is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): markdown is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): ns is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): ns.add is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): ns.code is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): ns.html is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): ns.image is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): ns.link is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): ns.var is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): smd is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): smd.line is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): smd.raw is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): stdinput is now disabled</em></span>
        <span class="debug green"><em>Method(toggle): utility is now disabled</em></span>
    [terminal2.wc_close_content]
[terminal.wc_close]

Okay, awesome, you can see that [smddebug.b] on it's own, simply toggles the state of each registered debug handler. In our case, everything was off, and so the first time [smddebug.b] was used, it toggled everything on. Then, the second time, everything was toggled back off. 

However, if one or more of the registered handlers was **on**, then the first time we issued the [smddebug.b] it would have toggled those off, and everything else on! It's a toggle, so that should be self explanatory. If you aren't sure, open up an [smd.b] session and try it, and see how it works.

[bluenote.with_content(c="NOTE: To be honest, enabling *all* of the debug handlers at once will most likely not be very useful for you. There are hundreds of debug messages that will be printed depending on what your markdown contains, and it'll be very tricky to follow along. In most cases, you will choose one or two of the handlers to enable, and then use the output from them to decode what is going on.")]

[link.ug_debug_parms]
[wrap_h.subsect(t="###The [smddebug.il] parameters")]

The parameters to [smddebug.b] are:

[html.td_desc._null_(_align="left")]
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item="on=\"regex\"" desc="turn the registered debug handler[E.lp]s[E.rp] on for all that match the **regex** string.")]
        [table_2col.row_alt(item="off=\"regex\"" desc="turn the registered debug handler[E.lp]s[E.rp] off for all that match the **regex** string.")]
        [table_2col.row_alt(item="toggle=\"regex\"" desc="toggle the state of the registered debug handler[E.lp]s[E.rp] for all that match the **regex** string.")]
        [table_2col.row_alt(item="enabled=\"regex\"" desc="dumps the current registered debug handler[E.lp]s[E.rp] and their state, without changing it[E.lp]s[E.rp] off for all that match the **regex** string.")]
        [table_2col.row_alt(item="tags=\"regex\"" desc="dumps the registered debug handler[E.lp]s[E.rp] names; if *name emphasized* it is disabled, or **name bold** it is enabled. Does this off for all that match the **regex** string.")]
    [table_2col.close]
[bigmargin._close]

Next, let's talk about the **regex** string that can be specified with each of these options. Regular Expressions are a convenient way of matching multiple things using a specific language if you will. I'm not going to get into describing that, but there are plenty of sites on the Internet that will cover it quite thoroughly. The important thing to remember is that the **regex** ***must*** be a Python-compliant regular expression in order for it to work as expected. Let's look at a few examples of how you can use it to match multiple debug handlers in [smd.b].

The various modules and subsystems in [smd.b] can register a debug handler using a name. If you look at the list of handlers above, you'll see the names within the output strings. For example, **ns**, **ns.add** and **ns.code** are all registered debug handler names. Let's say you want to toggle the state of all handlers that begin with *ns*. You could do that by typing *@debug toggle="ns"* or *@debug toggle="ns[E.ast]"*. Just be sure to put the **@debug** statement on a line by itself, because otherwise it will be treated as inline text.

But what if you wanted to toggle just the **ns** handler, but not all of the other ones that begin with *ns*? You would do that like this: *@debug toggle="[big.110p(t="ns$" cls=".red.bold")]*. The [big.110p(t="$")] signals the end of the string, or name in this current context. See how that works so far?

Now, let's say we wanted to toggle the state of the *utility* and *ns* debug handlers. Do we need to [smddebug.b] statements for that? Nope. Use this: *@debug toggle="[big.110p(t="utility | ns$")]"* statement. NOTE: I added spaces around the pipe [big.110p(t="|")] so it would be easier to read. Do **not** do that for real, or you won't get the results you expect.

Keep in mind that this method of using regular expressions for the parameter strings works the same in [smddebug.b] and [smddump.b], so it's definitely worth getting more familiar with.

This wraps up the section on the [smddebug.b] statement. Let's move along into [smddump.b] now, another useful debugging trick when writing your own builtins and macros.

[link.ug_dump_cmd]
[wrap_h.section(t="###The [smddump.il] keyword")]

The [smddump.b] keyword is used to dump the current declarations of variables. As you will see, you can dump a single variable, or multiple variables, in one or more namespaces. Let's first take a look at the syntax:

[syntax.wc_open(t="[smddump.il] Keyword Syntax")]
    [b]
    [tab.<][smddump.b] [E.lb]*tag*="*regex*" [E.lb]*tag*="*regex*" [E.lb] ... [E.rb] [E.rb] [E.rb][tab.>]
    [b]
    [tab.<][tab.<]***tag*** is one of [E.lt]**var | html | link | image | code | sysdef | tracked | help**[E.gt][tab.>][tab.>]
    [tab.<][tab.<]***regex*** is any Python-compliant regular expression[tab.>][tab.>]
[syntax.wc_close]

Okay, to start, you can see that, like [smddebug.b], the parameters to [smddump.b] are *all* optional. So, if we type [smddump.em], this is what happens:

[terminal2.wc_open(t="[smddump.il] keyword")]
    [terminal2.wc_open_content]
        *[smdcomment.b] Dump all the sysdef's, tracked files and variables in all namespaces*
        [smddump.b]
        ----------------------------------------
        System Defaults: .*
        ----------------------------------------
        [sp.4]Current system defaults
        ----------------------------------------
        Files seen during parsing: .*
        ----------------------------------------
        [sp.4]Files seen during parsing
        ----------------------------------------
        NAMESPACE: var
        ----------------------------------------
        [sp.4]Current [smdvar.b] variables
        ----------------------------------------
        NAMESPACE: link
        ----------------------------------------
        [sp.4]Current [smdlink.b] variables
        ----------------------------------------
        NAMESPACE: html
        ----------------------------------------
        [sp.4]Current [smdhtml.b] variables
        ----------------------------------------
        NAMESPACE: image
        ----------------------------------------
        [sp.4]Current [smdimage.b] variables
        ----------------------------------------
        NAMESPACE: code
        ----------------------------------------
        [sp.4]Current [smdcode.b] variables
    [terminal2.wc_close_content]
[terminal.wc_close]

Because there are hundreds of variables defined in even the simplist [smd.b] markdown session, I've chosen to show nothing in the list above. If you would like to see for yourself, then start [smd.b] interactively (type **[smd.il] -nd** in your terminal window), and then **@dump**. Let's review all of tag options for [smddump.b].

[link.ug_dump_parms]
[wrap_h.subsect(t="###The [smddump.il] parameters")]

The parameters to [smddump.b] are:

[html.td_desc._null_(_align="left")]
[bigmargin._open]
    [table_2col.open]
        [table_2col.header(item="Parameter" desc="Description")]
        [table_2col.row_alt(item="sysdef=\"regex\"" desc="Dump the system defaults whose name matches the **regex** string")]
        [table_2col.row_alt(item="tracked=\"regex\"" desc="Dump all the files that match the **regex** string")]
        [table_2col.row_alt(item="var=\"regex\"" desc="Dump all [smdvar.b] variables whose name matches the **regex** string")]
        [table_2col.row_alt(item="link=\"regex\"" desc="Dump all [smdlink.b] variables whose name matches the **regex** string")]
        [table_2col.row_alt(item="html=\"regex\"" desc="Dump all [smdhtml.b] variables whose name matches the **regex** string")]
        [table_2col.row_alt(item="image=\"regex\"" desc="Dump all [smdimage.b] variables whose name matches the **regex** string")]
        [table_2col.row_alt(item="code=\"regex\"" desc="Dump all [smdcode.b] variables whose name matches the **regex** string")]
        [table_2col.row_alt(item="help=\"True|False\"" desc="The allowable values for this parameter are either **True** or **False**. This controls whether or not [smddump.b] will print the **_help** attribute, if present")]
    [table_2col.close]
[bigmargin._close]


Anyway, note that like [smddebug.b], [smddump.b] also allows regular expressions to be used in the parameter for any of the tags. Given that, consider this example:

[terminal2.wc_open(t="[smddump.il] keyword")]
    [terminal2.wc_open_content]
        *[smdcomment.b] Dump [big.110p(t="b$")] and [big.110p(t="bb")] from [smdvar.b] namespace*
        [smddump.b] var="b$|bb"
        ----------------------------------------
        NAMESPACE: var
        ----------------------------------------
        b=
        [sp.4]_format=
        [sp]
        bb=
        [sp.4]_format={{b}}{{b}}
    [terminal2.wc_close_content]
[terminal.wc_close]

Unlike [smddebug.b], you can also specify multiple tags with [smddump.b]. Here's an example of that:

[terminal2.wc_open(t="[smddump.il] keyword - multiple tags")]
    [terminal2.wc_open_content]
        *[smdcomment.b] Dump [big.110p(t="b$")] and [big.110p(t="bb")] from [smdvar.b] namespace and [big.110p(t="table")] from [smdhtml.b] namespace*
        [smddump.b] var="b$|bb" html="table"
        ----------------------------------------
        NAMESPACE: var
        ----------------------------------------
        b=
        [sp.4]_format=
        [sp]
        bb=
        [sp.4]_format={{b}}{{b}}
        [sp]
        ----------------------------------------
        NAMESPACE: html
        ----------------------------------------
        table=
        [sp.4]_format=<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>
        [sp.4]_tag=table
        [sp]
        table_2=
        [sp.4]_format=<{{self._tag}}{{self._public_attrs_}}></{{self._tag}}>
        [sp.4]_tag=table
        [sp.4]style=margin-left:auto;margin-right:auto
    [terminal2.wc_close_content]
[terminal.wc_close]

Go ahead and try dumping different variables from the various namespaces to get familiar with using the regular expressions to choose only those you are interested in. This will be very helpful to you when you start writing your own markdown documents, you know, if you end up having an issue in your markdown that you need to debug. :)

There is also a builtin macro in the [smdcode.b] namespace called **code.dump** that can be used to display the help string for a given variable. It is used quite a bit in the user documentation, although unless you are writing documentation for your own extensions to [smd.b], it isn't likelly something you will get much use out of.

One final note is the special tag **help**. First, it does not take a regular expression like the other tags. Instead, it takes either **True** or **False**. By default, it is set to False, which tells it that it should **not** dump the **_help** attribute on a variable if one exists. If you set it to True, however, and a given variable has the **_help** attribute, then it will dump that too. It is set to False by default because in most cases, you don't want to see the help string, or if you do, it makes much more sense to display it with **varname.?** or **varname.??**, so it will be formatted in a way that you can read it!

[link.ug_common_issues]
[wrap_h.section(t="###A few common situations you might encounter")]

In this section, we will document how to debug common issues you may encounter while writing markdown for your project. Currently I have only identified a couple that are common things that happen to me, so I will address them now. As more things are identified going forward, I will add them here.

[wrap_h.subsect(t="####Markdown nesting error")]

Consider the following markdown:

[terminal2.wc_open(t="Markdown nested too deeply error")]
    [terminal2.wc_open_content]
        *[smdcomment.b] Declare two variables*
        [smdvar] x="{{y}}"
        [smdvar] y="{{x}}"
        [E.lb]x[E.rb]
        *[smdcomment.b] Boom*
        smd.core.exception.NestingError: Markdown().markdown--Expansion nested too deeply. Enable @debug on="markdown"
    [terminal2.wc_close_content]
[terminal.wc_close]

Did your computer make a small explosive sound? LoL. No? Okay, bad joke. Anyhow, it's likely obvious what has happened here: variable **x** says it should evaluate to **y** and **y** says it should evaluate to **x**. So this battle will continue 25 times, and then the markdown code will give up. The good news is that it pretty much tells you how to debug the issue at the end: *Enable @debug on="markdown"*. So, let's change the code as follows:

[terminal2.wc_open(t="Markdown nested too deeply error - enable debug")]
    [terminal2.wc_open_content]
        *[smdcomment.b] Declare two variables*
        [smdvar] x="{{y}}"
        [smdvar] y="{{x}}"
        [smddebug.il] on="markdown"
        [E.lb]x[E.rb]
        *[smdcomment.b] Boom*
        smd.core.exception.NestingError: Markdown().markdown--Expansion nested too deeply. Enable @debug on="markdown"
    [terminal2.wc_close_content]
[terminal.wc_close]

Looks the same, but if you scroll up a bit to the top of the exception stack, you will notice the following set of messages:

[terminal2.wc_open(t="Markdown recursion dump with debug enabled")]
    [terminal2.wc_open_content]
        markdown recursion dump:
            [sp.4]Item: 26: {{y}}
            [sp.4]Item: 25: [x]
            [sp.4]Item: 24: [y]
            [sp.4]Item: 23: [x]
            [sp.4]Item: 22: [y]
            [sp.4]Item: 21: [x]
            [sp.4]Item: 20: [y]
            [sp.4]Item: 19: [x]
            [sp.4]Item: 18: [y]
            [sp.4]Item: 17: [x]
            [sp.4]Item: 16: [y]
            [sp.4]Item: 15: [x]
            [sp.4]Item: 14: [y]
            [sp.4]Item: 13: [x]
            [sp.4]Item: 12: [y]
            [sp.4]Item: 11: [x]
            [sp.4]Item: 10: [y]
            [sp.4]Item: 9: [x]
            [sp.4]Item: 8: [y]
            [sp.4]Item: 7: [x]
            [sp.4]Item: 6: [y]
            [sp.4]Item: 5: [x]
            [sp.4]Item: 4: [y]
            [sp.4]Item: 3: [x]
            [sp.4]Item: 2: [y]
            [sp.4]Item: 1: [x]
        Traceback (most recent call last):
    [terminal2.wc_close_content]
[terminal.wc_close]

You can see from the recursion dump that **x** refers to **y**, then **y** refers back to **x**, and so on and so forth until it dies. Now this is a very simplistic example, but the good news is that in most cases, it will be easy to figure out if you toggle on the **markdown** debug handler, because it will show you each line that it tried to process, which will identify which variables and/or attributes are involved in the showdown.

Next up is using [ismd.b] to debug the raw HTML...

[wrap_h.subsect(t="####Debugging the raw HTML")]

Another useful thing to know is how to debug the raw HTML instead of looking at the rendered output, which at times might depend on the browser you are using to display it. Usually though, this method will help you figure out where your HTML markup is messing up, so it's definitely a good trick to know.

If you skipped the chapter on [ismd.b], now might be a good time to review it.

[TODO] Finish this when the command line docs for [ismd.b] are done, so I don't repeat a bunch of it...


//[docthis.open(h="Add this to debug-doc.md")]
//[docthis.close]

Okay, so that wraps the chapter on debugging. And it also marks the end of the primary documentation for [smd.b]. In the remaining chapters, we will look at several examples that illustrate how to accomplish some real-world applications for [smd.b].