[link.ug_samp_images]
[wrap_h.chapter(t="##Embedding Images in AV Shots [E.lp]avshot[E.rp]")]

@wrap divx,p

This chapter will cover using the various builtins for using images in combination with the **avshot** builtin. If you have yet to review the section on [link.ug_image_builtins._qlink(_qtext="[smdimage.b] builtins")], go ahead and do that now, because the rest of this chapter assumes you have! We will provide some additional examples on using the [smdimage.b] builtins in **avshot**'s, and then move on to the more powerful builtins that are declared in the **avs/[E.ast].md** files. 

@var image_path="[sys.root]/docs/samples/image"

@import '[sys.imports]/avs/avs.md'

@set _="code.dump" format="True" whitespace="True"

Recall from the section on [smdimage.b] builtins that you can manipulate the size of the image using the **IMG_SIZE** macros. The image sizing macros, when used inside the **avshot** builtin will seem different, given the fact that the visual and audio columns split the document window in half, and thus the width will be a percentage of that half... Here's an example to illustrate the point, starting with the markdown, and the rendering immediately follows it:

[terminal2.wc_open(t="Using image variables inside avshot builtin")]
    *[smdcomment.il] Declare an image variable*
    [encode_smd(t="@image")] _id="myshot" src="[E.lb]image_path[E.rb]/shot1.jpg" style="[E.lb]!var.IMG_STYLE.inline_border![E.rb]"
    *[smdcomment.il] Start the A/V shot declaration*
    [e_var(t="avshot.visual")]
    *[smdcomment.il] Change the image size to large and render it*
    [e_var(t="IMG_SIZE.large")]
    [e_var(t="myshot")]
    *[smdcomment.il] Change the image size to thumb and render it*
    [e_var(t="IMG_SIZE.thumb")]
    [e_var(t="myshot")]
    *[smdcomment.il] Close the A/V shot declaration*
    [e_var(t="avshot.noaudio")]
[terminal2.wc_close]

And here is what the browser will render:

@image _id="myshot" src="[image_path]/shot1.jpg" style="[!var.IMG_STYLE.inline_border!]"
[avshot.visual]
[IMG_SIZE.large]
[myshot]
[IMG_SIZE.thumb]
[myshot]
[avshot.noaudio]

So although we specified an image size of large, it only used half the window. This is because in **avshot**'s, each column uses half the window, so the relative sizes used in the styling for images is a percentage of that column. Of course it works the other way too:

[terminal2.wc_open(t="Declare an image variable")]
    *[smdcomment.il] Start the A/V shot declaration and add a shot descriptor*
    [e_var(t="avshot.visual")]
    WS: My wide shot tag here
    *[smdcomment.il] Switch to the Audio/Narrative*
    [e_var(t="avshot.audio")]
    *[smdcomment.il] Change the image size to large and render it*
    [e_var(t="IMG_SIZE.large")]
    [e_var(t="myshot")]
    *[smdcomment.il] Change the image size to thumb and render it*
    [e_var(t="IMG_SIZE.thumb")]
    [e_var(t="myshot")]
    *[smdcomment.il] Close the A/V shot declaration*
    [e_var(t="avshot.end")]
[terminal2.wc_close]

[avshot.visual]
WS: My wide shot tag here
[avshot.audio]
[IMG_SIZE.large]
[myshot]
[IMG_SIZE.thumb]
[myshot]
[avshot.end]

You will see many examples using these builtins throughout the user documentation, especially in the [link.examples._qlink(_qtext="**Samples**")] chapters, so you may want to look around at them to see more.

[wrap_h.section(t="### avs/shot.md builtins")]

Moving on, let's now spend some time looking at the more powerful builtins that are included in the **sys.imports/avs/shot.md** file that are part of [smd.b]. As we did previously, let's start by having a look at the help strings for the macros we will be using. 

Note that we won't look at all the building blocks in **shot.md**, just the more common things that you will use when writing A/V style markdown documents with shots and images. We will start with the factories: **image_factory**, **image_factory_abs_style** and **shot_factory**, which are used to create images and shots respectively, on the fly. The two image factories have additional macros to assist you, **image_factory_config** and **_img_template_**.

