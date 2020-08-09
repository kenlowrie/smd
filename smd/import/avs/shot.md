// Helpers for Shot Generation
@html _id="_table_si_" \
      _inherit="table" \
      class="shotinfo"
@html _id="_table_si2_" \
      _inherit="table" \
      class="shotinfo"\
      style="font-size:1.1em;margin:10px 10px;width:95%"
@html _id="_table_si_right_" \
      _inherit="table" \
      style="width:45%;float:right;margin-top:1em;margin-right:1em;padding:.7em 1em 1em;"\
      class="shotinfo"
@html _id="_td_header_" \
      _inherit="td" \
      class="center" \
      colspan="2"
@html _id="_td_2span_" \
      _inherit="td" \
      colspan="2"
@html _id="_td_2spanA_" \
      _inherit="td" \
      style="font-size:1.3em"\
      colspan="2"
@html _id="_td_item_" \
      _inherit="td" \
      style="padding:5px;width:20%;font-size:1.3em"\
      class="item" 
@html _id="_td_desc_" \
      _inherit="td" \
      style="padding:5px;width:75%;font-size:1.3em"\
      class="item" 
@html _id="_th_item_" \
      _tag="th"\
      _inherit="_td_item_"
@html _id="_th_desc_" \
      _tag="th"\
      _inherit="_td_desc_" 

//TODO: Add help, rename _notes2_ once I better understand its usage in forgiveme.md
@var _id="_shotinfo2_" \
     _format="{{self.visual}}"\
     visual="{{html._table_si_.<}}{{self._basic_}}{{html.table.>}}"\
     visual_wn="{{html._table_si_.<}}{{self._basic_}}{{self._n_row_}}{{html.table.>}}"\
     audio="{{html._table_si_right_.<}}{{self._basic_}}{{html.table.>}}"\
     audio_wn="{{html._table_si_right_.<}}{{self._basic_}}{{self._n_row_}}{{html.table.>}}"\
     _notes2_="{{html._table_si2_.<}}{{self._basic_}}{{self._n_row2_}}{{html.table.>}}"\
     _basic_="{{html.tr.<}}\
                {{html._td_header_.<}}***Shot Information***{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._th_item_.<}}Item{{html.th.>}}\
                {{html._th_desc_.<}}Description{{html.th.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Scene{{html.td.>}}\
                {{html._td_desc_.<}}***{{self.scene}}***{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Shot{{html.td.>}}\
                {{html._td_desc_.<}}{{self._id}}{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Desc{{html.td.>}}\
                {{html._td_desc_.<}}*{{self.desc}}*{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Lens{{html.td.>}}\
                {{html._td_desc_.<}}**{{self.lens}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}f-stop{{html.td.>}}\
                {{html._td_desc_.<}}**{{self.fstop}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}ISO{{html.td.>}}\
                {{html._td_desc_.<}}**{{self.iso}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Height{{html.td.>}}\
                {{html._td_desc_.<}}**{{self.height}}**{{html.td.>}}\
              {{html.tr.>}}\
              {{html.tr.<}}\
                {{html._td_item_.<}}Crane{{html.td.>}}\
                {{html._td_desc_.<}}{{self.crane}}{{html.td.>}}\
              {{html.tr.>}}"\
     _n_row_="{{html.tr.<}}\
                {{html._td_2span_.<}}{{self.notes}}{{html.td.>}}\
              {{html.tr.>}}"\
     _n_row2_="{{html.tr.<}}\
                {{html._td_2spanA_.<}}{{self.notes}}{{html.td.>}}\
              {{html.tr.>}}"

@code _id="split_as"\
      type="exec"\
      src="from .utility import CodeHelpers;print(CodeHelpers.split_as('{{self.t}}'))"\
      t="{{self._help}}" \
      _help="[sp.2]*{{self._}}(t=\"[E.lcb2]var._public_attrs_[E.rcb2]\")*[bb]\
[sp.4]Formats the public or private attributes string in a readable fashion[bb]\
[sp.2]**Examples:**[bb]\
[sp.4]{{self._}}(t=\"[E.lcb2]var._public_attrs_[E.rcb2]\")[b]\
[sp.4]{{self._}}(t=\"[E.lcb2]var._private_attrs_[E.rcb2]\")[b]"

//TODO: Add help
@var _id="_shot_defs_" \
     desc="Your shot description here." \
     lens="24mm" \
     fstop="f/2.8" \
     iso="320" \
     height="36in" \
     crane="No" \
     scene="" \
     notes="" \
     val="***default note text***"\
     _format="<strong><em>{{self._}}</em> defaults:</strong>[bb]{{code.split_as(t=\"{{self._public_attrs_}}\")}}"

//TODO: Add help, and add _help to the decl below, so it references this one copy, and doesn't include it everywhere...

