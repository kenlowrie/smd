#!/usr/bin/env python3

class _Error(Exception):
    """Base exception class for this module."""
    pass

class ConsoleMessage(object):
    def __init__(self, whoami):
        import kenl380.pylib as pylib

        self.me = pylib.context(whoami)
        self._usetid = True

    @property
    def usetid(self):
        return self._usetid
    
    @usetid.setter
    def usetid(self,value):
        self._usetid = value

    def o(self,msg,usetid=True):
        from threading import current_thread
        threadid = current_thread().native_id if usetid and self.usetid else ""
        print(f"{self.me.alias()}({threadid}): {msg}")

consoleMessage = ConsoleMessage(__file__).o

from pathlib import Path
from queue import SimpleQueue
from threading import Thread, Lock, current_thread

class watchlist(object):
    def __init__(self, filename, message=None):
        self.files = []             # I need to be able to remove things too. queue.Queue no good.
        self.lock = Lock()
        self.directory = filename.parent    # We are passed the qualified name on construction, hang on to it
        self.msg = message if message else consoleMessage
        self.addItem(filename.name)
    
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
            self.msg(f"watchlist: adding [{filename}] to watchlist for [{self.directory}]")
            self.files.append(filename)
        finally:
            self.release()

    def dump(self):
        self.acquire()
        try:
            for i in self.files:
                self.msg(f"\t{i}")
        finally:
            self.release()

from watchdog.events import FileSystemEventHandler

class watcher(FileSystemEventHandler):
    def __init__(self, message=None):
        super(watcher, self).__init__()  # Initialize the base class(es)

        self.directories = {}
        self.watchers = []
        self.q = SimpleQueue()

        self.msg = message if message else consoleMessage

        from watchdog.observers import Observer
        self.observer = Observer()
        self.msg(f"Starting Observer()")
        self.observer.start()

    def _addWatchItem(self,item):
        filespec = Path(item).resolve()

        if filespec.parent not in self.directories:
            self.msg(f"Creating watchlist() for [{filespec.parent}]")
            self.directories[filespec.parent] = watchlist(filespec)
        else:
            self.directories[filespec.parent].addItem(filespec.name)

    def _start(self, directory):
        self.msg(f"Scheduling watcher for [{directory}]")
        self.watchers.append(self.observer.schedule(self, str(directory), recursive = False))

    def _stop(self, watcher):
        if watcher in self.watchers:
            #//TODO: This won't work as-is. If needed, should make a small class to hold the
            # watcher stuff: directory, the watcher instance, etc.
            self.msg(f"UnScheduling watcher for [{directory}]")
            self.observer.unschedule(watcher)

    def on_modified(self, event):
        if event.is_directory: return None

        spec = Path(event.src_path).resolve()
        #path = spec.parent
        #name = spec.name
        if spec.parent in self.directories:
            if self.directories[spec.parent].exists(spec.name):
                self.msg(f"File {event.src_path} was modified. Adding to queue...")
                self.q.put(event.src_path)
            else:
                self.msg(f"File {event.src_path} was modified, but I don't care about it...")
        else:
            self.msg(f"Got notification of change to {spec.name} in directory {spec.parent} --> {event.src_path}")

    def begin(self, filelist):
        # hang on to the filelist so .reset() can efficiently determine a course of action
        self.filelist = filelist

        # first, create all the watchdir() for each unique directory
        for item in filelist:
            self._addWatchItem(item)

        # now, schedule an event handler(watchdog.watch) for each folder
        for dir in self.directories:
            self._start(dir)
    
    def reset(self, filelist):
        # if the filelist didn't change (true most of the time) ignore the reset
        if set(self.filelist) == set(filelist):
            self.msg("reset: no change to filelist, ignoring reset...")
            return
        
        # get list of directories being monitored
        self.msg("reset: shutting down directory observers...")
        self.observer.unschedule_all()
        self.directories = {}
        self.watchers = []
        self.begin(filelist)

    def end(self):
        self.observer.unschedule_all()
        self.observer.stop() 
        self.msg("\nObserver Stopped")
        self.observer.join()

    def look(self):
        return True if self.q.qsize() else False
    
    def get(self):
        return self.q.get() if self.q.qsize() else ""

    def dump(self):
        for i in self.directories:
            self.msg(f"Folder: {i}")
            self.directories[i].dump()
