@import '[sys.imports]/html.md'
@import '[sys.imports]/image.md'
@import '[sys.imports]/code.md'

@html _id="_div_av_" \
      _inherit="div" \
      class="av"

@var _id="avshot" \
          start="@@ {{html._div_av_.<}}{{html.ul.<}}" \
          trans="@@ {{html.ul.>}}" \
          end_shot="@@ {{html.div.>}}" \
          shot_only="{{code.pushlines(t=\"{{self._start_shot_}}\n{{self.end_shot}}\")}}"\
          shot_with_desc="{{code.pushlines(t=\"{{self._start_shot_}}\n[self.wrap_audio]\n{{self._d}}\n@parw 1\n{{self.end_shot}}\")}}"\
          _start_shot_="{{self.start}}\n[self.wrap_visual]\n{{self._s}}\n@parw 1\n{{self.trans}}"\
          visual="{{code.pushlines(t=\"{{self.start}}\n[self.wrap_visual]\")}}"\
          audio="{{code.pushlines(t=\"@parw\n{{self.trans}}\n[self.wrap_audio]\")}}"\
          end="{{code.pushlines(t=\"@parw\n{{self.end_shot}}\")}}"\
          noaudio="{{code.pushlines(t=\"@parw\n{{self.trans}}\n{{self.end_shot}}\")}}"\
          wrap_visual="@wrap li"\
          wrap_audio="@wrap p"\      
          _s="Your Shot Here"\
          _d="Your Shot Description here"\
          _help="[sp.2]*{{self._}}*[bb]\
[sp.4]Used to emit shots in A/V Script-style documents.[bb]\
[sp.2]**Common Parameters**[b]\
[sp.4]**_s** - shot info. e.g. WS: Lake with people swimming near shore[b]\
[sp.4]**_d** - shot description/narrative for opening wide shot[bb]\
[sp.2]**Methods**[b]\
[sp.4]**visual** - Open a shot declaration, ready for shot(s)[b]\
[sp.4]**audio** - Close shot section and transition to audio; ready for shot description[b]\
[sp.4]**end** - Close shot declaration[b]\
[sp.4]**noaudio** - Close shot declaration when no shot description will be set[b]\
[sp.4]**shot_only(_s)** - Create a complete shot declaration; shot(s) specified in **_s**[b]\
[sp.4]**shot_with_desc(_s,_d)** - Create complete shot declaration; shot(s) **_s**, description **_d**."
