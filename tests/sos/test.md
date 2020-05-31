//@embed "[sys.imports]/default_1920x1080o.md"
Your stuff here... and here too! and maybe here as well! And  wright up here too. awesome! right??
//@embed "[sys.imports]/default_1920x1080c.md"
[b]=<br />
[b]
@embed "[sys.imports]/def-html.md"  # these files need to check for existence of user override and honor it...
@embed "[sys.imports]/def-head.md"

### CHECK THIS OUT!!

// OR this way...

@embed "[sys.imports]/def-open.md"

## And then at the end

@embed "[sys.imports]/def-close.md"

// a very simple example
// @html _id="html" _tag="html"
// @html _id="body" _tag="body"
// @html _id="head" _tag="head"
// @html _id="title" _tag="title"
// @html _id="h1" _tag="h1"

// @@ [html.html.<]
// @@ [html.head.<][html.title.<]This is my cool title[html.title.>][html.head.>]
// @@ [html.body.<]
// @@ [html.h1.<]Hello, world![html.h1.>]
// @@ [html.body.>]
// @@ [html.html.>]

// I want @NS varname[=rval] [attr1=""] [attr2=""] [...]
// @var foo=this
// @var bar attr1="" attr2 = ""
// @var foo=this attr1="" attr2=""


the default startup needs to be absolutely nothing. you should have to type:
[sys.builtins]