[olist.wc_open]
**image_factory** - The most commonly used macro
**image_factory_abs_style** - A variant that allows CSS styles to be specified directly
**image_factory_config** - A macro used to change the default styles used by the two previous macros
**_img_template_** - The template that is used when either factory creates a new @image variable.
**shot_factory** - A macro used to create a variable to store the technical aspects of an image.
[olist.wc_close]

[bluenote.wc_open]
{:.bigandbold}What is a shot?[bb]
In this context, think of a *shot* as a way to describe the image in a technical fashion. Things like the camera information (lens, aperture, ISO, etc.) and even textual information. Because the two are *related*, this is one exception to the rule of avoiding using identical names across variables in namespaces. For this case, it makes sense to create both an [smdimage.b] *shot1* and an [smdvar.b] *shot1*. Later on, we will see how this is used to create even more flexible macros.
[bluenote.wc_close]

Let's look at the help strings for all of these, including the **shot_factory**.

[terminal2.wc_open(t="**image_factory** help:")]
[image_factory.?]
[terminal2.wc_close]

[terminal2.wc_open(t="**image_factory_abs_style** help:")]
[image_factory_abs_style.?]
[terminal2.wc_close]

[terminal2.wc_open(t="**_img_template_ - template for @image variables** help:")]
[_img_template_.?]
[box.inline(c="*_img_template_* is inherited by variables created with one of the image factories, so each of the above attributes will exist in any [smdimage.b] variables created. They provide a means for easily changing the CSS styling used by an image after it has been created.")]
[terminal2.wc_close]

[terminal2.wc_open(t="**image_factory_config** help:")]
[image_factory_config.?]
[terminal2.wc_close]

[terminal2.wc_open(t="**shot_factory** help:")]
[shot_factory.?]
[terminal2.wc_close]

For our first example of using the factories, let's write the markdown for both the **image_factory** and the **shot_factory**, and test them out in an **avshot** sequence. This is one of the more common ways that you will use the factories in your documents. For example, if we write:

[terminal2.wc_open(t="Declare an image and a shot and then render them in AV style")]
    *[smdcomment.il] Declare the image and the shot using the factories*
    [E.lb]image_factory[E.lp]nm="myshot" ip="/path/shot1.jpg" st="!IMG_STYLE.inline_border!"[E.rp]]
    [e_var(t="shot_factory[E.lp]nm=\"myshot\" d=\"WS: Crane down\" notes=\"Opening crane shot\" c=\"Yes\"[E.rp]")]

    *[smdcomment.il] Start the shot and render the image and notes inline*
    [e_var(t="avshot.visual")]
    [e_var(t="image.myshot")]

    *[smdcomment.il] Switch to audio/narration and render the shot info with notes*
    [e_var(t="avshot.audio")]
    [e_var(t="var.myshot.audio")]
    [e_var(t="avshot.end")]
[terminal2.wc_close]

This is what we will get:

[IMG_SIZE.custom(w="92.3%")]

[image_factory(nm="myshot" ip="[image_path]/shot1.jpg" st="!IMG_STYLE.inline_border!")]
[shot_factory(nm="myshot" d="WS: Crane down" notes="Opening crane shot" c="Yes")]

[avshot.visual]
    [image.myshot]
[avshot.audio]
    @@[var.myshot.audio]
[avshot.end]

[b]Alternatively, you can inline the shot info directly below the shot image. Take a look at how to do that:

[terminal2.wc_open(t="Declare an image and a shot and then render them in AV style")]
    *[smdcomment.il] Declare the image and the shot*
    [E.lb]image_factory[E.lp]nm="myshot" ip="/path/shot1.jpg" st="!IMG_STYLE.inline_border!"[E.rp]]
    [e_var(t="shot_factory[E.lp]nm=\"myshot\" d=\"WS: Crane down\" notes=\"Opening crane shot\" c=\"Yes\"[E.rp]")]

    *[smdcomment.il] Start the shot and render the image and notes inline*
    [e_var(t="avshot.visual")]
    [e_var(t="image.myshot")]
    [e_var(t="var.myshot")]

    *[smdcomment.il] Switch to audio/narration and render just the shot notes*
    [e_var(t="avshot.audio")]
    [e_var(t="var.myshot.notes")]
    [e_var(t="avshot.end")]
