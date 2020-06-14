// Variables that abstract the different types of DIVs
@import "[sys.imports]/html.md"

//    The case for @raw | @@. When you use them in emitted lines (or inline), any @wrap tag will NOT be applied.
//    This seems like the best case, otherwise the behaviour of the predefined code will not work as expected,
//    when used in the context of something else. If you really need this behavior, it can be overridden by
//    using inline HTML. e.g. <htmlcode>your code</htmlcode> or [html.tag.<]your code[html.tag.>]
//    This is worked around in some builtins using the .inline attribute to hold the code, and then _format="@@ {{self.inline}}"

@html _id="_div_extras_" \
      _inherit="div" \
      class="extras"

@html _id="_div_section_" \
      _inherit="div" \
      class="section"
@html _id="_div_section_pbb_" \
      _inherit="_div_section_" \
      class="section pbb"
@html _id="_p_section_" \
      _inherit="p" \
      class="divTitle"
@html _id="_p_section_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="section" \
          _format="@@ {{html._div_section_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._div_section_.>}}" \
          with_content="@@ {{html._div_section_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._p_section_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your section title" \
          c=""

@var _id="section_pbb" \
          _inherit="section" \ 
          _format="@@ {{html._div_section_pbb_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._div_section_.>}}" \
          with_content="@@ {{html._div_section_pbb_.<}}{{html._p_section_.<}}{{self.t}}{{html._p_section_.>}}{{html._p_section_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \

@html _id="_div_plain_" \
      _inherit="div" \
      class="plain"
@html _id="_div_plain_pbb_" \
      _inherit="div" \
      class="plain pbb"
@html _id="_p_plain_" \
      _inherit="p" \
      class="plainTitle"
@html _id="_p_plain_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="plain" \
          _format="@@ {{html._div_plain_.<}}{{html._p_plain_.<}}{{self.t}}{{html._p_plain_.>}}{{html._div_plain_.>}}" \
          with_content="@@ {{html._div_plain_.<}}{{html._p_plain_.<}}{{self.t}}{{html._p_plain_.>}}{{html._p_plain_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your plain title" \
          c="This is your plain content"

@html _id="code" _tag="code"

@html _id="_div_code_" \
      _tag="div" \
      class="code"
@html _id="_code_" \
      _inherit="code" \
      style="font-size:1.4em;font-weight:bold"
@html _id="_code_content_" \
      _inherit="_code_" \
      style="font-size:1.2em" 
 
@var _id="code" \
          _format="@@ {{html._div_code_.<}}{{html._code_.<}}{{self.t}}{{html._code_.>}}{{html._div_code_.>}}" \
          with_content="@@ {{html._div_code_.<}}{{html._code_.<}}{{self.t}}{{html._code_.>}}{{html._code_content_.<}}{{self.c}}{{html.code.>}}{{html.div.>}}" \
          t="This is your code title" \
          c="This is your code content"

@html _id="_div_av_" \
      _inherit="div" \
      class="av"
 
//TODO: Review this file. Lot's of goodies that will help with the docs.

@html _id="_div_toc_" \
      _inherit="div" \
      class="toc"
@html _id="_div_toc_pbb_" \
      _inherit="div" \
      class="toc pbb"
@html _id="_p_toc_" \
      _inherit="p" \
      class="divTitle"
@html _id="_p_toc_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="toc" \
          _format="@@ {{html._div_toc_.<}}{{html._p_toc_.<}}{{self.t}}{{html._p_toc_.>}}{{html._div_toc_.>}}" \
          with_content="@@ {{html._div_toc_.<}}{{html._p_toc_.<}}{{self.t}}{{html._p_toc_.>}}{{html._p_toc_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your toc title" \
          c="This is your toc content"

@html _id="_div_review_" \
      _inherit="div" \
      class="review"
@html _id="_div_review_pba_" \
      _inherit="div" \
      class="review pba"
@html _id="_p_review_" \
      _inherit="p" \
      class="divTitle"
@html _id="_p_review_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="review" \
          _format="@@ {{html._div_review_.<}}{{html._p_review_.<}}{{self.t}}{{html._p_review_.>}}{{html._div_review_.>}}" \
          with_content="@@ {{html._div_review_.<}}{{html._p_review_.<}}{{self.t}}{{html._p_review_.>}}{{html._p_review_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your review title" \
          c="This is your review content"

//TODO Add a code proper html wrapper for displaying inline code. with <pre> and <code> and ;display:block;white-space:pre-wrap where it makes sense

@html _id="_div_note_" \
      _inherit="_div_extras_"
@html _id="_div_note_pba_" \
      _inherit="_div_extras_"\
      class="pba extras"
@html _id="_p_note_" \
      _inherit="p" \
      class="note red indent"
@html _id="_p_note_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="note" \
          _format="@@ {{html._div_note_.<}}{{html._p_note_.<}}{{self.t}}{{html._p_note_.>}}{{html._div_note_.>}}" \
          with_content="@@ {{html._div_note_.<}}{{html._p_note_.<}}{{self.t}}{{html._p_note_.>}}{{html._p_note_content_.<}}{{self.c}}{{html.p.>}}{{html.div.>}}" \
          t="This is your note title" \
          c="This is your note content"

@var extras="{{html._div_extras_.<}}{{self.c}}{{html.div.>}}" c="default content"

@var divxp="{{self.open}}{{self.c}}{{self.close}}" c="default content" open="{{html._div_extras_.<}}{{html.p.<}}" close="{{html.p.>}}{{html.div.>}}"

@html _id="_div_syntax_" \
      _inherit="div" \
      class="syntax"
@html _id="_p_syntax_" \
      _inherit="p" \
      class="divTitle"
@html _id="_p_syntax_content_" \
      _inherit="p" \
      style="font-size:1.2em" 
 
@var _id="syntax" \
          _format="@@  {{self.inline}}"\
          inline="{{html._div_syntax_.<}}{{html._p_syntax_.<}}{{self.t}}{{html._p_syntax_.>}}{{html._div_syntax_.>}}"\
          with_content="@@ {{self.wc_inline}}" \
          wc_inline="{{self.open_inline}}{{self.c}}{{self.close_inline}}"\
          wc_open="@@ {{self.open_inline}}" \
          wc_close="@@ {{self.close_inline}}"\
          open_inline="{{html._div_syntax_.<}}{{html._p_syntax_.<}}{{self.t}}{{html._p_syntax_.>}}"\
          close_inline="{{html.div.>}}"\
          wc_p="@@ {{self.wc_p_inline}}"\
          wc_p_open="@@ {{self.wc_p_open_inline}}"\
          wc_p_inline="{{html._p_syntax_content_.<}}{{self.c}}{{html.p.>}}"\
          wc_p_open_inline="{{html._p_syntax_content_.<}}"\
          t="This is your syntax title" \
          c="This is your syntax content"
