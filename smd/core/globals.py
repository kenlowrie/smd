#!/usr/bin/env python

from pathlib import Path

def _getBasepath():
    return Path(__file__).resolve().parent.parent

def init_globals():
    return [
        '@var _id="sys" basepath="{}" imports="{}" root="{}"'.format(_getBasepath(), Path().joinpath(_getBasepath(),'import'), _getBasepath().parent ),
    ]

if __name__ == '__main__':
    print("Library module. Not directly callable.")
