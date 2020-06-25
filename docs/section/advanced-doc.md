
[link.advanced]
{:.plain}@@@ plainTitle
##Advanced Topics: @raw, @image, @var &amp; @set

{:.syntax}@@@ divTitle Syntax:
    {:.indent}**@raw raw HTML**
    {:.indent}**@image _id="name" src="/path/to/image" ...**
    {:.indent}**@var _id="name" attr1="value1" _format="fmt string"**

These keywords, @raw, @image and @var, can be used to incorporate more control over the output of your document. I'll provide a high level look at each of them, but probably the best way to see what type of flexibility they offer would be to review some of the samples in the "tests" directory.

First things first, because describing content dynamically using these keywords can get a bit long, you'll want to get familiar with the line continuation character '\'. The line continuation character can actually be used anywhere, but I document it here because it was this support that caused me to introduce it. Anyway, you can continue a line by ending it with the '\' character (spaces or tabs can follow, but it must be the last non-white space character on the line). When you do that, the internal file handler sees the continuation character, and reads the next line, concatenating it onto the current line. For example:

{:.syntax}--- .
    {:.indent}@var _id="myvar"  &#92;
    {:.indent4}attr1="value1" &#92;
    {:.indent4}attr2="value2"

Causes that line to be interpreted as **@var _id="myvar" attr1="value1" attr2="value2"**, as if it were all typed on the same line. You'll see this convention used quite a bit in the samples and the tests.

### @set keyword

Once you build some cool abstractions to assist with the automation of common tasks in your documents, you'll need to have a method for changing a value for an attribute in order to affect the generation of the output. Take the following example.

Say we want to display a storyboard in our shot AV file along with some common camera and setup information. So we create the following set of expansions to assist:

{:.indent.bigandbold}// provide default values[b]\
&#91;_i_width]=90%[b]\
[_b_size]=1px[b]\
[_b_type]=solid[b]\
[img-border-style]=border:[{{_b_size}}] [{{_b_type}}];padding:1em;[b]\
[img-inline-style]=margin-left:auto;margin-right:auto;width:[{{_i_width}}];[b]\
[img-st-inline]=[{{img-inline-style}}][b]\
[img-st-inline-border]=[{{img-inline-style}}][{{img-border-style}}][b]\
[ss]=[{{img-st-inline-border}}][b]\
// Some useful defaults for _i_width[b]\
[IMG_SIZE_THUMB]=20%[b]\
[IMG_SIZE_SMALL]=40%[b]\
[IMG_SIZE_MEDIUM]=70%[b]\
[IMG_SIZE_LARGE]=90%[b]\
[_shotinfo_]=&lt;table class="shotinfo"&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="center" colspan="2"&gt;***Shot Information***&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;th class="item"&gt;Item&lt;/th&gt;&lt;th class="desc"&gt;Description&lt;/th&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Shot&lt;/td&gt;&lt;td class="desc"&gt;{{self.name}}&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Desc&lt;/td&gt;&lt;td&gt;*{{self.desc}}*&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Lens&lt;/td&gt;&lt;td&gt;**{{self.lens}}**&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
    [SP][SP][SP][SP]&lt;tr&gt;&lt;td class="item"&gt;Crane&lt;/td&gt;&lt;td&gt;{{self.crane}}&lt;/td&gt;&lt;/tr&gt;&#92;[b]\
&lt;/table&gt;[b]\
@var _id="shotinfo" _format="- [var.{{self.shotid}}.desc]&lt;br /&gt;[image.{{self.shotid}}]&lt;br /&gt;[var.{{self.shotid}}]" shotid="NOTSET"

And now we agree to use the convention of defining an **@image** and an **@var** variable using the same ***_id*** value, which would result in us doing something like this in our document:

{:.indent.bigandbold} @var _id="shot1" name="WS: Sky with top of trunk bottom of frame" desc="*Short Description shot 1*" lens="**85mm**" crane="yes" _format="[_shotinfo_]"[b]\
@image _id="shot1" src="[imgpath]/shot1.jpg" style="[ss]"[b][b]\
@var _id="shot2" name="MS: Taking groceries from trunk" desc="*Short Description shot 2*" lens="**50mm**" crane="yes" _format="[_shotinfo_]"[b]\
@image _id="shot2" src="[imgpath]/shot2.jpg" style="[ss]"
And now, we can auto generate the shot and info using syntax like this:

