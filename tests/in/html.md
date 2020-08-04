@import "$/testsetup.md"

[var.testdoc.begin(title="html.md" desc="Testing @html namespace")]

@var ns="html"

@import "$/nsbasic.md"

[wrap_h.hash1]
[plain(t="Specific Namespace testing for ***@[ns]*** namespace")]

[plain(t="Testing @html builtin functions")]

0=[get_value(v="section", ret_type="0")]
1=[get_value(v="section", ret_type="1")]
2=[get_value(v="section", ret_type="2")]
// Return type 3 will return as [var.section.inline], which will then proceed to get marked down by the parser...
// It's a strange side effect, b/c of how it's being used here. You ask for an attribute value, and it gives it to you, but it isn't fully marked down yet (b/c you asked for it that way... :) In this case, you have to use esc_smd="True"
3=[get_value(v="section", ret_type="3")]
// This is a real janky workaround if you don't want to esc the SMD....
//@var x="[get_value(v=\"section\", ret_type=\"3\")]"
//3=[escape_var(v="x")]
3=[get_value(v="section", ret_type="3" esc_smd="True")]
9=[get_value(v="section", ret_type="9" escape="True")]

[b]**v="_section_div"**[b]
0=[get_value(v="_section_div_", ret_type="0")]
1=[get_value(v="_section_div_", ret_type="1")]
2=[get_value(v="_section_div_", ret_type="2")]
3=[get_value(v="_section_div_", ret_type="3" escape="True")]
9=[get_value(v="_section_div_", ret_type="9" escape="True")]
[b]**v="_section_div.[E.lt]"**[b]
0=[get_value(v="_section_div_.<", ret_type="0")]
1=[get_value(v="_section_div_.<", ret_type="1")]
2=[get_value(v="_section_div_.<", ret_type="2")]
3=[get_value(v="_section_div_.<", ret_type="3" escape="True")]
9=[get_value(v="_section_div_.<", ret_type="9" escape="True")]
[b]**v="_section_div.[E.lt]+"**[b]
0=[get_value(v="_section_div_.<+", ret_type="0")]
1=[get_value(v="_section_div_.<+", ret_type="1")]
2=[get_value(v="_section_div_.<+", ret_type="2")]
3=[get_value(v="_section_div_.<+", ret_type="3" escape="True")]
9=[get_value(v="_section_div_.<+", ret_type="9" escape="True" )]


[plain(t="Testing adding new @html builtins")]

@import "[sys.root]/docs/userdocs_macros.md"

[var.plain(t="User manual sections for [smdhtml.b]")]

[var.toc.wc_open(t="Table of Contents - Unittest [smdhtml.b]")]
@wrap nop
[b]
@import "[sys.root]/docs/section/nshtml-inc.md"
@parw
[var.toc.wc_close]

[wrap_h(t="###Review link bookmarks from nshtml-inc.md")]
@dump link="^ug_ns_html|ug_html_"

@import "[sys.root]/docs/section/nshtml-doc.md"


@set dump_ns_list="html=\".\" help=\"f\""

[var.testdoc.end]
