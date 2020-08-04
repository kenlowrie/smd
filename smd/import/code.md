//TODO: Validate difference between $.attrname and self.attrname. 

@code _id="esc_angles"\
      type="eval"\
      src="print('{{self.url}}'.replace('<', '&lt;').replace('>','&gt;'))"\
      url="{{self._help}}"\
      _help="[sp.2]*{{self._}}(url=\"[E.lt]text to escape[E.gt]\")*[bb]\
[sp.4]**url** = string to operate on[bb]\
[sp.4]Replace all occurrences of *[E.lt]* with *[E.amp]lt;* and *[E.gt]* with *[E.amp]gt;* in string **url**"

@code _id="escape"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html('{{self.t}}'))"\
      t="{{self._help}}"\
      _help="[sp.2]*{{self._}}(t=\"text to escape\")*[bb]\
[sp.4]**t** = string to operate on[bb]\
[sp.4]Same as code.esc_angles, but also replaces *[E.amp]* with *[E.amp]amp;*"

@code _id="escape_var"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.escape_html_var('{{self.v}}'))"\
      v="self._help"\
      _help="[sp.2]*{{self._}}(v=\"var_to_esc\")*[bb]\
[sp.4]**v** = existing variable / attribute to escape[bb]\
[sp.4]Same as code.escape, but takes an existing variable or attribute name to operate on."

@code _id="encodeURL"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encodeURL('{{self.t}}'))"\
      t="{{self._help}}"\
      _help="[sp.2]*{{self._}}(t=\"https://www.url.com?x=encode me\")*[bb]\
[sp.4]**t** = a URL string to be encoded[bb]\
[sp.4]Replaces all blanks in URL string e.g. \" \" with \"*%20*\"[bb]\
[sp.4]**NOTE:** If **t** begins with **mailto:** the entire string is encoded using a mix of dec/hex HTML character entities"

@code _id="encode_smd"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd('{{self.t}}'))"\
      t="{{self._help}}"\
      _help="[sp.2]*{{self._}}(t=\"smd markdown to encode\")*[bb]\
[sp.4]**t** = an smd string that will be encoded for display[bb]\
[sp.4]Use *[E.lt][sp][E.gt]* for *[E.lb][sp][E.rb]*, *2{* for *[E.lcb2]*, *2}* for *[E.rcb2]*, *2[E.plus]* for *[E.ins]* and *2[E.tilde]* for *[E.del]*.[bb]\
[sp.4]The entire list of replacements is:[b]\
[sp.6]*[E.lt]* becomes *[E.amp]lsqb;*[b]\
[sp.6]*[E.gt]* becomes *[E.amp]rsqb;*[b]\
[sp.6]*2[E.lcb]* becomes *[E.amp]lcub;[E.amp]lcub;*[b]\
[sp.6]*2[E.rcb]* becomes *[E.amp]rcub;[E.amp]rcub;*[b]\
[sp.6]*[E.ast]* becomes *[E.amp]#42;*[b]\
[sp.6]*[E.at]* becomes *[E.amp]#64;*[b]\
[sp.6]*2[E.plus]* becomes *[E.amp]plus;[E.amp]plus;*[b]\
[sp.6]*2[E.tilde]* becomes *[E.amp]tilde;[E.amp]tilde;*[bb]\
[sp.4]**NOTE1:** Do not use square brackets, curly braces, double plus or double tilde directly, because the parser will replace them with markdown.[bb]\
[sp.4]**NOTE2:** You need to use *[E.lb]E.lp[E.rb]* for *(* and *[E.lb]E.rp[E.rb]* for *)*, because parenthesis are used by the markdown to identify parameters to the macros."

@code _id="encode_smd_var"\
      type="exec"\
      src="from .utility import HtmlUtils;print(HtmlUtils.encode_smd_var('{{self.v}}'))"\
      v="self._help"\
      _help="[sp.2]*{{self._}}(v=\"var_to_encode\")*[bb]\
[sp.4]**v** = existing variable / attribute to markdown as smd[bb]\
[sp.4]Same as code.encode_smd, but takes an existing variable or attribute name to operate on"

@code _id="datetime_stamp"\
      type="exec"\
      src="from time import strftime;print(strftime(\"{{self.fmtstr}}\"))"\
      fmtstr="%Y%m%d @ %H:%M:%S"\
      _help="[sp.2]*{{self._}}(fmtstr=\"%Y%m%d @ %H:%M:%S\")*[bb]\
[sp.4]**fmtstr** is a Python strftime format string. The default format is: %Y%m%d @ %H:%M:%S[bb]\
[sp.4]**NOTE:** Unless you don't like the default format, you normally don't specify **fmtstr**"

@code _id="repeat"\
      type="eval"\
      src="print('{}'.format('{{self.t}}'*{{self.c}}))"\
      t="{{self._help}}"\
      c="1"\
      _help="[sp.2]*{{self._}}(t=\"chars to repeat\" c=\"# to repeat\")*[bb]\
[sp.4]**t** = character or string to repeat[b]\
[sp.4]**c** = number of times to repeat[bb]\
[sp.4]Example: code.repeat(t=\"%\" c=\"42\") will print 42 \"%\" percent characters"

@code _id="get"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.get_ns_var('{{self.v}}')"\
      v="variable_name"\
      _help="[sp.2]*{{self._}}(v=\"variable_name\")*[bb]\
[sp.4]**v** - variable / attribute name to get[bb]\
[sp.4]Emits the value of the variable / attribute **v**"

@code _id="get_value"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.get_ns_var('$.v', $.ret_type, $.escape, $.esc_smd)"\
      v="variable_name"\
      ret_type="9"\
      escape="False"\
      esc_smd="False"\
      _help="[sp.2]*{{self._}}(v=\"variable_name\" ret_type=\"0|1|2|3|9\" escape=\"True|False\" esc_smd=\"True|False\")*[bb]\
[sp.4]**v** - variable / attribute name to get[bb]\
[sp.4]**ret_type** - how to emit the value (0, 1, 2, 3 or 9)[b]\
[sp.6]**0** - will return the value raw i.e. not marked down[b]\
[sp.6]**1** - will return the value with the initial markdown pass, but without handling delayed expansion[b]\
[sp.6]**2** - will return the after replacing {{ with [ and }} with ][b]\
[sp.6]**3** - will return the after replacing **self.** with **ns.varname.**[b]\
[sp.6]**9** - will return the marked down value (default)[bb]\
[sp.4]**escape** - True to escape the HTML, False otherwise (default)[bb]\
[sp.4]**esc_smd** - True to escape the SMD, False otherwise (default)[bb]\
[sp.4]Emits the value of the variable / attribute **v**"

@code _id="get_default"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.default('$.v', '$.default')"\
      v="var or attr name"\
      default="default value"\
      _help="[sp.2]*{{self._}}(v=\"variable_name\", default=\"default value\")*[bb]\
[sp.4]**v** - The variable / attribute name to get[b]\
[sp.4]**default** - value to return if **v** is not defined[bb]\
[sp.4]Returns the value of **v** unless undefined, in which case it returns **default**"

@code _id="pushline"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushline('{{self.t}}')"\
      t="{{self._help}}"\
      _help="[sp.2]*{{self._}}(t=\"line to push onto input stream\")*[bb]\
[sp.4]t = string to push onto input stream[bb]\
[sp.4]**NOTE:** This macro does NOT split the string on the newline \n character. It will give[b]\
[sp.4]the illusion of doing so, but the newline will be treated as white space by a[b]\
[sp.4]browser. To push multiple lines, use either code.pushlines or code.pushvar.[bb]\
[sp.4]See also: code.pushlines, code.pushvar"

@code _id="pushlines"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushlines('{{self.t}}')"\
      t="{{self._help}}"\
      _help="[sp.2]*{{self._}}(t=\"lines to push onto input stream. separate lines with \n\")*[bb]\
[sp.4]t = string to push onto input stream[bb]\
[sp.4]**NOTE:** You can push multiple lines by inserting \n characters into the var/attr[bb]\
[sp.4]See also: code.pushline, code.pushvar"

@code _id="pushvar"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushvar('{{self.v}}')"\
      v="self._help"\
      _help="[sp.2]*{{self._}}(t=\"variable whose value will be pushed onto input stream. separate lines with \n\")*[bb]\
[sp.4]v = existing variable / attribute to push onto input stream[bb]\
[sp.4]**NOTE:** You can push multiple lines by inserting \n characters into the var/attr[b]\
[sp.4]e.g. if var.x=\"line1\nline2\" then pushvar(v=\"var.x\") inserts two lines:[bb]\
[sp.6]line1[b]\
[sp.6]line2[bb]\
[sp.4]See also: code.pushline, code.pushlines"

@code _id="ln_alias"\
      type="exec"\
      src="from .utility import CodeHelpers;print('@set _ns=\"link\" _id=\"{0}\" \
      {1}=\"{3}{0}.<{4}{2}{3}{0}.>{4}\"'.format('{{self.nm}}', \
      '{{self.attr}}', '{{self.lt}}', CodeHelpers.b(0), CodeHelpers.b(1)))"\
      nm="linkname" attr="_attr_name" lt="NEW_LINK_TEXT_HERE"\
      _help="[sp.2]*{{self._}}(**nm=**\"existing_link_name\", **attr=**\"_new_PRIVATE_attr_name\", **lt=**\"new link text\")*[bb]\
[sp.4]**nm** - The name of the existing @link variable you are adding an alias to[b]\
[sp.4]**attr** - The name of a new PRIVATE attribute that will be added[b]\
[sp.4]**lt** - The new link text you want to use for the hyperlink[bb]\
[sp.4]This macro adds a new alias for an existing link. That is, alternate text for the same underlying anchor.[bb]\
[sp.4]**NOTE:** Be sure you specify a PRIVATE attribute i.e. begins with ***_*** (underscore). If you do not, you[b]\
[sp.4]will create an infinite recursion during markdown because the open tag will reference the new attribute!"

@code _id="append"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.append('{{self.attr1}}', '{{self.attr2}}')"\
      attr1="ns.var.attr"\
      attr2="ns.txtvar.attr"\
      _help="[sp.2]*{{self._}}(attr1=\"ns.var.attr\", attr2=\"ns.var.attr with text to append\")*[bb]\
[sp.4]**attr1** - attribute to append text string to[b]\
[sp.4]**attr2** - attribute containing the text to append to **attr1**[bb]\
[sp.4]Appends text from **attr2** to existing attribute **attr1**."

@code _id="equals"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.equals('{{self.v1}}', '{{self.v2}}', '{{self.true}}', '{{self.false}}')"\
      v1="_ns.var.attr_"\
      v2="_ns.txtvar.attr_"\
      true="_ns.var.true_"\
      false="_ns.var.false_"\
      _help="[sp.2]*{{self._}}(v1=\"ns.var.attr1\", v2=\"ns.var.attr2\" true=\"ns.var.attr3\" false=\"ns.var.attr4\")[bb]*\
[sp.4]**v1** - attribute 1 for comparison[b]\
[sp.4]**v2** - attribute 2 for comparison[b]\
[sp.4]**true** - attribute to push if **v1** == **v2**[b]\
[sp.4]**false** - attribute to push if **v1** != **v2**[bb]\
[sp.4]Compare attribute **v1** to attribute **v2** and push line onto input stream based on results.[bb]\
[sp.4]This macro does a case-sensitive string comparison of **v1** and **v2**"

@code _id="wrap_stack"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.wrap_stack('{{self.w}}', {{self.encode}})"\
      w="*"\
      encode="False"\
      _help="[sp.2]*{{self._}}(w=\"< | > | # | tag.< | or tag.>\" [encode=\"True | False\"])*[bb]\
[sp.4]**w** = what you want to get from the wrap stack.[b]\
[sp.6][E.lt] - Will print the opening wrap tag[b]\
[sp.6][E.gt] - Will print the closing wrap tag[b]\
[sp.6]# - Will print the current wrap tag index[b]\
[sp.6]tag.[E.lt] - Will print the opening wrap tags in text form[b]\
[sp.6]tag.[E.gt] - Will print the closing wrap tags in text form[bb]\
[sp.4]**encode** = True if you want the HTML escaped, False for raw (default)[bb]\
[sp.4]See the documentation on @wrap for details on how to use this macro"

@code _id="replace"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.replace('{{self.var}}', '{{self.val}}', '{{self.str}}')"\
      var="varname_to_replace"\
      val="value_to_insert"\
      str="string to operate on"\
      _help="[sp.2]*{{self._}}(var=\"search_str\", val=\"attr_with_rep_val\" str=\"ns.var.attr to operate on\")*[bb]\
[sp.4]**var** - the string we are searching for[b]\
[sp.4]**val** - attribute containing replacement string[b]\
[sp.4]**str** - attribute containing string to operate on[bb]\
[sp.4]Replaces all occurrences of **var** with **val** in **str** and then push **str** onto input stream.[b]\
[sp.4]**NOTE:** Does NOT modify the attribute **str** in memory; simply pushes modified string onto input stream."

@code _id="attr_replace"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.attr_replace('{{self.s_str}}', '{{self.r_var}}', '{{self.attr}}', {{self.repl_nl}})"\
      s_str="string_to_replace"\
      r_var="variable with new_value"\
      attr="ns.var.attr"\
      repl_nl="True"\
      _help="[sp.2]*{{self._}}(s_str=\"search_str\", r_var=\"attr_with_rep_val\" attr=\"ns.var.attr to operate on\" repl_nl=\"True | False\")*[bb]\
[sp.4]**s_str** - the string we are searching for[b]\
[sp.4]**r_var** - attribute containing replacement string[b]\
[sp.4]**attr** - attribute containing string to operate on[b]\
[sp.4]**repl_nl** - replace escaped newline with newline (default:True)[bb]\
[sp.4]Replaces all occurrences of **s_str** with **r_var** in **attr** and updates **attr**.[b]\
[sp.4]**NOTE:** Like **code.replace** except modifies **attr** directly and does NOT push anything onto the input stream."

@code _id="attr_replace_str"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.attr_replace_str('{{self.s_str}}', '{{self.r_str}}', '{{self.attr}}', {{self.repl_nl}})"\
      s_str="string_to_replace"\
      r_str="new_value"\
      attr="ns.var.attr"\
      repl_nl="True"\
      _help="[sp.2]*{{self._}}(s_str=\"search_str\", r_str=\"repl_str\" attr=\"ns.var.attr to operate on\" repl_nl=\"True | False\")*[bb]\
[sp.4]**s_str** - the string we are searching for[b]\
[sp.4]**r_str** - the replacement string[b]\
[sp.4]**attr** - attribute containing string to operate on[b]\
[sp.4]**repl_nl** - replace escaped newline with newline (default:True)[bb]\
[sp.4]Replaces all occurrences of **s_str** with **r_str** in **attr** and updates **attr**.[b]\
[sp.4]**NOTE:** Like **code.attr_replace**, but accepts replacement string directly instead of indirectly via attribute."

@code _id="dump"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.dump('{{self.ns}}', '{{self.name}}', {{self.format}}, {{self.whitespace}}, {{self.help}})"\
      ns="var"\
      name=".*"\
      format="False"\
      whitespace="False"\
      help="False"\
      _help="[sp.2]*{{self._}}(ns=\"namespace\", name=\"var name regex\" format=\"False\" whitespace=\"False\" help=\"False\")*[bb]\
[sp.4]**ns** - the namespace that **name** is in[b]\
[sp.4]**name** - the variable/attribute name regex to dump[b]\
[sp.4]**format** - use formatting to aid readability[bb]\
[sp.4]**whitespace** - include prefix whitespace (HTML entities) and breaks [E.lt]br /[E.gt][bb]\
[sp.4]**help** - dump the help attribute value (if present)[bb]\
[sp.4]Dumps one or more variables that match **name**, formatting according to **format** and **whitespace**.[bb]\
[sp.4]**NOTE:** The default values work best when running **smd** interactively."

@var _id = "vpl"\
      attrlist="1,2,3,4,5"\
      1="Line 1" 2="Line 2" 3="Line 3" 4="Line 4" 5="Line 5"

@code _id="pushlist"\
      type="exec"\
      src="from .utility import CodeHelpers;CodeHelpers.pushlist('{{self.attrlist}}')"\
      attrlist="var.vpl.attrlist"\
      _help="[sp.2]*{{self._}}(attrlist=\"var.attr.list\")*[bb]\
[sp.4]**attrlist** - an existing variable or attribute[b]\
[sp.6]If **attrlist** is a variable, then that variable *must* contain an attribute named **attrlist**.[b]\
[sp.6]If **attrlist** is an attribute, then that attribute *must* contain a list of other attributes in the same variable.[bb]\
[sp.4]This macro pushes one or more lines specified by **attrlist** onto the input stream. The attributes must be in the same variable.[bb]\
[sp.4]**NOTE:** See **var.vpl** for a template of what the **attrlist** variable should look like."
