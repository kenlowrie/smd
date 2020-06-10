#!/usr/bin/env python

from smd.core.thread import initTLS, getTLS

from smd.core.constants import Constants

tls = initTLS()

from smd.core.ftrack import FileTrack
from smd.core.sysdef import SystemDefaults

#tls.fileTracker = FileTrack()
#tls.sysDefaults = SystemDefaults()
tls.addObjectToTLS(Constants.fileTracker, FileTrack())
tls.addObjectToTLS(Constants.sysDefaults, SystemDefaults())
tls.addObjectToTLS(Constants.rawOutput, True)

if tls.sysDefaults is None:
    print("wow!")

tls2 = getTLS()
if tls2.sysDefaults is None:
    print("WTF?")

print(tls2.__dict__.keys())

obj1 = tls.getObjectFromTLS(Constants.fileTracker)
obj2 = tls.getObjectByClassFromTLS(FileTrack)
obj3 = tls.getObjectFromTLS(Constants.rawOutput)
obj4 = tls.getObjectFromTLS(Constants.sysDefaults)
obj5 = tls.getObjectByClassFromTLS(SystemDefaults)
print("so far, so good")
initTLS()


from threading import current_thread
ctd = current_thread.__dict__

from smd.core.thread import _set_tls_data
_set_tls_data()
from smd.core.thread import _tls_data_

from smd.core.ftrack import FileTrack
from smd.core.sysdef import SystemDefaults
from smd.core.debug import Debug

_tls_data_.addObjectToTLS('fileTracker', FileTrack())
_tls_data_.addObjectToTLS('sysDefaults', SystemDefaults())
#_tls_data_.addObjectToTLS('sysDebug', Debug('foo'))

print("so far, so good")



from smd.core.ftrack import FileTrack

ft = FileTrack()

ft.seen = 'builtins.md'
ft.seen = 'smd.css'
ft.seen = 'userdocs.md'
ft.seen = '../smd/smd.css'
if ft.alreadySeen('builtins.md'): print("already saw builtins.md")
ft.dump()
print("---------Seen----------")
#for f in ft._list:
#    ft.seen = f.name

ft.dump2()
"""
files = ft.list

for f in files:
    print(f"Rootname: {f.basename()}\n\tDirectory: {f.parent()}\n\tFullname: {f.name}")
"""