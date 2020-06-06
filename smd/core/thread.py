#!/usr/bin/env python3

# Global that tells which way to access the TLS.
#   If True, the tls stored as current_thread.__dict__[ThreadLocalStorage.tls_smd_core]
#   If False, the tls stored in gb_tls_object global variable
#
# For now, I've decided to just store the ThreadLocalStorage instance into current_thread['tls_smd_core'].
# Seems cleaner and less convoluted, but might have to rethink if I find out why current_thread.local() is preferred.
#
#use_dict_instance = True

# This global is used to hold the thread local storage data; or the old way, it held current_thread.local()
# Leave for now, remove before release if it never comes back... #//TODO: 
#gb_tls_object = None

class ThreadLocalStorage(object):
    tls_smd_core = 'tls_smd_core'

    def __init__(self, _local_in=None):
        # Store reference to threading.local instance in here
        # Allow the caller to pass in a reference to an already allocated
        # local store (not sure if this will be useful, we will see)
        #//TODO: This isn't used, so remove before release v1.0
        #from threading import local
        #self._local_instance = _local_in if _local_in is not None else local()

        # And now store a reference to this object in the local instance object
        #self._local_instance.tls_smd_core = self
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
            #//TODO: Probably need to handle this
            pass

        return None

    def getObjectByClassFromTLS(self, objClass):
        for item in self.__dict__.keys():
            try:
                instance = eval(f'self.{item}')
                if isinstance(instance, objClass):
                    return instance
            except:
                #//TODO: Probably need to handle this
                pass

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
            #//TODO: Replace with debug print
            print(f"Resetting TLS...")
            keys = [i for i in tls.__dict__.keys()]
            for key in keys:
                del tls.__dict__[key]

            return tls

    #//TODO: go ahead and store this for now, we can test it out as we go. better than the global variable solution...
    from threading import current_thread
    newtls = ThreadLocalStorage()
    current_thread.__dict__[ThreadLocalStorage.tls_smd_core] = newtls

    return newtls

def getTLS():
    from threading import current_thread
    return current_thread.__dict__[ThreadLocalStorage.tls_smd_core] if hasattr(current_thread, ThreadLocalStorage.tls_smd_core) else None


if __name__ == '__main__':
    print("Library module. Not directly callable.")
