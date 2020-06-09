#!/usr/bin/env python
from pathlib import Path
from os import system

class commandLine(object):
    def __init__(self, name, inputfile, flags):
        self.input = Path().joinpath('in', inputfile)
        self.output = Path().joinpath('run', name).with_suffix(".html")
        self.diffo = self.output.with_suffix('.diff')
        self.html = Path().joinpath('out', Path(name).with_suffix(".html"))
        self.flags = flags
        self.name = name

    def cmdLine(self):
        return f"smd {self.flags} <{self.input} >{self.output}"

    def diffCmdLine(self):
        return f"diff {self.output} {self.html} >{self.diffo}"

    def dumpDiff(self):
        print(f"{'*'*60}\n{self.name}")
        system(f"cat {self.diffo}")

    def runTest(self):
        self.rc = system(self.cmdLine())
        self.drc = system(self.diffCmdLine())
        print(f"{self.name}: {'PASS' if self.drc == 0 else 'FAIL'}: Input File: '{self.input}' : Flags: [{self.flags}]")

cmdline_tests = [
    commandLine("test01",      "empty.md",         ""),
    commandLine("test01a",     "empty.md",         "-nu"),
    commandLine("test01b",     "empty.md",         "--no-user-files"),
    commandLine("test01c",     "empty.md",          "-nd"),
    commandLine("test01d",     "empty.md",          "--no-document-defaults"),
    commandLine("test01e",     "empty.md",          "-html"),
    commandLine("test01f",     "empty.md",          "--load-default-html"),
    commandLine("test01g",     "empty.md",          "-head"),
    commandLine("test01h",     "empty.md",          "--load-default-head"),
    commandLine("test01i",     "empty.md",          "-body"),
    commandLine("test01j",     "empty.md",          "--load-default-body"),
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
    commandLine("test02e",     "defaults.md",          "-html"),
    commandLine("test02f",     "defaults.md",          "--load-default-html"),
    commandLine("test02g",     "defaults.md",          "-head"),
    commandLine("test02h",     "defaults.md",          "--load-default-head"),
    commandLine("test02i",     "defaults.md",          "-body"),
    commandLine("test02j",     "defaults.md",          "--load-default-body"),
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


]

for test in cmdline_tests:
    test.runTest()

for test in cmdline_tests:
    if test.drc != 0:
        test.dumpDiff()


exit()



def run(inp, out, flags):

    htmlfile = Path(out).with_suffix('.html')
    system(f"smd {flags} <in/{inp} >run/{out}")
    rc = system(f"diff -q run/{out} out/{htmlfile}")
    print(f"{out} --- {'ok' if rc == 0 else 'fail'}")

run("empty.md", "test0.out", "-nd")
run("empty.md", "test1.out", "-nu -ndb")
run("empty.md", "test2.out", "-ndb")
run("empty.md", "test3.out", "-nd")




