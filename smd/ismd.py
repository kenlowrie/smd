#!/usr/bin/env python3

class _Error(Exception):
    """Base exception class for this module."""
    pass


class MonitorError(_Error):
    """Monitor exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg


class OutputMonitor():
    def __init__(self):
        pass
    def create(self):
        pass
    def activate(self):
        pass
    def refresh(self):
        pass
    def close(self):
        pass

import tkinter as tk

class Window(OutputMonitor):
    def __init__(self, filepath=None):
        super(Window, self).__init__()
        print("creating output window...")
        self.create(filepath)

    def activate(self):
        self.window.update()

    def create(self, filepath=None):
        if filepath is not None:
            self.filepath = filepath
            self.window = tk.Tk()
            self.scrollbar = tk.Scrollbar(self.window)
            self.textbox = tk.Text(self.window)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.textbox.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
            self.scrollbar.config(command=self.textbox.yview)
            self.textbox.config(yscrollcommand=self.scrollbar.set)
            self.refresh()
            self.activate()

    def refresh(self):
        data = "the new data: {}".format(time.asctime())
        with open(self.filepath) as f:
            data = f.read()

        self.textbox.replace("1.0", tk.END, data)

    def close(self):
        self.window.destroy()


from selenium import webdriver

class Browser(OutputMonitor):
    def __init__(self, url=None):
        super(Browser, self).__init__()
        print("starting browser...")
        self.driver = webdriver.Chrome()
        self.create(url)

    def create(self, url=None):
        if url is not None:
            self.driver.get(url)

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
        elif self.type == "window":
            self.monitor = Window(filepath)
        else:
            raise MonitorError("Invalid monitor type [{}]".format(monitor))

    def create(self):
        if self.monitor is not None:
            self.monitor.create()

    def activate(self):
        if self.monitor is not None:
            self.monitor.activate()

    def refresh(self):
        if self.monitor is not None:
            self.monitor.refresh()

    def close(self):
        if self.monitor is not None:
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

from smd.livesmd import _mkhtml
from pathlib import Path
import traceback

class ScriptParser():
    def __init__(self, inputFile, cssFile, outputDir):
        self.lastParseOK = False
        self.smdFile = Path(inputFile).resolve()
        self.cssFile = Path(cssFile).resolve()
        self.outDir = Path(outputDir).resolve()
        self.outFile = Path().joinpath(self.outDir, Path(self.smdFile.name).with_suffix(".html"))
        self.parse(True)

    def parameterInfo(self):
        print(f"smdFile={self.smdFile}\ncssFile={self.cssFile}\noutputDir={self.outDir}\nhtmlFile={self.outFile}")

    def parse(self,firstTime=False):
        try:
            print("Parsing {}{}".format(self.smdFile,"" if firstTime == False else " to start ..."))
            _mkhtml(str(self.smdFile), str(self.cssFile), str(self.outDir), False, title="//TODO: FIX My cool page title")
            self.lastParseOK = True
        except:
            print("Caught exception parsing the script ...")
            self.lastParseOK = False
            traceback.print_exc()

    def nothing(self):
        scriptMDfile = Path(args.filename).resolve()
        watchDirectory = Path(args.path).resolve()
        htmlFile = Path().joinpath(watchDirectory,Path(scriptMDfile.name).with_suffix(".html"))


import time 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 

class WatchDirectory: 
    def __init__(self, monitorWindow): 
        self.observer = Observer() 
        self.monitor = monitorWindow

    def run(self, watch_dir, sp): 
        self.watchDirectory = watch_dir
        event_handler = Handler()
        event_handler.mytickle = False
        self.observer.schedule(event_handler, self.watchDirectory, recursive = False) 
        self.observer.start() 
        global gb_file_events
        try: 
            while True: 
                self.monitor.activate()
                time.sleep(1)
                if gb_file_events.haveEvent():
                    print("file modified event received: {}".format(gb_file_events.popEvent())) 
                    sp.parse()
                    print(f"parse done, refreshing {self.monitor.type}...")
                    self.monitor.refresh()
        except: 
            self.observer.stop() 
            #traceback.print_exc()
            print("\nObserver Stopped")

        print("Shutting down browser observer thread...")
        self.observer.join() 

class Handler(FileSystemEventHandler): 

    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None

        elif event.event_type == 'created': 
            # Event is created, you can process it now 
            print("Watchdog received created event - %s." % event.src_path) 
        elif event.event_type == 'modified': 
            # Event is modified, you can process it now 
            print("Watchdog received modified event - %s." % event.src_path)
            global gb_file_events
            gb_file_events.pushEvent(event.src_path)
            #Handler.mytickle = True
            #gb_tickle = True




def ismd(arguments=None):
    """Create HTML page from a text file written in Script Markdown.

    Creates an HTML output file from the input file.

    if arguments is None, uses sys.argv - via argparse

    Exit code:
        0 -- Success
        1 -- File not found
        2 -- IO Error processing input file
        3 -- Invalid regex ID in main loop
    """
    from argparse import ArgumentParser
    from pathlib import Path

    parser = ArgumentParser(description='Create an HTML file in Audio-Visual script format from a text file.',
                            epilog='If filename is not specified, program reads from stdin.')
    parser.add_argument('-f', '--filename', required=True, help='the file that you want to parse')
    parser.add_argument('-c', '--cssfile', nargs='?', const='smd.css', default='smd.css', help='the CSS file you want used for the styling. Default is smd.css')
    parser.add_argument('-d', '--path', nargs='?', const='./html', default='./html', help='the directory that you want the HTML file written to')
    parser.add_argument('-m', '--monitor', nargs='?', const='browser', default='browser', help='the monitor you want used to display changes. Default is browser')

    args = parser.parse_args(None if arguments is None else arguments)

    sp = ScriptParser(args.filename, args.cssfile, args.path)

    if sp.lastParseOK == False:
        print("stopping, initial parse failed...")
        return 1

    monitor = Monitor(args.monitor, str(sp.outFile))

    watcher = WatchDirectory(monitor)
    watcher.run(str(sp.smdFile.parent), sp)

    return 0


if __name__ == '__main__':
    exit(ismd())
