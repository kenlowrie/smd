@var div_helper="{{self._all_keys_}}"\
    macro="macro.name"

// You have to use [!!] to set macro so it will expand before {{div_helper._null}} is processed, resulting in [code.pushlist.name] being what macro is set to...
@var dividers="{{self._public_keys_}}"\
    1="{{wrap_h.hash2}}"\
    2="@wrap divx,p"\
    3="{{div_helper._null_(macro=\"[!code.pushlist.name!]\")}}"\
    4="Testing {{var.div_helper.macro}}"\
    5="{{var.div_helper.macro}} testing complete"\
    6="@parw"\
    7="{{wrap_h.hash3}}"\
    8="{{self.{{var.dividers.attr}}}}"\
    start="1,2,3,4"\
    end="5,6,7"\
    attr="end"
@import "[sys.imports]/helpers.md"
@break

2=[get_value(v="dividers.4" ret_type="2")]



2=[get_value(v="section", ret_type="2")]
3=[get_value(v="section._format", ret_type="3" escape="True")]


@set _="pushlist" name="foo"
@dump code="pushlist"
[pushlist.name]
0=[get_value(v="dividers" ret_type="0")]
1=[get_value(v="dividers" ret_type="1")]
2=[get_value(v="dividers" ret_type="2")]
3=[get_value(v="dividers" ret_type="3")]
4=[get_value(v="dividers" ret_type="4")]
9=[get_value(v="dividers" ret_type="9")]
[dividers]
[bb]
//d.h.m = [div_helper.macro]
[sp][get_value(v="dividers.3" ret_type="0")]
[sp][get_value(v="dividers.3" ret_type="1")]
[sp][get_value(v="dividers.3" ret_type="2")]
[sp][get_value(v="dividers.3" ret_type="3")]
[sp][get_value(v="dividers.3" ret_type="4")]
[sp][get_value(v="dividers.3" ret_type="9")]
[bb]
[sp][get_value(v="dividers.4" ret_type="0")]
[sp][get_value(v="dividers.4" ret_type="1")]
[sp][get_value(v="dividers.4" ret_type="2")]
[sp][get_value(v="dividers.4" ret_type="3")]
[sp][get_value(v="dividers.4" ret_type="4")]
[sp][get_value(v="dividers.4" ret_type="9")]
[bb]
[sp][get_value(v="dividers.5" ret_type="0")]
[sp][get_value(v="dividers.5" ret_type="1")]
[sp][get_value(v="dividers.5" ret_type="2")]
[sp][get_value(v="dividers.5" ret_type="3")]
[sp][get_value(v="dividers.5" ret_type="4")]
[sp][get_value(v="dividers.5" ret_type="9")]
[bb]
[sp][get_value(v="dividers.7" ret_type="0")]
[sp][get_value(v="dividers.7" ret_type="1")]
[sp][get_value(v="dividers.7" ret_type="2")]
[sp][get_value(v="dividers.7" ret_type="3")]
[sp][get_value(v="dividers.7" ret_type="4")]
[sp][get_value(v="dividers.7" ret_type="9")]
[bb]
0=[sp][get_value(v="dividers.8" ret_type="0")]
1=[sp][get_value(v="dividers.8" ret_type="1")]
2=[sp][get_value(v="dividers.8" ret_type="2")]
3=[sp][get_value(v="dividers.8" ret_type="3")]
4=[sp][get_value(v="dividers.8" ret_type="4")]
9=[sp][get_value(v="dividers.8" ret_type="9")]
[bb]


@stop

@import "foo.bar"
@embed "peek.md"
@embed "peek.md"
@import "$/single.md"
