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


from pathlib import Path
from threading import Thread
import time

class watchlist(object):
    def __init__(self, filename):
        self.files = []
        self.addItem(filename)
    
    def addItem(self, filename):
        self.files.append(filename)
    
    def dump(self):
        for i in self.files:
            print(f"\t{i}")

class watchdir(object):
    def __init__(self, directory):
        self.directory = directory.parent
        self.files = watchlist(directory.name)
        self.keepAlive = True
        self.thread = Thread(target=self.monitor, args=(1,))
    
    def monitor(self, parm):
        print(f"Thread[{parm}] has started to monitor {self.directory}")
        while(self.keepAlive):
            time.sleep(1)
        print(f"Thread[{parm}] is exiting from monitoring {self.directory}")

    def addItem(self, filespec):
        self.files.addItem(filespec.name)

    def start(self):
        self.thread.start()

    def stop(self):
        self.keepAlive = False
        self.thread.join()

    def dump(self):
        self.files.dump()
    
class watcher(object):
    def __init__(self):
        self.directories = {}

    def addWatchItem(self,item):
        filespec = Path(item).resolve()

        if filespec.parent not in self.directories:
            self.directories[filespec.parent] = watchdir(filespec)
        else:
            self.directories[filespec.parent].addItem(filespec)

    def spinUpWorkers(self):
        for i in self.directories:
            print(f"spinning up thread for {i}")
            self.directories[i].start()

    def spinDownWorkers(self):
        for i in self.directories:
            print(f"spinning down thread for {i}")
            self.directories[i].stop()
            
    def dump(self):
        for i in self.directories:
            print(f"Folder: {i}")
            self.directories[i].dump()

w = watcher()    
for item in filelist:
    w.addWatchItem(item)

w.dump()

w.spinUpWorkers()


try:
    while(True):
        time.sleep(1)

except KeyboardInterrupt:
    print()
    w.spinDownWorkers()





"""

from list of files:



"""