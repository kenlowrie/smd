@link _id="_template_" \
      _format="{{self.<}}{{self._text}}{{self.>}}" \
      _text="Usage: link.{{self._}}(_text=\"Text to Link\")" \
      href="www.YOUR-URL-GOES-HERE.com" \
      _asurl="{{self.<}}{{code.esc_angles.run(url=\"{{self.href}}\")}}{{self.>}}" \
      _qlink="{{self.<}}{{self._qtext}}{{self.>}}" \
      _qtext="SETMETOLINKTEXT"
@link _id="ln_factory" \
      _format="@link _id=\"{{self.nm}}\" _inherit=\"_template_\" href=\"{{self.hr}}\" \
      _text=\"{{self.t}}\""
@link _id="bm_template" \
      id="{{self._}}" \
      _format="@@ {{self._inline}}" \
      _link_o="<a href=\"#{{self.id}}\">"\
      link="{{self._link_o}}{{self.text}}</a>" \
      text="TEXT-TO-DISPLAY-FOR-LINK"   \
      _inline="<a id=\"{{self.id}}\"></a>"\
      _qlink="{{self._link_o}}{{self._qtext}}</a>" \
      _qtext="SETMETOLINKTEXT"
@link _id="bm_factory" \
      _format="@link _id=\"{{self.nm}}\" _inherit=\"bm_template\" text=\"{{self.t}}\""
