@var _id="avwrapper" \
          start="{{html._div_av_.<}}{{html.ul.<}}{{html.li.<}}" \
          endul="{{html.li.>}}{{html.ul.>}}" \
          enddiv="{{html.div.>}}" \
          shot_only="{{self.start}}{{self._s}}{{self.endul}}{{self.enddiv}}"\
          shot_with_desc="{{self.start}}{{self._s}}{{self.endul}}{{html.p.<}}{{self._d}}{{html.p.>}}{{self.enddiv}}"

//TODO: This should include all the AV related imports, so you only have to @import one thing...

// Can I use pushlines or something to make this a little nicer?
// [var.startshot] -> pushlines[ [var.avwrapper2.begin] [@wrap li]]
// [var.transition] -> pushlines [ [@parw] [var.avwrapper2.end_shots] [@wrap p]]
// [var.endshot] -> pushlines [ [@parw] [[var.avwrapper2.end] [@break] ]
// Isn't this a lot of what is going on in the music video script? Have I already solved this problem?

@var _id="avwrapper2" \
          begin="{{html._div_av_.<}}{{html.ul.<}}" \
          end_shots="{{html.ul.>}}" \
          end="{{html.div.>}}" \
          shot_only="{{self.start}}{{self._s}}{{self.endul}}{{self.enddiv}}"\
          shot_with_desc="{{self.start}}{{self._s}}{{self.endul}}{{html.p.<}}{{self._d}}{{html.p.>}}{{self.enddiv}}"\
          b1="[code.pushlines(t=\"{{var.avwrapper2.begin}}\n@wrap li\")]"\
          t1="[code.pushlines(t=\"@parw\n{{var.avwrapper2.end_shots}}\n@wrap p\")]"\
          e1="[code.pushlines(t=\"@parw\n{{var.avwrapper2.end}}\n@break\")]"\
          e2="[code.pushlines(t=\"@parw\n{{var.avwrapper2.end_shots}}\n{{var.avwrapper2.end}}\n@break\")]"\

