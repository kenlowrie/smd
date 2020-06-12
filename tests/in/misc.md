@import "$/testsetup.md"

[var.testdoc.begin(title="misc.md" desc="Testing miscellaneous stuff")]

@parw

//Add tests here that don't fit elsewhere (or I'm too lazy to look)
//
@var var="{:.red}This text will be RED"
Example: [var]
@var SP="&nbsp;"

[var.syntax.wc_open(t="Variable Decorators")]

[b]
{:.bigandbold.indent}&#91;variable]={:.class}value
[bb]
So, if you declared this: &#91;mynewvar]={:.bigandbold.red}My new big bold value, and then put &#91;mynewvar], you'd get this:[bb]
@var mynewvar="{:.bigandbold.red}My new big bold value"
[mynewvar]
[var.syntax.wc_close]

@var title="Production Estimate"

// Define some useful variables for substitions
@var li="<li style=\"font-size:1.3em\">{{self.i}}</li>" 
@var ol="<div class=\"extras\"><ol style=\"margin-left:2em\">" close="</ol></div>"
@var break="<br />"
@var dblbrk="[break][break]"
@var UL="<span style=\"text-decoration:underline\">{{self.t}}</span>"

@var email="__DELETEME__mailto:you@youremailaddress.com"
@var FancyMe="{:.bigandbold}Firstname LastName"
@var phone="512.867.5309"
@var sigme="[FancyMe]<br />Producer<br />Production Company<br />[phone]<br />[email]"
@var signature="<br /><div class=\"extras\"><p>[sigme]</p></div>"

[var.plain(t="[title]")]

[var.syntax.wc_open(t="Specifics when choosing TRT option")]
    [break]
    {:.indent2}This rate applies to editing normal footage (video, photos, audio). As an example, the demo film that we produced would have all fit under this rate, with one exception (green screen footage that was keyed for ending). However, if we are given footage that requires *specialized attention*, a different rate will apply on a per clip basis.[dblbrk]
    {:.indent2}Some examples that require specialized attention are: Footage that is shot on green screen and must be keyed. Footage that is shaky and must be stabilized. Footage shot with incorrect color temperature. Any media (video/photos) that requires rotoscoping. Audio that must be cleaned up.
[bb]
[var.syntax.wc_p_open]
1. [UL(t="**Per hour**")]. Editing for this project will be billed at $60/hr. Since we bill based upon hours spent, there are no exceptions to the type of footage being edited, as is the case with the ***"Per runtime minute of film"*** estimate above.
[bb]
2. [UL(t="**Per project**")]. An estimate for the entire project requires a completed script in AV format, with all details ironed out, including exact clips to be used, footage to be shot, etc. Given those requirements, it is not feasible to provide this option for consideration at this time.
[html.p.>]

[var.syntax.wc_close]

[bb]
[var.divxp.open]
For this project, only billing options 1 and 2 will be offered.

[var.plain(t="Retainer")]

If you decide to hire [Cloudy Logic Studios] for this project, no retainer will be required.

[var.plain(t="Invoicing")]

Once the project is underway, we will invoice periodically as various milestones are met. These milestones will be set and agreed upon by both parties prior to commencement. They will be something like this:

//TODO: Fix this horrible formatting of this upper part (down to summary section)
[ol]
@wrap html.li
Rough cut *- might be in stages*
Picture lock *- no changes to timeline after this*
Color grade complete *- possible after audio mixing*
Audio mixing complete *- possible before color grade*
Film completion
@parw
[ol.close]

If the project is being billed per runtime minute, the milestone invoices will be billed in fractional estimates of the minimum runtime up until picture lock, at which time remaining invoices will be billed based on the actual total runtime.

If the project is being billed per hour, then invoices at each milestone will reflect the total based on hours invested to achieve the milestone.

Usually, work on the next milestone will not commence until the invoice for the prior milestone has been paid.

Finally, keep in mind that final media will not be released until all invoices are paid in full.

[var.divxp.close]

[var.plain(t="Summary")]

[var.divxp.open]
If you would like to move forward with the project, here are the [UL(t="**next steps**")]:
[var.divxp.close]

// The manual way to do this ...
[ol]
[var.li(i="Choose a billing option")]
[var.li(i="Iron out milestones")]
[var.li(i="Acceptance of Terms - return signed contract")]
[ol.close]

[var.divxp(c="\
    Thanks again for choosing us for your production needs. We look forward to working with you on this project.[bb]\
    Please let [me] know if you have any questions regarding this estimate, or if you need any clarifications and/or changes.[bb][bb]\
    Warmest regards,[bb]\
    [signature]\
")]

{:.pbb}## Terms and Signatures

[var.divxp.open]
If you agree to the terms and conditions outlined in this proposal, select a billing option, [UL(t="initial each page")], sign/print/date below, and return the entire contract to [info@cloudylogic.com].
[bb]
@var option1="{:.bigandbold}[SP][SP]{[SP][SP]} Per runtime minute."
@var option2="{:.bigandbold}[SP][SP]{[SP][SP]} Per hour."

**Choose your Billing Option**: [dblbrk][option1][break][option2] 
[bb]
Upon final acceptance of video, an invoice will be generated outlining the final amount due. Payment is due within 30 days of final acceptance.
[bb]
[var.note(t="{:.bigandbold}**NOTE**: Final media is *not delivered* until all outstanding invoices have been paid in full.")]
[dblbrk]
### Signatures
[var.divxp.close]

@wrap p
[var.testdoc.end]

@dump var="." html="." link="." image="."
@import "[sys.imports]/def_bodyclose.md"
@import "[sys.imports]/def_close.md"
