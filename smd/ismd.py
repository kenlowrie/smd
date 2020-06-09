#!/usr/bin/env python3

from smd.smdutil import _Error, ConsoleMessage
import traceback

class MonitorError(_Error):
    """Monitor exceptions raised by this module."""
    def __init__(self, errmsg):
        self.errmsg = errmsg

message = ConsoleMessage(__file__).o

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

from bottle import Bottle, static_file
from threading import Thread, Lock, current_thread

class Endpoint(OutputMonitor):
    def __init__(self, filename=None):
        super(Endpoint, self).__init__()
        from pathlib import Path
        self.filename = Path(filename).resolve()
        self.endpoint = f"/smd/<path:path>"

    def create(self):
        self.refresh()              # go ahead and load up self.filedata
        self.thread = Thread(target=self.bottle_thread, name=f"BottleThread({id(self)})")
        self.thread.daemon = True   #//TODO: Only way the Ctrl-C allows code to shutdown... Research further
        self.thread.start()

    def refresh(self):
        pass
        #with open(self.filename) as f:
        #    self.filedata = f.read()

    def close(self):
        message("closing the endpoint")
        self.app.close()    # shutdown the endpoint
        message("waiting for bottle thread to finish")
        #self.thread.join()  # block until the bottle thread stops running (no good for daemon thread)
    
    def bottle_thread(self):
        message(f"Creating endpoint app on bottle with url: {self.endpoint}")
        self.app = Bottle()
        self.app.route(self.endpoint, 'GET', self.getContent)
        message("Starting web server...")
        self.app.run()
        message(f"finishing bottle thread...")

    def getContent(self, path):
        message(f"path={path}");
        #static_file({self.filename.name}, root={self.filename.parent}")
        return static_file(str(path), root=str(self.filename.parent.parent))
        #return self.filedata

class Monitor():
    Browser = 'browser'
    HostGUI = 'hostgui'
    Endpoint = 'endpoint'

    def __init__(self, monitor, filepath):
        self.monitor = None
        self.type = monitor
        if self.type == Monitor.Browser:
            self.monitor = Browser(f"file://{filepath}")
        elif self.type == Monitor.HostGUI:
            self.monitor = Window(filepath)
        elif self.type == Monitor.Endpoint:
            self.monitor = Endpoint(filepath)
        else:
            raise MonitorError("Invalid monitor type [{}]".format(monitor))

    def create(self):
        if self.monitor is not None:
            message(f"creating {self.type} window...")
            self.monitor.create()

    def update(self):
        if self.monitor is not None:
            self.monitor.update()

    def refresh(self):
        if self.monitor is not None:
            message(f"refreshing {self.type} window...")
            self.monitor.refresh()

    def close(self):
        if self.monitor is not None:
            message(f"closing {self.type} window...")
            self.monitor.close()


from smd.smdutil import watcher

class iSMDLoop(object):
    def __init__(self, monitors, scriptParser): 
        self.sp = scriptParser
        self.watcher = watcher()
        self.monitors = [Monitor(monitor, str(self.sp.outFile)) for monitor in monitors]
        self.watcher.begin(self.sp.getFilesParsed())

    def getMonitorTypes(self):
        return [i.type for i in self.monitors]

    def run(self): 
        from time import sleep
        from pathlib import Path
        for monitor in self.monitors: monitor.create()
        try: 
            while True: 
                for monitor in self.monitors: monitor.update()
                sleep(0.1)
                if self.watcher.look():
                    curFile = Path(self.watcher.get())
                    self.sp.parse(copyCSSfiles=True if curFile.suffix.lower() == '.css' else False)
                    message(f"Parse done, refreshing {self.getMonitorTypes()}...")
                    for monitor in self.monitors: monitor.refresh()
                    self.watcher.reset(self.sp.getFilesParsed())
        except KeyboardInterrupt:
            for monitor in self.monitors:
                if monitor.type == Monitor.Endpoint:
                    monitor.close()
        except: 
            traceback.print_exc()   # let's see what happened; wasn't expecting this
        finally:
            self.watcher.end()


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

    #//TODO: Can any of these "common" args be moved to smdparse and shared?
    parser = ArgumentParser(description='Generate HTML file from a text file in Script Markdown format.',
                            epilog='The program monitors changes and keeps window updated until CTRL-C is pressed.')
    parser.add_argument('-f', '--filename', required=True, help='the file that you want to parse')
    parser.add_argument('-c', '--cssfile', nargs='*', dest="cssfilelist", help='the CSS file you want used for the styling. Default is smd.css')
    parser.add_argument('-d', '--path', nargs='?', const='./html', default='./html', help='the directory that you want the HTML file written to. Default is ./html')
    parser.add_argument('-i', '--import', nargs='*', dest="importfilelist", help='list of file(s) to import after builtins.md loaded. Default is None')
    parser.add_argument('-m', '--monitor', nargs='+', default=[Monitor.Browser], help=f'the monitor [{Monitor.Browser}, {Monitor.HostGUI}, {Monitor.Endpoint}] you want used to display changes. Default is {Monitor.Browser}')
    
    from smd.smd import smd_add_std_cmd_line_parms
    from smd.core.sysdef import SystemDefaults

    sysDefaults = SystemDefaults()

    args = smd_add_std_cmd_line_parms(parser, sysDefaults, arguments)

    from smd.smdparse import ScriptParser, handle_cssfilelist_parameter, get_importfilelist

    sp = ScriptParser(args.filename, handle_cssfilelist_parameter(args.cssfilelist), get_importfilelist(args), args.path, sysDefaults)

    if sp.lastParseOK == False:
        message("stopping because the initial parse failed...")
        #//TODO: Need a command line switch to ignore this failure
        return 1


    iSMDLoop(args.monitor, sp).run()

    return 0


if __name__ == '__main__':
    exit(ismd())
