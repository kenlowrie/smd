@code _id="esc_html"\
      type="eval"\
      src="print('$.url'.replace('<', '&lt;').replace('>','&gt;'))"\
      url="Usage: code.esc_html.run(url=\"text to escape\")"
@code _id="escape2"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html('$.__t'))"\
      __t="Usage: code.escape.run(t=\"text to escape\")"
@code _id="escape"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html('$.t'))"\
      t="Usage: code.escape.run(t=\"text to escape\")"
@code _id="encodeURL"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encodeURL('$.t'))"\
      t="code.encodeURL(t=\"https://www.url.com to encode\")"
@code _id="split_as"\
      type="exec"\
      src="from .utility import CodeHelpers;print(CodeHelpers.split_as('{{self.t}}'))"\
      t="Usage: {{self._}}(t=\"var._public_attrs_\")"
@code _id="pushline"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushline('{{self.t}}')"\
      t="Usage: {{self._}}(t=\"line to push onto input stream\")"
@code _id="pushvar"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushvar('{{self.t}}')"\
      t="Usage: {{self._}}(t=\"variable whose value will be pushed onto input stream\")"
@code _id="pushlines"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushlines('{{self.t}}')"\
      t="Usage: {{self._}}(t=\"lines to push onto input stream. separate lines with \\n \")"
@code _id="datetime_stamp"\
      type="exec"\
      src="from time import strftime;print(strftime(\"{{self.fmtstr}}\"))"\
      _format="{{self.last}}"\
      fmtstr="%Y%m%d @ %H:%M:%S"
@code _id="ln_alias"\
      type="exec"\
      src="from .utility import CodeHelpers;print('@set _id=\"{0}\" \
      {1}=\"{3}{0}.<{4}{2}{3}{0}.>{4}\"'.format('$.nm', \
      '$.attr', '$.lt', CodeHelpers.b(0), CodeHelpers.b(1)))"\
      nm="link.?" attr="_attr_name" lt="NEW_LINK_TEXT_HERE"\
      _help_="<strong><em>usage:</em> \
                {{self._}}</strong>(<em>nm=</em>&quot;link.name_to_add_alias&quot;, \
                <em>attr=</em>&quot;attr_name&quot;, \
                <em>lt=</em>&quot;new link text&quot;)"
@code _id="get"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.get_ns_var('{{self.v}}')"\
      v="variable_name"\
      _help_="Usage: {{self._}}(v=\"variable_name\")"
@code _id="get_default"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.default('$.v', '$.default')"\
      v="default"\
      default="undefined variable"\
      _help_="Usage: {{self._}}(v=&quot;variable_name&quot;, default=&quot;default value&quot;)"
@code _id="repeat"\
      type="eval"\
      src="print('{}'.format('$.t'*$.c))"\
      t="repeat_str "\
      c="2"
@code _id="append"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.append('$._var_', '$._txtvar_')"\
      _var_="_ns.var.attr_"\
      _txtvar_="_ns.txtvar.attr_"\
      _help_="Usage: <strong>{{self._}}(_var_=<em>&quot;ns.var.attr&quot;</em>, _txtvar_=<em>&quot;ns.var.attr with text to add&quot;</em>)</strong>"
@code _id="equals"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.equals('$.v1', '$.v2', '$.true', '$.false')"\
      v1="_ns.var.attr_"\
      v2="_ns.txtvar.attr_"\
      true="_ns.var.true_"\
      false="_ns.var.false_"
@code _id="replace"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.replace('$.var', '$.val', '$.str')"\
      var="varname_to_replace"\
      val="value_to_insert"\
      str="string to operate on"
@code _id="wrap_stack"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.wrap_stack('{{self.w}}', {{self.encode}})"\
      w="*"\
      encode="False"
@code _id="encode_smd"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd('$.t'))"\
      t="Usage: code.encode_smd.run(t=\"smd markdown to encode\")"
@code _id="escape_var"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html_var('$.v'))"\
      v="Usage: code.escape.run(v=\"var_to_esc\")"
@code _id="encode_smd_var"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd_var('$.v'))"\
      v="Usage: code.encode_smd_var.run(v=\"var_to_encode\")"
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
