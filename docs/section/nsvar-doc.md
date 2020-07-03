
[link.ns_var]
[wrap_h.chapter(t="## The @var Namespace")]

The @var keyword is used to construct a more flexible type of variable for your documents. These variables are stored in the @var namespace, and can have names that are identical to variables in other namespaces, although it is normally recommended that you avoid doing that. 

We will discuss this namespace first, because it is the basis for all namespaces, and most of the features, syntax and semantics apply to the others. Given that, it is a great starting point for our discussion on creating variables for use in [smd.b] documents.

[link.var_syntax]
[wrap_h.section(t="### @var Syntax")]

[syntax.wc_open(t="@var command syntax")]
    [b]
    [tab.<][smdvar.b] **name="value" [E.lb] attr="value" [E.lb]...]&nbsp;]**[bb][tab.>]
    [tab.<][smdvar.b] **_id="name" [E.lb]_format="value" [E.lb]...[E.rb][E.sp]]**[bb][tab.>]
    {:.red}[tab.<][tab.<]NOTE: either underscore [E.apos]**_**[E.apos] or [E.apos]**_id**[E.apos] can be used to name the variable.[tab.>][tab.>]
[syntax.wc_close]

[smdvar.b] variables are the only ones that can use the shorthand **name="value"** notation when defining a variable. All the other namespaces require that the **[E.lb]*_* or *_id*[E.rb]** special attribute name be used to specify the variable name.  Note that when the shorthand notation is used, it is the first **name="value"** pair that will be used to name the variable. Each of the following examples does exactly the same thing:

[terminal.wc_open(t="Defining a variable")]
[sp]
[smdvar_wp(parms="fu=\"bar\"")]
[smdvar_wp(parms="_=\"fu\" _format=\"bar\"")]
[smdvar_wp(parms="_id=\"fu\" _format=\"bar\"")]
[sp]
[terminal.wc_close]

Essentially, defining a variable in *any* of the namespaces is done in exactly this fashion. ***@ns*** followed by a series of attribute="value" pairs. Remember, only [smdvar.b] allows the shorthand **fu="bar"** format for naming the variable and setting the **_format** attribute value. All other namespaces require the alternate format.

[note.wc_open]
If you redeclare a variable, it will be overwritten with the new declaration. If you want to add attributes to an existing variable, use [smdset.b]
[note.wc_close]

[terminal.wc_open(t="Defining variables in other namespaces")]
[sp]
[smdvar_wp(parms="_id=\"fu\" _format=\"bar\"")]
[smdhtml_wp(parms="_id=\"fu\"")]
[smdlink_wp(parms="_id=\"fu\"")]
[sp]
[terminal.wc_close]

Notice that in the [smdhtml.b] and [smdlink.b] declarations we didn't specify the _format attribute. You'll see why when we get to the chapters on those namespaces, but for now, just realize that if you did specify the _format="bar" on those, then they would result in the exact same behavior as the @var variable. That is, when you write [e_var.b(t="var.fu")], [e_var.b(t="html.fu")], [e_var.b(t="link.fu")] in your markdown document, each would simply emit **bar**.

[terminal.wc_open(t="Using _format on [smdhtml.il] and [smdlink.il]")]
[sp]
[smdcomment] declare 'fu' in [smdvar.il], [smdhtml.il] & [smdlink.il]
[smdvar_wp(parms="_id=\"fu\" _format=\"bar\"")]
[smdhtml_wp(parms="_id=\"fu\" _format=\"bar\"")]
[smdlink_wp(parms="_id=\"fu\" _format=\"bar\"")]
[sp]
@var _id="fu" _format="bar"
@html _id="fu" _format="bar"
@link _id="fu" _format="bar"
[smdcomment] now print each one
[e_var(t="var.fu")] emits *[var.fu]*
[e_var(t="html.fu")] emits *[html.fu]*
[e_var(t="link.fu")] emits *[link.fu]*
[smdcomment] Redefine html.fu and link.fu
@html _id="fu"
@link _id="fu"
[smdcomment] now print each one
[e_var(t="var.fu")] emits *[var.fu]*
[e_var(t="html.fu")] emits *[escape_var(v="html.fu")]*
[e_var(t="link.fu")] emits *[escape_var(v="link.fu")]*

[terminal.wc_close]

The reason that [e_var.b(t="html.fu")] emits *[escape_var(v="html.fu")]* will be explained in the [smdhtml.b] chapter on variable declarations. For now, just go with it. [e_moji.big(e="tonguewink")]

