// Variables that abstract the different types of DIVs
@import "[sys.imports]/html.md"

@html _id="_div_extras_" \
      _inherit="div" \
      class="extras"

@var div_help_methods="{{self._public_keys_}}"\
      tc_variants="[sp.2]**Methods**[b]\
[sp.4]***NONE*** - If no method specified, uses **inline** with raw (i.e. *@@ inline*)[b]\
[sp.4]with_content(t,c) - **wc_inline** raw (i.e. *@@ wc_inline*)[b]\
[sp.4]inline(t) - insert $DIVNAME$ div with text **t**[b]\
[sp.4]wc_inline(t,c) - insert $DIVNAME$ div with title **t** and content **c**[b]\
[sp.4]wc_open(t) - open a $DIVNAME$ div with title **t** and **@wrap {{var.$DIVNAME$.wrapID}}** ready for content[b]\
[sp.4]wc_close - close $DIVNAME$ div opened with **wc_open**[b]\
[sp.4]wc_open_inline(t) - like **wc_open** but does not use **@wrap**[b]\
[sp.4]wc_close_inline - close $DIVNAME$ div opened with **wc_open_inline**"\
      justc_variants="[sp.2]**Methods**[b]\
[sp.4]***NONE*** - If no method specified, uses **inline** with raw prefix (i.e. *@@ inline*)[b]\
[sp.4]with_content(c) - **wc_inline** raw (i.e. *@@ wc_inline*)[b]\
[sp.4]inline(c) - insert $DIVNAME$ DIV with content **c**[b]\
[sp.4]inline_nd(c) - insert $DIVNAME$ with content **c** without DIV wrapper[b]\
[sp.4]wc_inline(c) - insert $DIVNAME$ DIV with content **c**[b]\
[sp.4]wc_open - open a $DIVNAME$ DIV and **@wrap {{var.$DIVNAME$.wrapID}}** ready for content[b]\
[sp.4]wc_close - close $DIVNAME$ DIV opened with **wc_open**[b]\
[sp.4]wc_open_inline - like **wc_open** but does not use **@wrap**[b]\
[sp.4]wc_close_inline - close $DIVNAME$ DIV opened with **wc_open_inline**[b]"\
      nd="[sp.4]***No DIV* variants**[b]\
[sp.4]nd(c) - **inline_nd** with raw prefix (i.e. *@@ inline_nd*)[b]\
[sp.4]nd_inline(c) - same as **inline_nd**[b]\
[sp.4]nd_open - open $DIVNAME$ without DIV wrapper using **wrap {{var.$DIVNAME$.wrapID}}**[b]\
[sp.4]nd_close - close $DIVNAME$ opened with **nd_open**[b]\
[sp.4]nd_open_inline - like **nd_open** but does not use **@wrap**[b]\
[sp.4]nd_close_inline - close $DIVNAME$ opened with **nd_open_inline**[b]"

@var div_help_attrs="{{self._public_keys_}}"\
      main="[sp.2]**Attributes**[b]\
[sp.4]**sID** - the div identifier **$DIVNAME$**[b]\
[sp.4]**wrapID** - the **@wrap** tag(s) *{{var.$DIVNAME$.wrapID}}*"