@var _id="_shot_template_" \
     _inherit="_shotinfo2_" \
     desc="{{code.get_default(v=\"self.d\", default=\"{{var._shot_defs_.desc}}\")}}" \
     lens="{{code.get_default(v=\"self.l\", default=\"{{var._shot_defs_.lens}}\")}}" \
     fstop="{{code.get_default(v=\"self.f\", default=\"{{var._shot_defs_.fstop}}\")}}" \
     iso="{{code.get_default(v=\"self.i\", default=\"{{var._shot_defs_.iso}}\")}}" \
     height="{{code.get_default(v=\"self.h\", default=\"{{var._shot_defs_.height}}\")}}" \
     crane="{{code.get_default(v=\"self.c\", default=\"{{var._shot_defs_.crane}}\")}}"\
     scene="{{code.get_default(v=\"self.s\", default=\"{{var._shot_defs_.scene}}\")}}"\
     notes="{{code.get_default(v=\"self.n\", default=\"{{var._shot_defs_.notes}}\")}}"\
     addNote="{{code.append(attr1=\"self.notes\", attr2=\"self.val\")}}"\
     addBB="{{self.addNote(val=\"{{bb}}\")}}"\
     val="{{var._shot_defs_.notes}}"\
     usage="Usage: **{{self._}}(d=&quot;desc&quot; l=&quot;lens&quot; c=&quot;crane&quot;)**)"\

//TODO: The docs for _notes_ and _notes2_ are incorrect. ID differences and fix...
// Add help for _shot_template (move it to the declaration above), and then reference in the shot factory
// actually, we should 

@code _id="shot_factory" type="eval" \
    src="print('@var _id=\"$.nm\" _inherit=\"_shot_template_\" \
                     d=\"$.d\" \
                     l=\"$.l\" \
                     f=\"$.f\" \
                     i=\"$.i\" \
                     h=\"$.h\" \
                     c=\"$.c\" \
                     s=\"$.s\" \
                     notes=\"$.notes\" \
    ')"\
    d = "{{var._shot_defs_.desc}}" \
    l = "{{var._shot_defs_.lens}}" \
    f = "{{var._shot_defs_.fstop}}" \
    i = "{{var._shot_defs_.iso}}" \
    h = "{{var._shot_defs_.height}}" \
    c = "{{var._shot_defs_.crane}}" \
    s = "{{var._shot_defs_.scene}}" \
    notes = "{{var._shot_defs_.notes}}" \
    _help="[sp.2]*{{self._}}(nm=\"varname\" d=\"desc\" notes=\"shot notes\" ...)*[bb]\
[sp.4]Generates a **shot** declaration on the fly[bb][sp.4]**Shots** are simply **@var** variables with a number of common attributes predefined, and several methods provided to perform common operations..[bb]\
[sp.2]**Parameters**[b]\
[sp.4]**nm** - Specifies the name to use for the **@var** (i.e. *shot*) variable[b]\
[sp.4]**d** - The shot description.[b]\
[sp.4]**l** - The lens length.[b]\
[sp.4]**f** - The f/stop.[b]\
[sp.4]**i** - The ISO.[b]\
[sp.4]**h** - The camera/crane height.[b]\
[sp.4]**c** - Crane shot (Yes or No).[b]\
[sp.4]**s** - The scene name.[b]\
[sp.4]**notes** - The shot notes.[bb]\
[sp.2]**Note**[b]\
[sp.4]When parameters are specified, they will override the default values.[bb]\
[sp.2]**Attributes**[b]\
[sp.4]**desc** - The shot description. Default: [E.lb]_shot_defs_.desc[E.rb][b]\
[sp.4]**lens** - The lens length. Default: [E.lb]_shot_defs_.lens[E.rb][b]\
[sp.4]**fstop** - The f/stop. Default: [E.lb]_shot_defs_.fstop[E.rb][b]\
[sp.4]**iso** - The ISO. Default: [E.lb]_shot_defs_.iso[E.rb][b]\
[sp.4]**height** - The camera/crane height. Default: [E.lb]_shot_defs_.height[E.rb][b]\
[sp.4]**crane** - Crane shot (Yes or No). Default: [E.lb]_shot_defs_.crane[E.rb][b]\
[sp.4]**scene** - The scene name. Default: [E.lb]_shot_defs_.scene[E.rb][b]\
[sp.4]**notes** - The shot notes. Default: [E.lb]_shot_defs_.notes[E.rb][bb]\
[sp.2]**Note**[b]\
[sp.4]The defaults are taken from **var._shot_defs_** unless they are specified when the shot is declared.[bb]\
[sp.2]**Methods**[b]\
[sp.4]***NONE*** - If no method specified, returns a basic info table e.g. **[E.lb]varname[E.rb]**[b]\
[sp.4]**_notes_** - Same as default, but returns the table floated right e.g. **[E.lb]varname._notes_[E.rb]**[b]\
[sp.4]**_notes2_** - Same as default, but using **shotinfo** CSS class for table[b]\
[sp.4]**addNote(val=\"more notes\")** - Appends **val** to **notes**[b]\
[sp.4]**addBB** - Appends double break to **notes**[bb]\
[sp.2]**Examples**[b]\
[sp.4]**[E.lb]shot_factory[E.lp]nm=\"myshot\" s=\"my scene\" d=\"opening shot\"[E.rp][E.rb]**[b]"


