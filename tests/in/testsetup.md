// Common setup for the test scripts

@import "[sys.imports]/builtins.md"
@import "[sys.imports]/divs.md"
@import "[sys.imports]/report.md"

@import "[sys.imports]/def_html.md"
@import "[sys.imports]/def_head.md"
@import "[sys.imports]/def_body.md"

@html _id="docwrap" _tag="p" style="font-size:1.2em"
@html _id="h2sh" _tag="h2" style="border-top: 3px solid black;border-bottom: 2px dashed black"
@html _id="h3sh" _tag="h3" style="font-size:1.3em;border-bottom: 3px solid black"
@html _id="divx" _inherit="_div_extras_"

@var dump_ns_list="var=\".\" html=\".\" link=\".\" image=\".\""
@var body_closure="@import \"{{sys.imports}}/def_bodyclose.md\""
@var doc_closure="@import \"{{sys.imports}}/def_close.md\""
@var wrap_h="{{code.pushlines(t=\"@wrap html.divx\n{{self.t}}\n@parw 1\")}}" hash1="{{code.pushlines(t=\"@wrap html.divx\n{{var.hash1}}\n@parw 1\")}}"


//  NOTE: You have to push the body and doc closures in reverse order because the line cache gives precedence
//  to cached lines over actually reading from an imported file...
@var _id="testdoc"\
    begin="{{code.pushlines(t=\"{{html._div_plain_.<}}\n{{html.h2sh.<}}Script: {{var.testdoc.title}}{{html.h2sh.>}}\n{{html.h3sh.<}}Purpose: {{var.testdoc.desc}}{{html.h3sh.>}}\n@wrap docwrap\")}}"\
    end="{{code.pushlines(t=\"@parw\n{{html._div_plain_.>}}\n@dump {{dump_ns_list}}\n{{doc_closure}}\n{{body_closure}}\")}}"\
    x="##{{self.title}}\
    y="###{{self.desc}}\
    title="name of script"\
    desc="purpose of script"

@var _id="testavdoc"\
    begin="{{code.pushlines(t=\"{{html.h2sh.<}}Script: {{var.testavdoc.title}}{{html.h2sh.>}}\n{{html.h3sh.<}}Purpose: {{var.testavdoc.desc}}{{html.h3sh.>}}\")}}"\
    end="{{code.pushlines(t=\"@dump {{dump_ns_list}}\n{{doc_closure}}\n{{body_closure}}\")}}"\
    x="##{{self.title}}\
    y="###{{self.desc}}\
    title="name of script"\
    desc="purpose of script"
