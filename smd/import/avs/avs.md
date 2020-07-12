@import '[sys.imports]/image.md'
@import '[sys.imports]/avs/shortcuts.md'
@import '[sys.imports]/avs/film.md'
@import '[sys.imports]/avs/shot.md'

// avshot - Method Attributes
// [var.avshot.visual]
// [var.avshot.audio]
// [var.avshot.end]
// [var.avshot.noaudio] 
// [var.avshot.shot_only(_s="your shot info here")]
// [var.avshot.shot_with_desc(_s="Shot info here" _d="Shot description/narrative here")]

@html _id="_div_av_" \
      _inherit="div" \
      class="av"

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