@var image_factory_config="Image builtins Configuration Macro: {{self._public_keys_}}"\
    set_default_abs_style="{{code.attr_replace_value(attr=\"code.image_factory_abs_style.st\" value=\"{{self.st}}\")}}"\
    set_default_style="{{code.attr_replace_value(attr=\"code.image_factory.st\" value=\"!{{self.st}}!\")}}"\
    _help="[sp.2]*{{self._}}* Macro[bb]\
[sp.4]This macro is used to change the default styling used by the image factories.[bb]\
[sp.2]**Methods**[b]\
[sp.4]**set_default_style(st)** - Set the default style in **code.image_factory** to **st**.[b]\
[sp.4]**set_default_style_abs_style(st)** - Set the default style in **code.image_factory_abs_style** to **st**.[bb]\
[sp.2]**Notes**[b]\
[sp.4]**st** is interpreted differently depending on which method is being used.[b]\
[sp.4]For **set_default_style**, it is an existing variable/attribute that is expanded when the image is rendered.[b]\
[sp.4]For **set_default_abs_style**, it is the CSS styling to be used when the image is rendered.[bb]\
[sp.2]**Examples**[b]\
[sp.4]**{{self._}}.set_default_style(st=\"IMG_STYLE.inline_border\")**[b]\
[sp.8]Sets **code.image_factory.st** to *[E.lb]IMG_STYLE.inline_border[E.rb]*[bb]\
[sp.4]**{{self._}}.set_default_abs_style(st=\"[E.lb]IMG_STYLE.inline[E.rb]\")**[b]\
[sp.8]Sets **code.image_factory.st** to *[IMG_STYLE.inline]*[bb]"

@image  _="_img_template_"\
        _set_style="{{code.attr_replace_value(attr=\"self.style\" value=\"{{self._st}}\")}}"\
        _set_style_as_var="{{code.attr_replace_value(attr=\"self.style\" value=\"[HEX.lb]{{self._st}}[HEX.rb]\")}}"\
        _help="[sp.4]Variable created by **image_factory** or **image_factory_abs_style**.[bb]\
[sp.2]**Methods**[bb]\
[sp.4]**_set_style(st)** - Set the CSS styling for this variable to **st**[b]\
[sp.4]**_set_style_as_var(st)** - Set the CSS styling for this variable to the variable **st**[bb]\
[sp.2]**Examples**[bb]\
[sp.4]**[E.lb]imagevar._set_style(st=\"[E.lcb2]IMG_STYLE.inline[E.rcb2]\")[E.rb]**[b]\
[sp.8]Sets **imagevar.style** to *[IMG_STYLE.inline]*[bb]\
[sp.4]**[E.lb]imagevar._set_style_as_var(st=\"IMG_STYLE.block\")[E.rb]**[b]\
[sp.8]Sets **imagevar.style** to *[E.lb]IMG_STYLE.block[E.rb]*[bb]"

@code _id="image_factory" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"_img_template_\" \
                     src=\"$.ip\" \
                     style=\"[HEX.lb]$.st[HEX.rb]\" \
                     _help=\"[sp.2]**Created with:** *[HEX.lcb2]self._[HEX.rcb2]*[bb][HEX.lcb2]image._img_template_._help[HEX.rcb2]\" \
    ')"\
    ip = "img_path/filename" \
    st = "!IMG_STYLE.inline_border!"\
      _help="[sp.2]*{{self._}}(nm=\"varname\" ip=\"img_srcpath\" st=\"CSS Style Var/Attr\")*[bb]\
[sp.4]Generates an @image declaration for **nm** with style specified as variable/attribute.[bb]\
[sp.4]See also: **image_factory_abs_style**.[bb]\
[sp.2]**Parameters**[b]\
[sp.4]**nm** - Specifies the name to use for the **@image** variable[b]\
[sp.4]**ip** - Specifies the image source path; can be absolute or relative[b]\
[sp.4]**st** - Specifies an existing variable or attribute with CSS styling for the image[bb]\
[sp.6]If **st** is wrapped with exclamation marks, it will defer expansion until runtime[b]\
[sp.6]Otherwise, the expansion occurs immediately. In other words, if you write:[bb]\
[sp.8]**st=\"*!IMG_STYLE.inline!***\" - then **style** is **[E.lb]IMG_STYLE.inline[E.rb]**[b]\
[sp.8]**st=\"*IMG_STYLE.inline***\" - then **style** is the value of **IMG_STYLE.inline**[bb]\
[sp.2]**Examples**[b]\
[sp.4]**[E.lb]image_factory[E.lp]nm=\"myshot\" ip=\"path/image.png\" st=\"!IMG_STYLE.inline!\"[E.rp][E.rb]**[b][sp.6]*Is the same as*[b][sp.4]@image _id=\"myshot\" _inherit=\"_img_template_\" src=\"path/image.png\" style=\"[E.lb]!IMG_STYLE.inline![E.rb]\"[bb]\
[sp.2]**Notes**[b]\
[sp.4]The @image variable created inherits attributes from **_img_template_**, which provides methods[b]\
[sp.4]to easily change the styling for the image after the variable is created. See *_img_template_.?*.[bb]"

