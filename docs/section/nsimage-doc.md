[link.ns_image]
[wrap_h.chapter(t="## The @image Namespace")]

The @image statement can be used to include images in your document. Basically, @image is a convenient way to abstract the &lt;IMG&gt; HTML tag. The full syntax is:

{:.syntax}--- divTitle @image keyword
    {:.indent}@image _id="imagename" src="pathtoimage" alt="" _private="val"

Here's how it works. _id="imagename" is going to be how you cause the &lt;img&gt; tag to be generated in your document. Any variable that begins with an underscore (_) is considered private, and will not be included in the generated IMG HTML code. So, if you were to write:

{:.indent}#### @image _id="img1" src="path/foo.jpg" alt="my text for alt" class="myclass" _private="My private note"

and then I wrote:
{:.indent}#### [img1]

The code that would be inserted in the an "extras" DIV would be:

{:.indent}#### &ltimg src="path/foo.jpg" alt="my text for alt" class="myclass" /&gt;

Note that _id wasn't included, nor was _private. However, I can reference them both using the syntax:

{:.indent}#### &#91;img1._id] and &#91;img1._private].

This also works to reference the normal attributes. e.g. &#91;img1.class] would print **myclass**.

Note that if there's ambiguity in the names used for regular variables, image variables and *as you'll see next*, varv2 variables, you can add a prefix to clarify. For example, ***image.*** in front of the name to force the correct namespace to resolve. For example:

{:.indent.bigandbold}&#91;img1]=image1[b]@image _id="img1" \
    src="foo.png"[b]&#91;img1] would expand as ***image1***, and \
    &#91;image.img1] would expand as the ***&ltimg ...&gt*** html code.
