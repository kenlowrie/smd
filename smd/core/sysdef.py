#!/usr/bin/env python

class SystemDefaults():
    def __init__(self):
        self._load_default_builtins = True
        self._load_user_builtins = True
        self._load_default_html = True
        self._load_default_head = True
        self._load_default_body = True
        self._load_user_files = True
        self._raw_output_file = None
        self._configData = {}
        self._importFiles = []

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

    def addImportFiles(self, importFiles):
        if importFiles:
            #print("Adding import file(s) {}".format(importFiles))
            self._importFiles.extend(importFiles)
        
    def getImportFiles(self):
        #print(f"looking for [{filename}]")
        return self._importFiles


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

    @property
    def raw_output_file(self):
        return self._raw_output_file

    @raw_output_file.setter
    def raw_output_file(self, value):
        self._raw_output_file = value

if __name__ == '__main__':
    print("Library module. Not directly callable.")
