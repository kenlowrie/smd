[link.title_pages]
[wrap_h.chapter(t="##Cover, Revision & Contact Sections")]

There are three (3) specialized sections that can be defined within your document to add commonly used information in script files. They are:

{:.syntax.width60}--- divTitle Specialized Sections
    [SP]
    {:.indent.bigandbold}@cover - To add a cover section
    {:.indent.bigandbold}@revision - To add a revision section
    {:.indent.bigandbold}@contact - To add a contact section

The details for each specialized section follows.

{:.plain}@@@ plainTitle
### Cover Title

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@cover title="title of script" author="written by" logline="logline or short description"

Each element is optional, and they can appear in any order. Also note that the value of any parameter can be whatever you want. Just because it says "author", doesn't mean you have to put the author name there. You could instead write *"Roses are Red"*, and that would be just fine...

{:.plain}@@@ plainTitle
### Revision

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@revision v="revision" timestamp="yes"
Specify the revision number of your document within the angle brackets. If timestamp is either not specified or has any value other than "No", "Off", "False" or "0", the current date and time of the document at the time of processing will also be inserted immediately following the revision number. This provides additional clarification of the version, in case you forget to bump the version number.

If you specify timestamp="No" | "Off" | "False" | "0", then the timestamp will not be added to the revision string.

{:.plain}@@@ plainTitle
### Contact

{:.syntax}@@@ divTitle Syntax:
    [SP]
    {:.indent.bigandbold}@contact cn="name" ph="phone" em="email" c1="copyright 1" c2="copyright 2" c3="copyright 3"

The contact section allows you to specify several key elements about the script project. They include the following elements:

{:.syntax.width60}@@@ divTitle Contact Elements
    [SP]
    {:.indent.bigandbold}cn="Contact Name"
    {:.indent.bigandbold}ph="Contact Phone"
    {:.indent.bigandbold}em="Contact Email"
    {:.indent.bigandbold}c1="Copyright Line 1"
    {:.indent.bigandbold}c2="Copyright Line 2"
    {:.indent.bigandbold}c3="Copyright Line 3"

Each contact element is optional, and the elements can appear in any order. To see these tags in action, take a look at the **userguideheading.md** document in the import folder of this user guide.