@var div_help_common="{{self._public_keys_}}"\
      var_p="[sp.2]*$DIVNAME$(t=[E.dquot]title[E.dquot] c=[E.dquot]content[E.dquot])*[bb]\
[sp.2]**Common Parameters**[b]\
[sp.4]**t** - The title to use for the $DIVNAME$ div[b]\
[sp.4]**c** = The content to use for the $DIVNAME$ div"\
      var_code="common **$DIVNAME$** var code"\
      var_simple="[sp.2]*$DIVNAME$(c=[E.dquot]content[E.dquot])*[bb]\
[sp.2]**Common Parameters**[b]\
[sp.4]**c** = The content to use for the $DIVNAME$ div"\
      var_term="common var **terminal**"\
      var_term2="common var **terminal2**"\
      var_lists="[sp.2]*$DIVNAME$(c=[E.dquot]content[E.dquot])*[bb]\
[sp.2]**Common Parameters**[b]\
[sp.4]**c** = The content to use for the $DIVNAME$[bb]\
[sp.2]**Attributes**[b]\
[sp.4]**tag** = An [smdhtml.b] variable used to wrap content when **_tag** methods are used[b]\
[sp.4]**wrap** = An [smdhtml.b] or [smdvar.b] variable used to wrap content when **_wrap** methods are used[bb]\
[sp.2]**Public Methods**[b]\
[sp.4]***NONE*** - If no method specified, uses **_inline** with raw prefix (i.e. *@@ _inline*)[b]\
[sp.4]**with_content**(c) - emit content **c** wrapped with *_open_inline* / *_close_inline*[b]\
[sp.4]**wc_open(c)** - emit *_open*[b]\
[sp.4]**wc_close** - emit *_close*[b]\
[sp.4]**wc_tag_open(c)** - emit *_open* prefixed with *tag.[E.lt]*[b]\
[sp.4]**wc_tag_close** - emit *_close* with *tag.[E.gt]* appended[b]\
[sp.4]**wc_wrap_open(c)** - emit *_open* prefixed with *wrap._open*[b]\
[sp.4]**wc_wrap_close** - emit *_close* with *wrap._close* appended[bb]\
[sp.2]**Private Methods**[b]\
[sp.4]**_content** - emit *html.li.[E.lt]* **c** *html.li.[E.gt]*[b]\
[sp.4]**_inline** - emit *$DIVNAME$.[E.lt]* **_content** *$DIVNAME$.[E.gt]*[b]\
[sp.4]**_open** - set [smdwrap.b] li then emit *_open_inline*[b]\
[sp.4]**_close** - emit *_close_inline* then [smdparw.b] 1[b]\
[sp.4]**_open_inline** - emit *html.$DIVNAME$.[E.lt]*[b]\
[sp.4]**_close_inline** - emit *html.$DIVNAME$.[E.gt]*"

@var div_help_var_p="[var.div_help_common.var_p][bb][var.div_help_attrs.main][bb][var.div_help_methods.tc_variants]"
@var div_help_var_code="[var.div_help_var_p]"
@var div_help_var_simple="[var.div_help_common.var_simple][bb][var.div_help_attrs.main][bb][var.div_help_methods.justc_variants][b][var.div_help_methods.nd]"
@var div_help_var_term="[var.div_help_var_p]"
@var div_help_var_term2="[var.div_help_var_p]"
@var div_help_var_lists="[var.div_help_common.var_lists]"

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
      with_content="@@ {{self.wc_inline}}"\
      wc_inline="{{self.wc_open_inline}}{{self.wc_content}}{{self.wc_close_inline}}"\
      wc_open="{{code.pushlines(t=\"@@{{self.wc_open_inline}}\n@wrap {{self.wrapID}}\")}}"\
      wc_close="{{code.pushlines(t=\"@parw 1\n@@{{self.wc_close_inline}}\")}}"

@var _="_df_var_p_" _str="@var _=\"$DIVNAME$\" _inherit=\"_df_var_template\" \
      inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_p_.<}}{{self.t}}{{html._$DIVNAME$_p_.>}}{{html._$DIVNAME$_div_.>}}\"\
      wc_open_inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_p_.<}}{{self.t}}{{html._$DIVNAME$_p_.>}}\"\
      wc_close_inline=\"{{html.div.>}}\"\
      wc_content=\"{{html._$DIVNAME$_p_content_.<}}{{self.c}}{{html.p.>}}\"\
      sID=\"$DIVNAME$\"\
      wrapID=\"_$DIVNAME$_p_content_\"\
      t=\"$DIVNAME$ default title\" \
      c=\"$DIVNAME$ default content\"\
      _help=\"[var.div_help_var_p]\""

@var _="_df_var_code_" _str="@var _=\"$DIVNAME$\" _inherit=\"_df_var_template\" \
      inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_.<}}{{self.t}}{{html._$DIVNAME$_.>}}{{html._$DIVNAME$_div_.>}}\"\
      wc_open_inline=\"{{html._$DIVNAME$_div_.<}}{{html._$DIVNAME$_.<}}{{self.t}}{{html._$DIVNAME$_.>}}\"\
      wc_close_inline=\"{{html.div.>}}\"\
      wc_content=\"{{html._$DIVNAME$_content_.<}}{{self.c}}{{html._$DIVNAME$_content_.>}}\"\
      sID=\"$DIVNAME$\"\
      wrapID=\"_$DIVNAME$_content_\"\
      t=\"$DIVNAME$ default title\" \
      c=\"$DIVNAME$ default content\"\
      _help=\"[var.div_help_var_code]\""
      
@var _="_df_var_simple_nd_template"\
      _inherit="_df_var_template"\
      nd="@@{{self.inline_nd}}"\
      nd_inline="{{self.inline_nd}}"\
      nd_open="{{code.pushlines(t=\"@@{{self.nd_open_inline}}\n@wrap {{self.wrapID}}\")}}"\
      nd_close="{{code.pushlines(t=\"@parw 1\n@@{{self.nd_close_inline}}\")}}"

