
//@var _="_df_var_SAVEME" _str="@var _=\"$DIVNAME$\"\
      _format=\"@@ {{html._div_$DIVNAME$_.<}}{{html._p_$DIVNAME$_.<}}{{self.t}}{{html._p_$DIVNAME$_.>}}{{html._div_$DIVNAME$_.>}}\" \
      with_content=\"@@ {{html._div_$DIVNAME$_.<}}{{html._p_$DIVNAME$_.<}}{{self.t}}{{html._p_$DIVNAME$_.>}}{{html._p_$DIVNAME$_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}\" \
      sID=\"$DIVNAME$\"\
      t=\"$DIVNAME$ default title\" \
      c=\"$DIVNAME$ default comment\""







































// real 1st try is below

@var div_name="???Need A Name???"

@var _="_df_parts"\
      html_1="@html _=\"_div_{{var.div_name}}_\" _inherit=\"div\" class=\"{{var.div_name}}\""\
      html_2="@html _=\"_div_{{var.div_name}}_pbb\" _inherit=\"_div_{{var.div_name}}_\" class=\"{{var.div_name}} pbb\""\
      html_3="@html _=\"_p_{{var.div_name}}_\" _inherit=\"p\" class=\"divTitle\""\
      html_4="@html _=\"_p_{{var.div_name}}_content_\" _inherit=\"p\" style=\"font-size:1.2em\""

@var _="_df_var_parts"\
      0_all="@var _=\"{{var.div_name}}\" _format=\"{{self.1_format}}\" with_content=\"{{self.2_with_content}}\" t=\"{{self.3_t}}\" c=\"{{self.4_c}}\""\
      1_format="@@ %{html._div_{{var.div_name}}_.<}%%{html._p_{{var.div_name}}_.<}%%{self.t}%%{html._p_{{var.div_name}}_.>}%%{html._div_{{var.div_name}}_.>}%\""\
      2_with_content="@@ %{html._div_{{var.div_name}}_.<}%%{html._p_{{var.div_name}}_.<}%%{self.t}%%{html._p_{{var.div_name}}_.>}%%{html._p_{{var.div_name}}_content_.<}%%{self.c}%%{html.p.>}%%{html.div.>}%"\
      3_t="{{var.div_name}} default title"\
      4_c="{{var.div_name}} default comment"\
      5="@set _ns=\"var\" _=\"{{var.div_name}}\" _format=\"{{html._div_{{var.div_name}}}}\""

@var _dfactory=""\
      setup="@set _ns=\"var\" _=\"div_name\" _format=\"{{self.dn}}\""\
      name="{{code.pushline(t=\"{{self.setup}}\")}}"\
      part1="{{code.pushline(t=\"{{var._df_parts.html_1}}\")}}"\
      part2="{{code.pushlines(t=\"{{var._df_parts.html_4}}\n{{var._df_parts.html_3}}\n{{var._df_parts.html_2}}\")}}"\
      part3="{{code.pushline(t=\"{{var._df_var_parts.0_all}}\")}}"\
      part4="{{code.pushline(t=\"{{var._df_var_parts.5}}\")}}"\
      part5="{{code.replace(var=\"$DIVNAME$\", val=\"var.div_name\", str=\"var._mt_._string\")}}"\
      part6="{{code.replace(var=\"$DIVNAME$\", val=\"var.div_name\", str=\"var._ms_._string\")}}"\

@var _="_ms_" _string="@html _=\"_div_$DIVNAME$_\" _inherit=\"div\" class=\"$DIVNAME$\"\
      \n@html _=\"_div_$DIVNAME$_pbb\" _inherit=\"_div_$DIVNAME$_\" class=\"$DIVNAME$ pbb\"\
      \n@html _=\"_p_$DIVNAME$_\" _inherit=\"p\" class=\"divTitle\"\
      \n@html _=\"_p_$DIVNAME$_content_\" _inherit=\"p\" style=\"font-size:1.2em\""


@var _="xt" _str="$$DN$$ hello\n$$DN$$ world"
@var echo = "echo"
@debug toggle="utility"
[code.replace(var="$$DN$$" val="var.echo" str="var.xt._str")]
@debug toggle="utility"



@var _="_mt_" _string="@var $DIVNAME$=\"@@ {{html._div_$DIVNAME$_.<}}{{html._p_$DIVNAME$_.<}}{{self.t}}{{html._p_$DIVNAME$_.>}}{{html._div_$DIVNAME$_.>}}\" \
          with_content=\"@@ {{html._div_$DIVNAME$_.<}}{{html._p_$DIVNAME$_.<}}{{self.t}}{{html._p_$DIVNAME$_.>}}{{html._p_$DIVNAME$_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}\" \
          t=\"$DIVNAME$ default title\" \
          c=\"$DIVNAME$ default comment\""

@dump var=".*factory|_mt_"
-----------
TRY 2
[_dfactory.name(dn="plain7")]
//[_dfactory.part1]
//[_dfactory.part2]
//[_dfactory.part3]
//[_dfactory.part4]
@debug toggle="utility"
[_dfactory.part6]
[_dfactory.part5]
@debug toggle="utility"

Create variable
[code.replace(var="$DIVNAME$", val="var.div_name", str="var._mt_._string")]

@dump var="plain" html=".*plain"

[plain.with_content]
[plain.with_content(t="foo" c="bar")]
@stop

@break
Create variable
@var MAKEVAR="@var {{self.name}}=\"{{var._\""
@dump var="test"
Update variable
[code.replace(var="$.dn", val="var.div_name", str="var.test")]

@dump var="test"

@stop

//[code.replace(var="%%" val="[" str="var.section._format")]
-----------
@dump var=".*factory_parts|div_name"
-----------&&&&&&&&&

@dump var=".*factory"

@parw

@dump html=".*xxxsection" var="section|div_name"


@stop