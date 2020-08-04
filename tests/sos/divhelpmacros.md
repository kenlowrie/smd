@var _dfixer="macro to replace div section wildcard with qualified divname"\
      1="{{code.attr_replace(s_str=\"$DIVNAME$\", r_var=\"_dfactory.dn\", attr=\"var.[!var._dfactory.dn!].wc_open\" repl_nl=\"False\")}}"\
      2="{{code.attr_replace(s_str=\"$DIVNAME$\", r_var=\"_dfactory.dn\", attr=\"var.[!var._dfactory.dn!].wc_close\" repl_nl=\"False\")}}"\
      3="{{code.attr_replace(s_str=\"$DIVNAME$\", r_var=\"_dfactory.dn\", attr=\"var.[!var._dfactory.dn!].wc_open_nd\" repl_nl=\"False\")}}"\
      4="{{code.attr_replace(s_str=\"$DIVNAME$\", r_var=\"_dfactory.dn\", attr=\"var.[!var._dfactory.dn!].wc_close_nd\" repl_nl=\"False\")}}"\
      attrlist="1,2,3,4"

[code.pushlist(attrlist="var._dfixer")]


//[dump(ns="var" name="section$" format="False" whitespace="False")]

        """
        if ret_type in [AdvancedNamespace._rtype_phase3, AdvancedNamespace._rtype_phase4]:
            # markdown phase2 and see if anything resolves, return if requested
            fmt_str = self._markdown(fmt_str)
            self.dbgPrint("P3-{1}-0: <em>{0}</em>".format(HtmlUtils.escape_html(fmt_str), passnum))
            if ret_type == AdvancedNamespace._rtype_phase3: return fmt_str

            # markdown 
            return self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))

        """
        #elif ret_type == AdvancedNamespace._rtype_phase4:
        #    fmt_str = self._markdown(fmt_str).replace('self.','{}{}.'.format(self.namespace, id0))
        #    self.dbgPrint("P4-{1}-0: <em>{0}</em>".format(HtmlUtils.escape_html(fmt_str), passnum))
        #    return fmt_str

        # And now, markdown again, to expand the self. namespace variables
        #s = self._markdown(fmt_str.replace('self.','{}{}.'.format(self.namespace, id0)))

        ##################s = self._markdown(fmt_str)



from html namespace

                # Markdown again to see if any new variables will expand, return if requested
                #fmt_str = self._markdown(fmt_str)
                #if ret_type == AdvancedNamespace._rtype_phase3: return fmt_str




                #//TODO: Was semantically different before. We translated {{}} and then marked down, and then did the self. replacement/markdown...
                #fmt_str = self._markdown(self.getElementPartial(el0).replace('{{','[').replace('}}',']'))
                # And now, markdown again, to expand the self. namespace variables
