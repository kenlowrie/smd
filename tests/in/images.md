@import "$/testsetup.md"

[var.testdoc_nw.begin(title="images.md" desc="Testing Images in Shots support from image.md")]

[var.plain(t="Test the builtins in sys.import/avs/shot.md for images and shots")]

@import '[sys.imports]/avs/avs.md'

@set _="code.dump" format="True" whitespace="True"

@wrap divx, p

**image_factory(nm="imT0")**
[image_factory(nm="imT0")]
[imT0.?]
[dump(ns="image" name="imT0$")]

**image_factory(nm="imT0a" ip="/path/2/image.jpg")**
[image_factory(nm="imT0a" ip="/path/2/image.jpg")]
[dump(ns="image" name="imT0a")]

**image_factory(nm="imT0b" st="IMG_STYLE.inline")**
[image_factory(nm="imT0b" st="IMG_STYLE.inline"))]
[dump(ns="image" name="imT0b")]

**image_factory(nm="imT0c" st="!IMG_STYLE.block!")**
[image_factory(nm="imT0c" st="!IMG_STYLE.block!"))]
[dump(ns="image" name="imT0c")]

[hash3]

**image_factory_abs_style(nm="imT1")**
[image_factory_abs_style(nm="imT1")]
[dump(ns="image" name="imT1$")]

**image_factory_abs_style(nm="imT1a" ip="/path/2/image.jpg")**
[image_factory_abs_style(nm="imT1a" ip="/path/2/image.jpg")]
[dump(ns="image" name="imT1a")]

**image_factory_abs_style(nm="imT1b" st="[E.lb]IMG_STYLE.inline[E.rb]")**
[image_factory_abs_style(nm="imT1b" st="[IMG_STYLE.inline]"))]
[imT1b.?]
[dump(ns="image" name="imT1b")]

**image_factory_abs_style(nm="imT1c" st="{{IMG_STYLE.block}}")**
[image_factory_abs_style(nm="imT1c" st="{{IMG_STYLE.block}}"))]
[dump(ns="image" name="imT1c")]

**image_factory_abs_style(nm="imT1d" st="[!IMG_STYLE.block!]")**
[image_factory_abs_style(nm="imT1d" st="[!IMG_STYLE.block!]"))]
[dump(ns="image" name="imT1d")]

*Dump of image_factory*
[dump(ns="code" name="image_factory")]
[dump(ns="var" name="image_factory")]

*Dump of image_factory_config*
[dump(ns="var" name="image_factory_config")]

*Dump of image._img_template_*
[dump(ns="image" name="_img_template_")]

[hash1]
[hash1]

***Changing it0***
Current value=
[dump(ns="image" name="imT0$")]

Change it with .set_style absolute
**it0._set_style(_st="{{IMG_STYLE.inline}}")**
[imT0._set_style(_st="{{IMG_STYLE.inline}}")]
[dump(ns="image" name="imT0$")]

Change it with .set_style_as_var
**imT0._set_style_as_var(_st="IMG_STYLE.block")**
[imT0._set_style_as_var(_st="IMG_STYLE.block")]
[dump(ns="image" name="imT0$")]

[hash1]
[hash2]

*Changing default style to block border and declaring variable*

Current value of image_factory attributes
[dump(ns="code" name="image_factory$")]

Change the default in the template to a different variable/attribute
**image_factory_config.set_default_style(st="IMG_STYLE.block_border")**
[image_factory_config.set_default_style(st="IMG_STYLE.block_border")]
[dump(ns="code" name="image_factory$")]

**image_factory(nm="imT2")**
[image_factory(nm="imT2")]
[dump(ns="image" name="imT2$")]

[hash1]

Current value of image_factory_abs_style attributes
[dump(ns="code" name="image_factory_abs_style")]

