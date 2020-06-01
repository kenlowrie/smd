#!/usr/bin/env python

from pathlib import Path


class ConfigFileObject():
    """Keeps track of a configuration file

    filename - the fully qualified path
    okay2load - bool that tells whether to return this files contents or not
    filedata - the actual filedata, if set statically prior to initialization

    The default behavior is to return the contents of a system (or user) specified
    file. However, consumers of the ScriptParser() class may wish to override the
    contents coming from the locally defined system or user files, so they
    are able to "preload" the contents they wish returned for any/all system files
    by constructing a SystemDefaults() object ahead of time, and passing it when
    they instantiate a ScriptParser() object. See smdparse.py as an example of
    how this latter behavior works.

    for SMD, the default configuration file heirarchy is as follows:
        <installpath>/import/builtins.md - The default builtins that are loaded
        ~/.smd/import/builtins.md - User specific builtins that are loaded *after*

        <installpath>/import/def_html.md - Default Document start HTML
        <installpath>/import/def_head.md - Default <head>...</head> contents
        <installpath>/import/def_body.md - Default <body> contents
        <installpath>/import/def_bodyclose.md - Default closing body contents
        <installpath>/import/def_close.md - Default Document closing

        The Default Document section contents can be overridden by placing
        a file with the same name in the ~/.smd folder. For example:

        ~/.smd/import/def_html.md, if this exists, supercedes the default above.

        There are a number of command lines switches that change the behavior
        of both the builtins and each document section configuraiton file.
    
    See the argument parsing in smd.py and smdparse.py for examples of how
    you can change the behavior of the program via command line switches.
    """
    def __init__(self,name,path, okay2load):
        self.filename = Path().joinpath(path,name)
        self.okay2load = okay2load
        from .utility import _tls_data
        # filedata will be either None (if not present, or the data)
        self.filedata = _tls_data.sd.getConfigFileData(name)

    def data(self):
        # This is set per-config file
        if not self.okay2load:
            return []

        # If a program instantiates its own copy of SystemDefaults(), it
        # can provide default data for each config file, overriding the
        # default files that the system provides.
        if self.filedata:
            return self.filedata

        # okay, if we get here, we gotta read the contents from disk
        with open(self.filename) as f:
            self.builtins = [line for line in f]

        # return the lines
        return self.builtins

    def datastack(self):
        # return the lines, but reverse the order first. This is normally
        # used by the Cache() code, because the cache data is managed as
        # a stack, so we need to order it properly
        return self.data()[::-1]

class LocalUserConfigFile(ConfigFileObject):
    """Same as ConfigFile, but looks in the ~/.smd folder

    This provides identical functionality to ConfigFile, but instead of
    looking in <installpath>, it looks in ~/.smd. We maintain this
    specialized version, because most things can exist in both places,
    and we want to track them accordingly.
    """
    def __init__(self, name, okay2load):
        path = Path().joinpath(Path().home(), ".smd/")
        super(LocalUserConfigFile, self).__init__(name,path,okay2load)

class ConfigFile(ConfigFileObject):
    """Track configuration files
    
    This object tracks both the system default config file as well 
    as a user specific config file. We track both of them and then
    provide overrides for the underlying methods, that return the
    user-specific data if present, unless we are being instructed
    otherwise -- usually by command line parameters.
    """
    def __init__(self, name, okay2load, user_ver=True):
        from .globals import _getBasepath
        super(ConfigFile, self).__init__(name,_getBasepath(),okay2load)
        from .utility import _tls_data
        
        # load_user_files by default is True, but can be set to False,
        # which will prevent any user-specific files from being loaded
        # also, user_ver is by default True, but can be overridden to
        # provide another way of preventing the object from giving
        # precedence to the user specifc configuration file.
        self.localuser = LocalUserConfigFile(name,okay2load) if _tls_data.sd.load_user_files and user_ver else None

    def data(self):
        # Return the user specific contents if available
        if (self.localuser and self.localuser.filename.is_file()):
            return self.localuser.data()

        # Return the system default version instead
        return super(ConfigFile,self).data()

    def datastack(self):
        # Return the user specific contents if available
        if (self.localuser and self.localuser.filename.is_file()):
            return self.localuser.datastack()

        # Return the system default version instead
        return super(ConfigFile,self).datastack()


class SystemDefaults():
    def __init__(self):
        self._load_default_builtins = True
        self._load_user_builtins = True
        self._load_default_html = True
        self._load_default_head = True
        self._load_default_body = True
        self._load_user_files = True
        self._configData = {}

    # //TODO: Not sure if this is how I want to do this permanently, but works for now.
    # Basically, these two methods provide a way to "override" loading the various
    # configuration files from disk, and instead allow them to be passed in

    def addConfigFileData(self, filename, filedata):
        #print("Adding [{}] to [{}]".format(filedata,filename))
        self._configData[filename] = filedata

    def getConfigFileData(self, filename):
        #print(f"looking for [{filename}]")
        if filename in self._configData.keys():
            #print(f"returning [{self._configData[filename]}")
            return self._configData[filename]
        
        return None

    def dump(self, oprint=print):
        #//TODO: HACK
        f0="strong"
        f1="em"
        from .utility import HtmlUtils
        for key,val in self.__dict__.items():
            oprint(f"<{f0}>{key}</{f0}>: <{f1}>{HtmlUtils.escape_html(val)}</{f1}><br />")

    @property
    def load_default_builtins(self):
        return self._load_default_builtins

    @load_default_builtins.setter
    def load_default_builtins(self, value):
        self._load_default_builtins = value

    @property
    def load_user_builtins(self):
        return self._load_user_builtins

    @load_user_builtins.setter
    def load_user_builtins(self, value):
        self._load_user_builtins = value

    @property
    def load_default_html(self):
        return self._load_default_html

    @load_default_html.setter
    def load_default_html(self, value):
        self._load_default_html = value

    @property
    def load_default_head(self):
        return self._load_default_head

    @load_default_head.setter
    def load_default_head(self, value):
        self._load_default_head = value

    @property
    def load_default_body(self):
        return self._load_default_body

    @load_default_body.setter
    def load_default_body(self, value):
        self._load_default_body = value

    @property
    def load_user_files(self):
        return self._load_user_files

    @load_user_files.setter
    def load_user_files(self, value):
        self._load_user_files = value

if __name__ == '__main__':
    print("Library module. Not directly callable.")
