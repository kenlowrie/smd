// Variables that abstract the different types of DIVs
@import "[sys.imports]/html.md"

@html _id="_div_extras_" \
      _inherit="div" \
      class="extras"

@var _="_df_html_p_" _str="@html _=\"_$DIVNAME$_div_\" _inherit=\"div\" class=\"$DIVNAME$\"\
      \n@html _=\"_$DIVNAME$_div_pbb_\" _inherit=\"_$DIVNAME$_div_\" class=\"$DIVNAME$ pbb\"\
      \n@html _=\"_$DIVNAME$_p_\" _inherit=\"p\" class=\"divTitle\"\
      \n@html _=\"_$DIVNAME$_p_content_\" _inherit=\"p\""

@var _="_df_html_code_" _str="@html _=\"_$DIVNAME$_div_\" _inherit=\"div\" class=\"$DIVNAME$\"\
      \n@html _=\"_$DIVNAME$_\" _inherit=\"code\" style=\"font-size:1.4em;font-weight:bold\"\
      \n@html _=\"_$DIVNAME$_content_\" _inherit=\"code\" style=\"font-size:1.2em\""

@var _="_df_html_simple_" _str="@html _=\"_$DIVNAME$_div_\" _inherit=\"div\" class=\"extras\"\
      \n@html _=\"_$DIVNAME$_div_pbb_\" _inherit=\"_$DIVNAME$_div_\" class=\"extras pbb\"\
      \n@html _=\"_$DIVNAME$_div_pba_\" _inherit=\"_$DIVNAME$_div_\" class=\"extras pba\"\
      \n@html _=\"_$DIVNAME$_p_\" _inherit=\"p\" class=\"$DIVNAME$\""

@var _df_var_template="usage: this is meant to be inherited by _df_var_"\
      _format="@@ {{self.inline}}"\
      nd="@@{{self.inline_nd}}"\
      with_content="@@ {{self.wc_inline}}"\
      with_content_nd="@@ {{self.wc_inline_nd}}"\
      wc_inline="{{self.wc_open_inline}}{{self.wc_content}}{{self.wc_close_inline}}"\
      wc_inline_nd="{{self.wc_open_inline_nd}}{{self.wc_content}}{{self.wc_close_inline_nd}}"\
      wc_open="{{code.pushlines(t=\"@@{{self.wc_open_inline}}\n@wrap {{self.wrapID}}\")}}"\
      wc_close="{{code.pushlines(t=\"@parw 1\n@@{{self.wc_close_inline}}\")}}"\
      wc_open_nd="{{code.pushlines(t=\"@@{{self.wc_open_inline_nd}}\n@wrap {{self.wrapID}}\")}}"\
      wc_close_nd="{{code.pushlines(t=\"@parw 1\n@@{{self.wc_close_inline_nd}}\")}}"

@var _="_df_var_p_" _str="@var _=\"$DIVNAME$\" _inherit=\"_df_var_template\" \
      inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_p_.<}}{{self.t}}{{html._$DIVNAME$_p_.>}}{{html._$DIVNAME$_div_.>}}\"\
      wc_open_inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_p_.<}}{{self.t}}{{html._$DIVNAME$_p_.>}}\"\
      wc_close_inline=\"{{html.div.>}}\"\
      wc_content=\"{{html._$DIVNAME$_p_content_.<}}{{self.c}}{{html.p.>}}\"\
      sID=\"$DIVNAME$\"\
      wrapID=\"_$DIVNAME$_p_content_\"\
      t=\"$DIVNAME$ default title\" \
      c=\"$DIVNAME$ default content\""

@var _="_df_var_code_" _str="@var _=\"$DIVNAME$\" _inherit=\"_df_var_template\" \
      inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_.<}}{{self.t}}{{html._$DIVNAME$_.>}}{{html._$DIVNAME$_div_.>}}\"\
      wc_open_inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_.<}}{{self.t}}{{html._$DIVNAME$_.>}}\"\
      wc_close_inline=\"{{html.div.>}}\"\
      wc_content=\"{{html._$DIVNAME$_content_.<}}{{self.c}}{{html._$DIVNAME$_content_.>}}\"\
      sID=\"$DIVNAME$\"\
      wrapID=\"_$DIVNAME$_content_\"\
      t=\"$DIVNAME$ default title\" \
      c=\"$DIVNAME$ default content\""
      
