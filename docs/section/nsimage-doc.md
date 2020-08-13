[link.ug_ns_image]
[wrap_h.chapter(t="## The @image Namespace")]

@wrap divx, p

The [smdimage.b] keyword is used to declare variables that are used to include images in your document. Basically, [smdimage.b] is a convenient way to abstract the [e_tag.b(t="img")] HTML tag. 

Despite being an abstraction of the HTML element **img**, [smdimage.b] is not based on the [smdhtml.b] namespace. Given that, the underlying semantics do not support the [smdhtml.b] built-in attributes such as [big.multi(t=".[E.lt]" cls=".red.bold")], [big.multi(t=".[E.gt]")] and [big.multi(t=".[E.lt]+")]. The full syntax is:

[syntax.wc_open(t="[smdimage.il] Syntax")]
    [generic.wc_open_inline]
        @image _id="imagename" src="pathtoimage" alt="" _private="val"
    [generic.wc_close_inline]
[syntax.wc_close]

Here's how it works. Like all namespaces, *_id="imagename"* is what names the variable in the [smdimage.b] namespace. You will use that name to cause the [e_tag.b(t="img")] tag to be emitted in your document. Also recall that attributes that start with an underscore [big.multi(t="_")] are considered private, and are not included in the generated [smdimage.b] HTML code. So, if you were to write:

[terminal.wc_open(t="Creating variables in [smdimage.il] namespace")]
    [E.at]image _id="img1" src="path/foo.jpg" alt="my text for alt" class="myclass" _private="My private note"
[terminal.wc_close]

@image _id="img1" src="path/foo.jpg" alt="my text for alt" class="myclass" _private="My private note"

and then write:

{:.indent}[big.120(t="[E.lb]img1[E.rb]")]

The code that would be inserted would be:

[tab.<]**[escape_var(v="img1")]**[tab.>]

Note that _id wasn't included, nor was _private. However, I can reference them both using the syntax:

[tab.<][e_var.b(t="img1._id")] which emits *[img1._id]* and [e_var.b(t="img1._private")] which emits [big.120(t="[img1._private]")][tab.>]

This also works to reference the normal attributes. e.g. [e_var.b(t="img1.class")] which emits [big.120(t="[img1.class]")].

And as is the case for all namespaces, if there's ambiguity in the names used in different namespaces, you can add the namespace prefix to clarify. For example, ***image.*** in front of the name to force the correct namespace to resolve. For example, if I write the following two lines in my document:

[terminal.wc_open(t="")]
    [smdvar.b] img1="my variable img1 in [smdvar.il] namespace"
    [smdimage.b] _id="img1" src="foo.png"
[terminal.wc_close]

@var img1="my variable img1 in [smdvar.il] namespace"
@image _id="img1" src="foo.png"

Then, when I write [e_var.b(t="var.img1")] the parser will emit *[var.img1]* and when I write [e_var.b(t="image.img1")] the parser emits *[escape_var(v="image.img1")]*.

Let's go ahead and include an inline image to see [smdimage.b] in action. I will write:

[terminal.wc_open(t="")]
    [smdimage.b] _="shot1" src="[E.lb]sys.root[E.rb]/docs/import/shot1.jpg" alt="shot 1" style="width:30%"
[terminal.wc_close]

@image _="shot1" src="[sys.root]/docs/import/shot1.jpg" alt="shot 1" style="width:30%"

When I write [e_var.b(t="shot1")], the parser emits *[escape_var(v="image.shot1")]* and the browser renders:

[shot1]

Pretty straightforward, don't you think? Okay, now it's time to take a look at the system provided builtins for [smdimage.b], so we can tap into some additional flexibility when rendering images with [smd.b].


[link.ug_image_builtins]
[wrap_h.section(t="### [smdimage.il] builtins")]

// Include image.md before we embed it, otherwise it won't load...

@import "[sys.imports]/image.md"

The [smdimage.b] namespace provides a limited set of builtins to get you started with using images in your markdown. These builtins are a good starting point for your own image styling, so let's begin with a quick overview of the builtins in **sys.imports/image.md**. 

 **IMG_DEF** contains four different default styles, each of which can be selected using the **IMG_STYLE** attribute shortcuts:

[ulistplain.wc_open]
@wrap [code.wrap_stack(w="tag.<")],strong
[e_var(t="IMG_STYLE.inline")]
[e_var(t="IMG_STYLE.inline_border")]
[e_var(t="IMG_STYLE.block")]
[e_var(t="IMG_STYLE.block_border")]
@parw
[ulistplain.wc_close]

In addition, four fixed size attributes and one custom size attribute is provided via the **IMG_SIZE** declaration:

[ulistplain.wc_open]
@wrap [code.wrap_stack(w="tag.<")],strong
[e_var(t="IMG_SIZE.thumb")]
[e_var(t="IMG_SIZE.small")]
[e_var(t="IMG_SIZE.medium")]
[e_var(t="IMG_SIZE.large")]
[e_var(t="IMG_SIZE.custom[E.lp]w=\"##%\"[E.rp])")]
@parw
[ulistplain.wc_close]

For a quick example of the size and styling shortcuts, let's write the following markdown in this document and see what we get:

[terminal.wc_open(t="")]
    [e_var(t="IMG_SIZE.thumb")]
    [smdimage] _="shot1" src="[E.lb]sys.root[E.rb]/docs/import/shot1.jpg" style="[E.lcb2]IMG_STYLE.inline_border[E.rcb2]"
    [e_var(t="shot1")]
