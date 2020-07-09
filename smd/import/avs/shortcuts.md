// Define some useful variables for substitutions

// First get the basic divs
@import '[sys.imports]/divs.md'

// Declare some custom film/video DIVs

[_dfactory(dn="lyrics")]
@set _="html._lyrics_p_" class="lyrics italic"

[_dfactory(dn="scene")]


@html _id="_span_" \
      _inherit="span" \
      _format="{{self.<}}{{self._t}}{{self.>}}"\
      _t="spantext" 

@html _id="_props_" \
      _inherit="_span_"\
      class="props" \
      _t="prop"

@html _id="_cast_" \
      class="cast"\
      _inherit="_span_" \
      _t="castmembername" 

@var _id="_castmember_" \
      _format="{{html._cast_.<}}{{self.castmember}}{{html._cast_.>}}" \
      name="{{html._cast_.<}}{{self.actor}}{{html._cast_.>}}" \
      name_e="{{html._cast_.<+}}{{self.actor}}{{html._cast_.>}}" \
      castmember="UNDEFINED" \
      actor="UNDEFINED"\
      _help_="See *code.cast_factory*"

@var _id="_propitem_" \
      _format="{{html._props_.<}}{{self.prop}}{{html._props_.>}}" \
      prop="UNDEFINED" \
      _help_="See *code.prop_factory*"

// Example: [cast_factory(nm="Jones" a="Harrison Ford" m="Indiana Jones")]
@code _id="cast_factory" type="eval" \
    src="print('@var _id=\"$.nm\" _inherit=\"_castmember_\" castmember=\"$.c\" actor=\"$.a\" fname=\"$.m\"')"\
    c = "*UNDEFINED*" \
    a = "*UNDEFINED*" \
    m = "*UNDEFINED*" \
    usage="Usage: **{{self.nm}}(c=&quot;castmember&quot;, n=&quot;actorname&quot; m=&quot;charactername&quot;)**)"

@code _id="prop_factory" type="eval" \
    src="print('@var _id=\"$.nm\" _inherit=\"_propitem_\" prop=\"$.p\"')"\
    p = "*UNDEFINED*" \
    usage="Usage: **{{self.nm}}(p=&quot;prop&quot;)**)"