to get it to the "current state", before I completely rewrite builtins.md... only need this to do initial testing, then scrap old tests/in/*, tests/out/*

@embed "[sys.open]"
@embed "[sys.defaulthead]"

{:.section}--- . // OR

{:ignore}// this should be to make it so it's essentially ready for the "<div class="wrapper">" startup like before...
@embed "[sys.old_default]"  
{:ignore}// old default.start or something, so you can can call [sys.old_default.close] at the end...

@embed "[imports]/mydefaultstartup.md"      # need to have several default ones to get things going quickly

// and then

@embed "[sys.openbody]"

[doc.open]
[doc.head.<]
[var.standardheading]
[doc.head.>]
[doc.body]

import something good here

[doc.close]

// LATE ENTRY, BUT MOST CURRENT!!
[var.head.title("this is my new title")]

@rawfile (or perhaps smd?)
@template "sys.template['default']"
@template 

{:.ignore}//note: i can make this work however i want. don't need "buildtins.md" or whatever, I can make the default behavior match \
whatever SMD wants to do and/or assume. That would make more sense, right?
{:ignore}//todo: so basically, when i type "//note:", it should be automatically classed with ".ignore", so it shows up in HTML, but not on screen....

no built-ins by default. i should have to invoke them, e.g. [sys.builtins] or something, right at start...

@var ns = "doc" _id="title" _format("My New Document Title")

@dump ns="var"

@@ [html.table.<]

@embed "def.doc.start()

@embed "myheading.md"

[var.title]
@dump var="title"

Yo.
{:.bigandbold} this is some text on line 2
{:.bigandbold} this is some text on line 3 ... Yes .. NO .. and both
gonna be cool!

@import "$/../in/divs.md"

{:.bigandbold} this is some text

{:.plain}--- plain Writing some junk here.

@var _id="header" \
     _format="# [code.repeat.run(t=\"-\", c=\"42\")]"

[header]

@stop

@debug on="ns.b"
### @debug enabled="."
@debug enabled="."
### @debug tags=""
@debug tags="."
//@debug on=""

//@debug on="ns.code"

[code.equals(v1="display.print", v2="display.test", true="display.true", false="display.false")]

@dump code="equals" var="display"

# Ideas here

Need to be able to set the browser tab title, ideally via the script markdown file being read... maybe easier said than done.

Did it change?


//@dump all="1"

[header]
I'm just writing nonsense here....
{:toc}--- . This is a title

@@ <div class="extras"><h1>Heading</h1>
@@ <p>some random text here to see how it's formatted.</p>
@@ </div>

{:section}--- divTitle what the hell

{:syntax}--- . This has to go. So dumb...

@break

## wtf
* a shot
this is something else
    how do you continue this?
that is one way
//@break
this is another
//## Yo!

and yet one more (after a blank line too!)

[ken]=Ken Lowrie

@break

What do I need to get done first?

Make a list of ...?

1. something
2. else
3. entirely
4. or the same thing you just thought of? Wait what?

And what if I type here in the middle?

more stuff.

[bb][bb][bb]
This is the bottom.












@stop

@var _id="display0" \
    print="0"\
    test="1"\ 
    _format="{{code.equals(v1=\"self.print\", v2=\"self.test\", true=\"self.true\", false=\"self.false\")}}"\
    true="[code.replace(var=\"$.shotid\", val=\"var.display.shotid\", str=\"var.display.push\")]"\
    push="[code.pushlines(shotid=\"$.shotid\" t=\"[basic.shot_left]\")]"\
    false=""

//@debug on="ns.code"
@dump code="equals" var="display"
[code.equals(v1="display.print", v2="display.test", true="display.true", false="display.false")]

 
@import '[sys.imports]/shot.md' 
@import '[sys.imports]/../../avscript/import/shot.md' 

[header]
//@debug on="avscript.line"
[var.display(shotid="shot00", print="1")]
@dump var="display"
[header]
[var.display2(shotid="shot00", print="1")]
@dump var="display0"

@stop


//@debug toggle="." on="." off="." enabled="." foo="bar"  
@embed 'filename' - like @import, except just includes the code without processing. Could be useful for inserting raw html directly into the output, w/o processing at all. Would be especially cool if you could do this inline, like this:
&#91;myvar]=@embed 'foo.html'
Then, the embedded file would be marked down as normal, giving more flexibility. This wouldn't work, though, because it would have \n in the input, and that would fail, right?
@ @raw @embed 'foo.html'

[header]
// -------------------------------------------------------------------

@import '[sys.imports]/divs.md'
@import '[sys.imports]/shot.md'
@import '[sys.imports]/image.md'
[ss]=[{{var.img_def.img_st_inline_border}}]
[IMG_SIZE_LARGE]
[img_factory(nm="shot1", s="[sys.basepath]/../docs/import/shot1.jpg")]
[img_factory(nm="shot2a", s="[sys.basepath]/../docs/import/shot2.jpg")]
[code.shot_factory(nm="shot1", d="my desc")] 
[code.shot_factory(nm="shot2a", d="my really cool shot")] 
[shotinfo2(shotid="shot1")]

@break

# Example of code.pushline
[code.pushline(t="[var.shot1]")][code.pushline(t="@@ - [image.shot1]")]

//@debug on="ns.var" 
# Example of code.pushlines
//[code.pushlines(shotid="shot1", t="@@ [avwrapper.start][image.$.shotid][avwrapper.end]\n@@ <p>[var.$.shotid]</p>")] 
@break

//[storyboard]=@@ [{{avwrapper.start}}][image.$.shotid][{{avwrapper.end}}]
//[shotdetail]=@@ {{html.p.<}}[var.$.shotid]{{html.p.>}}
//[shot_split]=[{{storyboard}}]\n[{{shotdetail}}]

# Example of code.pushlines2
[code.pushlines(shotid="shot1", t="[storyboard]\n@@ <p>[var.$.shotid]</p>")] 
@break
[code.pushlines(shotid="shot2a", t="[storyboard]\n[shotdetail]")] 
[code.pushlines(shotid="shot1", t="[storyboard]\n[shotdetail]")] 
[code.pushlines(shotid="shot1", t="[shot_split]")] 
[IMG_SIZE_THUMB] 
[code.pushlines(shotid="shot1", t="[shot_split]")] 


// implement the quick and dirty "disable debug prints" while 
// executing code. See how that works

