@import "$/testsetup.md"

[var.testdoc.begin(title="wrap.md" desc="Testing @wrap and @parw functionality")]

@html _id="wt1" _tag="p" class="myclass1"
@html _id="wt2" _tag="p" class="myclass2"
@html _id="wt3" _tag="p" class="myclass3"

[hash2]
----------#TS> Wrapper from the testsetup.begin call in effect out here

### Test group 1 - Specifying the html tag inside an @var variable attribute

@var wt1="html.wt1" works="html.wt2" alsoworks="html.wt3" _format="html.wt1"

@wrap p
----------#0a> Put a plain p wrapper in effect
#### start wrap via indirection
wt1 = [wt1]
wt1.works = [wt1.works]
wt1.alsoworks = [wt1.alsoworks]
[hash3]
### --->wt1
@wrap [wt1]
----------#1a> wt1 line wrap test
#### --->wt1.works
@wrap [wt1.works]
----------#2a> wt1.works line wrap test
#### --->wt1.alsoworks
@wrap [wt1.alsoworks]
----------#3a> wt1.alsoworks line wrap test
@@:---------:#4a> raw lines should never be wrapped[b]
@@ :---------:#4b> raw lines should never be wrapped[b]
@raw:---------:#4c> raw lines should never be wrapped[b]
@raw     :---------:#4d> raw lines should never be wrapped[b]
#### --->popping stack back 1 level p class=myclass2
@parw
----------#2b> wt1.works line wrap test
#### --->popping stack back 1 level p class=myclass1
@parw
----------#1b> wt1 line wrap test
@parw
----------#0b> back to plain p wrapper

### stop wrap via indirection

@var wt2="[html.wt1]" fails="[html.wt2]" alsofails="{{html.wt3}}"

#### start tests that will fail because raw html is being passed in
wt2 = [wt2]
wt2.works = [wt2.fails]
wt2.alsoworks = [wt2.alsofails]

[hash3]

@wrap [wt2]
@wrap [wt2.fails]
@wrap [wt2.alsofails]

#### start tests that will fail because a non html namespace is being used


[hash3]

@wrap wt2
@wrap wt2.fails
@wrap wt2.alsofails

#### and now just some random testing ...
-------------->This should be the plain p wrapper still

@wrap li
item 1
item 2
item 3

[html.ol.<]
apple
orange
banana[html.ol.>]

@parw

This will generate an error[b]
@wrap wt1
@wrap html.wt1
And this is just a bunch of other random content, wrapped in the p class=myclass1 tag

@parw

And now back to the plain p tag

@parw

And now back to the testsetup default wrapper tag.

@parw *

And now we've cleared all stacked tags, so the next line will generate a warning...

@set dump_ns_list="var=\"wt\" html=\"wt\""
[var.testdoc.end]
