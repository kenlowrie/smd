#!/usr/bin/env python
from pathlib import Path
from os import system
from os import chdir


class UserSMDPathError(Exception):
    """Path exceptions raised by this module."""
    def __init__(self, errno, errmsg):
        self.errno = errno
        self.errmsg = errmsg


cwd = Path(__file__).parent.resolve()
#chdir(Path().joinpath(parent,'sos'))
chdir(cwd)
print(f"Current working directory: {Path().cwd()}")

class userImports(object):
    smdDir = '.smd'
    smdTestDir = 'cmdline-test-dir'
    smdDirSave = smdTestDir + '-backup'
    def __init__(self):
        self.cmdlineTestDir = cwd
        self.userSMDdir = Path().joinpath(Path().home(), userImports.smdDir)
        self.userSMDsaveDir = Path().joinpath(self.userSMDdir.parent, self.userSMDdir.name + userImports.smdDirSave)
        self.hadUserSMDdir = self.userSMDdir.is_dir()
        self.copiedTestDir = False
        #print(f"userSMDdir = {self.userSMDdir}")
        #print(f"userSMDsaveDir = {self.userSMDsaveDir}")
        #print(f"cmdlineTestDir = {self.cmdlineTestDir}")

    def saveUserDir(self):
        if self.userSMDsaveDir.is_dir():
            print(f"User save directory {self.userSMDsaveDir} already exists. Ignoring save request.")
            return

        if self.hadUserSMDdir:
            print(f"Saving existing user directory: {self.userSMDdir}")
            try:
                self.userSMDdir.rename(self.userSMDsaveDir)
            except Exception as ex:
                print(f"exception {ex.args} during rename")
                raise UserSMDPathError(1, "error attempting to save local user folder")

        self.transferTestingUserDirectory()


    def transferTestingUserDirectory(self):
        userTestSrcDir = Path().joinpath(self.cmdlineTestDir, userImports.smdTestDir)
        if not userTestSrcDir.is_dir():
            print(f"User test source directory {userTestSrcDir} does not exist. Cannot continue.")
            return

        print(f"Copydir {userTestSrcDir} to {self.userSMDdir} ...")
        from shutil import copytree
        try:
            copytree(userTestSrcDir, self.userSMDdir)
        except Exception as ex:
                print(f"exception {ex.args} during copytree")
                raise UserSMDPathError(2, "error attempting to transfer testing directory")
            
        self.copiedTestDir = True

    def restoreUserDir(self):
        if self.copiedTestDir:
            print(f"Removing the test directory that we copied ...")
            if not self.userSMDdir.is_dir():
                print(f"User directory {self.userSMDdir} does not exist. Ignoring removing request.")
            else:
                print(f"Removing current user directory {self.userSMDdir}.")
                from shutil import rmtree
                try:
                    rmtree(self.userSMDdir)
                except Exception as ex:
                    print(f"exception {ex.args} during rmtree")
                    raise UserSMDPathError(3, "error attempting to remove local testing folder")

        if not self.userSMDsaveDir.is_dir():
            print(f"User save directory {self.userSMDsaveDir} does not exist. Ignoring restore request.")
        else:
            print(f"Restoring original user directory.")
            try:
                self.userSMDsaveDir.rename(self.userSMDdir)
            except Exception as ex:
                print(f"exception {ex.args} during restore original user directory")
                raise UserSMDPathError(4, "error attempting to restore local user folder")

            print(f"Rename {self.userSMDsaveDir} to {self.userSMDdir} ...")

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
    commandLine("test03ia",    "defdump.md",          "-ldb -nub"),
    commandLine("test03j",     "defdump.md",          "-ndb"),
    commandLine("test03k",     "defdump.md",          "-lub"),
    commandLine("test03ka",    "defdump.md",          "-lub -ndb"),
    commandLine("test03l",     "defdump.md",          "-nub"),
    commandLine("test03m",     "defdump.md",          "-o"),

    commandLine("test04a",     "defdump.md",         "-nub -lub"),
    commandLine("test04b",     "defdump.md",          "-ndb -ldb"),
    commandLine("test04c",     "defdump.md",          "-nd -nu"),
    commandLine("test04d",     "defdump.md",          "-nu"),
    
    commandLine("test05a",     "docovrd.md",          "-head fu.bar -nohead"),
    commandLine("test05b",     "docovrd.md",          "-html fu.bar -nohtml"),
    commandLine("test05c",     "docovrd.md",          "-close fu.bar -nohtml"),
    commandLine("test05d",     "docovrd.md",          "-body fu.bar -nobody"),
    commandLine("test05e",     "docovrd.md",          "-bodyclose fu.bar -nobody"),
    commandLine("test05f",     "docovrd.md",          "-html in/html_oride.md"),
    commandLine("test05g",     "docovrd.md",          "-head in/head_oride.md"),
    commandLine("test05h",     "docovrd.md",          "-body in/body_oride.md"),
    commandLine("test05i",     "docovrd.md",          "-bodyclose in/bodyclose_oride.md"),
    commandLine("test05j",     "docovrd.md",          "-close in/close_oride.md"),
    commandLine("test05k",     "docovrd.md",          "-html in/html_oride.md -head in/head_oride.md -body in/body_oride.md -bodyclose in/bodyclose_oride.md -close in/close_oride.md"),
]
ignore=[

    commandLine("test05a",     "docovrd.md",          "-head fu.bar -nohead"),
    commandLine("test05b",     "docovrd.md",          "-html fu.bar -nohtml"),
    commandLine("test05c",     "docovrd.md",          "-close fu.bar -nohtml"),
    commandLine("test05d",     "docovrd.md",          "-body fu.bar -nobody"),
    commandLine("test05e",     "docovrd.md",          "-bodyclose fu.bar -nobody"),
    commandLine("test05f",     "docovrd.md",          "-html in/html_oride.md"),
    commandLine("test05g",     "docovrd.md",          "-head in/head_oride.md"),
    commandLine("test05h",     "docovrd.md",          "-body in/body_oride.md"),
    commandLine("test05i",     "docovrd.md",          "-bodyclose in/bodyclose_oride.md"),
    commandLine("test05j",     "docovrd.md",          "-close in/close_oride.md"),
    commandLine("test05k",     "docovrd.md",          "-html in/html_oride.md -head in/head_oride.md -body in/body_oride.md -bodyclose in/bodyclose.md -close in/close_oride.md"),


]
from sys import argv
which = cmdline_tests if len(argv) == 1 else [x for x in cmdline_tests if x.name.startswith(argv[1])]
#print(which)
#exit()

print(f"Saving local user state")
userDir = userImports()
userDir.saveUserDir()

#which = cmdline_tests[0:]
for test in which:
    test.runTest()

errors = 0
for test in which:
    if test.drc != 0:
        errors+=1
        test.dumpDiff()

print(f"All tests are PASSING!" if errors == 0 else f"{errors} test{'s' if errors == 1 else ''} have FAILED.")
print(f"Restoring local user state")
userDir.restoreUserDir()
print("all done...")


exit()

