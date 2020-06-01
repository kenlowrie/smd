#!/usr/bin/env python

class SystemDefaults():
    def __init__(self):
        self._load_default_builtins = True
        self._load_user_builtins = True
        self._load_default_html = True
        self._load_default_head = True
        self._load_default_body = True
        self._load_user_files = True

    def dump(self, oprint=print):
        #//TODO: HACK
        f0="strong"
        f1="em"
        for key,val in self.__dict__.items():
            oprint(f"<{f0}>{key}</{f0}>: <{f1}>{val}<{f1}><br />")

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