Change the default in the template to a different variable/attribute
**image_factory_config.set_default_abs_style(st="[E.lb]IMG_STYLE.block_border[E.rb]")**
[image_factory_config.set_default_abs_style(st="[IMG_STYLE.block_border]")]
[dump(ns="code" name="image_factory_abs_style")]

**image_factory(nm="imT3")**
[image_factory_abs_style(nm="imT3")]
[dump(ns="image" name="imT3$")]

[hash3]
**image_factory_config.set_default_abs_style(st="{{IMG_STYLE.block}}")**
[image_factory_config.set_default_abs_style(st="{{IMG_STYLE.block}}")]
[dump(ns="code" name="image_factory_abs_style")]

**image_factory(nm="imT4")**
[image_factory_abs_style(nm="imT4")]
[dump(ns="image" name="imT4$")]

**image_factory_config.set_default_abs_style(st="[E.lb]HEX.lcb2[E.rb]IMG_STYLE.block[E.lb]HEX.rcb2[E.rb]")**
[image_factory_config.set_default_abs_style(st="[HEX.lcb2]IMG_STYLE.block[HEX.rcb2]")]
[dump(ns="code" name="image_factory_abs_style")]

**image_factory(nm="imT5")**
[image_factory_abs_style(nm="imT5")]
[dump(ns="image" name="imT5$")]

**image_factory_config.set_default_abs_style(st="[E.lb]HEX.lb[E.rb]!IMG_STYLE.block![E.lb]HEX.rb[E.rb]")**
[image_factory_config.set_default_abs_style(st="[HEX.lb]!IMG_STYLE.block![HEX.rb]")]
[dump(ns="code" name="image_factory_abs_style")]

**image_factory(nm="imT6")**
[image_factory_abs_style(nm="imT6")]
[dump(ns="image" name="imT6$")]

[var.plain(t="Use the various combinations of image and shot factory vars with avshot")]
@var p0="[code.repeat(t=\"%\" c=\"42\")]"
@var ss="{{var.IMG_STYLE.inline_border}}"
@var image_path="[sys.root]/docs/samples/image"

[IMG_SIZE.large]

[shot_factory(nm="shot1")]
[image_factory(nm="shot1" ip="[image_path]/shot1.jpg")]

//[code.dump(name="shot1")]
Can be used inside a shot like this
[var.avshot.visual]
    WS:a shot
    [image.shot1]
[var.avshot.audio]
    Use it inside an AV shot
    @@[var.shot1.audio]
[var.avshot.end]

Or can be used outside a shot like this:
[image.shot1]
[var.shot1]

Use it @raw, except it smashes against the sides...
@raw [image.shot1]
@raw [var.shot1]

[shot_factory(nm="shot0")]
[var.shot0._null_(d="*Short Description*" c="yes" l="85mm")]
[image_factory(nm="shot0" ip="[image_path]/shot1.jpg" st="!ss!")]

[var.avshot.visual]
    [var.shotdetail(shotid="shot0")]
[var.avshot.audio]
    And here is some info about shot0
[var.avshot.end]

Create the @image variables by hand with all four styles

[IMG_SIZE.small]

@image _id="shot2a" src="[image_path]/shot1.jpg" style="[!var.IMG_STYLE.inline!]" title="inline"
@image _id="shot2b" src="[image_path]/shot1.jpg" style="[!var.IMG_STYLE.inline_border!]" title="inline_border"
@image _id="shot3a" src="[image_path]/shot1.jpg" style="[!var.IMG_STYLE.block!]" title="block"
@image _id="shot3b" src="[image_path]/shot1.jpg" style="[!var.IMG_STYLE.block_border!]" title="block_border"

Create and set the corresponding shot info for each of them

[shot_factory(nm="shot2a")]
[var.shot2a._null_(d="shot1.jpg" c="yes" l="85mm")]
[shot_factory(nm="shot2b")]
[var.shot2b._null_(d="shot1.jpg" c="yes" l="50mm")]
[shot_factory(nm="shot3a")]
[var.shot3a._null_(d="shot1.jpg" c="yes" l="24mm")]
[shot_factory(nm="shot3b")]
[var.shot3b._null_(d="shot1.jpg" c="yes" l="70mm")]

