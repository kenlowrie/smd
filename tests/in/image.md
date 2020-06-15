@import "$/testsetup.md"

[var.testavdoc.begin(title="image.md" desc="Testing Images in Shots support from avs/image.md")]

@var imports="../in/import"

@import '[sys.imports]/avs/image.md'
@import '[sys.imports]/avs/avs.md'

[IMG_SIZE_LARGE]
@var ss="{{var.img_def.img_st_inline_border}}"
@var trythis="{:.red.bold}Try to get this shot"
@var beforeshoot="{:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION"

@import '[sys.imports]/avs/shot.md'
@image _id="needshot" src="[imports]/needshot.png" style="[ss]"

[shot_factory(nm="shot1")]
[var.shot1._null_(d="*Short Description Here*" c="yes" l="85mm")]
[img_factory(nm="shot1" s="[imports]/shot1.jpg")]

//Can be used inside a shot like this
[var.avshot.visual]
WS:a shot
[image.shot1]
[var.avshot.audio]
Use it inside an AV shot
[var.shot1]
[var.avshot.end]

//Or can be used outside a shot like this
[divxp(c="[image.shot1]")]
[divxp(c="[var.shot1]")]

//Use it @raw, except it smashes against the sides...
@raw [image.shot1]
@raw [var.shot1]

[shot_factory(nm="shot0")]
[var.shot0._null_(d="*Short Description*" c="yes" l="85mm")]
[img_factory(nm="shot0" s="[imports]/shot1.jpg")]

//@image _id="shot0" src="[imports]/shot0.jpg" style="[ss]"
//@var _id="shot0" \
     desc="*Short Description*" \
     lens="**85mm**" \
     crane="yes" \
     _format="[_shotinfo_]"

[var.avshot.visual]
[var.shotinfo2(shotid="shot0")]
[var.avshot.audio]
And here is some info about shot0
[var.avshot.end]

[shot_factory(nm="needshot")]
[var.needshot._null_(d="*Short Description*" c="yes" l="50mm")]
[divxp.open]
[var.needshot(shotid=\"shot0\")]
[divxp.close]

[var.avshot.visual]
[var.shotinfo2(shotid="needshot")]
[var.avshot.noaudio]

@image _id="shot2a" src="[imports]/shot1.jpg" style="[var.img_def.img_st_inline]"
@image _id="shot2b" src="[imports]/shot1.jpg" style="[var.img_def.img_st_inline_border]"
@image _id="shot3a" src="[imports]/shot1.jpg" style="[var.img_def.img_st_block]"
@image _id="shot3b" src="[imports]/shot1.jpg" style="[var.img_def.img_st_block_border]"

[shot_factory(nm="shot2a")]
[var.shot2a._null_(d="shot1.jpg" c="yes" l="85mm")]
[shot_factory(nm="shot2b")]
[var.shot2b._null_(d="shot1.jpg" c="yes" l="50mm")]
[shot_factory(nm="shot3a")]
[var.shot3a._null_(d="shot1.jpg" c="yes" l="24mm")]
[shot_factory(nm="shot3b")]
[var.shot3b._null_(d="shot1.jpg" c="yes" l="70mm")]

[var.avshot.visual]
Single Shot Sequence
    [image.shot2a]
    [image.shot2b]
    [image.shot3a]
    [image.shot3b]
[var.avshot.noaudio]

//TODO: Move this to divs.md, but will cause lots of failures during testing.
//TODO: Is it a bug that _div_extras_ doesn't output as raw? Shouldn't it?
//TODO: Need a way to have multiple tags. either @wrap tag1, tag2 (clean) or ability to specify opentag and closetag on html (this wouldn't work because of classes and other attrs...)
//@html _="divxp" _tag="div><p" _format="<div class=\"extras\"><p>{{self.c}}"

//@wrap html.divx, html.p

@wrap _div_extras_

@var _="wrap_kludge" c="default content" _format="<p>{{self.c}}</p>"
@var divx_kludge="@@[html._div_extras_.<]" close="@@[html._div_extras_.>]"

[divx_kludge]
##Inline SHOTS
[divx_kludge.close]
[wrap_kludge(c="[image.shot2a]")]
[wrap_kludge(c="[image.shot2b]")]
[wrap_kludge(c="[image.shot3a]")]
[wrap_kludge(c="[image.shot3b]")]

[divx_kludge]
## @raw inline SHOTS
[divx_kludge.close]
@parw

@raw [image.shot2a]
@raw [image.shot2b]
@raw [image.shot3a]
@raw [image.shot3b]

[divx_kludge]
## Splitting smart shots
[divx_kludge.close]

[var.avshot.visual]
[var.shotinfo2(shotid="shot2a")]
[var.avshot.noaudio]

[var.avshot.visual]
[var.shotinfo2(shotid="shot2b")]
[var.avshot.noaudio]

[var.avshot.visual]
[var.shotinfo2(shotid="shot3a")]
[var.avshot.noaudio]

[var.avshot.visual]
[var.shotinfo2(shotid="shot3b")]
[var.avshot.noaudio]

[divx_kludge]
## Testing namespaces
[divx_kludge.close]

[var.avshot.visual]
[shotinfo2]
[var.avshot.audio]
shotinfo2._=[shotinfo2._]
shotinfo2._id=[shotinfo2._id]
shotinfo2.shotid=[shotinfo2.shotid]
[var.avshot.end]

[divx_kludge]
### Namespace with prefix
[divx_kludge.close]

[var.avshot.visual]
[var.shotinfo2]
[var.avshot.audio]
var.shotinfo2._=[var.shotinfo2._]
var.shotinfo2._id=[var.shotinfo2._id]
var.shotinfo2.shotid=[var.shotinfo2.shotid]
[var.avshot.end]

[divx_kludge]
## Now just 'shot2a' in the brackets with attributes
[divx_kludge.close]
@wrap _div_extras_
[wrap_kludge(c="[image.shot2a]")]
[wrap_kludge(c="shot2a=[shot2a.desc]")]
[wrap_kludge(c="shot2a.lens=[shot2a.lens]")]
[wrap_kludge(c="shot2a._format=[shot2a._format]")]

[divx_kludge]
### with image. prefix on shot2a
[divx_kludge.close]

[wrap_kludge(c="[image.shot2a]")]
[wrap_kludge(c="[image.shot2a.src]")]
[wrap_kludge(c="[image.shot2a.style]")]

[divx_kludge]
### with varv2. prefix on shot2a
[divx_kludge.close]
[wrap_kludge(c="[var.shot2a]")]
[wrap_kludge(c="[var.shot2a.desc]")]
[wrap_kludge(c="[var.shot2a.lens]")]
[wrap_kludge(c="[var.shot2a._format]")]
@parw

[var.testavdoc.end]