@var _="_df_var_simple_" _str="@var _=\"$DIVNAME$\" _inherit=\"_df_var_template\" \
      inline=\"{{html._$DIVNAME$_div_.<}}{{self.inline_nd}}{{html._$DIVNAME$_div_.>}}\"\
      inline_nd=\"{{html._$DIVNAME$_p_.<}}{{self.t}}{{html._$DIVNAME$_p_.>}}\"\
      wc_open_inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_p_.<}}\"\
      wc_close_inline=\"{{html.p.>}}{{html.div.>}}\"\
      wc_open_inline_nd=\"{{html._$DIVNAME$_p_.<}}\"\
      wc_close_inline_nd=\"{{html.p.>}}\"\
      wc_content=\"{{self.c}}\"\
      sID=\"$DIVNAME$\"\
      wrapID=\"nop\"\
      t=\"$DIVNAME$ default title\" \
      c=\"$DIVNAME$ default content\""
      
@var _dfactory="{{self.as_p}}"\
      as_p="{{self.p}}{{self.var_p}}"\
      as_code="{{self.code}}{{self.var_code}}"\
      as_simple="{{self.simple}}{{self.var_simple}}"\
      var_p="{{code.replace(var=\"$DIVNAME$\", val=\"_dfactory.dn\", str=\"var._df_var_p_._str\")}}"\
      var_code="{{code.replace(var=\"$DIVNAME$\", val=\"_dfactory.dn\", str=\"var._df_var_code_._str\")}}"\
      var_simple="{{code.replace(var=\"$DIVNAME$\", val=\"_dfactory.dn\", str=\"var._df_var_simple_._str\")}}"\
      p="{{code.replace(var=\"$DIVNAME$\", val=\"_dfactory.dn\", str=\"var._df_html_p_._str\")}}"\
      code="{{code.replace(var=\"$DIVNAME$\", val=\"_dfactory.dn\", str=\"var._df_html_code_._str\")}}"\
      simple="{{code.replace(var=\"$DIVNAME$\", val=\"_dfactory.dn\", str=\"var._df_html_simple_._str\")}}"\
      dn="UNDEFINED"\
      usage="**usage: [E.lb]_dfactory(dn=\"divName\")[E.rb]**"
      

[_dfactory(dn="section")]
@var _="section_pbb" _inherit="section"
[code.attr_replace_str(s_str="html._section_div" r_str="html._section_div_pbb" attr="var.section_pbb.inline")]
[code.attr_replace_str(s_str="html._section_div" r_str="html._section_div_pbb" attr="var.section_pbb.wc_open_inline")]

[_dfactory(dn="toc")]
[_dfactory(dn="syntax")]

[_dfactory(dn="review")]
@html _="_review_pba_div_" _inherit="_review_div_" class="review pba"

[_dfactory(dn="plain")]
@set _="html._plain_p_" class="plainTitle"

//as_code uses a different markup: essentially code instead of p
[_dfactory.as_code(dn="source")]

//as_simple is a much simpler version of markup for notes, questions, etc.
[_dfactory.as_simple(dn="note")]
[_dfactory.as_simple(dn="vo")]
[_dfactory.as_simple(dn="box")]
[_dfactory.as_simple(dn="question")]
[_dfactory.as_simple(dn="greyout")]
[_dfactory.as_simple(dn="important")]

@var extras="@@{{html._div_extras_.<}}{{self.c}}{{html.div.>}}" c="default content"

@var divxp="@@ {{self.inline}}"\
      inline="{{self.open}}{{self.c}}{{self.close}}"\
      c="default content"\
      open="{{html._div_extras_.<}}{{html.p.<}}"\
      close="{{html.p.>}}{{html.div.>}}"

// Terminal doesn't really fit the factory, and it seems unnecessary to 1 off like I did with code...

@html _="prewrap" _inherit="pre" style="white-space:pre-wrap"

@html _id="_terminal_div_" \
      _tag="div" \
      class="plain" style="padding-left:3em;padding-right:3em"
 
@html _id="_terminal_prewrap_" \
      _inherit="prewrap" \
      class="divTitle"\
      style="background-color:lightgray;font-style:italic;padding:5px 10px;{{html.prewrap.style}}"
@html _id="_terminal_prewrap_content_" \
      _inherit="prewrap" \
      class="divTitle"\
      style="background-color:lightgray;font-weight:100;padding:5px 10px;{{html.prewrap.style}}"