{:.indent.bigandbold} @set _id="shotinfo" shotid="shot1"[b]\
[var.shotinfo][b]\
And some random shot comments here.[b]\
[b]\
@set _id="shotinfo" shotid="shot2"[b]\
[var.shotinfo][b]\
Some random shot 2 comments here.

And then, when we run the prior code, we'd get this:

// provide default values
[_i_width]=90%
[_b_size]=1px
[_b_type]=solid
[img-border-style]=border:[{{_b_size}}] [{{_b_type}}];padding:1em;
[img-inline-style]=margin-left:auto;margin-right:auto;width:[{{_i_width}}];
[img-st-inline]=[{{img-inline-style}}]
[img-st-inline-border]=[{{img-inline-style}}][{{img-border-style}}]
[img-st-block]=display:block;[{{img-inline-style}}]
[img-st-block-border]=display:block;[img-inline-style][img-border-style]
[ss]=[{{img-st-inline-border}}]
// Some useful defaults for _i_width
[IMG_SIZE_THUMB]=20%
[IMG_SIZE_SMALL]=40%
[IMG_SIZE_MEDIUM]=70%
[IMG_SIZE_LARGE]=90%

[_shotinfo_]=<table class="shotinfo">\
    <tr><td class="center" colspan="2">***Shot Information***</td></tr>\
    <tr><th class="item">Item</th><th class="desc">Description</th></tr>\
    <tr><td class="item">Shot</td><td class="desc">{{self.name}}</td></tr>\
    <tr><td class="item">Desc</td><td>*{{self.desc}}*</td></tr>\
    <tr><td class="item">Lens</td><td>**{{self.lens}}**</td></tr>\
    <tr><td class="item">Crane</td><td>{{self.crane}}</td></tr>\
</table>

@var _id="shotinfo" _format="- [var.{{self.shotid}}.desc]<br />[image.{{self.shotid}}]<br />[var.{{self.shotid}}]" shotid="NOTSET"

@var path="../import"

@var _id="shot1" name="WS: Sky with top of trunk bottom of frame" desc="*Short Description*" lens="**85mm**" crane="yes" _format="[_shotinfo_]"
@image _id="shot1" src="[path]/shot1.jpg" style="[ss]"

@var _id="shot2" name="MS: Taking groceries from trunk" desc="*Short Description*" lens="**50mm**" crane="yes" _format="[_shotinfo_]"
@image _id="shot2" src="[path]/shot2.jpg" style="[ss]"


@set _id="shotinfo" shotid="shot1"
[var.shotinfo]
And some random shot comments here.[b]\

@set _id="shotinfo" shotid="shot2"
[var.shotinfo]
Some random shot 2 comments here.

@break
What the ...? Sweeeeet! So basically, by simply changing the value of the attribute **shotid** in the **shotinfo** variable, we can cause **shotinfo** to display different shots (both images and shot information)!

Okay, that should give you an idea of how you can use these advanced keywords to build some cool automation for your AV documents. There's quite a bit of these already built and included in the various tests that I've created to assist with the development, so take a look at them, and build from there! And when you come up with some new and improved versions of them, please share!

Keep in mind that once you have this stuff defined, it's easy to change. For example, if I write &#91;_i_width]=80%, and then write &#91;varv2.shotinfo], look what happens:

[_i_width]=80%
[varv2.shotinfo]

@break
And look what happens if we generate the image outside of a shot. I'll do that by just writing the image reference, like so: &#91;image.shot1], and you'll get this:

@break
[image.shot1]

I can make it small by setting the width to one of those predefined sizes. For example, &#91;_i_width]=&#91;IMG_SIZE_SMALL]. And then I'll get this:

[_i_width]=[IMG_SIZE_SMALL]
[image.shot1]

Awww. And if I don't want the border, I could choose a different style. So if I write this:

{:.indent.bigandbold} &#91;ss]=&#91;{{img-st-inline}}[b]\
    &#91;image.shot1]

I'll get this instead:

[ss]=[{{img-st-inline}}]
[image.shot1]

Same image, but without a border.

So that pretty much sums up the advanced section. Hopefully it was helpful, if not, ask questions, and I'll clarify. Or better yet, improve the docs, and submit a pull request. :)
