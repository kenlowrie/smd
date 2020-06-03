#!/usr/bin/env python3

from smd.smdutil import _Error, ConsoleMessage
import traceback

class MonitorError(_Error):
    """Monitor exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg

"""
//TODO: Figure out if this is still needed for any use case, such as when module is imported???
try:
    myself = __file__
except NameError:
    myself = argv[0]
"""

message = ConsoleMessage(__file__)

class OutputMonitor():
    def __init__(self):
        pass
    def create(self):
        pass
    def update(self):
        pass
    def refresh(self):
        pass
    def close(self):
        pass

import tkinter as tk

class Window(OutputMonitor):
    def __init__(self, filepath=None):
        super(Window, self).__init__()
        self.filepath = filepath

    def create(self):
        self.window = tk.Tk()
        self.scrollbar = tk.Scrollbar(self.window)
        self.textbox = tk.Text(self.window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.scrollbar.config(command=self.textbox.yview)
        self.textbox.config(yscrollcommand=self.scrollbar.set)
        self.refresh()
        self.update()

    def refresh(self):
        with open(self.filepath) as f:
            data = f.read()

        self.textbox.replace("1.0", tk.END, data)

    def update(self):
        self.window.update()

    def close(self):
        self.window.destroy()

from selenium import webdriver

class Browser(OutputMonitor):
    def __init__(self, url=None):
        super(Browser, self).__init__()
        self.url = url

    def create(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

class Monitor():
    def __init__(self, monitor, filepath):
        self.monitor = None
        self.type = monitor
        if self.type == "browser":
            self.monitor = Browser(f"file://{filepath}")
        elif self.type == "hostgui":
            self.monitor = Window(filepath)
        else:
            raise MonitorError("Invalid monitor type [{}]".format(monitor))

    def create(self):
        if self.monitor is not None:
            message.o(f"creating {self.type} window...")
            self.monitor.create()

    def update(self):
        if self.monitor is not None:
            self.monitor.update()

    def refresh(self):
        if self.monitor is not None:
            message.o(f"refreshing {self.type} window...")
            self.monitor.refresh()

    def close(self):
        if self.monitor is not None:
            message.o(f"closing {self.type} window...")
            self.monitor.close()


class FileEvents:
    def __init__(self):
        self._cache = []

    def haveEvent(self):
        return self._cache

    def pushEvent(self,pathstr):
        self._cache.append(pathstr)

    def popEvent(self):
        if self.haveEvent():
            return self._cache.pop()

        return None

gb_file_events = FileEvents()


import time 
import threading
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 

class WatchDirectory: 
    def __init__(self, monitors, scriptParser): 
        self.observer = Observer() 
        self.sp = scriptParser
        self.monitors = [Monitor(monitor, str(self.sp.outFile)) for monitor in monitors]

    def run(self): 
        for monitor in self.monitors: monitor.create()
        #self.monitor.create()   # make sure the monitor is up and running
        self.watchDirectory = str(self.sp.smdFile.parent)
        event_handler = Handler()
        event_handler.mytickle = False
        self.observer.schedule(event_handler, self.watchDirectory, recursive = False) 
        self.observer.start() 
        global gb_file_events
        try: 
            while True: 
                for monitor in self.monitors: monitor.update()
                time.sleep(0.1)
                if gb_file_events.haveEvent():
                    curFile = gb_file_events.popEvent()
                    if curFile == str(self.sp.smdFile):
                        self.sp.parse()
                        message.o(f"Parse done, refreshing {self.monitors}...")
                        for monitor in self.monitors: monitor.refresh()
                    else:
                        message.o(f"Modified file: {curFile} is not being watched; ignoring ...")
        except KeyboardInterrupt:
            pass    # don't need to see a traceback for this
        except: 
            traceback.print_exc()   # let's see what happened; wasn't expecting this
        finally:
            self.observer.stop() 
            message.o("\nObserver Stopped")

        message.o("Shutting down watch observer thread...")
        self.observer.join() 

class Handler(FileSystemEventHandler): 

    #//TODO: Can I change this to use non-static handler with single method: on_modified()? like this (last example): https://www.geeksforgeeks.org/create-a-watchdog-in-python-to-look-for-filesystem-changes/

    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None

        elif event.event_type == 'created': 
            # Event is created, you can process it now 
            message.o("Watchdog received created event - %s." % event.src_path) 
        elif event.event_type == 'modified': 
            # Event is modified, you can process it now 
            message.o(f"Watchdog received modified event - {event.src_path}")
            global gb_file_events
            gb_file_events.pushEvent(event.src_path)



def ismd(arguments=None):
    """Interactive Script Markdown Command Line Utility.
    
    This program creates an HTML page from a text file written in Script Markdown format, and monitors the input file for changes, refreshing the monitor window as the file is updated.

    if arguments is None, uses sys.argv - via argparse

    Exit code:
        0 -- Success
        1 -- File not found
        2 -- IO Error processing input file
        3 -- Invalid regex ID in main loop
    """
    from argparse import ArgumentParser
    from pathlib import Path

    parser = ArgumentParser(description='Generate HTML file from a text file in Script Markdown format.',
                            epilog='The program monitors changes and keeps window updated until CTRL-C is pressed.')
    parser.add_argument('-f', '--filename', required=True, help='the file that you want to parse')
    parser.add_argument('-c', '--cssfile', nargs='*', dest="cssfilelist", help='the CSS file you want used for the styling. Default is smd.css')
    parser.add_argument('-d', '--path', nargs='?', const='./html', default='./html', help='the directory that you want the HTML file written to. Default is ./html')
    parser.add_argument('-i', '--import', nargs='*', dest="importfilelist", help='list of file(s) to import after builtins.md loaded. Default is None')
    parser.add_argument('-m', '--monitor', nargs='+', default=['browser'], help='the monitor [browser, hostgui] you want used to display changes. Default is browser')


    from smd.smd import smd_add_std_cmd_line_parms
    from smd.core.sysdef import SystemDefaults

    sysDefaults = SystemDefaults()

    args = smd_add_std_cmd_line_parms(parser, sysDefaults, None if arguments is None else arguments)

    from smd.smdparse import ScriptParser, handle_cssfilelist_parameter, get_importfilelist

    sp = ScriptParser(args.filename, handle_cssfilelist_parameter(args.cssfilelist), get_importfilelist(args), args.path, sysDefaults)

    if sp.lastParseOK == False:
        message.o("stopping because the initial parse failed...")
        return 1


    WatchDirectory(args.monitor, sp).run()

    return 0


if __name__ == '__main__':
    exit(ismd())
