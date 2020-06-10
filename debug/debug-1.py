#!/usr/bin/env python

"""
from sys import path
from os.path import dirname, abspath, realpath, split, join
bin_path, whocares = split(dirname(realpath('__file__')))
lib_path = join(abspath(bin_path),'avscript')
path.insert(0, lib_path)
"""
from pathlib import Path
from os import chdir

parent = Path(__file__).parent
chdir(Path().joinpath(parent,'sos'))

import smd

#from smd import smd_parse_file


#smd.smd.smd_parse_file(['-f', 'clean.md', '-nd', '-ndb'])
smd.smdparse.parse(['-f', 'peek.md', '-c', '-o'])


print("nothing to see here.")
