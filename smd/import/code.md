//TODO: Validate difference between $.attrname and self.attrname. 
//      
//      Looks like it's only attrs, and furthermore, it's a mesh between the static attrs
//      and the jit_attrs on the markdown call. Starts with static attrs of variable, and
//      then adds/updates those with the values from jit_attrs. Then, any references to
//      $.attr is replaced with value from the temp dict, and then the original dict is
//      restored, but with the side affect of any new attributes becoming sticky...
//      Add unittests to cover all these cases. Does not markdown {{var.attr}}

// code.esc_angles(url="string")
//    url = string to operate on
//    Replace all occurrences of '<' with '&lt;' and '>' with '&gt;'
@code _id="esc_angles"\
      type="eval"\
      src="print('{{self.url}}'.replace('<', '&lt;').replace('>','&gt;'))"\
      url="{{self._help}}"\
      _help="Usage: {{self._}}.run(url=\"[E.lt]text to escape[E.gt]\")[b]\
            [tab.<]**url** = string to operate on[tab.>][bb]\
            [tab.<]Replace all occurrences of *[E.lt]* with *[E.amp]lt;* and *[E.gt]* with *[E.amp]gt;*[tab.>]"

// code.escape(t="string")
//    t = string to operate on
//    Same as code.esc_angles, but also replaces '&' with '&amp;'
@code _id="escape"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html('{{self.t}}'))"\
      t="{{self._help}}"\
      _help="Usage: code.escape.run(t=\"text to escape\")"

// code.escape_var(v="var.attr")
//    v = existing variable / attribute to escape
//    Same as code.escape, but takes an existing variable or attribute name to operate on.
@code _id="escape_var"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html_var('{{self.v}}'))"\
      v="self._help"\
      _help="Usage: code.escape_var.run(v=\"var_to_esc\")"

// code.encodeURL(t="url string")
//    t = a URL to be encoded
//    Replaces all blanks i.e. ' ' with '%20'
//    If string begins with 'mailto:', string encoded using mix of dec/hex HTML character entities
@code _id="encodeURL"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encodeURL('{{self.t}}'))"\
      t="{{self._help}}"\
      _help="code.encodeURL(t=\"https://www.url.com?x=encode me\")"


// code.encode_smd(t="smd markdown")
//    t = an smd string that will be encoded for display
//
//    So, we have to use <> for [] and 2{ for {{ and 2} for }}. The entire list of replacements:
//          < - &lsqb; or [
//          > - &rsqb; or ]
//          2{ - &lcub;&lcub; or {{
//          2} - &rcub;&rcub; or }}
//          * - &#42;
//          @ - &#64;
//          ++ - &plus;&plus;
//          ~~ - &sim;&sim;
//    NOTE: We cannot use [] or {{}} directly, because the parser would replace them with markdown.
//          Also, you need to use [E.lp] for ( and [E.rp] for ), because () are used by the markdown
//          to identify parameters to the macros.
@code _id="encode_smd"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd('{{self.t}}'))"\
      t="{{self._help}}"\
      _help="Usage: code.encode_smd.run(t=\"smd markdown to encode\")"

// code.encode_smd_var(v="variable or attribute to encode as smd markdown")
//    v = existing variable / attribute to markdown as smd
//    Same as code.encode_smd, but takes an existing variable or attribute name to operate on
@code _id="encode_smd_var"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd_var('{{self.v}}'))"\
      v="self._help"\
      _help="Usage: code.encode_smd_var.run(v=\"var_to_encode\")"

// code.datetime_stamp(fmtstr="Python_strftime_format_string")
//    fmtstr is a Python strftime format string. Default is: %Y%m%d @ %H:%M:%S
//    NOTE: Unless you don't like the default format, you normally don't specify fmtstr
@code _id="datetime_stamp"\
      type="exec"\
      src="from time import strftime;print(strftime(\"{{self.fmtstr}}\"))"\
      _help="code.datetime_stamp(fmtstr=\"Python_strftime_format_string. Default: %Y%m%d @ %H:%M:%S\")"\
      fmtstr="%Y%m%d @ %H:%M:%S"

// code.repeat(t="chars to repeat" c="count")
//    t = character or string to repeat
//    c = number of times to repeat
//    e.g. code.repeat(t="%" c="42") will print 42 '%' characters
@code _id="repeat"\
      type="eval"\
      src="print('{}'.format('{{self.t}}'*{{self.c}}))"\
      t="{{self._help}}"\
      c="1"\
      _help="Usage: {{self._}}(t=\"chars to repeat\" c=\"# to repeat\")"

@code _id="get"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.get_ns_var('{{self.v}}')"\
      v="variable_name"\
      _help="Usage: {{self._}}(v=\"variable_name\")"

@code _id="get_variable"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.get_ns_var('$.v', $.ret_type, $.escape)"\
      v="variable_name"\
      ret_type="2"\
      escape="False"\
      _help="Usage: {{self._}}(v=\"variable_name\" ret_type=\"0|1|2\" escape=\"True|False\")"

@code _id="get_default"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.default('$.v', '$.default')"\
      v="default"\
      default="undefined variable"\
      _help="Usage: {{self._}}(v=\"variable_name\", default=\"default value\")"

// code.pushline(t="string to push onto input stream")
//    t = string to push onto input stream
//    NOTE: This macro does NOT split the string on the newline \n character. It will give
//          the illusion of doing so, but the newline will be treated as white space by a
//          browser. To push multiple lines, use either code.pushlines or code.pushvar.
//    See also: code.pushlines, code.pushvar
@code _id="pushline"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushline('{{self.t}}')"\
      t="{{self._help}}"\
      _help="Usage: {{self._}}(t=\"line to push onto input stream\")"

// code.pushlines(t="string to push onto input stream")
//    t = string to push onto input stream
//    NOTE: You can push multiple lines by inserting \n characters into the var/attr
//    See also: code.pushline, code.pushvar
@code _id="pushlines"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushlines('{{self.t}}')"\
      t="{{self._help}}"\
      _help="Usage: {{self._}}(t=\"lines to push onto input stream. separate lines with \\n\")"

// code.pushvar(v="var_to_push")
//    v = existing variable / attribute to push onto input stream
//    NOTE: You can push multiple lines by inserting \n characters into the var/attr
//    e.g. if var.x="line1\nline2" then [pushvar(v="var.x")] inserts two lines:
//      line1
//      line2
//    See also: code.pushline, code.pushlines
@code _id="pushvar"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushvar('{{self.v}}')"\
      v="self._help"\
      _help="Usage: {{self._}}(t=\"variable whose value will be pushed onto input stream. separate lines with \\n\")"

@code _id="ln_alias"\
      type="exec"\
      src="from .utility import CodeHelpers;print('@set _ns=\"link\" _id=\"{0}\" \
      {1}=\"{3}{0}.<{4}{2}{3}{0}.>{4}\"'.format('$.nm', \
      '$.attr', '$.lt', CodeHelpers.b(0), CodeHelpers.b(1)))"\
      nm="linkname" attr="_attr_name" lt="NEW_LINK_TEXT_HERE"\
      _help="***usage:* {{self._}}**(*nm=*\"existing_link_name\", *attr=*\"new_attr_name\", *lt=*\"new link text\")"

@code _id="append"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.append('$._var_', '$._txtvar_')"\
      _var_="_ns.var.attr_"\
      _txtvar_="_ns.txtvar.attr_"\
      _help="Usage: <strong>{{self._}}(_var_=<em>\"ns.var.attr\"</em>, _txtvar_=<em>\"ns.var.attr with text to add\"</em>)</strong>"

@code _id="equals"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.equals('$.v1', '$.v2', '$.true', '$.false')"\
      v1="_ns.var.attr_"\
      v2="_ns.txtvar.attr_"\
      true="_ns.var.true_"\
      false="_ns.var.false_"

// code.wrap_stack(w="< | > | # | tag.< | or tag.>" [encode="True | False"])
//    w = what you want to get from the wrap stack.
//          < - Will print the opening wrap tag
//          > - Will print the closing wrap tag
//          # - Will print the current wrap tag index
//          tag.< - Will print the opening wrap tags in text form
//          tag.> - Will print the closing wrap tags in text form
//    encode = True if you want the HTML escaped
//             False if you want the HTML raw (default)
//    See the documentation on @wrap for details on how to use this macro
@code _id="wrap_stack"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.wrap_stack('{{self.w}}', {{self.encode}})"\
      w="*"\
      encode="False"\
      _help="code.wrap_stack(w=\"< | > | # | tag.< | or tag.>\" [encode=\"True | False\"])"

@code _id="replace"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.replace('$.var', '$.val', '$.str')"\
      var="varname_to_replace"\
      val="value_to_insert"\
      str="string to operate on"

@code _id="attr_replace"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.attr_replace('$.s_str', '$.r_var', '$.attr')"\
      s_str="string_to_replace"\
      r_var="variable with new_value"\
      attr="ns.var.attr"

@code _id="attr_replace_str"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.attr_replace_str('$.s_str', '$.r_str', '$.attr')"\
      s_str="string_to_replace"\
      r_str="new_value"\
      attr="ns.var.attr"


// Things that belong elsewhere e.g. shots.md, etc. below here
@code _id="split_as"\
      type="exec"\
      src="from .utility import CodeHelpers;print(CodeHelpers.split_as('{{self.t}}'))"\
      t="Usage: {{self._}}(t=\"var._public_attrs_\")"


// Things that are no longer needed below here