One other caveat to the shorthand notation: if you specify also specify the **_format= attribute**, whatever you attempt to assign as part of the declaration will be ignored, and the value specified with _format will win. For example:

@var fu="bar" _format="123"
[terminal.wc_open(t="Using shorthand notation and specifiying _format")]
[sp]
[smdvar_wp(parms="fu=\"bar\" _format=\"123\"")]
[sp]
Then [e_var(t="fu")] will emit **[fu]** instead of *bar*
[sp]
[terminal.wc_close]


[link.var_syntax]
[wrap_h.section(t="### @var Variable names")]

Variable names in the [smdvar.b] namespace, well actually, in **any** namespace are restricted to these requirements:

[ulist.wc_open]
Must begin with a letter or the underscore character
Must contain only letters, numbers or underscores
Are case sensitive. That is, abc and ABC are different variable names
[ulist.wc_close]

Here are some examples of variable names:
[question.wc_open]
Need some table/header/row/data helpers
[question.wc_close]

[ulist.wc_open]
a - valid
a1 - valid
a_1 - valid
_a1 - valid
A - valid
{:.red}1a - invalid
{:.red}a-b - invalid
{:.red}1+ - invalid
{:.red}%a - invalid
[ulist.wc_close]

Attribute names, on the other hand, are restricted to these requirements:

[ulist.wc_open]
Must contain only letters, numbers, underscores or dashes
Are case sensitive. That is, abc and ABC are different variable names
[ulist.wc_close]

Here are some examples of attribute names:

[ulist.wc_open]
a - valid
a1 - valid
a_1 - valid
_a1 - valid
A - valid
1a - valid
a-b - valid
{:.red}1+ - invalid
{:.red}%a - invalid
[ulist.wc_close]

As you can see, attribute names are not quite as restrictive in their naming as variable names, allowing dashes to be used, and also allowing names to begin with numbers.

[link.var_attrs]
[wrap_h.section(t="### @var Built-in Attributes")]

[smdvar.b] variables have a number of built-in attributes to extract common components. In fact, all namespaces share these built-in attributes, and in the case of variables based on the [smdhtml.b] namespace, they are relied on much more, but nonetheless, they can be useful in any of the namespaces, if for no other reason to assist in debugging complex declarations.

Here is the full list of built-in attributes supported across all namespaces:

[ulist.wc_open]
_=The name of the variable
_id=The name of the variable
_private_attrs_=All of the private attributes (those that begin with underscore [E.apos]_[E.apos])
_public_attrs_=All of the public attributes (those that do not begin with underscore)
_private_attrs_esc_=Same as private attributes, but quotes are escaped.
_public_attrs_esc_=Same as public attributes, but quotes are escaped.
_public_keys_=The public attribute names
_private_keys_=The private attribute names
_all_attrs_=All attributes
_all_attrs_esc_=Same as all attributes, but quotes are escaped.
_null_=A null attribute - emits nothing, used to set default values of any public/private attribute

[ulist.wc_close]

[terminal.wc_open(t="Examples")]
[e_var.b(t="var.fu._")] *=* [fu._]
[e_var.b(t="var.fu._id")] *=* [fu._id]
[e_var.b(t="var.fu._all_attrs_")] *=*[fu._all_attrs_]
[e_var.b(t="var.fu._private_keys_")] *=*[fu._private_keys_]
[sp]
[e_var.b(t="html.divx._all_attrs_")] *=*[html.divx._all_attrs_]
[e_var.b(t="html.divx._private_attrs_")] *=*[html.divx._private_attrs_]
[e_var.b(t="html.divx._public_attrs_")] *=*[html.divx._public_attrs_]
[terminal.wc_close]

[link.var_misc]
[wrap_h.subsect(t="### @var Miscellaneous Examples")]

Here are just a few examples to help drive home your understanding of the declaration and usage of variables in the [smdvar.b] namespace.



//As you might expect, **ln_factory** inherits from **link._template**, and as such, it inherits attributes including **_asurl**. For example, [e_var.emb(t="link.sample._asurl")] which expands to **[escape_var(v="link.sample._asurl")]** and renders as: [link.sample._asurl]. 

Consider this declaration: 

[tab.<][smdvar_wp.b(parms="_id=\"varname\" attr1=\"value1\" _format=\"format string\"")][tab.>]

@var _id="varname" attr1="value1" _format="format string"

And now we write the following markdown:

[terminal.wc_open(t="")]

