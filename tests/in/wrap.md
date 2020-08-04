@import "$/testsetup.md"

[var.testdoc.begin(title="wrap.md" desc="Testing @wrap and @parw functionality")]

@var fs_attr="font-size:1.3em"
@html _id="wt1" _tag="span" class="myclass1" style="color:red;[var.fs_attr]"
@html _id="wt2" _tag="span" class="myclass2" style="color:blue;{{var.fs_attr}}"
@html _id="wt3" _tag="span" class="myclass3" style="color:green;[var.fs_attr]"

[wrap_h.hash2]
----------#TS> Put html.divx,p wrapper in effect for document

[wrap_h(t="### Test group 1 - Specifying the html tag inside an @var variable attribute")]

@var wt1="html.wt1" works="html.wt2" alsoworks="html.wt3" _format="html.wt1"

----------#0a> Use the primary document wrapper to begin
[wrap_h(t="#### start wrap via indirection")]
wt1 = [wt1]
wt1.works = [wt1.works]
wt1.alsoworks = [wt1.alsoworks]
[wrap_h.hash3]
[wrap_h(t="### --->wt1")]
@wrap [wt1]
----------#1a> wt1 line wrap test if this is **RED**
[wrap_h(t="#### --->wt1.works")]
@wrap [wt1.works]
----------#2a> wt1.works line wrap test if this is **BLUE**
[wrap_h(t="#### --->wt1.alsoworks")]
@wrap [wt1.alsoworks]
----------#3a> wt1.alsoworks line wrap test if this is **GREEN**
@break
@@:---------:#4a> raw lines should never be wrapped[b]
@@ :---------:#4b> raw lines should never be wrapped[b]
@raw:---------:#4c> raw lines should never be wrapped[b]
@raw     :---------:#4d> raw lines should never be wrapped[b]
[wrap_h(t="#### --->popping stack back 1 level p class=myclass2")]
@parw
----------#2b> wt1.works line wrap test
[wrap_h(t="#### --->popping stack back 1 level p class=myclass1")]
@parw
----------#1b> wt1 line wrap test
@parw
----------#0b> back to starting html.divx, p

[wrap_h(t="### end wrap via indirection")]
[wrap_h.hash1]

@var wt2="[html.wt1]" fails="[html.wt2]" alsofails="{{html.wt3}}"

[wrap_h(t="#### start tests that will fail because raw html is being passed in")]

@wrap [wt2]
@wrap [wt2.fails]
@wrap [wt2.alsofails]

[wrap_h.hash3]

[wrap_h(t="#### start tests that will fail because a non html namespace is being used")]

@wrap bb
@wrap wt2.fails
@wrap wt2.alsofails

[wrap_h(t="#### and now just some random testing ...")]
-------------->This should be the starting divx, p wrapper still

@wrap li
item 1
item 2
item 3[html.ol.<]
apple
orange
banana[html.ol.>]

@parw

This will generate an error[b]
@wrap var.wt1
This will still be the default @wrap format
@wrap wt1
This will work, and be red[bb]
@wrap html.wt1
Also wrapped in the span class=myclass1 tag[b]

@parw 2

And now back to the default html.divx, p tag

@parw

And now we will test the special behavior of @wrap.[b]

@wrap html.divx, p, html.wt2
Default wrap is now the blue one
@wrap nop
this should have no decoration
@parw 1
back to previous (blue)
@parw *
Now I've cleared everything[b]
@wrap html.divx, p, html.wt3
Now I'm using the html.divx,p,html.wt3 (green) wrap
@wrap null
Once again, nothing.[bb]
Now I'm going to pass an invalid parameter to @parw[b]
@parw -1
Still nothing, after trying a negative number with @parw[bb]
And now, let's pass 25 to @parw, but there's only 2 items on the stack...[b]
@parw 25
Back to empty @wrap q, passed count of 25[bb]
Going to pop on empty stack, will issue warning[bb]
@parw
@wrap html.divx, p, html.wt1
Going red.
Another red line.
@wrap html.divx, p, html.wt2
And now blue
@wrap html.divx, p, html.wt3
And now green
@parw *
And now I've cleared everything once again.[bb]

[wrap_h.hash2]
[wrap_h(t="#### Finally, let&apos;s check all the edge conditions for parameter passing in one place")]

@html _="uniq1" _tag="p" class="plainTitle" style="color:purple;[fs_attr]" attr_issue="this will fail"
@var uniq1="value" attr_issue"will not get here"

@wrap var.uniq1
@wrap var.uniq1.attr_issue
@wrap divx, uniq1
This is a test
@wrap uniq1.attr_issue
And this will be a regular p, but will float right with a thin top border.
@parw
And now we're back to the divx, uniq1
@wrap divx, html.uniq1
Similar, but using hard coded namespace.
@wrap html.uniq1.attr_issue
Again with the float right thing cause of attribute error.
@parw
back to plain purple.
@wrap html.foo.bar.a

@parw *

Now let's test to make sure that the wrapper stack is maintained across imports ...
Current wrap stack level is: [code.wrap_stack(w="#")]
@wrap meta
@wrap link
Current wrap stack level is: [code.wrap_stack(w="#")]
Current tag before import of wrap1.md should be 'link': [code.wrap_stack(w="*")]
@import '$/import/wrap1.md'
Current tag after import of wrap1.md should be 'link': [code.wrap_stack(w="*")]
Current wrap stack level is: [code.wrap_stack(w="#")]
@parw *

[b]
@wrap nop
TEST::: [code.escape_var(v="code.wrap_stack")]
@wrap divx
TEST::: [code.escape_var(v="code.wrap_stack")]
@parw *

[wrap_h(t="### And this is the end of the @wrap test.")]

[var.plain(t="User manual section for @wrap")]

@import "[sys.root]/docs/userdocs_macros.md"

[var.toc.wc_open(t="Table of Contents - Unittest [smdwrap.il]")]
@wrap nop
[b]
@import "[sys.root]/docs/section/wrap-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from wrap-inc.md")]
@dump link="^ug_wrap$"

@wrap divx,p
@import "[sys.root]/docs/section/wrap-doc.md"
@parw

Going to get one more warning about the wrapper stack being empty, cause I flushed it at the end of the @wrap unittests above...[b]

@set dump_ns_list="var=\"wt\" html=\"wt\""
[var.testdoc.end]
