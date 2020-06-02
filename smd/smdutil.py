#!/usr/bin/env python3

class _Error(Exception):
    """Base exception class for this module."""
    pass

class ConsoleMessage(object):
    def __init__(self, whoami):
        import kenl380.pylib as pylib

        self.me = pylib.context(whoami)
    
    def o(self,msg):
        from threading import current_thread
        threadid = current_thread().native_id
        print(f"{self.me.alias()}({threadid}): {msg}")

