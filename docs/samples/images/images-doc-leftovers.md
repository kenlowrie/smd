
@image _="_img_template_" style="{{IMG_STYLE.inline_border}}"

@var _id="img_factory2" \
      _format="{{code.pushlines(t=\"{{self._decl}}\n{{self._check}}\")}}"\
      _decl="@image _id=\"{{self.nm}}\" _inherit=\"_img_template_\" src=\"{{self.s}}\""\
      _check="{{code.equals(v1=\"self.test1\" v2=\"self.st\" true=\"self.true\" false=\"self.false\")}}"\
      _setst="@set _id=\"image.{{self.nm}}\" style=\"[!{{self.st}}!]\""\
      test1="."\
      true=""\
      false="[!code.pushline(t=\"{{img_factory2._setst}}\")!]"\
      s="path_to_image"\
      st="."

[dump(ns="var" name="img_factory")]

### what if we use [e_var(t="code.get")] to read the value on the fly?
Would that work better?
Need a reasonable default, and an easy way to override.
Would also be nice if we had a similar feature to before, where you set it to [ss]=newvalue, and because the factory generated vars all use that varname, it would work the same way. maybe it's a variant that you get via a method: [image.myshot.mystyle_var] or something...

-->1

[img_factory2(nm="myshot" s="[image_path]/shot1.jpg")]
//@debug toggle="utility"
[dump(ns="image" name="myshot")]

[img_factory2(nm="myshot" s="[image_path]/shot1.jpg" st="IMG_STYLE.inline_border")]
//@debug toggle="utility"
[dump(ns="image" name="myshot")]

-->2
@set _="image.myshot" style="[!IMG_STYLE.inline_border!]"
[dump(ns="image" name="myshot")]


//        get_style="{{code.get_value(v=\"image.{{self._}}.style\" ret_type=\"0\")}}"

//@code _id="img_factory3" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"_img_template_\" \
                     s=\"$.s\" \
                     t=\"$.t\" \
    ')"\
    s = "img_path/filename" \
    t = "style"

----------------



----------------




@image _="_img_template_" style="{{IMG_STYLE.inline_border}}"\
    set_style="@set _=\"image.{{self._}}\" style=\"[{{code.echo(t=\"IMG_DEF.in1\")}}]\""\
    ss2="@set _=\"image.{{self._}}\" style=\"{{code.get_value(v=\"self.value\" ret_type=\"0\")}}\""

@code _="echo" type="eval" src="print('!$.t!')" t="(undefined)"

@code _id="if3" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"_img_template_\" \
                     s=\"$.s\" \
                     t=\"$.t\" \
    ')"\
    s = "img_path/filename" \
    t = "style"

[if3(nm="it0")]
[dump(ns="image" name="it0")]
[dump(ns="code" name="echo")]
//[code.echo(t="IMG_DEF.inline")]
-->3

[it0.set_style(t="IMG_STYLE.inline")]
[dump(ns="image" name="it0")]

[it0.ss2(value="[!III.xxx!]")]
[dump(ns="image" name="it0")]

@stop






## this is a problem. The image factory is not allowing me to prevent expansion of the style...
[IMG_SIZE.medium]
@var img_style="[!IMG_STYLE.inline_border!]"
[img_factory(nm="myshot" s="[image_path]/shot1.jpg" st="{{var.img_style}}")]
[shot_factory(nm="myshot" d="WS: Crane down" notes="Opening crane shot" c="Yes")]
[dump(ns="image" name="myshot")]

[avshot.visual]
    [image.myshot]
    [var.myshot]
[avshot.audio]
    [var.myshot.notes]
[avshot.end]







------almost working-----
@var img_config="Image builtin Config: {{self._public_keys_}}"\
    set_default_style="{{code.attr_replace_value(attr=\"image._img_template_.style\" value=\"[E.lbx]{{self.st}}[E.rbx]\")}}"

@image  _="_img_template_"\
        style="{{IMG_STYLE.inline_border}}"\
        set_style="{{code.attr_replace_value(attr=\"self.style\" value=\"[E.lbx]{{self.st}}[E.rbx]\")}}"

@code _id="img_factory3" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"_img_template_\" \
                     src=\"$.s\" \
                     style=\"[E.lbx]$.t[E.rbx]\" \
    ')"\
    s = "img_path/filename" \
    t = "!IMG_STYLE.inline_border!"

//@code _id="test" type="exec"\
    src="'print( 1 if \"x\" != \"_default_\" else 2)'"

//x=[code.test.run]
-->4

// reasonable defaults
[img_factory3(nm="it0")]
[img_factory3(nm="it1" s="/path/file.png")]
// override, but !! will defer the expansion
[img_factory3(nm="it2" t="!IMG_STYLE.block!")]
// without the !!, it will evaluate on the fly
[img_factory3(nm="it3" t="IMG_STYLE.inline" s="/path2/file2.jpg")]
// proof of the !!
[img_factory3(nm="it4" t="!IMG_STYLE.inline!" s="/path2/file2.jpg")]

