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
from threading import Thread, Lock, current_thread

def msg(s):
    print(f"{current_thread().native_id}: {s}")

from pathlib import Path
import time
from queue import SimpleQueue

class watchlist(object):
    def __init__(self, filename):
        self.files = []             # I need to be able to remove things too. queue.Queue no good.
        self.lock = Lock()
        self.addItem(filename)
    
    def acquire(self):
        self.lock.acquire()
    
    def release(self):
        self.lock.release()

    """
    def duplicateList(self):
        newlist = []
        self.acquire()
        try:
            msg(f"watchlist: duplicating list...")
            newlist = [i for i in self.files]
        finally:
            self.release()
        
        return newlist
    """
    def addItem(self, filename):
        self.acquire()
        try:
            msg(f"watchlist: adding [{filename}]")
            self.files.append(filename)
        finally:
            self.release()
    """
    def removeItem(self, filename):
        self.acquire()
        try:
            if filename in self.files:
                msg(f"watchlist: removing [{filename}]")
                self.files.remove(filename)
        finally:
            self.release()
    """    
    def dump(self):
        self.acquire()
        try:
            for i in self.files:
                msg(f"\t{i}")
        finally:
            self.release()

"""
class simplelist(watchlist):
    def __init__(self, filename):
        # don't call the constructor, we don't need a lock. Just overridding
        # acquire and release, rest of baseclass methods are fine for this class
        self.files = []
        self.addItem(filename)
    
    def acquire(self):
        pass
    
    def release(self):
        pass

"""

from watchdog.events import FileSystemEventHandler
#from watchdog.observers.api import EventQueue

class watchdir(FileSystemEventHandler):
    def __init__(self, observer, fullpath):
        super(watchdir, self).__init__()  # Initialize the base class(es)

        self.directory = fullpath.parent
        self.observer = observer            # The observer we can use to schedule with
        self.watcher = None                 # So we don't unschedule if we never scheduled
        self.files = watchlist(fullpath.name)
        self.q = SimpleQueue()
        #self.thread = Thread(target=self.monitor, name=f"{id(self)}")
    
    def addItem(self, filespec):
        self.files.addItem(filespec.name)

    def start(self):
        msg(f"Scheduling watcher for [{self.directory}]")
        self.watcher = self.observer.schedule(self, str(self.directory), recursive = False)

    def stop(self):
        if self.watcher is not None:
            msg(f"UnScheduling watcher for [{self.directory}]")
            self.observer.unschedule(self.watcher)

    def on_modified(self, event):
        if event.is_directory: return None

        self.q.put(event.src_path)

    def look(self):
        if self.q.qsize():
            msg(f"Modified: {self.q.get()}")

    def dump(self):
        self.files.dump()

from watchdog.events import FileSystemEventHandler

class watcher(object):
    def __init__(self):
        self.directories = {}
        from watchdog.observers import Observer
        self.observer = Observer()
        msg(f"Starting Observer()")
        self.observer.start()

    def begin(self, filelist):
        # first, create all the watchdir() for each unique directory
        for item in filelist:
            self.addWatchItem(item)

        # now, schedule an event handler(watchdog.watch) for each folder
        for dir in self.directories:
            self.directories[dir].start()
    

    def refresh(self, filelist):
        # get list of directories being monitored
        msg("refreshing list of directories")
        """
        tmplist = {}
        for item in filelist:
            spec = Path(item).resolve()
            if spec.parent not in tmplist:
                msg(f"Creating watchlist() for [{spec}]")
                tmplist[spec.parent] = simplelist(spec.name)
            else:
                tmplist[spec.parent].addItem(spec.name)
        msg(f"updated file list:")
        for dir in tmplist:
            msg(f"updated files in dir: {dir}")
            tmplist[dir].dump()
        """
        msg("shutting down directory observers...")
        self.observer.unschedule_all()
        self.directories = {}
        self.begin(filelist)
        """
        for dir in self.directories:
            if dir not in tmplist:
                msg(f"directory {dir} no longer being monitored, removing ...")
                self.directories[dir].stop()
                del self.directories[dir]
            else:
                try:
                    msg(f"looking for files no longer being monitored...")
                    watchlist = self.directories[dir].files.duplicateList()
                    for file in watchlist:
                        if file not in tmplist[dir].files:
                            self.directories[dir].files.removeItem(file)

                    msg(f"looking for files that have been added to existing folder...")
                    watchlist = self.directories[dir].files.duplicateList()
                    for file in tmplist[dir].files:
                        if file not in watchlist:
                            self.directories[dir].files.addItem(file)
                finally:
                    pass
        """

    def end(self):
        self.observer.unschedule_all()
        self.observer.stop() 
        msg("\nObserver Stopped")
        self.observer.join()

    def addWatchItem(self,item):
        filespec = Path(item).resolve()

        if filespec.parent not in self.directories:
            msg(f"Creating watchlist() for [{filespec}]")
            self.directories[filespec.parent] = watchdir(self.observer, filespec)
        else:
            self.directories[filespec.parent].addItem(filespec)

    def look(self):
        for i in self.directories:
            self.directories[i].look()

    def dump(self):
        for i in self.directories:
            msg(f"Folder: {i}")
            self.directories[i].dump()

w = watcher()    
#for item in filelist:
#    w.addWatchItem(item)
msg(f'{"*"*100}')
w.begin(filelist)
w.dump()
msg(f'{"*"*100}')
w.refresh(filelist[:-1])
w.dump()
msg(f'{"*"*100}')
w.refresh(filelist[:-2])
w.dump()
msg(f'{"*"*100}')
w.refresh(filelist[1:])
w.dump()
msg(f'{"*"*100}')


try:
    while(True):
        time.sleep(1)
        w.look()

except KeyboardInterrupt:
    msg("")

w.end()




"""
WatcherWrapperClass(args.monitorAKAdisplays, sp).run()
.init
    self.observer = Observer()  #????? okay, since we can schedule multiple watchers...
    self.scriptParser = sp  # this has already run once and we have a list of files available via TLS
    self.monitors = [Monitor(monitor, str(self.sp.outFile) for monitor in monitors)]
    self.watcher = watcher()
.run
    monitor.create() # create the GUI monitor
    self.watcher.begin(sp.listofcurrentfiles)

    try:
        while True:
            monitor.update()    # refresh GUI windows
            time.sleep(0.1)     # we need to constantly update the gui windows (just hostgui)
            if have_event:
                popevent()
                if event is monitored file:
                    sp.parse()
                    self.watcher.refresh(sp.listofcurrentfiles)
                else:
                    msg not monitored


from list of files:



"""