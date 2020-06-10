#!/usr/bin/env python
from pathlib import Path
from os import system
from os import chdir

parent = Path(__file__).parent
#chdir(Path().joinpath(parent,'sos'))
chdir(parent)

class commandLine(object):
    def __init__(self, name, inputfile, flags, dcl=None, input_as=None):
        self.dcl = "smd" if dcl is None else dcl
        self.input_as = "-f " if input_as is None else input_as
        self.input = Path().joinpath('in', inputfile)
        self.output = Path().joinpath('run', name).with_suffix(".html")
        self.diffo = self.output.with_suffix('.diff')
        self.html = Path().joinpath('out', Path(name).with_suffix(".html"))
        self.flags = flags
        self.name = name

    def cmdLine(self):
        return f"{self.dcl} {self.flags} {self.input_as}{self.input} >{self.output} 2>&1"

    def diffCmdLine(self):
        return f"diff {self.html} {self.output} >{self.diffo}"

    def dumpDiff(self):
        print(f"{'*'*60}\n{self.name}")
        system(f"cat {self.diffo}")

    def runTest(self):
        #print(f"-->{self.cmdLine()}")
        self.rc = system(self.cmdLine())
        #print(f"-->{self.diffCmdLine()}")
        self.drc = system(self.diffCmdLine())
        print(f"{self.name}: {'PASS' if self.drc == 0 else 'FAIL'}: Input File: '{self.input}' : Flags: [{self.flags}]")