[dump(ns="image" name="it")]

Changing it0
// regardless, we can change it with .set_style
[it0.set_style(st="IMG_STYLE.inline")]

[dump(ns="var" name="img_config")]
[dump(ns="image" name="_img_template_")]
Changing default style to block border and declaring it0a
// change the default in the template
[img_config.set_default_style(st="IMG_STYLE.block_border")]
[dump(ns="var" name="img_config")]
[dump(ns="image" name="_img_template_")]
[img_factory3(nm="it0a")]

[dump(ns="image" name="it")]


------------
@code _id="_img_factory_1" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"_img_template_\" \
                     src=\"$.s\" \
                     style=\"[HEX.lb]$.t[HEX.rb]\" \
    ')"\
    s = "img_path/filename" \
    t = "!IMG_STYLE.inline_border!"

@code _id="_img_factory_2" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"_img_template_\" \
                     src=\"$.s\" \
                     style=\"$.t\" \
    ')"\
    s = "img_path/filename" \
    t = "IMG_STYLE.inline_border"





@var image_factory="Image Factory"\
    reg="{{code._img_factory_1(nm=\"{{self.nm}}\" s=\"{{self.s}}\" t=\"{{self.t}}\")}}"\
    abs="{{code._img_factory_2(nm=\"{{self.nm}}\" s=\"{{self.s}}\" t=\"{{self.t}}\")}}"\
    s = "/img_path/filename" \
    t = "styling"


[var.image_factory._all_attrs_]

[var.image_factory.reg(nm="imT0")]
[dump(ns="image" name="imT0")]

[var.image_factory.abs(nm="imT1")]
[dump(ns="image" name="imT1")]



------------

@var _id="img_factory" \
      _format="@image _id=\"{{self.nm}}\" src=\"{{self.s}}\" style=\"{{self.st}}\""\
      s="path_to_image"\
      st="[!ss!]"\
      _help="[sp.2]*{{self._}}(nm=\"varname\" s=\"srcpath\" st=\"CSS Style\")*[bb]\
[sp.4]Generates an @image declaration on the fly[bb][sp.4]This simply provides a concise method for declaring an image variable.[bb]\
[sp.2]**Parameters**[b]\
[sp.4]**nm** - Specifies the name to use for the **@image** variable[b]\
[sp.4]**s** - Specifies the source path to the image[b]\
[sp.4]**st** - Specifies the CSS style to use when rendering the image[bb]\
[sp.2]**Examples**[b]\
[sp.4]**[E.lb]img_factory[E.lp]nm=\"myshot\" s=\"path/image.png\" st=\"[E.lb]!IMG_STYLE.inline![E.rb]\"[E.rp][E.rb]**[b][sp.6]*Is the same as*[b][sp.4]@image _id=\"myshot\" src=\"path/image.png\" style=\"[E.lb]!IMG_STYLE.inline![E.rb]\""

_________________________

@var _id="display" \
    print="0"\
    test="1"\ 
    _format="{{code.equals(v1=\"self.print\", v2=\"self.test\", true=\"self.true\", false=\"self.false\")}}"\
    true="{{code.replace(var=\"$.shotid\", val=\"var.display.shotid\", str=\"var.display.push\")}}"\
    push="{{code.pushlines(shotid=\"$.shotid\" t=\"{{var.shot_emitter.shot_left}}\")}}"\
    layout2="{{code.equals(v1=\"self.print\", v2=\"self.test\", true=\"self.true2\", false=\"self.false\")}}"\
    true2="{{code.replace(var=\"$.shotid\", val=\"var.display.shotid\", str=\"var.display.push2\")}}"\
    push2="{{code.pushlines(shotid=\"$.shotid\" t=\"{{var.shot_emitter.shot_split}}\")}}"\
    layout3="{{code.equals(v1=\"self.print\", v2=\"self.test\", true=\"self.true3\", false=\"self.false\")}}"\
    true3="{{code.replace(var=\"$.shotid\", val=\"var.display.shotid\", str=\"var.display.push3\")}}"\
    push3="{{code.pushlines(shotid=\"$.shotid\" t=\"{{var.shot_emitter.shot_only}}\")}}"\
    layout4="{{code.equals(v1=\"self.print\", v2=\"self.test\", true=\"self.true4\", false=\"self.false\")}}"\
    true4="{{code.replace(var=\"$.shotid\", val=\"var.display.shotid\", str=\"var.display.push4\")}}"\
    push4="{{code.pushlines(shotid=\"$.shotid\" t=\"{{var.shot_emitter.shot_s2}}\")}}"\
    false=""

