#!/usr/bin/env python3

from .debug import Debug

#/TODO: Wonder if I can put the debug register in the tls store too? That would be much cleaner...

# Global that tells which way to access the TLS.
# If True, the tls stored as current_thread.__dict__[ThreadLocalStorage.tls_smd_core]
# If False, the tls stored in gb_tls_object global variable
#use_dict_instance = True

# This global is used to hold the thread local storage data
#gb_tls_object = None

class ThreadLocalStorage(object):
    tls_smd_core = 'tls_smd_core'

    def __init__(self, _local_in=None):
        # Store reference to threading.local instance in here
        # Allow the caller to pass in a reference to an already allocated
        # local store (not sure if this will be useful, we will see)
        from threading import local
        #//TODO: This isn't used, so I should remove it...
        #self._local_instance = _local_in if _local_in is not None else local()

        # And now store a reference to this object in the local instance object
        #self._local_instance.tls_smd_core = self
    
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
            print(f"Resetting TLS...")
            keys = [i for i in tls.__dict__.keys()]
            for key in keys:
                del tls.__dict__[key]

            return tls

    #global use_dict_instance
    #if use_dict_instance:
    #    pass
    #else:
    #    pass

    #//TODO: For now, let's store it both ways for testing...
    #global gb_tls_object
    #gb_tls_object = ThreadLocalStorage()

    #//TODO: go ahead and store this for now, we can test it out as we go. better than the global variable solution...
    from threading import current_thread
    #current_thread.__dict__[ThreadLocalStorage.tls_smd_core] = gb_tls_object
    newtls = ThreadLocalStorage()
    current_thread.__dict__[ThreadLocalStorage.tls_smd_core] = newtls

    return newtls

def getTLS():
    #global use_dict_instance
    #if use_dict_instance:
    from threading import current_thread
    return current_thread.__dict__[ThreadLocalStorage.tls_smd_core] if hasattr(current_thread, ThreadLocalStorage.tls_smd_core) else None

    #global gb_tls_object
    #return gb_tls_object


if __name__ == '__main__':
    print("Library module. Not directly callable.")
