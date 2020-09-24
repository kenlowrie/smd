#!/usr/bin/env python

from pathlib import Path

def _getBasepath():
    return Path(__file__).resolve().parent.parent

def _getUserpath():
    return Path().joinpath(Path().home(), '.smd')

def init_globals():
    return [
        '@var _id="sys" basepath="{}" imports="{}" root="{}" user_basepath="{}" user_imports="{}" user_root="{}"'.format(
                _getBasepath(), 
                Path().joinpath(_getBasepath(),'import'), 
                _getBasepath().parent,
                _getUserpath(),
                Path().joinpath(_getUserpath(), 'import'),
                _getUserpath().parent)
    ]

if __name__ == '__main__':
    print("Library module. Not directly callable.")