@var _="_df_var_simple_" _str="@var _=\"$DIVNAME$\" _inherit=\"_df_var_simple_nd_template\" \
      inline=\"{{html._$DIVNAME$_div_.<}}{{self.inline_nd}}{{html._$DIVNAME$_div_.>}}\"\
      inline_nd=\"{{html._$DIVNAME$_p_.<}}{{self.c}}{{html._$DIVNAME$_p_.>}}\"\
      wc_open_inline=\"{{html._$DIVNAME$_div_.<}}{{self.nd_open_inline}}\"\
      wc_close_inline=\"{{html.p.>}}{{html.div.>}}\"\
      wc_content=\"{{self.c}}\"\
      nd_open_inline=\"{{html._$DIVNAME$_p_.<}}\"\
      nd_close_inline=\"{{html.p.>}}\"\
      sID=\"$DIVNAME$\"\
      wrapID=\"nop\"\
      c=\"$DIVNAME$ default content\"\
      _help=\"[var.div_help_var_simple]\""
      
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
[_dfactory.as_simple(dn="generic")]

@var extras="@@{{html._div_extras_.<}}{{self.c}}{{html.div.>}}" c="default content" _help="[sp.2]*{{self._}}(c=[E.dquot]content[E.dquot])*[bb]\
[sp.2]**Parameters**[b]\
[sp.4]**c** = The content to use for the {{self._}}[bb]\
[sp.2]**Methods**[b]\
[sp.4]***NONE*** - emit content **c** wrapped with div class=\"extras\""

@var divxp="@@ {{self.inline}}"\
      inline="{{self.open}}{{self.c}}{{self.close}}"\
      c="default content"\
      open="{{self._open}}"\
      close="{{self._close}}"\
      _open="{{html._div_extras_.<}}{{html.p.<}}"\
      _close="{{html.p.>}}{{html.div.>}}"\
      _help="[sp.2]*{{self._}}(c=[E.dquot]content[E.dquot])*[bb]\
[sp.2]**Common Parameters**[b]\
[sp.4]**c** = The content to use for the {{self._}}[bb]\
[sp.2]**Public Methods**[b]\
[sp.4]***NONE*** - If no method specified, uses **inline** with raw prefix (i.e. *@@ inline*)[b]\
[sp.4]**inline(c)** - emit content **c** wrapped with div class=\"extras\" p[b]\
[sp.4]**open** - invokes *_open*[b]\
[sp.4]**close** - invokes *_close*[bb]\
[sp.2]**Private Methods**[b]\
[sp.4]**_open** - emit open tags *div class=\"extras\" p*[b]\
[sp.4]**_close** - emit close tags */p /div*"

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
          c="This is your terminal content" \
          _help="[var.div_help_var_term]"
[code.attr_replace_str(s_str="$DIVNAME$" r_str="terminal" attr="var.terminal._help")]

@var _id="terminal2" _inherit="terminal"\
          wc_open="{{code.pushlines(t=\"@@{{self.wc_open_inline}}\n@wrap html._terminal_prewrap_content_\")}}"\
          wc_close="{{code.pushlines(t=\"@parw 1\n@@{{self.wc_close_inline}}\")}}"\
          wc_open_inline="{{html._terminal_div_.<}}{{html._terminal_prewrap_.<}}{{self.t}}{{html._terminal_prewrap_.>}}"\
          wc_close_inline="{{html.div.>}}"\
          wc_open_content="{{code.pushlines(t=\"@wrap nop\n{{html._terminal_prewrap_content_.<}}\")}}"\
          wc_close_content="{{code.pushlines(t=\"{{html._terminal_prewrap_content_.>}}\n@parw 1\")}}"\
          _help="[var.div_help_var_term2]"
[code.attr_replace_str(s_str="$DIVNAME$" r_str="terminal2" attr="var.terminal2._help")]

// specialized ordered and unordered lists
//TODO.md: Might want to consider adapting the Note DIVs to follow this model, or vice-versa
//TODO.md: Finish writing the _help strings for all these builtins.

