@import "$/testsetup.md"

[var.testavdoc.begin(title="wrap.md" desc="Testing @wrap and @parw functionality")]

@html _id="wt1" _tag="span" class="myclass1" style="color:red"
@html _id="wt2" _tag="span" class="myclass2" style="color:blue"
@html _id="wt3" _tag="span" class="myclass3" style="color:green"

@wrap html.divx, p
[wrap_h(t="[hash2]")]
----------#TS> Put html.divx,p wrapper in effect for document

[wrap_h(t="### Test group 1 - Specifying the html tag inside an @var variable attribute")]

@var wt1="html.wt1" works="html.wt2" alsoworks="html.wt3" _format="html.wt1"

----------#0a> Use the primary document wrapper to begin
[wrap_h(t="#### start wrap via indirection")]
wt1 = [wt1]
wt1.works = [wt1.works]
wt1.alsoworks = [wt1.alsoworks]
[wrap_h(t="[hash3]")]
[wrap_h(t="### --->wt1")]
@wrap [wt1]
----------#1a> wt1 line wrap test
[wrap_h(t="#### --->wt1.works")]
@wrap [wt1.works]
----------#2a> wt1.works line wrap test
[wrap_h(t="#### --->wt1.alsoworks")]
@wrap [wt1.alsoworks]
----------#3a> wt1.alsoworks line wrap test
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

[wrap_h(t="### stop wrap via indirection")]

@var wt2="[html.wt1]" fails="[html.wt2]" alsofails="{{html.wt3}}"

[wrap_h(t="#### start tests that will fail because raw html is being passed in")]
wt2 = [wt2]
wt2.works = [wt2.fails]
wt2.alsoworks = [wt2.alsofails]

[wrap_h(t="[hash3]")]

@wrap [wt2]
@wrap [wt2.fails]
@wrap [wt2.alsofails]

[wrap_h(t="#### start tests that will fail because a non html namespace is being used")]


[wrap_h(t="[hash3]")]

@wrap wt2
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
@wrap wt1
This will work, and be red[b]
@wrap html.wt1
And this is just a bunch of other random content, wrapped in the p class=myclass1 tag

@parw

And now back to the default html.divx, p tag

@parw

And now we will test the special behavior of @wrap.[bb]

@wrap html.divx, p, html.wt2
Default wrap is now the blue one
@wrap nop
this should have no decoration
@parw 1
back to previous (blue)
@parw *
Now I've cleared everything[bb]
@wrap html.divx, p, html.wt3
Now I'm using the html.divx,p,html.wt3 (green) wrap
@wrap null
Once again, nothing.
@parw -1
Still nothing, after trying a negative number with @parw[bb]
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

[wrap_h(t="### And this is the end of the @wrap test.")]

@set dump_ns_list="var=\"wt\" html=\"wt\""
[var.testavdoc.end]
