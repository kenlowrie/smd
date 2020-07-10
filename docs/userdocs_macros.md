// These macros are helpers for the manual. Not really useful outside of the guide...
// Except for the unittests, which includes this whenever including markdown from the manual...
@var smdtag="@@{{self.il}}" p="" il="[encode_smd(t=\"{{self.p}}\")]" b="**{{self.il}}**" em="*{{self.il}}*" emb="***{{self.il}}***"

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
