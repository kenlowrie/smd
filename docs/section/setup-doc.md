[link.setup]
[wrap_h.chapter(t="## Setting up smd")]

this will talk about how to setup your environment for smd. Needs to pull from the readme.md from the root! That way it stays up to date..

this is where you can say pip install . or pip install -e . or pipenv install

[docthis.open(h="Add this to setup-doc.md")]

Make the build process create a "compiled" version of the documentation as a part of the build tree, so the instructions in the README.md can say to just "open this file with your browser" to read the docs current with the release you are looking at... Doesn't need to be a build thing, just needs to be a "release" thing.

[docthis.close]
[wrap_h.section(t="### README.md from root of this tree")]
@wrap divx
@html _="divxplus" _inherit="divx" style="margin:5em;margin-right:250px;background-color:lightgray;padding:2em"
@@[divxplus.<]
@import "[sys.basepath]/../README.md"
@@[divxplus.>]
@parw 1