[terminal2.wc_close]

This is what we will get:

[avshot.visual]
    [image.myshot]
    [var.myshot]
[avshot.audio]
    [var.myshot.notes]
[avshot.end]

Because we are using the dynamic styling version of the image factory, if we use one of the **IMG_SIZE** methods to change the width, the same exact code will render the image differently. For example, assume the same sequence of markdown as before, only this time, right before we render the sequence, let's add [e_var.b(t="IMG_SIZE.medium")]. Now we get this:

[IMG_SIZE.medium]
[avshot.visual]
    [image.myshot]
    [var.myshot]
[avshot.audio]
    [var.myshot.notes]
[avshot.end]

So far so good, right? We have now seen how to use the image and shot factories to easily create variables that we can use when creating AV scripts. And by combining those with the **avshot** builtin, we can easily create detailed breakdowns for a film/video shoot. 

Of course we can use these same *factory-created* image and shot variables outside **avshot**, so let's take one quick look at that before moving on to the next topic.

[terminal2.wc_open(t="Use image and shot factory variables outside avshot")]
    *[smdcomment.il] Declare the image and the shot*
    [E.lb]image_factory[E.lp]nm="myshot" ip="/path/shot1.jpg" st="!IMG_STYLE.inline_border!"[E.rp]]
    [e_var(t="shot_factory[E.lp]nm=\"myshot\" d=\"WS: Crane down\" notes=\"Opening crane shot\" c=\"Yes\"[E.rp]")]

    *[smdcomment.il] Render the image and then the shot info*
    [e_var(t="image.myshot")]
    [e_var(t="var.myshot.notes")]
[terminal2.wc_close]

Which will render the following:

[image.myshot]
[var.myshot]

One thing to notice if you didn't catch it is that you will always want to prefix the variable names with their namespace to guarantee that the parser will emit what you intend. If not, it will always emit the **var.** variable, since the **var** namespace variables have precedence over **image** namespace variables.

Before moving on, let's see a few more combinations of using the factory-created image and shot variables in different contexts.

[wrap_h.subsect(t="### More examples using the **avs/shot.md** builtins")]

Begin by creating a few variables we can use in our examples.

[terminal2.wc_open(t="Declare some common variables to use in examples")]
    *[smdcomment.il] Declare the image and the shot*
    [encode_smd(t="@var ss=\"[E.lcb2]var.IMG_STYLE.inline_border[E.rcb2]\"")]
    [encode_smd(t="@var trythis=\"{:.red.bold}Try to get this shot\"")]
    [encode_smd(t="@var beforeshoot=\"{:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION\"")]
[terminal2.wc_close]

@var ss="{{var.IMG_STYLE.inline_border}}"
@var trythis="{:.red.bold}Try to get this shot"
@var beforeshoot="{:.red.bold}NEED TO GET THIS DONE BEFORE PRODUCTION"

Although it's convenient to declare as many of the attributes as possible when the factory variable is created, it is also possible to add/update them after the fact. This is most commonly done with variables created by the **shot_factory**.

[terminal2.wc_open(t="Declaring shot attributes after factory creation step")]
    *[smdcomment.il] Declare the variable using the factory and render it*
    [E.lb]shot_factory[E.lp]nm="shot1"[E.rp]]
    [e_var(t="var.shot1")]

    *[smdcomment.il] Update attributes using the ._null_ method and render again*
    [E.lb]var.shot1._null_(d="[E.ast]WS: Crane down to reveal MOM[E.ast]" c="yes" l="85mm")[E.rb]
    [e_var(t="var.shot1")]
[terminal2.wc_close]

And here is what we get:

[shot_factory(nm="shot1")]
[var.shot1]
[var.shot1._null_(d="*WS: Crane down to reveal MOM*" c="yes" l="85mm")]
[var.shot1]