@var _="_lists_"\
      _format="@@ {{self._inline}}"\
      with_content="@@ {{self._open_inline}}{{self._content}}{{self._close_inline}}"\
      wc_open="{{code.pushlines(t=\"{{self._open}}\")}}"\
      wc_close="{{code.pushlines(t=\"{{self._close}}\")}}"\
      wc_tag_open="{{code.pushlines(t=\"@@{{[!self.tag!].<}}\n{{self._open}}\")}}"\
      wc_tag_close="{{code.pushlines(t=\"{{self._close}}\n@@{{[!self.tag!].>}}\")}}"\
      wc_wrap_open="{{code.pushlines(t=\"@@{{[!self.wrap!]._open}}\n{{self._open}}\")}}"\
      wc_wrap_close="{{code.pushlines(t=\"{{self._close}}\n@@{{[!self.wrap!]._close}}\")}}"\
      tag="html.divx"\
      wrap="var.divxp"\
      _open="@wrap li\n@@{{self._open_inline}}"\
      _close="@@{{self._close_inline}}\n@parw 1"\
      _content="{{html.li.<}}{{self.c}}{{html.li.>}}"\
      _help="[var.div_help_var_lists]"

//    {{var._lists_.get_wrap}}
//    get_wrap="@wrap [!code.wrap_stack(w=\"tag.<\")!],html.li"
//    wc_open_inline="{{code.pushlines(t=\"@wrap li\n@@{{self._open_inline}}\")}}"
//    wc_close_inline="{{code.pushlines(t=\"@@{{self._close_inline}}\n@parw 1\")}}"

@var _="ulist"\
      _inherit="_lists_"\
      _inline="{{html.ulist.<}}{{self._content}}{{html.ulist.>}}"\
      _open_inline="{{html.ulist.<}}"\
      _close_inline="{{html.ulist.>}}"\
      sID="ulist"\
      c="var.{{self.sID}} default content"

@var _="ulistplain" _inherit="ulist"\
      _inline="{{html.ulistplain.<}}{{self._content}}{{html.ulist.>}}"\
      _open_inline="{{html.ulistplain.<}}"

[code.attr_replace_str(s_str="$DIVNAME$" r_str="ulist" attr="var.ulist._help")]
[code.attr_replace_str(s_str="$DIVNAME$" r_str="ulistplain" attr="var.ulistplain._help")]

@var _="olist"\
      _inherit="_lists_"\
      _inline="{{html.olist.<}}{{self._content}}{{html.olist.>}}"\
      _open_inline="{{html.olist.<}}"\
      _close_inline="{{html.olist.>}}"\
      sID="olist"\
      c="var.{{self.sID}} default content"

@var _="olistAlpha" _inherit="olist"\
      _inline="{{html.olistAlpha.<}}{{self._content}}{{html.olist.>}}"\
      _open_inline="{{html.olistAlpha.<}}"

@var _="olistalpha" _inherit="olist"\
      _inline="{{html.olistalpha.<}}{{self._content}}{{html.olist.>}}"\
      _open_inline="{{html.olistalpha.<}}"

@var _="olistRoman" _inherit="olist"\
      _inline="{{html.olistRoman.<}}{{self._content}}{{html.olist.>}}"\
      _open_inline="{{html.olistRoman.<}}"

@var _="olistroman" _inherit="olist"\
      _inline="{{html.olistroman.<}}{{self._content}}{{html.olist.>}}"\
      _open_inline="{{html.olistroman.<}}"

@var _="olistGreek" _inherit="olist"\
      _inline="{{html.olistGreek.<}}{{self._content}}{{html.olist.>}}"\
      _open_inline="{{html.olistGreek.<}}"

@var _="olistgreek" _inherit="olist"\
      _inline="{{html.olistgreek.<}}{{self._content}}{{html.olist.>}}"\
      _open_inline="{{html.olistgreek.<}}"

[code.attr_replace_str(s_str="$DIVNAME$" r_str="olist" attr="var.olist._help")]
[code.attr_replace_str(s_str="$DIVNAME$" r_str="olistAlpha" attr="var.olistAlpha._help")]
[code.attr_replace_str(s_str="$DIVNAME$" r_str="olistGreek" attr="var.olistGreek._help")]
[code.attr_replace_str(s_str="$DIVNAME$" r_str="olistRoman" attr="var.olistRoman._help")]
[code.attr_replace_str(s_str="$DIVNAME$" r_str="olistalpha" attr="var.olistalpha._help")]
[code.attr_replace_str(s_str="$DIVNAME$" r_str="olistgreek" attr="var.olistgreek._help")]
[code.attr_replace_str(s_str="$DIVNAME$" r_str="olistroman" attr="var.olistroman._help")]

//@dump var="[_dfactory.dn]|review" html=".*[_dfactory.dn]|^_div_rev|^_p_rev"
//@dump var="[_dfactory.dn]|code" html=".*[_dfactory.dn]|^_div_cod|^_code"
//@dump var="note" html="^.*note"
