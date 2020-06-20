// Common setup for the test scripts

@import "[sys.imports]/builtins.md"
@import "[sys.imports]/divs.md"
@import "[sys.imports]/report.md"

@import "[sys.imports]/def_html.md"
@import "[sys.imports]/def_head.md"
@import "[sys.imports]/def_body.md"

@var hash1="# [code.repeat.run(t=\"-\", c=\"42\")]"
@var hash2="## [code.repeat.run(t=\"-\", c=\"42\")]"
@var hash3="### [code.repeat.run(t=\"-\", c=\"42\")]"

@html _id="h2sh" _tag="h2" style="border-top: 3px solid black;border-bottom: 2px dashed black"
@html _id="h3sh" _tag="h3" style="font-size:1.3em;border-bottom: 3px solid black"
@html _id="divx" _inherit="_div_extras_"

@var dump_ns_list="var=\".\" html=\".\" link=\".\" image=\".\""
@var body_closure="@import \"{{sys.imports}}/def_bodyclose.md\""
@var doc_closure="@import \"{{sys.imports}}/def_close.md\""

@var wrap_h="{{code.pushlines(t=\"@wrap html.divx\n{{self.t}}\n@parw 1\")}}"\
    hash1="{{code.pushlines(t=\"@wrap html.divx\n{{var.hash1}}\n@parw 1\")}}"\
    hash2="{{code.pushlines(t=\"@wrap html.divx\n{{var.hash2}}\n@parw 1\")}}"\
    hash3="{{code.pushlines(t=\"@wrap html.divx\n{{var.hash3}}\n@parw 1\")}}"

//  NOTE: You have to push the body and doc closures in reverse order because the line cache gives precedence
//  to cached lines over actually reading from an imported file...
@var _id="testdoc"\
    begin="{{code.pushlines(t=\"{{html.h2sh.<}}Script: {{var.testdoc.title}}{{html.h2sh.>}}\n{{html.h3sh.<}}Purpose: {{var.testdoc.desc}}{{html.h3sh.>}}\n@wrap html.divx, p\")}}"\
    end="{{code.pushlines(t=\"@parw\n@dump {{dump_ns_list}}\n{{doc_closure}}\n{{body_closure}}\")}}"\
    title="name of script"\
    desc="purpose of script"

@var _id="testdoc_nw"\
    begin="{{code.pushlines(t=\"{{html.h2sh.<}}Script: {{var.testdoc_nw.title}}{{html.h2sh.>}}\n{{html.h3sh.<}}Purpose: {{var.testdoc_nw.desc}}{{html.h3sh.>}}\")}}"\
    end="{{code.pushlines(t=\"@dump {{dump_ns_list}}\n{{doc_closure}}\n{{body_closure}}\")}}"\
    title="name of script"\
    desc="purpose of script"
