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
    
    def exists(self, name):
        # This should be atomic, so no need to lock the data structure.
        return True if name in self.files else False

    def addItem(self, filename):
        self.acquire()
        try:
            msg(f"watchlist: adding [{filename}]")
            self.files.append(filename)
        finally:
            self.release()

    def dump(self):
        self.acquire()
        try:
            for i in self.files:
                msg(f"\t{i}")
        finally:
            self.release()

from watchdog.events import FileSystemEventHandler

class watcher(FileSystemEventHandler):
    def __init__(self):
        super(watcher, self).__init__()  # Initialize the base class(es)

        self.directories = {}
        self.watchers = []
        self.q = SimpleQueue()

        from watchdog.observers import Observer
        self.observer = Observer()
        msg(f"Starting Observer()")
        self.observer.start()

    def _addWatchItem(self,item):
        filespec = Path(item).resolve()

        if filespec.parent not in self.directories:
            msg(f"Creating watchlist() for [{filespec}]")
            self.directories[filespec.parent] = watchlist(filespec.name)
        else:
            self.directories[filespec.parent].addItem(filespec.name)

    def _start(self, directory):
        msg(f"Scheduling watcher for [{directory}]")
        self.watchers.append(self.observer.schedule(self, str(directory), recursive = False))

    def _stop(self, watcher):
        if watcher in self.watchers:
            #//TODO: This won't work as-is. If needed, should make a small class to hold the
            # watcher stuff: directory, the watcher instance, etc.
            msg(f"UnScheduling watcher for [{directory}]")
            self.observer.unschedule(watcher)

    def on_modified(self, event):
        if event.is_directory: return None

        spec = Path(event.src_path).resolve()
        #path = spec.parent
        #name = spec.name
        if spec.parent in self.directories:
            if self.directories[spec.parent].exists(spec.name):
                msg(f"File {event.src_path} was modified. Adding to queue...")
                self.q.put(event.src_path)
            else:
                msg(f"File {event.src_path} was modified, but I don't care about it...")
        else:
            msg(f"Got notification of change to {spec.name} in directory {spec.parent} --> {event.src_path}")

    def begin(self, filelist):
        # first, create all the watchdir() for each unique directory
        for item in filelist:
            self._addWatchItem(item)

        # now, schedule an event handler(watchdog.watch) for each folder
        for dir in self.directories:
            self._start(dir)
    
    def reset(self, filelist):
        # get list of directories being monitored
        msg("reset: shutting down directory observers...")
        self.observer.unschedule_all()
        self.directories = {}
        self.watchers = []
        self.begin(filelist)

    def end(self):
        self.observer.unschedule_all()
        self.observer.stop() 
        msg("\nObserver Stopped")
        self.observer.join()

    def look(self):
        if self.q.qsize():
            msg(f"Modified: {self.q.get()}")

    def dump(self):
        for i in self.directories:
            msg(f"Folder: {i}")
            self.directories[i].dump()

w = watcher()    

msg(f'{"*"*100}')
w.begin(filelist)
w.dump()
msg(f'{"*"*100}')
w.reset(filelist[:-1])
w.dump()
msg(f'{"*"*100}')
w.reset(filelist[:-2])
w.dump()
msg(f'{"*"*100}')
w.reset(filelist[1:])
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