@code _id="image_factory_abs_style" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"_img_template_\" \
                     src=\"$.ip\" \
                     style=\"$.st\" \
                     _help=\"[sp.2]**Created with:** *[HEX.lcb2]self._[HEX.rcb2]*[bb][HEX.lcb2]image._img_template_._help[HEX.rcb2]\" \
    ')"\
    ip = "img_path/filename" \
    st = "[HEX.lcb2]IMG_STYLE.inline_border[HEX.rcb2]"\
      _help="[sp.2]*{{self._}}(nm=\"varname\" ip=\"img_srcpath\" st=\"CSS Style\")*[bb]\
[sp.4]Generates an @image declaration for **nm** with style specified inline.[bb]\
[sp.4]See also: **image_factory**.[bb]\
[sp.2]**Parameters**[b]\
[sp.4]**nm** - Specifies the name to use for the **@image** variable[b]\
[sp.4]**ip** - Specifies the image source path; can be absolute or relative[b]\
[sp.4]**st** - Specifies the CSS styling for the image. Default: **[E.lcb2]IMG_STYLE.inline_border[E.rcb2]**[bb]\
[sp.2]**Examples**[b]\
[sp.4]**[E.lb]image_factory[E.lp]nm=\"myshot\" ip=\"path/image.png\" st=\"[E.lcb2]IMG_STYLE.inline[E.rcb2]\"[E.rp][E.rb]**[b][sp.6]*Is the same as*[b][sp.4]@image _id=\"myshot\" _inherit=\"_img_template_\" src=\"path/image.png\" style=\"[E.lcb2]IMG_STYLE.inline[E.rcb2]\"[bb]\
[sp.2]**Notes**[b]\
[sp.4]The @image variable created inherits attributes from **_img_template_**, which provides methods[b]\
[sp.4]to easily change the styling for the image after the variable is created. See *_img_template_.?*.[bb]"










@var _id="shotinfo2" _format="[var.{{self.shotid}}.desc][b][image.{{self.shotid}}][b][var.{{self.shotid}}]" shotid="NOTSET"
@var _id="needshot" \
     _format="[var.{{self.shotid}}.desc][image.needshot]<br />[var.{{self.shotid}}]" shotid="NOTSET"

//TODO: @set now requires _ns="namespace", and _="variablename" ... For these to work, must fix...
@var _id="shot_formatter" \
        imagestyle="@set _=\"image.$.shotid\" style=\"{{ss}}\""\
        pagebreak="{{html._div_plain_pbb_.<}}{{html._div_plain_pbb_.>}}"\
        storyboard="@@ {{avwrapper.start}}{{image.$.shotid}}{{avwrapper.endul}}"\
        shotdetail="{{var.$.shotid.audio_wn}}{{avwrapper.enddiv}}"\
        storyboard2="@@ {{avwrapper.start}}{{image.$.shotid}}{{var.$.shotid}}{{avwrapper.endul}}"\
        shotdetail2="@@ {{html.p.<}}{{var.$.shotid.notes}}{{html.p.>}}{{avwrapper.enddiv}}"\
        storyboard3="@@ {{image.$.shotid}}"\
        shotdetail4="@@ {{var.$.shotid._notes2_}}"

@var _id="shot_emitter" \
        shot_split="{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyboard}}{{var.shot_formatter.shotdetail}}"\
        shot_left="{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyboard2}}\n{{var.shot_formatter.shotdetail2}}"\
        shot_only="{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyboard3}}"\
        shot_s2="@@ {{var.shot_formatter.pagebreak}}\n{{var.shot_formatter.imagestyle}}\n{{var.shot_formatter.storyboard3}}\n{{var.shot_formatter.shotdetail4}}"

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