[terminal.wc_close]

And here is what the browser renders:

[IMG_SIZE.thumb]
@image _="shot1" src="[sys.root]/docs/import/shot1.jpg" style="{{var.IMG_STYLE.inline_border}}"
[shot1]

@var image_path="[sys.root]/docs/samples/image"

@import '[sys.imports]/avs/avs.md'

@set _="code.dump" format="True" whitespace="True"

Let's take a closer look at the builtins declared in **image.md** to assist with using images in your documents. We will start by looking at the built-in help for each builtin, and then we'll move on to using them in our document.

[terminal2.wc_open(t="**IMG_DEF** Help:")]
[IMG_DEF.?]
[terminal2.wc_close]

[terminal2.wc_open(t="**IMG_SIZE** Help:")]
[IMG_SIZE.?]
[terminal2.wc_close]

[terminal2.wc_open(t="**IMG_STYLE** Help:")]
[IMG_STYLE.?]
[terminal2.wc_close]

The builtins you normally use in your documents are **IMG_SIZE** and **IMG_STYLE**. **IMG_SIZE** is used to set the size of the image that will be displayed in the document. Before we get too far, though, we need to actually declare an **@image** variable that we can experiment with. Let's begin with the following declaration:

[terminal2.wc_open(t="Declare an image variable")]
    *[smdcomment.il] Set image size to large, declare myshot var and render*
    [e_var(t="IMG_SIZE.large")]
    [encode_smd(t="@image _id=\"myshot\" src=\"[E.lb]sys.imports[E.rb]/avs/needshot.png\" style=\"[E.lb]IMG_STYLE.inline_border[E.rb]\"")]
    [e_var(t="myshot")]
[terminal2.wc_close]

And when we do that, here's what we get:

[IMG_SIZE.large]
@image _id="myshot" src="[sys.imports]/avs/needshot.png" style="[IMG_STYLE.inline_border]"
[myshot]

Okay, not too complicated thus far. The first thing to note is that the image size takes up almost the entire document window. This is because the width is currently set to **[IMG_DEF._i_width]**. So let's go ahead and set the size to [e_var.b(t="IMG_SIZE.small")], and then render the image again:

[terminal2.wc_open(t="Change image size to small and render again")]
    *[smdcomment.il] Set image size to small again and just render*
    [e_var(t="IMG_SIZE.small")]
    [e_var(t="myshot")]
[terminal2.wc_close]

[IMG_SIZE.small]
[myshot]

Wait, this looks the same! What's going on? Let's begin by taking a look at the declaration for **myshot**:

[terminal.wc_open(t="Declaration of image.myshot")]
    [code.dump(ns="image" name="myshot" format="False" whitespace="False")]
[terminal.wc_close]

Okay, looks like the issue is that **style** is hard-coded to the **inline_border** style. So, if we redeclare our @image variable, but this time use either "**[!IMG_STYLE.inline_border!]**" or "**{{IMG_STYLE.inline_border}}**", either of which will cause the parser to not evaluate the variable until it is used, that should allow us to override it. So basically, here's the markdown:

[terminal2.wc_open(t="Declare an image variable")]
    *[smdcomment.il] Declare myshot, set image size to small, render*
    [encode_smd(t="@image _id=\"myshot\" src=\"[E.lb]image_path[E.rb]/needshot.png\" style=\"[E.lb]!IMG_STYLE.inline_border![E.rb]\"")]
    [e_var(t="IMG_SIZE.small")]
    [e_var(t="myshot")]
[terminal2.wc_close]

@image _id="myshot" src="[image_path]/needshot.png" style="[!IMG_STYLE.inline_border!]"
// This next step isn't needed right now, because the prior call to it actually set the width, it's just that it was hardcoded in the attrribute of myshot...
[IMG_SIZE.small]
[myshot]

And now if I write [e_var.b(t="IMG_SIZE.thumb")] followed by [e_var.b(t="myshot")] I will get:

[terminal2.wc_open(t="Change image size to thumb and render again")]
    *[smdcomment.il] Set image size to thumb and just render*
    [e_var(t="IMG_SIZE.thumb")]
    [e_var(t="myshot")]
[terminal2.wc_close]

[IMG_SIZE.thumb]
[myshot]

Let's review the new definition of **myshot** to see how this change affected the variable definition:

[terminal.wc_open(t="Declaration of image.myshot")]
    [code.dump(ns="image" name="myshot" format="False" whitespace="False")]
[terminal.wc_close]

You can see that **style=** is now set to [e_var.b(t="IMG_STYLE.inline_border")] instead of being hardcoded. Using the [big.130p(t="[E.lb]![sp]![E.rb]" cls=".red")] around a variable name in an attribute declaration causes the parser to delay evaluation of the variable until it is actually used. Note that you would get the same effect by surrounding the variable/attribute name with curly braces, i.e. [big.120p(t="[E.lcb2][sp][E.rcb2]")].

//Let's have a look at the contents of **image.md**:

//[terminal.wc_open(t="Contents of sys.imports/image.md")]
//@embed "[sys.imports]/image.md" esc="y"
//[terminal.wc_close]

You can see more of these builtins and the [smdimage.b] support in action by reviewing the [link.examples._qlink(_qtext="samples")] that are included in the user guide.

//[docthis.open(h="Add this to nsimage-doc.md")]
//[docthis.close]

