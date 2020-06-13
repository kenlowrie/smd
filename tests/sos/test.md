// Another file used for doing adhoc testing...

@stop

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

