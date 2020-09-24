#!/usr/bin/env python

filelist = [
    '/Users/ken/Dropbox/shared/src/script/smd/tests/sos/peek.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/builtins.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/defaults.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/common.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/code.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/link.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/html.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/def_html.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/def_head.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/def_body.md',
    '/Users/ken/Dropbox/shared/src/script/smd/smd/import/divs.md',
    '/Users/ken/.smd/import/builtins.md',
    '/Users/ken/.smd/import/def_body.md',
]
import time
from threading import current_thread

from smd.smdutil import watcher, consoleMessage

w = watcher()    

consoleMessage(f'{"*"*100}')
w.begin(filelist)
w.dump()
consoleMessage(f'{"*"*100}')
w.reset(filelist[:-1])
w.dump()
consoleMessage(f'{"*"*100}')
w.reset(filelist[:-2])
w.dump()
consoleMessage(f'{"*"*100}')
w.reset(filelist[1:])
w.dump()
consoleMessage(f'{"*"*100}')


try:
    while(True):
        time.sleep(1)
        w.look()

except KeyboardInterrupt:
    consoleMessage("")

w.end()

