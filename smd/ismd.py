#!/usr/bin/env python3

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

class Browser():
    def __init__(self, url=None):
        self.driver = webdriver.Chrome()
        self.load(url)

    def load(self, url=None):
        if url is not None:
            self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

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
        self.compile(True)

    def parameterInfo(self):
        print(f"smdFile={self.smdFile}\ncssFile={self.cssFile}\noutputDir={self.outDir}\nhtmlFile={self.outFile}")

    def compile(self,firstTime=False):
        try:
            print("Parsing {}{}".format(self.smdFile,"" if firstTime == False else " to start ..."))
            _mkhtml(str(self.smdFile), str(self.cssFile), str(self.outDir), False)
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
    def __init__(self, browserWindow): 
        self.observer = Observer() 
        self.bWin = browserWindow

    def run(self, watch_dir, sp): 
        self.watchDirectory = watch_dir
        event_handler = Handler()
        event_handler.mytickle = False
        self.observer.schedule(event_handler, self.watchDirectory, recursive = False) 
        self.observer.start() 
        global gb_file_events
        try: 
            while True: 
                time.sleep(1)
                if gb_file_events.haveEvent():
                    print("file modified event received: {}".format(gb_file_events.popEvent())) 
                    sp.compile()
                    print("parse done, refreshing browser...")
                    self.bWin.refresh()
        except: 
            self.observer.stop() 
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

    args = parser.parse_args(None if arguments is None else arguments)

    sp = ScriptParser(args.filename, args.cssfile, args.path)

    if sp.lastParseOK == False:
        print("stopping, initial parse failed...")
        return 1

    print("starting browser...")

    # looks like they are monitoring keyboard interrupt and cleaning up, so don't call browser.close()...
    browserWindow = Browser(f"file://{str(sp.outFile)}")

    watcher = WatchDirectory(browserWindow)
    watcher.run(str(sp.smdFile.parent), sp)

    return 0


if __name__ == '__main__':
    exit(ismd())
