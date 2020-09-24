#!/usr/bin/env python3

"""
This module implements an endpoint for doing "live" processing on
script markdown files that are processed by the smd package. This enables
the automatic update/refresh of a webpage, as changes are made to the
underlying markdown text files.

//TODO.py: Finish the documentation for this script. What is the purpose of this script? It was before ismd -m endpoint, so no longer needed, right?

creates an HTML document suitable for serving to local/network clients.


usage:

    smdlive -h

"""

from smd.smdutil import _Error, ConsoleMessage
import traceback

class MonitorError(_Error):
    """Monitor exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg

message = ConsoleMessage(__file__).o


from bottle import route

@route('/smd')
def smd():
    return '<h1>test83a</h1>'

def smdliveLoop():
    from bottle import run

    run()


def smdlive(arguments=None):
    """Make an HTML Page from a Script Markdown text file.

    Creates an HTML output file from the input file.

    if arguments is None, uses sys.argv - via argparse

    Exit code:
        0 -- Success
        1 -- File not found
        2 -- IO Error processing input file
        3 -- Invalid regex ID in main loop
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Create an HTML file in Audio-Visual script format from a text file.',
                            epilog='If filename is not specified, program reads from stdin.')
    parser.add_argument('-f', '--filename', required=True, help='the file that you want to parse')
    parser.add_argument('-c', '--cssfile', nargs='?', const='smd.css', default='smd.css', help='the CSS file you want used for the styling. Default is smd.css')
    parser.add_argument('-d', '--path', nargs='?', const='./html', default='./html', help='the directory that you want the HTML file written to')
    parser.add_argument('-o', '--open', nargs='?', const=True, default=False, help='whether or not to open the resulting HTML output file with the default system app')

    args = parser.parse_args(None if arguments is None else arguments)

    return smdliveLoop()


if __name__ == '__main__':
    exit(smdlive())
