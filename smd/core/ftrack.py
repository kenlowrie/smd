#!/usr/bin/env python3

from pathlib import Path

#//TODO: This class probably isn't needed any longer.
class FileName(object):
    def __init__(self,name):
        self._name = Path(name).resolve()
    
    @property
    def name(self):
        return str(self._name)
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def parent(self):
        return str(self._name.parent)
    
    def basename(self):
        return str(self._name.name)

class FileTrack(object):
    """A class to keep track of files that are opened."""
    def __init__(self):
        self._seen = [] # List of pathlib.Path objects
    
    @property
    def seen(self):
        return self._seen   # Return the list of pathlib.Path objects
    
    @seen.setter
    def seen(self,name):
        candidate = Path(name).resolve()
        if candidate not in self.seen:
            self.seen.append(candidate)
        else:
            #//TODO: Add a debug statement here?
            pass

    def alreadySeen(self,name):
        return Path(name).resolve() in self.seen

    #//TODO: This seems no longer needed
    def seenAsFileNameList(self):
        return [FileName(fn) for fn in self._seen]

    def dump(self):
        #//TODO: All of these prints need to go through the output module...
        print("Files seen during parsing:")
        for fn in self.seen:
            print(f"\tFullname: {fn.resolve()}")

    def dump1(self):
        for fn in self.seen:
            print(f"Rootname: {fn.name}\n\tDirectory: {fn.parent}\n\tFullname: {fn.resolve()}")

    def dump2(self):
        for fn in self.seenAsFileNameList():
            print(f"Rootname: {fn.basename()}\n\tDirectory: {fn.parent()}\n\tFullname: {fn.name}")


if __name__ == '__main__':
    print("Library module. Not directly callable.")