[e_var.b(t="varname.attr1")] would emit ***[varname.attr1]***.
[e_var.b(t="varname._id")] would emit ***[varname._id]***.
[e_var.b(t="varname._format")] would emit ***[varname._format]***.

[terminal.wc_close]

So that's pretty cool, but there's a bit more to the _format attribute. You can reference the attributes contained within the variable by using **{{self}}.attrname**. Given that, if we rewrote the prior example as:

[tab.<][smdvar_wp.b(parms="_id=\"fullname\" first=\"ken\" last=\"lowrie\" _format=\"[E.lcb2]self.first[E.rcb2] [E.lcb2]self.last[E.rcb2]\"")][tab.>]

@var _id="fullname" first="ken" last="lowrie" _format="{{self.first}} {{self.last}}"

[terminal.wc_open(t="")]
[e_var.b(t="fullname")] would emit ***[fullname]***.
[terminal.wc_close]

Using that, you can build some pretty powerful tools for automating frequently used tasks in your documents. Take a look at the **film.md**, **image.md** and **avs.md** tests to get an idea of what you can do.

Before we leave this, take note of the difference between {{first}} and {{self.first}}. Both syntaxes are valid, but the first one references the normal variable first, while the second one (self.first) references the first attribute defined within the *varname* variable. Also take note that you can reference the attributes of other @var variables as long as you qualify them. Let me show you a quick example of that. Take this:

[tab.<][smdvar_wp.b(parms="_id=\"var1\" first=\"ken\" last=\"lowrie\"")][tab.>]
[tab.<][smdvar_wp.b(parms="_id=\"var2\" prefix=\"mr.\" _format=\"{{self.prefix}} {{var1.first}} {{var1.last}}\"")][tab.>]

@var _id="var1" first="ken" last="lowrie"
@var _id="var2" prefix="mr." _format="{{self.prefix}} {{var1.first}} {{var1.last}}"

Then, if you write this:

[terminal.wc_open(t="")]
[e_var.b(t="var2")] would emit ***[var2]***.
[terminal.wc_close]

One last thing, remember how we discussed that sometimes you need a way to resolve ambiguities of variables across the different variable types? **image.** can be used to resolve a variable inside the [smdimage.b] namespace, and **var.** can be used to resolve a variable inside the [smdvar.b] namespace. Given that:

[terminal.wc_open(t="")]
[e_var.b(t="var2")] and [e_var.b(t="*var*.var2")] resolve to the same thing.
[terminal.wc_close]

This can let you build some really cool automation in your documents. But you need one more thing before you get started. A way to change one or more attributes of an existing variable in any namespace. Enter [smdset.b] and the **_null_** attribute.

[link.set_keyword]
[wrap_h.subsect(t="### The [smdset.il] Keyword")]

Attributes of any variable in any namespace can be added or updated at any time. There are two (perhaps three depending on semantics) ways this can be done in all namespaces except [smdcode.b]. In [smdcode.il], there is only one way to update an attribute value, and that is with [smdset.b]. Let's see how it's done.

[terminal.wc_open(t="Updating attribute values with [smdset.il]")]
[smdcomment_wp(parms="First, let's declare a new variable called 'fu'")]
[smdvar_wp.b(parms="fu=\"bar\" attr1=\"value1\"")]
@var fu="bar" attr1="value1"
[e_var.b(t="fu.attr1")] emits **[fu.attr1]**

[sp]
[smdcomment_wp(parms="using [smdset.il], change the value of attr1 to 'value2'")]
[smdset_wp.b(parms="_=\"fu\" attr1=\"value2\"")]
@set _="fu" attr1="value2"
[e_var.b(t="fu.attr1")] emits **[fu.attr1]**

[sp]
[smdcomment_wp(parms="using the _null_ attribute, change the value of attr1 to 'value3'")]
[e_var.b(t="fu._null_[E.lp]attr1=\"value3\"[E.rp]")]
[fu._null_(attr1="value3")]
[e_var.b(t="fu.attr1")] emits **[fu.attr1]**

[terminal.wc_close]

[note(t="The **_null_** attribute illustrates an important concept with the attributes of variables in [smd.b]. That is, any time an attribute value is changed by specifying a new value when a method is invoked, that value becomes the new value for that attribute. This is true with all namespaces except [smdcode.b]; in the [smdcode.b] namespace, attribute values overridden via a method invocation are temporary. Once the method returns, the original attribute values are restored.[bb]As previously mentioned, the only way to change the value of a variable in the [smdcode.b] namespace is by using [smdset.b]. When this is done, the code behind the variable (Python source code) is recompiled, which essentially updates their usage in the compiled code stored as part of the variable.")]