@var _id="terminal" \
          _format="@@ {{self.inline}}" \
          inline="{{html._terminal_div_.<}}{{html._terminal_prewrap_content_.<}}{{self.t}}{{html._terminal_prewrap_content_.>}}{{html._terminal_div_.>}}"\
          with_content="@@ {{self.wc_inline}}" \
          wc_inline="{{self.wc_open_inline}}{{self.c}}{{self.wc_close_inline}}"\
          wc_open="{{code.pushlines(t=\"@wrap nop\n{{self.wc_open_inline}}\")}}"\
          wc_close="{{code.pushlines(t=\"{{self.wc_close_inline}}\n@parw 1\")}}"\
          wc_open_inline="{{html._terminal_div_.<}}{{html._terminal_prewrap_.<}}{{self.t}}{{html._terminal_prewrap_.>}}{{html._terminal_prewrap_content_.<}}"\
          wc_close_inline="{{html.prewrap.>}}{{html.div.>}}"\
          t="This is your terminal title" \
          c="This is your terminal content"

@var _id="terminal2" _inherit="terminal"\
          wc_open="{{code.pushlines(t=\"@@{{self.wc_open_inline}}\n@wrap html._terminal_prewrap_content_\")}}"\
          wc_close="{{code.pushlines(t=\"@parw 1\n@@{{self.wc_close_inline}}\")}}"\
          wc_open_inline="{{html._terminal_div_.<}}{{html._terminal_prewrap_.<}}{{self.t}}{{html._terminal_prewrap_.>}}"\
          wc_close_inline="{{html.div.>}}"\
          wc_open_content="{{code.pushlines(t=\"@wrap nop\n{{html._terminal_prewrap_content_.<}}\")}}"\
          wc_close_content="{{code.pushlines(t=\"{{html._terminal_prewrap_content_.>}}\n@parw 1\")}}"

// specialized ordered and unordered lists


@var _="_lists_"\
      _format="@@ {{self.inline}}"\
      with_content="@@ {{self.wc_inline}}"\
      wc_inline="{{self.wc_open_inline}}{{self.c}}{{self.wc_close_inline}}"\
      wc_open="{{code.pushlines(t=\"@wrap li\n@@{{self.wc_open_inline}}\")}}"\
      wc_close="{{code.pushlines(t=\"@@{{self.wc_close_inline}}\n@parw 1\")}}"

@var _="ulist"\
      _inherit="_lists_"\
      inline="{{html._div_extras_.<}}{{html.ulist.<}}{{self.t}}{{html.ulist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.ulist.<}}"\
      wc_close_inline="{{html.ul.>}}{{html.div.>}}"\
      sID="ulist"\
      t="var.{{self.sID}} default title" \
      c="var.{{self.sID}} default content"

@var _="ulistplain" _inherit="ulist"\
      inline="{{html._div_extras_.<}}{{html.ulistplain.<}}{{self.t}}{{html.ulist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.ulistplain.<}}"

@var _="olist"\
      _inherit="_lists_"\
      inline="{{html._div_extras_.<}}{{html.olist.<}}{{self.t}}{{html.olist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.olist.<}}"\
      wc_close_inline="{{html.ol.>}}{{html.div.>}}"\
      sID="olist"\
      t="var.{{self.sID}} default title" \
      c="var.{{self.sID}} default content"

@var _="olistAlpha" _inherit="olist"\
      inline="{{html._div_extras_.<}}{{html.olistAlpha.<}}{{self.t}}{{html.olist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.olistAlpha.<}}"

@var _="olistRoman" _inherit="olist"\
      inline="{{html._div_extras_.<}}{{html.olistRoman.<}}{{self.t}}{{html.olist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.olistRoman.<}}"

@var _="olistGreek" _inherit="olist"\
      inline="{{html._div_extras_.<}}{{html.olistGreek.<}}{{self.t}}{{html.olist.>}}{{html._div_extras_.>}}"\
      wc_open_inline="{{html._div_extras_.<}}{{html.olistGreek.<}}"


//@dump var="[_dfactory.dn]|review" html=".*[_dfactory.dn]|^_div_rev|^_p_rev"
//@dump var="[_dfactory.dn]|code" html=".*[_dfactory.dn]|^_div_cod|^_code"
//@dump var="note" html="^.*note"
