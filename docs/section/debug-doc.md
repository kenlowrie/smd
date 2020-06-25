[link.debug]
{:.plain}@@@ plainTitle
{:.plainTitle}##Debugging

Dumping variables and links


.//TODO: This is completely out of date. These tags are not supported, and debugging has been completely redone, so need to document it.

There are two debugging tags that can be used in your document, and like ***///Shotlist///***, they must be on a line of their own.

{:.indent}###///Links/// - dumps all the links defined so far
{:.indent}###///Variables/// - dumps all the variables (aliases) defined

Here are those two tags in action for this document.

///Links///
@dump link="."

///Variables///
@dump basic="." var="."

