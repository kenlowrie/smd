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
from threading import Thread, Lock, current_thread
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
    def __init__(self, observer, directory):
        self.directory = directory.parent
        self.observer = observer
        self.files = watchlist(directory.name)
        self.lock = Lock()
        self.thread = Thread(target=self.monitor, name=f"{id(self)}")
    
    def monitor(self):
        print(f"Thread[{self.thread.name}] has started to monitor {self.directory}")
        self.lock.acquire()
        print(f"Thread[{self.thread.name}] is exiting from monitoring {self.directory}")

    def addItem(self, filespec):
        self.files.addItem(filespec.name)

    def start(self):
        self.lock.acquire() # acquire the thread lock so it blocks when the thread is run and it acquires lock
        self.thread.start()

    def stop(self):
        self.lock.release() # signal the thread to wake up, clean up, and exit
        self.thread.join()  # block until the thread stops running

    def watch(self):
        #self.wd_watch = self.observer.schedule()
        pass

    def dump(self):
        self.files.dump()


class watcher(object):
    def __init__(self):
        self.directories = {}
        from watchdog.observers import Observer
        self.observer = Observer()

    def begin(self, filelist):
        # first, create all the watchdir() for each unique directory
        for item in filelist:
            self.addWatchItem(item)

        # now, schedule an event handler(watchdog.watch) for each folder
        for dir in self.directories:
            self.directories[dir].watch()
    

    def refresh(self, filelist):
        # get list of directories being monitored
        print("refreshing list")
        pass

    def end(self):
        self.observer.unschedule_all()
        pass

    def addWatchItem(self,item):
        filespec = Path(item).resolve()

        if filespec.parent not in self.directories:
            self.directories[filespec.parent] = watchdir(self.observer, filespec)
        else:
            self.directories[filespec.parent].addItem(filespec)

    def spinUpWorkers(self):
        for i in self.directories:
            #print(f"spinning up thread for {i}")
            self.directories[i].start()

    def spinDownWorkers(self):
        for i in self.directories:
            #print(f"spinning down thread for {i}")
            self.directories[i].stop()
            
    def dump(self):
        for i in self.directories:
            print(f"Folder: {i}")
            self.directories[i].dump()

w = watcher()    
#for item in filelist:
#    w.addWatchItem(item)
w.begin(filelist)
w.dump()
time.sleep(2)
w.refresh(filelist)
w.dump()
w.end()

w.spinUpWorkers()


try:
    while(True):
        time.sleep(1)

except KeyboardInterrupt:
    print()
    w.spinDownWorkers()

