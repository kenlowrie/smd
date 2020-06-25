[link.ns_var]
[wrap_h(t="## The @var Namespace")]

The @var keyword is used to construct a more flexible type of variable for your documents. It uses a syntax similar to the @image keyword.


{:.syntax}--- divTitle @image keyword
    {:.indent}@var _id="varname" attr1="value1" _format="format string"

Here's how it works. _id="varname" is going to be how you reference any of the attributes of the variable. You can specify up to 20 attributes per variable, including the name, so really only 19. Accessing the variable attributes is similar to what we say with the @image attributes, using the dot syntax. Given the prior example:

{:.indent.bigandbold}&#91;varname.attr1] would be ***value1***[b] \
            &#91;varname._id] would be ***varname***, and [b]\
            &#91;varname._format] would be ***format string***.

So that's pretty cool, but there's a bit more to the _format attribute. You can reference the attributes contained within the variable by using **{{self}}.attrname**. Given that, if we rewrote the prior example as:

{:.indent.bigandbold} @var _id="fullname" first="ken" last="lowrie" _format="{{self.first}} {{self.last}}" 

and then we wrote:

{:.indent.bigandbold}&#91;fullname]

@var _id="fullname" first="ken" last="lowrie" _format="{{self.first}} {{self.last}}"

The result would be: **[fullname]**

Using that, you can build some pretty powerful tools for automating frequently used tasks in your documents. Take a look at the film.md, image.md and varv2.md tests to get an idea of what you can do.

Before we leave this, take note of the difference between {{first}} and {{self.first}}. Both syntaxes are valid, but the first one references the normal variable first, while the second one (self.first) references the first attribute defined within the *varname* variable. Also take note that you can reference the attributes of other @var variables as long as you qualify them. Let me show you a quick example of that. Take this:

{:.indent.bigandbold} @var _id="var1" first="ken" last="lowrie"[b] \
@var _id="var2" prefix="mr." _format="{{self.prefix}} {{var1.first}} {{var1.last}}"[b] \
&#91;var2]

When you run it, you get:

@var _id="var1" first="ken" last="lowrie"
@var _id="var2" prefix="mr." _format="{{self.prefix}} {{var1.first}} {{var1.last}}"
{:.indent}**[var2]**

One last thing, remember how we discussed that sometimes you need a way to resolve ambiguities of variables across the different variable types? **image.** can be used to resolve a variable inside the @image namespace, and **varv2.** can be used to resolve a variable inside the @var namespace. Given that:

{:indent.bigandbold} &#91;var2] and &#91;***varv2.***var2] resolve to the same variable.

This can let you build some really cool automation in your documents. But you need one more thing before you get started. A way to change one or more attributes of an existing @image or @var variable. Enter @set.

