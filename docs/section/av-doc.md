[link.avs]

[wrap_h.chapter(t="## AV Visual Script Formatter")]

[docthis.open(h="Add this to av-doc.md")]

avshot ...

[docthis.close]

[TODO] This may no longer be needed, given all the samples. Perhaps some type of overview that talks about using smd as an AV Script generator, and pointing you to the examples, possibly talking about doing simple AV Scripts (using avshot) vs more complex docuemnts using the shot.md builtins...

Let's see a quick example now. The next line will begin with an ***&#42;*** and then contain the text that describes the visual, and the line after that will contain the narration that goes with it.



## This will have to be moved to a "shots" doc

{:.bigandbold.green}Seems to me that an example that shows how you could use SMD to generate an A/V script would be useful, and would be a way for me to bring over all the film, shot, etc, markdown, put into a directory, such as import/avs or something.  Then, I could use isolate all of that into a shot-specific userguide, and leave this one for the main smd utility.[bb]Also, the formatting in the new doc looks different than the old version, need to run that down to make sure it was intentional.[bb]

[avshot.shot_with_desc(_s="WS:Sunrise", _d="\
    There&apos;s just something about a sunrise that gets the blood flowing...\
    And here&apos;s some additional narration.[bb]\
    and here is some additional shot notes.\
")]

// Seems like @break is essentially a way of doing a "clear:both" thru the use of a display:block element such as headers...
//@break Not really needed, because the avshot macro properly handles the closure...
//{:.extras}# --- This also works...

[var.note(t="When you want to force the document out of shot mode, use ***@break*** or ***@exit*** on an empty line. That will reset the floats which are controlling the AV formatting, and start a new section. See how the document leaves the narration mode of the prior shot, and starts this new block paragraph?")]
@break

**[at]break** [lt]--Use @break or @exit to close a shot DIV."

You can have as much narration as required, just keep writing, even starting new regular paragraphs. When you're done, start a new visual, or add any other block element, such as links, aliases, headers, divs, etc. To add another shot, just repeat the steps above, like this:

//TODO: This requires that we rework aws.md and eliminate avwrapper and avwrapper2 in favor of avshot. But avshot is also
// broken, in that it needs to rely on pushlines when using shot_only or shot_with_desc due to the @@ requirement...


[avshot.shot_with_desc(_s="CU:Coffee pot heating on wire rack of fire pit", _d="\
    There&apos;s nothing like waking up to the smell of coffee percolating in the outdoors.\
    ")]

If you have text you want included in the HTML document, but do not want it rendered by the browser, use the **{:.ignore}** class prefix. For example, on the next line, we'll write {:.ignore}You won't see this.[bb]
{:.ignore}You won't see this.
When you examine the HTML, you'll see the prior text wrapped in **[lt]p[gt]** tags, inside **[lt]div class="extras"[gt]** markup. However, it will not be rendered by the browser, unless you modify the CSS rule for the ignore class.
Lines that begin with a double forward slash [***//***] are treated as comments, and are discarded by AVScript. They will not appear in the HTML at all. As another example, we'll write *//This will not appear in the HTML* on the next line.
//This will not appear in the HTML
If you examine the HTML output, you will not see the previous line in the output.

//TODO: This needs to be defined in the builtins
