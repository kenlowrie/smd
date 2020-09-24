#!/usr/bin/env python

class SystemDefaults():
    DefaultBuiltinsName = 'import/builtins.md'
    DefaultHtmlName = 'import/def_html.md'
    DefaultHeadName = 'import/def_head.md'
    DefaultBodyName = 'import/def_body.md'
    DefaultBodyCloseName = 'import/def_bodyclose.md'
    DefaultHtmlCloseName = 'import/def_close.md'

    def __init__(self):
        self._load_default_builtins = True
        self._load_user_builtins = True
        self._load_default_html = True
        self._load_default_head = True
        self._load_default_body = True
        self._html_name = None
        self._head_name = None
        self._body_name = None
        self._bodyclose_name = None
        self._close_name = None
        self._load_user_files = True
        self._raw_output_file = None
        self._configData = {}
        self._importFiles = []

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

    def dump(self, which=None, oprint=None):
        """Dumps the system defaults that match the pattern."""
        which = which if which is not None else '.*'
        oprint = oprint if oprint is not None else print
        from .utility import HtmlUtils
        oprint("{1}<br />\nSystem Defaults: {0}<br />\n{1}<br />".format(HtmlUtils.escape_html(which),'-'*40))
        from .regex import RegexSafe
        reObj = RegexSafe(which)
        for default in self.__dict__.keys():
            if reObj.is_match(default) is None:
                continue

            oprint("&nbsp;&nbsp;<strong>{0}=</strong>{1}<br />".format(default,  
                                                                       HtmlUtils.escape_html(self.__dict__[default])))

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

    @property
    def html_name(self):
        return self._html_name

    @html_name.setter
    def html_name(self, value):
        self._html_name = value

    @property
    def head_name(self):
        return self._head_name

    @head_name.setter
    def head_name(self, value):
        self._head_name = value

    @property
    def body_name(self):
        return self._body_name

    @body_name.setter
    def body_name(self, value):
        self._body_name = value

    @property
    def bodyclose_name(self):
        return self._bodyclose_name

    @bodyclose_name.setter
    def bodyclose_name(self, value):
        self._bodyclose_name = value

    @property
    def close_name(self):
        return self._close_name

    @close_name.setter
    def close_name(self, value):
        self._close_name = value

if __name__ == '__main__':
    print("Library module. Not directly callable.")
