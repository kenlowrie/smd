#!/usr/bin/env python3

"""
This module provides a wrapper for the most common use cases of smd.

Essentially, that is to parse a file in script markdown format and create an HTML document from it.

usage:

    smdparse --help

"""

from smd.smdutil import ConsoleMessage

message = ConsoleMessage(__file__)

# Override the default (def_html.md) markdown that smd uses, and provide our custom version.
# def_html.md, def_body.md, def_bodyclose.md and def_close.md are all okay as-is.
def get_head(mdfile, cssFileList, title = None):
    the_title = title if title is not None else str(mdfile.name)

    #stylesheets = [file.name for file in cssFileList]
    stylesheets = [f'\n    <link rel="stylesheet" href="{file.name}" />' for file in cssFileList]

    head = """<head>
    <title>"""
    head += the_title
    head += """</title>
    <meta charset="UTF-8">{0}
</head>
""".format(''.join(i for i in stylesheets) if len(stylesheets) > 0 else '')

    return [head]


from pathlib import Path
import traceback

class ScriptParser():
    def __init__(self, inputFile, cssFileList, importFileList, outputDir, sysDefaults):
        self.lastParseOK = False
        self.smdFile = Path(inputFile).resolve()
        self.cssFileList = [Path(item).resolve() for item in cssFileList] # Path(cssFile).resolve() if cssFile is not None else cssFile
        self.outDir = Path(outputDir).resolve()
        self.outFile = Path().joinpath(self.outDir, Path(self.smdFile.name).with_suffix(".html"))
        self.importFileList = importFileList
        self.sysDefs = sysDefaults
        self._copy_cssfiles()
        self.parse(True)

    def _copy_cssfiles(self):
        for file in self.cssFileList:
            if not file.is_file():
                message.o("Can't find [{}], ignoring ...".format(file))
                continue

            if not self.outDir.is_dir():
                self.outDir.mkdir()
            from shutil import copy2
            try:
                copy2(file, self.outDir)
            except OSError as why:
                message.o("Error copying CSS file: {}".format(str(why)))
 

    def _parse_script(self):
        htmlfile = open(self.outFile, "w")

        from smd.smd import ScriptParser

        self.sysDefs.addConfigFileData("import/def_head.md", get_head(self.smdFile,self.cssFileList))
        self.sysDefs.addImportFiles(self.importFileList)

        message.o("Creating: " + str(self.outFile))
        
        smdscript_obj = ScriptParser(self.sysDefs)
        smdscript_obj.stdoutput = htmlfile
        smdscript_obj.open_and_parse(str(self.smdFile))
        
        htmlfile.close()

    def dump(self):
        message.o("Dumping the ScriptParser Instance variables.")
        message.o(f"lastParseOK={self.lastParseOK}")
        message.o(f"smdFile={self.smdFile}")
        message.o(f"cssFileList={self.cssFileList}")
        message.o(f"outputDir={self.outDir}")
        message.o(f"htmlFile={self.outFile}")
        message.o(f"sysDefs (SystemDefaults Instance):")
        self.sysDefs.dump(message.o)

    def parse(self,firstTime=False):
        try:
            message.o("Parsing {}{}".format(self.smdFile,"" if firstTime == False else " initially ..."))
            self._parse_script()
            self.lastParseOK = True
        except:
            message.o("Caught exception parsing the script ...")
            self.lastParseOK = False
            traceback.print_exc()


def handle_cssfilelist_parameter(cssfilelist):
    """Convert optional list of css files into a consistent list form

    Specifying one or more css files is optional, and the argparser will provide
    inconsistent results depending on whether the optional parameter is used, so
    we need to normalize the list.
    """
    # if -c/--cssfile was specified but no arg passed, use the built-in default css.
    # if -c/--cssfile is not specified, args.cssfilelist = None
    # if -c/--cssfile specified w/o filename, then args.cssfilelist == []
    if cssfilelist is not None and len(cssfilelist) == 0:
        from smd.core.globals import _getBasepath
        new_cssfile = Path().joinpath(_getBasepath(), "css/smd.css")
        return [str(new_cssfile)]
    
    return [] if cssfilelist is None else cssfilelist

def get_importfilelist(args):
    """Convert optional list of import files into a consistent list form

    Specifying one or more import files to load at startupis optional.
    
    If the -i/--import switch isn't provided, then None is passed on.
    
    if the -i/--import is specified without a filename, then we will
    place Path("import_--filename.md") as the only item in the list.
    
    Otherwise, the list of files will be passed on as-is.
    """
    if args.importfilelist is not None and len(args.importfilelist) == 0:
        filename = Path(args.filename).resolve()
        return [str(Path().joinpath(filename.parent, f'import_{filename.name}'))]
    
    return args.importfilelist


def parse(arguments=None):
    """Create an HTML file from a text file written in Script Markdown.
    
    if arguments is None, uses sys.argv - via argparse
    
    Exit code:
        0 -- Success
        1 -- Failure
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Generate HTML file from a text file in Script Markdown format.',
                            epilog='This utility exits after parsing the input file.')
    parser.add_argument('-f', '--filename', required=True, help='the file that you want to parse')
    parser.add_argument('-c', '--cssfile', nargs='*', dest="cssfilelist", help='the CSS file you want used for the styling. Default is smd.css')
    parser.add_argument('-i', '--import', nargs='*', dest="importfilelist", help='list of file(s) to import after builtins.md loaded. Default is None')
    parser.add_argument('-d', '--path', nargs='?', const='./html', default='./html', help='the directory that you want the HTML file written to. Default is ./html')
    parser.add_argument('-dbg', '--debug', action='store_true', help=f'display additional debug information. Default is: {False}')
    #parser.add_argument('-o', '--open', nargs='?', const=True, default=False, help='whether or not to open the resulting HTML output file with the default system app')

    from smd.smd import smd_add_std_cmd_line_parms
    from smd.core.sysdef import SystemDefaults

    sysDefaults = SystemDefaults()

    args = smd_add_std_cmd_line_parms(parser, sysDefaults, arguments)

    sp = ScriptParser(args.filename, handle_cssfilelist_parameter(args.cssfilelist), get_importfilelist(args), args.path, sysDefaults)

    if args.debug: sp.dump()

    return 0 if sp.lastParseOK else 1
    

if __name__ == '__main__':
    from sys import exit
    exit(parse())
