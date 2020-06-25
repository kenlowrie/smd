
[link.mailto_links]
###mailto links
You can create mailto: links in your document too, which enables users to click on a link to automatically compose an email addressed to the specified email address. AVScript will encode the entire mailto: link URL using a mix of decimal and hexadecimal HTML entities as a deterrent to spam bots that mine email addresses from HTML documents. Here's the syntax for a *mailto:* link:
 
{:.syntax}@@@ divTitle mailto Link Syntax
    {:.indent2.bigandbold}&lt;&#91;*LinkID*&#93;&gt; &lt; : &gt; &lt;***mailto:you@yourdomain.com***&gt;
    [SP]
    {:.indent2.bigandbold}Examples:
    [SP]
    {:.indent3.bigandbold}&#91;email_me&#93;:mailto:user@mydomain.com *&lt;-- mailto Link Example*
    {:.indent3.bigandbold}&#91;feedback&#93;:mailto:user@mydomain.com?subject=feature%20feedback*&lt;-- mailto link with subject*
[email_me]:mailto:user@mydomain.com
[feedback]:mailto:user@mydomain.com?subject=feature%20feedback

I've defined the previous examples inline in the user docs, so now we can use them by embedding the link id within square brackets, like so: [email_me]. Or using the second form, send me [feedback].

{:.syntax}--- divTitle Variable Decorators
    [SP]
    {:.bigandbold.indent}&#91;variable]={:.class}value

So, if you declared this: [encode_smd(t="@var mynewvar=\"{:.bigandbold.red}My new big bold value\"")], and then write &#91;mynewvar], you'd get this:
@var mynewvar="{:.bigandbold.red}My new big bold value"
[mynewvar] &lt;-- At the start of the line
And it can also be used inline: [mynewvar]

### Delayed Expansion

Sometimes, it's useful to delay the expansion of a variable until right before it's used. Take the following example:

&#91;first]=Ken<br />&#91;last]=Lowrie[b]&#91;full]=&#91;first]&#91;last]

When you look at this, the expectation might be that the variable **&#91;full]** would be different if I changed &#91;first]=Brenda. But let's see what happens when we do that. Here's the code:

&#91;first]=Ken<br />&#91;last]=Lowrie[b]&#91;full]={:.red}&#91;first]&#91;last] \
[b]&#91;full][b]&#91;first]=Brenda[b]&#91;full]

And when we run that code:

[first]=Ken
[last]=Lowrie
[full]={:.red}[first] [last]
[full]
[first]=Brenda
[full]

This happens because any variable used in an assignment is expanded at the time that the variable is defined, and not when it's actually used. However, it's possible to force that behavior using **{{}}** when defining a variable. In this example, we'll change the line **&#91;full]={:.red}[{{first}}] [{{last}}]**, but everything else remains the same. Let's see what happens.

[first]=Ken
[last]=Lowrie
[full]={:.red}[{{first}}] [{{last}}]
[full]
[first]=Brenda
[full]

Sweet! Just what we wanted. By using the {{}} around a variable name used in an assignment of another variable, expansion is delayed until the variable is used. This feature is used quite a bit in the film, shot and image support later on. Check the examples in the tests directory to see it in action.

## Link aliases

Building on that, we can create aliases for inline links. Say I define a reference link like this: 
{:.indent}###&#91;cls]:https://cloudylogic.com
[cls]:https://cloudylogic.com
Now, when I write **&#91;cls]**, it is replaced with a link to https://cloudylogic.com. For example: [cls].
And that's all good. It's concise, I only have to write *cls* in [ ] and it is wrapped with an HTML link. Saves a lot of typing and potential mistakes. But what if I want to have other, more descriptive names for that URL? Good news, we can do that using a special form of aliases: [Descriptive Text]=[id], where *id* is the name of a previously described reference link. Let me go ahead and create an alias for the *cls* link so the descriptive name is Cloudy Logic.
{:.indent}###&#91;Cloudy Logic]=cls
[Cloudy Logic]=cls
Now, when I write [Cloudy Logic], it is wrapped with the link for *cls*. Cool!
