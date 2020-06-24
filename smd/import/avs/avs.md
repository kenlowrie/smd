//TODO: Remove all the commented out code
//TODO: Should this include all the AV related imports, so you only have to @import one thing?

//@var _id="avwrapper" \
//          start="@@ {{html._div_av_.<}}{{html.ul.<}}{{html.li.<}}" \
//          endul="@@ {{html.li.>}}{{html.ul.>}}" \
//          enddiv="@@ {{html.div.>}}" \
//          shot_only="{{self.start}}{{self._s}}{{self.endul}}{{self.enddiv}}"\
//          shot_with_desc="{{self.start}}{{self._s}}{{self.endul}}{{html.p.<}}{{self._d}}{{html.p.>}}{{self.enddiv}}"


//@var _id="avwrapper2" \
//          begin="@@ {{html._div_av_.<}}{{html.ul.<}}" \
//          end_shots="@@ {{html.ul.>}}" \
//          end="@@ {{html.div.>}}" \
//          shot_only="{{self.start}}{{self._s}}{{self.endul}}{{self.enddiv}}"\
//          shot_with_desc="{{self.start}}{{self._s}}{{self.endul}}{{html.p.<}}{{self._d}}{{html.p.>}}{{self.enddiv}}"\
//          b1="{{code.pushlines(t=\"{{var.avwrapper2.begin}}\n@wrap li\")}}"\
//          t1="{{code.pushlines(t=\"@parw\n{{var.avwrapper2.end_shots}}\n@wrap p\")}}"\
//          e1="{{code.pushlines(t=\"@parw\n{{var.avwrapper2.end}}\n@break\")}}"\
//          e2="{{code.pushlines(t=\"@parw\n{{var.avwrapper2.end_shots}}\n{{var.avwrapper2.end}}\n@break\")}}"

// avshot
// [var.avshot(v="WS: Info here", a="vo info")]
// [var.avshot.visual]
// [var.avshot.audio]
// [var.avshot.end]
// [var.avshot.noaudio] 

//TODO: Should I encode ' before compiling to avoid syntax errors?
@var _id="avshot" \
          start="@@ {{html._div_av_.<}}{{html.ul.<}}" \
          trans="@@ {{html.ul.>}}" \
          end_shot="@@ {{html.div.>}}" \
          shot_only="{{code.pushlines(t=\"{{self._start_shot_}}\n{{self.end_shot}}\")}}"\
          shot_with_desc="{{code.pushlines(t=\"{{self._start_shot_}}\n@wrap p\n{{self._d}}\n@parw 1\n{{self.end_shot}}\")}}"\
          _start_shot_="{{self.start}}\n@wrap li\n{{self._s}}\n@parw 1\n{{self.trans}}"\
          visual="{{code.pushlines(t=\"{{self.start}}\n@wrap li\")}}"\
          audio="{{code.pushlines(t=\"@parw\n{{self.trans}}\n@wrap p\")}}"\
          end="{{code.pushlines(t=\"@parw\n{{self.end_shot}}\")}}"\
          noaudio="{{code.pushlines(t=\"@parw\n{{self.trans}}\n{{self.end_shot}}\")}}"\          
          _s="Your Shot Here"\
          _d="Your Shot Description here"

