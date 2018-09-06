#!/usr/bin/env python

class HtmlUtils():

    @staticmethod
    def escape_html(s):
        if type(s) != type(''):
            # If we weren't passed a string, convert it to a string before we escape it.
            s = str(s)

        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

class CodeHelpers():

    @staticmethod
    def b(i):
        return '{{' if i == 0 else '}}'

if __name__ == '__main__':
    print("Library module. Not directly callable.")
