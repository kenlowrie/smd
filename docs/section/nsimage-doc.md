[link.ug_ns_image]
[wrap_h.chapter(t="## The @image Namespace")]

@wrap divx, p

The [smdimage.b] keyword is used to declare variables that are used to include images in your document. Basically, [smdimage.b] is a convenient way to abstract the [e_tag.b(t="img")] HTML tag. 

Despite being an abstraction of the HTML element **img**, [smdimage.b] is not based on the [smdhtml.b] namespace. Given that, the underlying semantics do not support the [smdhtml.b] built-in attributes such as **.[E.lt], .[E.gt] and .[E.lt]+**. The full syntax is:

[syntax.wc_open(t="[smdimage.il] Syntax")]
    [generic.wc_open_inline]
        @image _id="imagename" src="pathtoimage" alt="" _private="val"
    [generic.wc_close_inline]
[syntax.wc_close]

Here's how it works. Like all namespaces, _id="imagename" is what names the variable in the [smdimage.b] namespace. You will use that name to cause the [e_tag.b(t="img")] tag to be emitted in your document. Also recall that attributes that start with an underscore (_) are considered private, and are not included in the generated [smdimage.b] HTML code. So, if you were to write:

[source.wc_open(t="")]
    {:.indent}#### @image _id="img1" src="path/foo.jpg" alt="my text for alt" class="myclass" _private="My private note"
[source.wc_close]

@image _id="img1" src="path/foo.jpg" alt="my text for alt" class="myclass" _private="My private note"

and then write:
{:.indent}#### [e_var(t="img1")]

The code that would be inserted would be:

[tab.<]**[escape_var(v="img1")]**[tab.>]

Note that _id wasn't included, nor was _private. However, I can reference them both using the syntax:

[tab.<][e_var.b(t="img1._id")] which emits *[img1._id]* and [e_var.b(t="img1._private")] which emits *[img1._private]*[tab.>]

This also works to reference the normal attributes. e.g. [e_var.b(t="img1.class")] which emits *[img1.class]*.

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

Easy enough. Now let's take a look at the system provided builtins for [smdimage.b].


[link.ug_image_builtins]
[wrap_h.section(t="### [smdimage.il] builtins")]

// Include image.md before we embed it, otherwise it won't load...

@import "[sys.imports]/image.md"

The [smdimage.b] namespace provides a limited set of builtins to get you started with using images in your markdown. Let's have a look at the contents of **image.md**:

[terminal.wc_open(t="Contents of sys.imports/image.md")]
@embed "[sys.imports]/image.md" esc="y"
[terminal.wc_close]

This limited set of builtins is intended as a starting point for your own image styling. **IMG_DEF** contains four different default styles, each of which can be selected using the **IMG_STYLE** attribute shortcuts:

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

You can see more of these builtins and the [smdimage.b] support in action by reviewing the [link.examples.<]samples[link.examples.>] that are included in the user guide.


//[docthis.open(h="Add this to nsimage-doc.md")]
//[docthis.close]

