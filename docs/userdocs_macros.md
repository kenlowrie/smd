// These macros are helpers for the manual. Not really useful outside of the guide...
// Except for the unittests, which includes this whenever including markdown from the manual...
@var smdtag="@@{{self.il}}" p="" il="{{encode_smd(t=\"{{self.p}}\")}}" b="**{{self.il}}**" em="*{{self.il}}*" emb="***{{self.il}}***"

@var _="smdvar" _inherit="smdtag" p="@var"
@var _="smdvar_wp" _inherit="smdtag" p="@var {{self.parms}}"
@var _="smdhtml" _inherit="smdtag" p="@html"
@var _="smdhtml_wp" _inherit="smdtag" p="@html {{self.parms}}"
@var _="smdcode" _inherit="smdtag" p="@code"
@var _="smdcode_wp" _inherit="smdtag" p="@code {{self.parms}}"
@var _="smdlink" _inherit="smdtag" p="@link"
@var _="smdlink_wp" _inherit="smdtag" p="@link {{self.parms}}"
@var _="smdimage" _inherit="smdtag" p="@image"
@var _="smdimage_wp" _inherit="smdtag" p="@image {{self.parms}}"
@var _="smdimport" _inherit="smdtag" p="@import"
@var _="smdimport_wp" _inherit="smdtag" p="@import {{self.parms}}"
@var _="smdembed" _inherit="smdtag" p="@embed"
@var _="smdembed_wp" _inherit="smdtag" p="@embed {{self.parms}}"
@var _="smdwatch" _inherit="smdtag" p="@watch"
@var _="smdwatch_wp" _inherit="smdtag" p="@watch {{self.parms}}"
@var _="smdset" _inherit="smdtag" p="@set"
@var _="smdset_wp" _inherit="smdtag" p="@set {{self.parms}}"
@var _="smddump" _inherit="smdtag" p="@dump"
@var _="smddump_wp" _inherit="smdtag" p="@dump {{self.parms}}"
@var _="smdbreak" _inherit="smdtag" p="@break"
@var _="smdbreak_wp" _inherit="smdtag" p="@break {{self.parms}}"
@var _="smdstop" _inherit="smdtag" p="@stop"
@var _="smdstop_wp" _inherit="smdtag" p="@stop {{self.parms}}"
@var _="smdexit" _inherit="smdtag" p="@exit"
@var _="smdexit_wp" _inherit="smdtag" p="@exit {{self.parms}}"
@var _="smdquit" _inherit="smdtag" p="@quit"
@var _="smdquit_wp" _inherit="smdtag" p="@quit {{self.parms}}"
@var _="smdraw" _inherit="smdtag" p="@raw"
@var _="smdraw_wp" _inherit="smdtag" p="@raw {{self.parms}}"
@var _="smddebug" _inherit="smdtag" p="@debug"
@var _="smddebug_wp" _inherit="smdtag" p="@debug {{self.parms}}"
@var _="smdcomment" _inherit="smdtag" p="//"
@var _="smdcomment_wp" _inherit="smdtag" p="// {{self.parms}}"
@var _="smdwrap" _inherit="smdtag" p="@wrap"
@var _="smdwrap_wp" _inherit="smdtag" p="@wrap {{self.parms}}"
@var _="smdparw" _inherit="smdtag" p="@parw"
@var _="smdparw_wp" _inherit="smdtag" p="@parw {{self.parms}}"

@var sp4="[sp][sp][sp][sp]"

// The name SMD (smd) should be abstracted in a variable at the lowest level, such that I can change it on the fly and it would reflect throughout the docs.

@var smd="{{self.lcase}}" ucase="SMD" lcase="smd" short="Script Markdown" desc="{{self.ucase}} - {{self.short}}" b="**{{self._format}}**" em="*{{self._format}}*" emb="***{{self._format}}***" B="**{{self.ucase}}**" EM="*{{self.ucase}}*" EMB="***{{self.ucase}}***" short_b="**{{self.short}}**" desc_b="**{{self.desc}}**"

@var _="ismd" _inherit="smd" ucase="iSMD" lcase="ismd" short="Interactive Script Markdown"
@var _="smdparse" _inherit="smd" ucase="SMDParse" lcase="smdparse"  short="Script Markdown Parser"

//TODO: When I add a developer switch (or mode), this should be one of the things that is added
//      Very useful to create a marker in large output documents to find where you are when debugging. :)
@var mk="{{self.s}}" s="@@<br/>{{code.repeat(t=\"&\" c=\"100\")}}<br />" e="@@<br/>{{code.repeat(t=\"%\" c=\"100\")}}<br />"

// This is used when we are documenting attribute creation, because you can't use {{self.}} directly
// If you do, it evaluates to the variable being used to emit the docs. DOH!
@var _self_="&#x73;elf"
@var _self="@@{{self.il}}" il="{{E.lcb2}}{{_self_}}.{{self.p}}{{E.rcb2}}"

