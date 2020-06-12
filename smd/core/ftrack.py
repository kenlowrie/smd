#!/usr/bin/env python3

from pathlib import Path
from .debug import Debug

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
            # cannot instantiate the debug instance during startup; no guarantee TLS is there yet.  
            # let's check it now ...
            from .thread import getTLS
            if getTLS() is not None:
                # add the debug object if not already there
                if not hasattr(self, 'debug'): self.debug = Debug('ftrack')
                self.debug.print(f"cannot add candidate {candidate} to seen list; already accounted for.")

    def alreadySeen(self,name):
        return Path(name).resolve() in self.seen

    def dump(self, oprint):
        oprint("Files seen during parsing:")
        for fn in self.seen:
            oprint(f"\tFullname: {fn.resolve()}")


if __name__ == '__main__':
    print("Library module. Not directly callable.")
