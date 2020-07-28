// Set the defaults for code.dump so I don't have to specify them every time...
@import "[sys.imports]/builtins.md"
@import "[sys.imports]/divs.md"
@set _id="code.dump" help="False" ns="code" whitespace="True"
//@debug toggle="markdown"
@var test="{{code.pushlines(t=\"{{self.1}}\n{{self.2}}\n{{self.3}}\n{{self.4}}\")}}"\
    1="{{generic(t=\"**Dump of code.[!var.test.name!]**:\")}}"\
    2="{{box.wc_open}}"\
    3="{{code.dump(name=\"[!var.test.name!]\")}}"\
    4="{{box.wc_close}}"\
    al="1,2,3,4"\
    name="esc_angles"
//@debug toggle="utility"
[section.wc_open]
[dump(ns="code" name="pushlist")]
@debug toggle="utility"
[pushlist]
[pushlist(attrlist="var.test.al")]
@debug toggle="utility"
[section.wc_close]
[pushlist.?]
@stop

[test.1]
[test.2]
[test.3]
[test.4]
@dump var="test$"

@stop




@var x="{{var.y}}"
@var y="{{var.z}}"
@var z="{{var.a}}"
@var a="{{var.b}}"
@var b="{{var.c}}"
@var c="{{var.x}}"
@debug on="markdown"
//[x]




[ln_factory(nm="tk" hr="https://tkdocs.com/tutorial/install.html" t="Tk")]
@set _ns="link" _="tk" tkinter="{{self.<}}tkinter{{self.>}}" target="_blank"
@dump link="tk"
//@debug on="markdown"
// Next line crashes parser b/c tkinter is *public* and refers to itself {{self.<}} ... Can I detect this?
[tk]

@var lb="["
@var rb="]"
{{code.encode(t="{{self.fu}}" u="{{self.{{self.bar}}}}")}}

When you are marking down, you have to drill down to the lowest level thing, then evaluate that, by recursively calling it, so that you can force it to completely evaluation, before coming back to pick up the next thing. That would work, right?

what if:

D1="b"
y="{{lb}}{{D1}}{{rb}}"
{{x(a="{{y}}")}}

So, {{x(a="{{y}}")}} parses to {{y}} first, which becomes [b], which 

D1="b"
y="{{lb}}{{D1}}{{rb}}"
[x(a="[y]")]

[y] is first, but we have to call _markdown() to evaluate it, so that getValue() will parse {{lb}}{{D1}}{{rb}} to [D1] and call _markdown()



