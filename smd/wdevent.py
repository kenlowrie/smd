#!/usr/bin/env python3

import time 
import threading
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
from watchdog.observers.api import EventQueue

import traceback
#from watchdog.observers.api import EventDispatcher, EventEmitter, EventQueue
from pathlib import Path

class WatchDirectory(FileSystemEventHandler): 
    def __init__(self): 
        super(WatchDirectory,self).__init__()
        self.observer = Observer() 
        self.q = EventQueue()

    def run(self): 
        #self.monitor.create()   # make sure the monitor is up and running
        self.observer.schedule(self, str(Path('.').resolve()), recursive = False) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(3)
                if self.q.qsize():
                    print(f'found: {self.q.get()}')
        except KeyboardInterrupt:
            pass    # don't need to see a traceback for this
        except: 
            traceback.print_exc()   # let's see what happened; wasn't expecting this
        finally:
            self.observer.stop() 
            print("\nObserver Stopped")

        print("Shutting down watch observer thread...")
        self.observer.join() 

    def on_modified(self, event): 
        if event.is_directory: 
            return None

        elif event.event_type == 'modified': 
            # Event is modified, you can process it now 
            print(f"Watchdog received modified event - {event.src_path}")
            self.q.put(event.src_path)

class Handler(FileSystemEventHandler): 
    def __init__(self):
        self.me = "ken"
        self.q = []
        self.q.append('mfile.txt')

    #@staticmethod
    def on_modified(self, event): 
        if event.is_directory: 
            return None

        elif event.event_type == 'modified': 
            # Event is modified, you can process it now 
            print(f"Watchdog received modified event - {event.src_path}")
            self.q.append(event.src_path)


WatchDirectory().run()