cmdline_tests = [
    commandLine("test00a",     "notexist.md",         "",      dcl="smdparse"),
    commandLine("test00b",     "notexist.md",         "-nu",   dcl="ismd"),
    commandLine("test00c",     "notexist.md",         "-nu"),
    commandLine("test00d",     "notexist.md",         "-h",    dcl="smdparse"),
    commandLine("test00e",     "notexist.md",         "-h",   dcl="ismd"),
    commandLine("test00f",     "notexist.md",         "-h"),
    commandLine("test00g",     "notexist.md",         "--help",    dcl="smdparse"),
    commandLine("test00h",     "notexist.md",         "--help",   dcl="ismd"),
    commandLine("test00i",     "notexist.md",         "--help"),
    commandLine("test00j",     "notexist.md",         "-f",    dcl="smdparse"),
    commandLine("test00k",     "notexist.md",         "-f",   dcl="ismd"),
    commandLine("test00l",     "notexist.md",         "-f"),

    commandLine("test01",      "empty.md",         "", input_as="<"),
    commandLine("test01a",     "empty.md",         "-nu", input_as="<"),
    commandLine("test01b",     "empty.md",         "--no-user-files"),
    commandLine("test01c",     "empty.md",          "-nd"),
    commandLine("test01d",     "empty.md",          "--no-document-defaults"),
    commandLine("test01e",     "empty.md",          "-html htmldoc.md"),
    commandLine("test01f",     "empty.md",          "--set-html-name htmldoc.md"),
    commandLine("test01g",     "empty.md",          "-head headdoc.md"),
    commandLine("test01h",     "empty.md",          "--set-head-name headdoc.md"),
    commandLine("test01i",     "empty.md",          "-body bodydoc.md"),
    commandLine("test01j",     "empty.md",          "--set-body-name bodydoc.md"),
    commandLine("test01ja",    "empty.md",          "-bodyclose bodyclosedoc.md"),
    commandLine("test01jb",    "empty.md",          "--set-bodyclose-name bodyclosedoc.md"),
    commandLine("test01jc",    "empty.md",          "-close closedoc.md"),
    commandLine("test01jd",    "empty.md",          "--set-close-name closedoc.md"),
    commandLine("test01k",     "empty.md",          "-nohtml"),
    commandLine("test01l",     "empty.md",          "--no-default-html"),
    commandLine("test01m",     "empty.md",          "-nohead"),
    commandLine("test01n",     "empty.md",          "--no-default-head"),
    commandLine("test01o",     "empty.md",          "-nobody"),
    commandLine("test01p",     "empty.md",          "--no-default-body"),

    commandLine("test02",      "defaults.md",         ""),
    commandLine("test02a",     "defaults.md",         "-nu"),
    commandLine("test02b",     "defaults.md",         "--no-user-files"),
    commandLine("test02c",     "defaults.md",          "-nd"),
    commandLine("test02d",     "defaults.md",          "--no-document-defaults"),
    commandLine("test02e",     "defaults.md",          "-html htmldoc.md"),
    commandLine("test02f",     "defaults.md",          "--set-html-name htmldoc.md"),
    commandLine("test02g",     "defaults.md",          "-head headdoc.md"),
    commandLine("test02h",     "defaults.md",          "--set-head-name headdoc.md"),
    commandLine("test02i",     "defaults.md",          "-body bodydoc.md"),
    commandLine("test02j",     "defaults.md",          "--set-body-name bodydoc.md"),
    commandLine("test02ja",    "defaults.md",          "-bodyclose bodyclosedoc.md"),
    commandLine("test02jb",    "defaults.md",          "--set-bodyclose-name bodyclosedoc.md"),
    commandLine("test02jc",     "defaults.md",         "-close closedoc.md"),
    commandLine("test02jd",     "defaults.md",         "--set-close-name closedoc.md"),
    commandLine("test02k",     "defaults.md",          "-nohtml"),
    commandLine("test02l",     "defaults.md",          "--no-default-html"),
    commandLine("test02m",     "defaults.md",          "-nohead"),
    commandLine("test02n",     "defaults.md",          "--no-default-head"),
    commandLine("test02o",     "defaults.md",          "-nobody"),
    commandLine("test02p",     "defaults.md",          "--no-default-body"),
    commandLine("test02q",     "defaults.md",          "-ldb"),
    commandLine("test02r",     "defaults.md",          "--load-default-builtins"),
    commandLine("test02s",     "defaults.md",          "-ndb"),
    commandLine("test02t",     "defaults.md",          "--no-default-builtins"),
    commandLine("test02u",     "defaults.md",          "-lub"),
    commandLine("test02v",     "defaults.md",          "--load-user-builtins"),
    commandLine("test02w",     "defaults.md",          "-nub"),
    commandLine("test02x",     "defaults.md",          "--no-user-builtins"),
    commandLine("test02y",     "defaults.md",          "-o"),
    commandLine("test02z",     "defaults.md",          "--output-raw-data"),

    commandLine("test03",      "defdump.md",         ""),
    commandLine("test03a",     "defdump.md",         "-nu"),
    commandLine("test03b",     "defdump.md",          "-nd"),
    commandLine("test03c",     "defdump.md",          "-html htmldoc.md"),
    commandLine("test03d",     "defdump.md",          "-head headdoc.md"),
    commandLine("test03e",     "defdump.md",          "-body bodydoc.md"),
    commandLine("test03ea",    "defdump.md",          "-bodyclose bodyclosedoc.md"),
    commandLine("test03eb",    "defdump.md",          "-close closedoc.md"),
    commandLine("test03f",     "defdump.md",          "-nohtml"),
    commandLine("test03g",     "defdump.md",          "-nohead"),
    commandLine("test03h",     "defdump.md",          "-nobody"),
    commandLine("test03i",     "defdump.md",          "-ldb"),
    commandLine("test03j",     "defdump.md",          "-ndb"),
    commandLine("test03k",     "defdump.md",          "-lub"),
    commandLine("test03l",     "defdump.md",          "-nub"),
    commandLine("test03m",     "defdump.md",          "-o"),

    commandLine("test04a",     "defdump.md",         "-nub -lub"),
    commandLine("test04b",     "defdump.md",          "-ndb -ldb"),
    commandLine("test04c",     "defdump.md",          "-nd -nu"),
    
]
ignore=[

    commandLine("test04d",     "defdump.md",          "-head"),
    commandLine("test04e",     "defdump.md",          "-body"),
    commandLine("test04f",     "defdump.md",          "-nohtml"),
    commandLine("test04g",     "defdump.md",          "-nohead"),
    commandLine("test04h",     "defdump.md",          "-nobody"),
    commandLine("test04i",     "defdump.md",          "-ldb"),
    commandLine("test04j",     "defdump.md",          "-ndb"),
    commandLine("test04k",     "defdump.md",          "-lub"),
    commandLine("test04l",     "defdump.md",          "-nub"),
    commandLine("test04m",     "defdump.md",          "-o"),


]

which = cmdline_tests[0:]
for test in which:
    test.runTest()

for test in which:
    if test.drc != 0:
        test.dumpDiff()


exit()

