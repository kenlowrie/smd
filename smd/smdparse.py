#!/usr/bin/env python3

"""
This module provides a wrapper for the most common use case of smd.

usage:

    parsesmd --help

"""

from os import system, mkdir
from os.path import split, splitext, join, isdir, isfile

from sys import argv, exit

import kenl380.pylib as pylib


def context():
    """returns the context object for this script."""

    try:
        myself = __file__
    except NameError:
        myself = argv[0]

    return pylib.context(myself)


me = context()


def message(msgstr):
    print('{0}: {1}'.format(me.alias(), msgstr))

def get_head(mdfile, cssFile, title = None):
    path, name = split(mdfile)
    file, ext = splitext(name)
    the_title = title if title is not None else str(file)

    head = """<head>
    <title>"""
    head += the_title
    head += """</title>
    <meta charset="UTF-8">
    <link rel='stylesheet' href='{0}' />
</head>
""".format(str(cssFile.name))

    return [head]


def get_tail():
    return """
</body>
</html>
"""




"""
TODO:
Need to make it so if you specify a path on cssfile, we strip it off since
it will be copied to the destination folder. We only need the path when
doing the transfer.

outpath should also be handled better so that we can use relative or absolute
and it will do the right thing with either.

"""

from pathlib import Path
import traceback

class ScriptParser():
    def __init__(self, inputFile, cssFile, outputDir, sysDefaults):
        self.lastParseOK = False
        self.smdFile = Path(inputFile).resolve()
        self.cssFile = Path(cssFile).resolve()
        self.outDir = Path(outputDir).resolve()
        self.outFile = Path().joinpath(self.outDir, Path(self.smdFile.name).with_suffix(".html"))
        self.sysDefs = sysDefaults
        self._copy_cssfile()
        self.parse(True)

    def _copy_cssfile(self):
        if not isfile(self.cssFile):
            print("Can't find [{}]. Giving up.".format(self.cssFile))
            raise FileNotFoundError

        if not isdir(self.outDir):
            mkdir(self.outDir)
        from shutil import copy2
        try:
            copy2(self.cssFile, self.outDir)
        except OSError as why:
            print("Error copying CSS file: [{}]".format(str(why)))
 

    def parse_script(self):
        htmlfile = open(self.outFile, "w")

        from smd.smd import ScriptParser

        self.sysDefs.addConfigFileData("import/def_head.md", get_head(self.smdFile,self.cssFile))
        #self.sysDefs.addConfigFileData("import/def_head.md", get_head(self.smdFile,self.cssFile,self.smdFile))

        #sd.addConfigFileData("import/def_body.md", ["<body class=\"my-cool-class\">", "<div class=\"wrapper\">"])

        message("Creating: " + str(self.smdFile))
        
        avscript_obj = ScriptParser(self.sysDefs)
        avscript_obj.stdoutput = htmlfile
        avscript_obj.open_and_parse(str(self.smdFile))
        
        htmlfile.close()

    def parameterInfo(self):
        print(f"smdFile={self.smdFile}\ncssFile={self.cssFile}\noutputDir={self.outDir}\nhtmlFile={self.outFile}")

    def parse(self,firstTime=False):
        try:
            print("Parsing {}{}".format(self.smdFile,"" if firstTime == False else " initially ..."))
            self.parse_script()
            self.lastParseOK = True
        except:
            print("Caught exception parsing the script ...")
            self.lastParseOK = False
            traceback.print_exc()


def parse(arguments=None):
    """Make an Audio-Visual Script from a text file written in a Markdown-like syntax.

    Creates an HTML output file from the input file.

    if arguments is None, uses sys.argv - via argparse
    if no filename is specified, parses sys.stdin -- //TODO: IS THIS TRUE?

    Exit code:
        0 -- Success
        1 -- File not found
        2 -- IO Error processing input file
        3 -- Invalid regex ID in main loop
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Generate HTML file from a text file in Script Markdown format.',
                            epilog='This utility exits after parsing the input file.')
    parser.add_argument('-f', '--filename', required=True, help='the file that you want to parse')
    parser.add_argument('-c', '--cssfile', nargs='?', const='smd.css', default='smd.css', help='the CSS file you want used for the styling. Default is smd.css')
    parser.add_argument('-d', '--path', nargs='?', const='./html', default='./html', help='the directory that you want the HTML file written to. Default is ./html')
    parser.add_argument('-o', '--open', nargs='?', const=True, default=False, help='whether or not to open the resulting HTML output file with the default system app')

    from smd.smd import smd_add_std_cmd_line_parms
    from smd.core.sysdef import SystemDefaults

    sysDefaults = SystemDefaults()

    args = smd_add_std_cmd_line_parms(parser, sysDefaults, None if arguments is None else arguments)

    # //TODO: Not sure if I like this hack...
    if not Path(args.cssfile).is_file():
        from smd.core.globals import _getBasepath
        new_cssfile = Path().joinpath(_getBasepath(), "css/smd.css")
        args.cssfile = str(new_cssfile)

    sp = ScriptParser(args.filename, args.cssfile, args.path, sysDefaults)

    return 0 if sp.lastParseOK else 1
    

if __name__ == '__main__':
    exit(parse())