You can also add more attributes using the same technique. For example, say you want to add **title** and **class** attributes to your factory image variable. Here's how you could do that:

[terminal2.wc_open(t="Adding image attributes after factory creation step")]
    *[smdcomment.il] Declare the variable using the factory and render it*
    [e_var(t="IMG_SIZE.small")]
    [E.lb]image_factory[E.lp]nm="shot1" ip="/path/shot1.jpg" st="!IMG_STYLE.inline_border!"[E.rp]]
    [e_var(t="image.shot1")]

    *[smdcomment.il] Add attributes using the ._null_ method and render again*
    [E.lb]image.shot1._null_(title="title text for image" class="myimageclass")[E.rb]
    [e_var(t="image.shot1")]
[terminal2.wc_close]

[IMG_SIZE.small]
[image_factory(nm="shot1" ip="[image_path]/shot1.jpg" st="!IMG_STYLE.inline_border!")]

After the declaration of **image.shot**, the public attributes are:
[box.wc_open]
    [code.split_as(t="{{image.shot1._public_attrs_}}")]
[box.wc_close]

And it renders like this:

[image.shot1]

[image.shot1._null_(title="title text for image" class="myimageclass")]

After the addition of the **title** and **class** attributes, the public attributes are:
[box.wc_open]
    [code.split_as(t="{{image.shot1._public_attrs_}}")]
[box.wc_close]

And it renders like this (hover over both images for a couple of seconds to see the title on the 2nd):
[image.shot1]

Variables created with the **shot_factory** contain another attribute and methods that are specialized, the *notes* attribute and its companion methods *addNote* and *addBB*. Let's see how they can be used to add additional textual information to a shot variable.

Recall that we previously created a shot variable called **shot1** using the **shot_factory** macro. Let's dump the shot now to see what it contains:

[box.wc_open]
    [code.dump(ns="var" name="shot1")]
[box.wc_close]

For now, let's focus in on **notes**, **addNote** and **addBB**. Let's print the current value of each of those attributes now, just to clear things up:

[note.wc_open]
    **var.shot1.notes=**[get_value(v="var.shot1.notes" ret_type="0" escape="True" esc_smd="True")][b]
    **var.shot1.addNote=**[get_value(v="var.shot1.addNote" ret_type="0" escape="True" esc_smd="True")][b]
    **var.shot1.addBB=**[get_value(v="var.shot1.addBB" ret_type="0" escape="True" esc_smd="True")][b]
[note.wc_close]

 You can see that by default, **notes** returns the value of *[E.lcb2]var._shot_defs_.notes[E.rcb2]* which, if you have not changed it, is an empty string. We can add notes to a shot using the method **addNote**, and we can add a double blank line using **addBB**. So, if we wrote something like this:

[note.wc_open]
    *[smdcomment.il] Add a shot note to **shot1***[b]
    [E.lb]shot1.addNote(val="Mom reaches in and takes grocery bags from trunk")[E.rb][bb]
    *[smdcomment.il] Render the shot info table[b]*
    [E.lb]shot1.with_notes[E.rb]
[note.wc_close]

Will render as follows:

[shot1.addNote(val="Mom reaches in and takes grocery bags from trunk")]
[shot1.with_notes]

If we review the current value of the **notes** attribute, we see:

[note.wc_open]
    **var.shot1.notes=**[get_value(v="var.shot1.notes" ret_type="0" escape="True" esc_smd="True")][b]
[note.wc_close]

Notice that the *[E.lcb2]var._shot_defs_.notes[E.rcb2]* is still there, and our note has been appended to the value. This is intentional, allowing some type of document **default** to be present in the shot notes for every factory-generated shot variable. However, you can easily override it by simply setting the **notes** attribute to an empty string (or any other value), and then any additional calls to **addNote** will append to that.

Moving on, let's say we want to add another note, in this case, the previously defined **trythis** constant we created. We could do that with the following markdown:

