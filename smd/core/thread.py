#!/usr/bin/env python3

from .exception import ObjectNotFoundError

class ThreadLocalStorage(object):
    tls_smd_core = 'tls_smd_core'

    def __init__(self, _local_in=None):
        pass
    
    @property
    def tls(self):
        return self._local_instance
    
    @tls.setter
    def tls(self, tls_object):
        self._local_instance = tls_object

    # These methods provide a way for quick thread level instance data to be added, without
    # having direct support built into the class. Seems like using properties for the well
    # known items, however, is cleaner. We will see once I try to implement it.

    def addObjectToTLS(self, objName, objInstance=None):
        if hasattr(self, objName): 
            raise AttributeError(f"TLS already has {objName} attribute")

        exec(f"self.{objName} = objInstance")
    
    def removeObjectFromTLS(self, objName):
        if objName not in self.__dict__.keys():
            raise AttributeError(f"TLS does not have any attribute named {objName}")

        del self.__dict__[objName]
    
    def getObjectFromTLS(self, objName):
        try:
            if objName in self.__dict__.keys():
                return self.__dict__[objName]
        except:
            raise ObjectNotFoundError(f"No object named {objName} found in TLS")

        return None

    def getObjectByClassFromTLS(self, objClass):
        for item in self.__dict__.keys():
            try:
                instance = eval(f'self.{item}')
                if isinstance(instance, objClass):
                    return instance
            except:
                raise ObjectNotFoundError(f"No object of class {objClass} found in TLS")
    
        return None

def initTLS(reset_if_initialized=True):
    tls = getTLS()
    if tls is not None:
        if not reset_if_initialized:
            raise AssertionError("ThreadLocalStorage is already initialized.")
        else:
            # Alternative implementation might be to put a reset method on the class.
            # Then consumers of the ScriptParser() class could decide when it's okay to
            # reset the TLS (like after they extract fileTracker, etc.)
            keys = [i for i in tls.__dict__.keys()]
            for key in keys:
                del tls.__dict__[key]

            return tls

    from threading import current_thread
    newtls = ThreadLocalStorage()
    current_thread.__dict__[ThreadLocalStorage.tls_smd_core] = newtls

    return newtls

def getTLS():
    from threading import current_thread
    return current_thread.__dict__[ThreadLocalStorage.tls_smd_core] if hasattr(current_thread, ThreadLocalStorage.tls_smd_core) else None


if __name__ == '__main__':
    print("Library module. Not directly callable.")
