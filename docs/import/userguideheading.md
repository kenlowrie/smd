// This document contains the standard document heading for a user guide.
// First let's declare some common links and aliases (variables)
// [workingtitle] and [storysummary] need to be defined *before* you include
// this template.
@link _id="cls" _inherit="_template_" _text="Cloudy Logic Studios" href="https://cloudylogic.com"
@var _id="cloudylogic" _format="{{link.cls._qlink(_qtext=\"cloudylogic.com\")}}"
@link _id="me" _inherit="_template_" _text="me@mydomain.com" href="mailto:you@yourdomain.com"
@link _id="fbemailaddr" _inherit="_template_" _text="Ken Lowrie" href="mailto:me@mydomain.com?subject=[workingtitle]%20Feedback"
[var.cover(title="[workingtitle]" author="**This guide is NOT Confidential**" logline="[storysummary]")]
[var.revision(v="0.4.2")]
[var.contact(cn="Ken Lowrie" ph="*512-867-5309*" em="[link.me]" c1="Copyright (c) 2018-2020 by [cls], LLC." c2="All Rights Reserved." c3="www.cloudylogic.com")]
[var.review.with_content(t="Notes to Reviewer", c="\
    Please send [link.fbemailaddr] any and all feedback, preferably by marking up the PDF using embedded comments. If you edit the PDF text, do so inline using comment boxes, or if you edit the text directly, change the color and/or font size so I can easily find it. Within different versions of this proposal, ++additions are marked like this++ and ~~deletions are marked like this~~\
")]