[var.avshot.visual]
Four different image styles in Single Shot Sequence
    [image.shot2a]
    [image.shot2b]
    [image.shot3a]
    [image.shot3b]
[var.avshot.noaudio]

##Inline SHOTS
[image.shot2a]
[image.shot2b]
[image.shot3a]
[image.shot3b]

## @raw inline SHOTS

@raw [image.shot2a]
@raw [image.shot2b]
@raw [image.shot3a]
@raw [image.shot3b]

## avshot using shotdetail smart shots


[IMG_SIZE.custom(w="100%")]
[var.avshot.visual]
    [var.shotdetail(shotid="shot2a")]
[var.avshot.noaudio]

[IMG_SIZE.custom(w="92.3%")]
[var.avshot.visual]
    [var.shotdetail(shotid="shot2b")]
[var.avshot.noaudio]

[IMG_SIZE.custom(w="100%")]
[var.avshot.visual]
    [var.shotdetail(shotid="shot3a")]
[var.avshot.noaudio]

[IMG_SIZE.custom(w="92.3%")]
[var.avshot.visual]
    [var.shotdetail(shotid="shot3b")]
[var.avshot.noaudio]

## Testing namespaces

[var.avshot.visual]
    [shotdetail]
[var.avshot.audio]
    shotdetail._=[shotdetail._]
    shotdetail._id=[shotdetail._id]
    shotdetail.shotid=[shotdetail.shotid]
[var.avshot.end]

### Namespace with prefix

[var.avshot.visual]
    [var.shotdetail]
[var.avshot.audio]
    var.shotdetail._=[var.shotdetail._]
    var.shotdetail._id=[var.shotdetail._id]
    var.shotdetail.shotid=[var.shotdetail.shotid]
[var.avshot.end]

[IMG_SIZE.small]

## Now just 'shot2a' in the brackets with attributes
[image.shot2a]
shot2a=[shot2a.desc]
shot2a.lens=[shot2a.lens]
shot2a._format=[shot2a._format]

### with image. prefix on shot2a
[image.shot2a]
[image.shot2a.src]
[image.shot2a.style]

### with var. prefix on shot2a
[var.shot2a]
[var.shot2a.desc]
[var.shot2a.lens]
[var.shot2a._format]

[var.plain(t="Help Strings for shot2a")]
[shot2a.?]

[var.plain(t="Help Strings for _shotdetail_")]
[_shotdetail_.?]

[var.plain(t="Help Strings for _shot_defs_")]
[_shot_defs_.?]

[var.plain(t="Help Strings for _shot_template_")]
[_shot_template_.?]

[var.plain(t="Help Strings for shot_factory")]
[shot_factory.?]

[var.plain(t="Help Strings for image_factory_config")]
[image_factory_config.?]

[var.plain(t="Help Strings for _img_template_")]
[_img_template_.?]

[var.plain(t="Help Strings for image_factory")]
[image_factory.?]

[var.plain(t="Help Strings for image_factory_abs_style")]
[image_factory_abs_style.?]

[var.plain(t="Help Strings for shotdetail")]
[shotdetail.?]

[var.plain(t="Help Strings for shot_format")]
[shot_format.?]

[var.plain(t="Help Strings for shot_emitter")]
[shot_emitter.?]

@parw

@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for samples/images/images-doc.md")]

[var.toc.wc_open(t="Table of Contents - Unittest samples/images/images-inc.md")]
@wrap nop
[b]
@import "[sys.root]/docs/samples/images/images-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from images-inc.md")]
@dump link="^ug_samp_images"

@import "[sys.root]/docs/samples/images/images-doc.md"

//@stop

@set dump_ns_list="image=\".\" var=\".\""


[var.testdoc_nw.end]
