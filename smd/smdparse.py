#!/usr/bin/env python3

"""
This module provides a wrapper for the most common use cases of smd.

Essentially, that is to parse a file in script markdown format and create an HTML document from it.

usage:

    smdparse --help

"""

from smd.smdutil import ConsoleMessage

message = ConsoleMessage(__file__).o

# Override the default (def_html.md) markdown that smd uses, and provide our custom version.
# def_html.md, def_body.md, def_bodyclose.md and def_close.md are all okay as-is.
def get_head(mdfile, cssFileList, title = None):
    the_title = title if title is not None else str(mdfile.name)

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
from smd.core.ftrack import FileTrack
from smd.core.exception import FileError

class ScriptParser():
    def __init__(self, inputFile, cssFileList, importFileList, outputDir, sysDefaults):
        self.lastParseOK = False
        self.smdFile = Path(inputFile).resolve()
        if not self.smdFile.is_file(): raise FileError(1, f"{self.smdFile} does not exist")
        self.cssFileList = [Path(item).resolve() for item in cssFileList]
        self.outDir = Path(outputDir).resolve()
        if not self.outDir.is_dir(): self.outDir.mkdir()
        self.outFile = Path().joinpath(self.outDir, Path(self.smdFile.name).with_suffix(".html"))
        self.importFileList = importFileList
        self.sysDefs = sysDefaults
        self.parse(firstTime=True)

    def _copy_cssfiles(self):
        for file in self.cssFileList:
            if not file.is_file():
                message("Can't find [{}], ignoring ...".format(file))
                continue
            from shutil import copy2
            try:
                message("Copying CSS file: {}".format(file))
                copy2(file, self.outDir)
            except OSError as why:
                message("Error copying CSS file: {}".format(str(why)))
    
    def _parse_script(self):
        htmlfile = open(self.outFile, "w")

        from smd.smd import ScriptParser

        self.sysDefs.addConfigFileData("import/def_head.md", get_head(self.smdFile,self.cssFileList))
        self.sysDefs.addImportFiles(self.importFileList)

        message("Creating: " + str(self.outFile))
        
        smdscript_obj = ScriptParser(self.sysDefs, self.fileTracker)
        smdscript_obj.stdoutput = htmlfile
        smdscript_obj.open_and_parse(str(self.smdFile))
        
        htmlfile.close()

    def dump(self):
        message("Dumping the ScriptParser Instance variables.")
        message(f"lastParseOK={self.lastParseOK}")
        message(f"smdFile={self.smdFile}")
        message(f"cssFileList={self.cssFileList}")
        message(f"outputDir={self.outDir}")
        message(f"htmlFile={self.outFile}")
        message(f"sysDefs (SystemDefaults Instance):")
        self.sysDefs.dump(message)

    def parse(self,firstTime=False, copyCSSfiles=False):
        message("Instantiating file tracker...")
        self.fileTracker = FileTrack()  # need a fresh instance each time we parse
        for file in self.cssFileList:
                self.fileTracker.seen = file
        try:
            if firstTime or copyCSSfiles: self._copy_cssfiles()
            message("Parsing {}{}".format(self.smdFile,"" if firstTime == False else " initially ..."))
            self._parse_script()
            self.lastParseOK = True
        except:
            message("Caught exception parsing the script ...")
            self.lastParseOK = False
            traceback.print_exc()
    
    def getFilesParsed(self):
        return self.fileTracker.seen


def handle_cssfilelist_parameter(cssfilelist):
    """Convert optional list of css files into a consistent list form

    Specifying one or more css files is optional, and the argparser will provide
    inconsistent results depending on whether the optional parameter is used, so
    we need to normalize the list.
    """
    # if -c/--cssfile was specified but no arg passed, use the built-in default css.
    # if -c/--cssfile is not specified, args.cssfilelist = None
    # if -c/--cssfile specified with one or more filenames, then args.cssfilelist == [file1 [,file2]]
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

    try:
        sp = ScriptParser(args.filename, handle_cssfilelist_parameter(args.cssfilelist), get_importfilelist(args), args.path, sysDefaults)
    except FileError as fe:
        message(f"FileError exception: {fe.errno} - {fe.errmsg}", False)
        return 1

    if args.debug: sp.dump()

    return 0 if sp.lastParseOK else 1
    

if __name__ == '__main__':
    from sys import exit
    exit(parse())