[note.wc_open]
    *[smdcomment.il] Add a double blank and the trythis note to **shot1***[b]
    [E.lb]shot1.addBB[E.rb][b]
    [E.lb]shot1.addNote(val="[E.lb]trythis[E.rb]")[E.rb][bb]
[note.wc_close]

And now, it will render as follows:

[shot1.addBB]
[shot1.addNote(val="[trythis]")]
[shot1.with_notes]

If we review the current value of the **notes** attribute, we see:

[note.wc_open]
    **var.shot1.notes=**[get_value(v="var.shot1.notes" ret_type="0" escape="True" esc_smd="True")][b]
[note.wc_close]

You get the idea, right? Add as many or as few additional notes to your shots, so that when you generate any documents for your production team, they will be alerted to things that need to be done. Before we leave, it's worth mentioning that it's quite common to actually use the shot table below the shot image in an AV script, and then print the shot notes in the audio/narrative section by simply referencing the **notes** attribute. Let's see how that is done.

[terminal2.wc_open(t="Show usage of image and shot with notes in AV style")]
    *[smdcomment.il] Start the shot and render the image and shot table inline*
    [e_var(t="avshot.visual")]
    [e_var(t="image.shot1")]
    [e_var(t="var.shot1")]

    *[smdcomment.il] Switch to audio/narration and render just the shot notes*
    [e_var(t="avshot.audio")]
    [e_var(t="var.shot1.notes")]
    [e_var(t="avshot.end")]
[terminal2.wc_close]

This is what we will get:

[IMG_SIZE.custom(w="92.3%")]
[avshot.visual]
    [image.shot1]
    [var.shot1]
[avshot.audio]
    [var.shot1.notes]
[avshot.end]

Up to this point, we have seen how to use the builtins in **avs/shot.md** to create variables that allow us to manage all the details of a *shot*. Again, a *shot* in this context refers to an [smdimage.b] variable and a [smdvar.b] variable that collectively describe a shot for a film or video project.

And the usage of these *shots* is simplified through the use of the attributes and methods associated with the two variables that together make up a shot, which greatly reduces the amount of markdown required to create rich documents to describe your project to others.

But as we've seen, many times we are still repeating a lot of markdown for each shot, so it seems that additional gains can be made through the addition of another level of builtins. As luck would have it, such a level is part **avs/shot.md**, so let's take a look at it now.

[wrap_h.subsect(t="### Wrappers for avs/shot.md builtins")]

As we were discussing, although the builtins covered so far greatly reduce the markdown needed to manage shots in your documents, we are still repeating quite a bit of code each time we want to emit a shot and all of its accompanying information. The first step we need is a builtin that wraps a *shot*, and emits the more common cases via methods on that builtin. Enter **shotdetail**.

That the following markdown:

[terminal2.wc_open(t="Markdown to emit shot details")]
    [e_var(t="var.shot1.desc")]
    [e_var(t="image.shot1")]
    [e_var(t="var.shot1.with_notes")]
[terminal2.wc_close]

That markdown will render as follows:

[IMG_SIZE.custom(w="88%")]
[var.shot1.desc]
[image.shot1]
[var.shot1.with_notes]

The first thing to notice is that all three builtins take the name of the shot, in this case *shot1*. Besides that, the markdown would be the same for any shots created with the factories. So what we need is a builtin that takes a parameter, say *shotid*, and substitutes it on each of the lines where *shot1* is written, and then it would only take a single line of markdown to generate the same thing. That builtin is called **shotdetail**, so let's try it now and see what happens. We will write ***[E.lb]shotdetail.with_notes(shotid="shot1")[E.rb]***, and this is what the parser will emit:

[shotdetail.with_notes(shotid="shot1")]

Okay, so that's much more abbreviated, and we get the same results. Let's take a quick look at the help for **shotdetail** to see what it supports:

[terminal2.wc_open(t="**shotdetail** help:")]
[shotdetail.?]
[terminal2.wc_close]

You probably noticed the two special methods **needshot** and **needshot_wn** that are available in **shotdetail**. These methods come in handy when you don't have an image readily available to show the framing or storyboard for the shot you are documenting. In this case, you can use the **needshot** methods, as they will use a system-provided image as a placeholder when generating the markdown for your shot. Later, when you have an image, you can update your document to use either **basic** or **with_notes**.