You can also add new attributes to an existing variable with [smdset.b]. And, if you [smdset.b] a variable that does not exist, [smdset.b] will create it. Let's see both of these things in action now.

[terminal2.wc_open(t="Adding attributes with [smdset.il]")]
[terminal2.wc_open_content]
[smdcomment_wp.il(parms="add a new attribute to 'fu' using [smdset.il]")]
[smdset_wp.b(parms="_=\"fu\" attr2=\"value42\"")]
@set _="fu" attr2="value42"
[e_var.b(t="fu.attr2")] emits **[fu.attr2]**
[sp]
[smdcomment_wp.il(parms="adding a new attribute doesn't affect existing attributes in 'fu'")]
[e_var.b(t="fu.attr1")] still emits **[fu.attr1]**

[sp]
[smdcomment_wp.il(parms="using the _null_ attribute, add attr3 to 'fu'")]
[e_var.b(t="fu._null_[E.lp]attr3=\"many ways to add attributes\"[E.rp]")]
[fu._null_(attr3="many ways to add attributes")]
[e_var.b(t="fu.attr3")] emits **[fu.attr3]**

[sp]
[smdcomment_wp.il(parms="We can also add and update variables at the same time")]
[e_var.b(t="fu._null_[E.lp]attr3=\"update 3rd attribute\" attr4=\"add 4th attribute\"[E.rp]")]
[fu._null_(attr3="update 3rd attribute" attr4="add 4th attribute")]
[e_var.b(t="fu.attr3")] emits **[fu.attr3]** and [e_var.b(t="fu.attr4")] emits **[fu.attr4]**

[sp]
[smdcomment_wp.il(parms="We can also add and update variables at the same time using [smdset.b]")]
[smdset_wp.b(parms="_=\"fu\" attr2=\"update attr2\" attr6=\"6th attribute\"")]
@set _="fu" attr2="update attr2" attr6="6th attribute"
[e_var.b(t="fu.attr2")] emits **[fu.attr2]** and [e_var.b(t="fu.attr6")] emits **[fu.attr6]**
[terminal2.wc_close_content]
[terminal2.wc_close]

Let's dump the variable 'fu' to see all the attributes and their values.


[fatmargin._open] 
[var.code.wc_open(t="Current definition of [E.apos]fu[E.apos] variable")]
@dump var="fu$"
[var.code.wc_close]
[fatmargin._close]

And finally, you can also specify the namespace two different ways with [smdset.b]. Witness:

[terminal.wc_open(t="Specifying the namespace")]

[smdcomment_wp(parms="Specify the namespace with @set; don't leave it to chance!")]
[smdset_wp.b(parms="*_ns=\"var\"* _=\"fu\" attr6=\"update attr6\"")]
@set _ns="var" _="fu" attr6="update attr6"
[e_var.b(t="fu.attr6")] emits **[fu.attr6]**
[sp]
[smdcomment_wp(parms="Alternate method to set namespace")]
[smdset_wp.b(parms="_=\"*var.*fu\" attr6=\"update attr6 again!\"")]
@set _="var.fu" attr6="update attr6 again!"
[e_var.b(t="fu.attr6")] emits **[fu.attr6]**

[terminal.wc_close]

One last time let's dump the variable 'fu' to see all the attributes and their values.

[fatmargin._open] 
[var.code.wc_open(t="Current definition of [E.apos]fu[E.apos] variable")]
@dump var="fu$"
[var.code.wc_close]
[fatmargin._close]

Here are just a few examples to help drive home your understanding of the declaration and usage of variables in the [smdvar.b] namespace.

[question.wc_open]
Discuss @set and also [e_var.b(t="var._null_[E.lp]attr=\"\"[E.rp]")]
[question.wc_close]

[note(t="[smdcode.b] attributes cannot be changed via _null_ or when markdown is applied. You must use [smdset.b] to do that")]

@var ns="var"

@set _ns="[ns]" _="c2" attr1="*attribute 1*" attr2="**attribute 2**" attr3="{{self.attr1}}--{{self.attr2}}" attr4="[self.attr2]--[self.attr1]"
[encode_smd(t="[c2.attr1]")] = [c2.attr1]
[encode_smd(t="[c2.attr2]")] = [c2.attr2]
[encode_smd(t="[c2.attr3]")] = [c2.attr3]
[encode_smd(t="[c2.attr4]")] = [c2.attr4]

//[docthis.open(h="Add this to nsvar-doc.md")]
//[docthis.close]

