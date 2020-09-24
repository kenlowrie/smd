
//image factory was broken because you couldn't have embedded quotes...
@debug toggle="ns.link|ns.code"

@import '[sys.imports]/shot.md'
[path]=/users/ken/path/to/nowhere

[header]
## Define image template and factory2 code
@debug toggle="ns.image|ns.code"
//An alternative that doesn't expand values until runtime (compile(src))
@image _id="img_template" \
      _format="<{{self._tag}}{{self._public_attrs_esc_}}/>"

@code _id="img_factory2" type="eval" \
    src="print('@image _id=\"$.nm\" _inherit=\"img_template\" src=\"$.s\" style=\"$.t\"\
    ')" \
    s = "path_to_image" \
    t = "[ss]" \
    usage="Usage: **{{self.nm}}(s=&quot;image_path&quot; st=&quot;style&quot;)**)"\

@debug toggle="ns.image|ns.code"
@dump image="img_template" code="img_factory2"
[header]
## Define image shot23b2 using img_factory2
@debug toggle="ns.image|ns.code"
[img_factory2(nm="shot23b2", s="{{path}}/SHOT 23B.JPG")]

@debug toggle="ns.image|ns.code"
@dump image="shot23b2"
[header]
## Define image shot23b using old img_factory
@debug toggle="ns.image|ns.code"
//Would be easier to use html to create IMG, so we could just set the format like we want...
//@set _id="shot23b2" _format="<{{self._tag}} src=\"{{self.src}}\" style=\"{{self.style}}\""/>"

// Playing with preventing src= and style= from expanding until execution time.
[img_factory(nm="shot23b", s="[path]/SHOT 23B.JPG")]
@debug toggle="ns.image|ns.code"
@dump image="shot23b"
[header]
## Generate shot shot23b
@debug toggle="ns.image|ns.code"
[shot_factory(nm="shot23b", d="{{cu}}{{note}} blows into frame, other side", l="50mm", c="no")]
@debug toggle="ns.image|ns.code"
[header]
## Render shot 23b
@debug toggle="ns.image|ns.code"
[var.shotinfo2(shotid="shot23b")]
//@dump image="shot23b" var="shot23b|shotinfo2|img_factory" code="shot|img"
//[img_factory2(nm="shot23b2", s="{{path}}/SHOT 23B.JPG")]
//@dump image="shot23b"
//@set _id="shot23b2" _format="<{{self._tag}} src=\"{{self.src}}\" style=\"{{self.style}}\""/>"
//@dump image="shot23b"
//[var.shotinfo2(shotid="shot23b2")]