Let's see how you can use **needshot** in your document. Assume we are documenting **shot38**, which is a drone shot flying over a pasture somewhere. You've written the following markdown, but you know that the **image.shot38** variable will not resolve to a valid image at this point. So instead of using *[E.lb]shotdetail.basic(shotid="shot38")[E.rb]*, you will write *[E.lb]shotdetail.needshot(shotid="shot38")[E.rb]*.

[terminal2.wc_open(t="Sample showing usage of .needshot method")]
    *[smdcomment.il] Generate the shot38 variables*
    [E.lb]image_factory(nm="shot38")[E.rb]
    [E.lb]shot_factory(nm="shot38")[E.rb]
    [E.lb]var.shot38._null_(d="[E.ast]WS: Drone flying over pasture[E.ast]" c="No" l="50mm")[E.rb]    
    *[smdcomment.il] Use needshot image since we don't have our own image for shot38 at this time*
    [E.lb]shotdetail.needshot(shotid="shot38")[E.rb]
[terminal2.wc_close]

That markdown will render as follows:

[image_factory(nm="shot38")]
[shot_factory(nm="shot38")]
[var.shot38._null_(d="*WS: Drone flying over pasture*" c="No" l="50mm")]
[shotdetail.needshot(shotid="shot38")]

//TODO.py: Consider the _c(c="content") addition to @html namespace. _ea="True" could enable the _c/_r support...

Of course we can also use the **shotdetail** builtin inside **avshot** sequences as well. For example:

[terminal2.wc_open(t="Using .needshot inside *avshot*")]
    [E.lb]avshot.visual[E.rb]
    [E.lb]shotdetail.needshot(shotid="shot38")[E.rb]
    [E.lb]avshot.noaudio[E.rb]
[terminal2.wc_close]

That markdown will render as follows:

[var.avshot.visual]
    [var.shotdetail.needshot(shotid="shot38")]
[var.avshot.noaudio]

So this seems to point out the next missing piece of the puzzle: builtins that wrap the **avshot** sequences. Let's take a look at those.

[wrap_h.subsect(t="### Using the avs/shot.md builtins that wrap *avshot*")]

The last two builtin we will cover is the **shot_emitter**. It provides a convenient way to emit shots in the most commonly used formats. Here's the help for **shot_emitter**:

[terminal2.wc_open(t="**shot_emitter** help:")]
[shot_emitter.?]
[terminal2.wc_close]

Let's take a closer look at each of them. First up is **shot_emitter.split**, which emits an **avshot** sequence, and splits the visual (image) and the audio (notes) between the two columns. This is a space saving way to emit a shot list with storyboards. Here's what it looks like when we use write **[E.lb]shot_emitter.split(shotid="shot1")[E.rb]**:

[shot_emitter.split(shotid="shot1")]
[bb]
Next up is shot left, which also emits an **avshot** sequence, but in this variant, it places the image and details on the left, and then puts the shot notes on the right. This is more typical of how you would use it in an A/V script. The markdown is: **[E.lb]shot_emitter.left(shotid="shot1")[E.rb]**:

[shot_emitter.left(shotid="shot1")]

Next up is **shot_only**, which, as you probably guessed, simply emits the shot. The markdown: **[E.lb]shot_emitter.shot_only(shotid="shot1")[E.rb]**:

[shot_emitter.shot_only(shotid="shot1")]

And finally, there's **shot_with_notes**, which displays the shot and notes table inline and raw, so you can use this version in or outside of an **avshot** sequence. The markdown: **[E.lb]shot_emitter.shot_with_notes(shotid="shot1")[E.rb]**:

[shot_emitter.shot_with_notes(shotid="shot1")]

And we finally come to the end of this chapter. We've covered quite a bit, but hopefully you've got a good idea on how to use the builtins available for generating images and shot details for your documents. Be sure to review the actual markdown that was used to generate this documentation, as it will give more insight into how everything works.

@parw
