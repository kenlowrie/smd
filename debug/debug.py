#!/usr/bin/env python

"""
from sys import path
from os.path import dirname, abspath, realpath, split, join
bin_path, whocares = split(dirname(realpath('__file__')))
lib_path = join(abspath(bin_path),'smd')
path.insert(0, lib_path)
"""
from pathlib import Path
from os import chdir

parent = Path(__file__).parent
chdir(Path().joinpath(parent,'../tests/sos'))

import smd

#from smd import smd_parse_file

if False:
    from threading import current_thread, local

    current = current_thread
    mytlsdict = current_thread.__dict__
    tls = local()


#smd.smd.smd_parse_file(['-f', 'clean.md', '-nd', '-ndb'])
#smd.smd.smd_parse_file(['-nd', '-ndb', '-o'])
smd.smd.smd_parse_file()


print("nothing to see here.")

#avscript.avscript_md.av_parse_file(['-f', '/Users/ken/Dropbox/clp/projects/2018/buddyvargas/video/forgiveme/forgiveme-musicvideo.md'])