@var dumpit="a macro to dump a variable string"\
    1="[!bmgreybg._open!]"\
    2="[!var.source.wc_open_inline(t=\"[!code.pushlist.title!]\")!]"\
    2a="@wrap [var.source.wrapID]"\
    3="[!divxp.open!]"\
    4="{{code.dump(ns=\"[!code.pushlist.nsvar!]\" name=\"[!code.pushlist.nsname!]\" whitespace=\"True\" format=\"True\")}}"\
    5="[!divxp.close!]"\
    5a="@parw1"\
    6="[!var.source.wc_close_inline!]"\
    7="[!bmgreybg._close!]"\
    attrlist="1,2,2a,3,4,5,5a,6,7"

@html _id="td_item" _inherit="td" class="item" style="padding:5px;width:auto;font-size:1.3em;text-align:{{self._align}}" _align="center"
@html _id="td_desc" _inherit="td" class="item" style="padding:5px;width:auto;font-size:1.3em;text-align:{{self._align}}" _align="center"
@html _id="th_item" _tag="th"     _inherit="td_item"
@html _id="th_desc" _tag="th"     _inherit="td_desc" 
@html _id="table_2" _inherit="table" style="margin-left:auto;margin-right:auto"

@var table_2col="Macro for emitting 2 column table"\
    open="{{code.pushlines(t=\"@wrap null\n[_div_extras_.<+][table_2.<+]\")}}"\
    close="{{code.pushlines(t=\"[table.>][_div_extras_.>]\n@parw 1\")}}"\
    row="[tr.<]{{td_item.<}}{{self.item}}[td.>]{{td_desc.<}}{{self.desc}}[td.>][tr.>]"\
    row_alt="[tr.<]{{td_item.<}}*{{self.item}}*[td.>]{{td_desc.<}}{{self.desc}}[td.>][tr.>]"\
    header="[tr.<]{{th_item.<}}{{self.item}}[td.>]{{th_desc.<}}{{self.desc}}[td.>][tr.>]"\

@html _="bigtext" _inherit="span" \
        style="font-size:{{self._size}}"\
        _size="150%" \
        _format="[self.<]{{self._t}}[self.>]" \
        _prefix="{:{{self._cls}}}{{self._format}}"\
        _defsize_="150%"

@var _="big" _format="{{bigtext(_t=\"{{self.t}}\" _size=\"[html.bigtext._defsize_]\")}}"\
        red="{{bigtext._prefix(_t=\"{{self.t}}\" _cls=\".red\" _size=\"[html.bigtext._defsize_]\")}}"\
        blue="{{bigtext._prefix(_t=\"{{self.t}}\" _cls=\".blue\" _size=\"[html.bigtext._defsize_]\")}}"\
        green="{{bigtext._prefix(_t=\"{{self.t}}\" _cls=\".green\" _size=\"[html.bigtext._defsize_]\")}}"\
        multi="{{bigtext._prefix(_t=\"{{self.t}}\" _cls=\"{{self.cls}}\" _size=\"[html.bigtext._defsize_]\")}}"\
        ger="{{bigtext._prefix(_t=\"{{self.t}}\" _cls=\"{{self.cls}}\" _size=\"200%\")}}"\
        110="{{bigtext(_t=\"{{self.t}}\" _size=\"110%\")}}"\
        110p="{{bigtext._prefix(_t=\"{{self.t}}\" _size=\"110%\" _cls=\"{{self.cls}}\")}}"\
        120="{{bigtext(_t=\"{{self.t}}\" _size=\"120%\")}}"\
        120p="{{bigtext._prefix(_t=\"{{self.t}}\" _size=\"120%\" _cls=\"{{self.cls}}\")}}"\
        130="{{bigtext(_t=\"{{self.t}}\" _size=\"130%\")}}"\
        130p="{{bigtext._prefix(_t=\"{{self.t}}\" _size=\"130%\" _cls=\"{{self.cls}}\")}}"\
        142="{{bigtext(_t=\"{{self.t}}\" _size=\"142%\")}}"\
        142p="{{bigtext._prefix(_t=\"{{self.t}}\" _size=\"142%\" _cls=\"{{self.cls}}\")}}"\
        size="{{bigtext(_t=\"{{self.t}}\" _size=\"{{self.sz}}\")}}"\
        sizep="{{bigtext._prefix(_t=\"{{self.t}}\" _size=\"{{self.sz}}\" _cls=\"{{self.cls}}\")}}"\
        sz="150%"

//[big(t="text")] 
//[big.red(t="really big text")]
//[big.blue(t="really big text")]
//[big.green(t="really big text")]
//[big.multi(t="really big text" cls=".red.bigandbold")]
//[big.ger(t="really big text" cls=".green")]
//[big.green(t="really big text")]
