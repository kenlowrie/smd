#!/usr/bin/env python

from pathlib import Path
from os import chdir

print("FILE={}".format(__file__))
parent = Path(__file__).parent
chdir(parent)

from sys import path
from os.path import dirname, abspath, realpath, split, join
bin_path, whocares = split(dirname(realpath('__file__')))
lib_path = abspath(bin_path)
path.insert(0, lib_path)
print("smd Package unittest")
print("PYTHONPATH=")
for item in path:
    print('  {}'.format(item))

import io
import sys
from unittest import TestCase, TestLoader, TextTestRunner

import smd.smd


def decode(html_string):
    from sys import version_info
    from html import unescape

    return unescape(html_string)


class TestSMD(TestCase):
    def setUp(self):
        from smd.core.sysdef import SystemDefaults
        sysDefaults = SystemDefaults()
        sysDefaults.load_default_html = False
        sysDefaults.load_default_head = False
        sysDefaults.load_default_body = False
        sysDefaults.load_user_files = False
        sysDefaults.load_default_builtins = False
        self.smd = smd.smd.ScriptParser(sysDefaults)
        self.capturedOutput = io.StringIO()     # Create StringIO object
        self.smd.stdoutput = (self.capturedOutput, False)   # and redirect stdout.

    def tearDown(self):
        self.smd.stdoutput = sys.__stdout__     # Reset redirect.
        del self.smd
        self.smd = None
        del self.capturedOutput

    def process(self, which, checkEqual=True):
        self.smd.open_and_parse("in/{}.md".format(which))
        with open('run/{}.out'.format(which), 'w') as mf2:
            mf2.write(self.capturedOutput.getvalue())

        if(checkEqual):
            with open('out/{}.html'.format(which), 'r') as myfile:
                data = myfile.read()
            self.assertEqual(self.capturedOutput.getvalue(), data)

    def test_markdown(self):
        self.process('markdown')

    def test_help(self):
        self.process('help')

    def test_var(self):
        self.process('var')

    def test_film(self):
        self.process('film')

    def test_quit(self):
        self.process('quit')

    def test_stop(self):
        self.process('stop')

    def test_link(self):
        self.process('link')

    def test_dump(self):
        self.process('dump')

    def test_html(self):
        self.process('html')

    def test_code(self):
        self.process('code')

    def test_wrap(self):
        self.process('wrap')

    def test_misc(self):
        self.process('misc')

    def test_image(self):
        self.process('image')

    def test_images(self):
        self.process('images')

    def test_divs(self):
        self.process('divs')

    def test_specials(self):
        self.process('specials')

    def test_import(self):
        self.process('import')

    def test_script1(self):
        self.process('script1')

    def test_transitions(self):
        self.process('transitions')

    def test_revision(self):
        """
        Validate Revision keyword output with date/time stamps

        We can't use the standard way of comparing the output to a known
        data set, since the date/time stamp changes on each execution.
        So, we gotta look at each one and make sure it's in the right format,
        and length, etc., etc.
        """
        self.process('revision', False)
        g1 = r'<p class\=\"revTitle\">Revision:([^\(]*)([^<]*)</p>'
        g2 = r'\(([0-9]{8})\s@\s([0-9]{2}:[0-9]{2}:[0-9]{2})\)'
        from re import findall, match
        from time import strftime
        ts_date = "{}".format(strftime("%Y%m%d"))
        ts_time = "{}".format(strftime("%H:%M:%S"))

        # Find all the <p class="revTitle">Revision: n (date @ time)</p> lines
        m = findall(g1, self.capturedOutput.getvalue())
        self.assertEqual(len(m), 3)
        for rev_set in m:
            # extract the revision and timestamp from a match
            r, ts = rev_set
            # extract the date and time
            m2 = match(g2, ts)
            self.assertEqual(len(m2.groups()), 2)    # should be a date and a time
            self.assertEqual(m2.group(0)[0:1], '(')  # should start with (
            self.assertEqual(m2.group(0)[-1], ')')   # should end with )
            self.assertEqual(len(m2.group(1)), 8)    # date length is 8
            self.assertEqual(m2.group(1),ts_date)
            self.assertEqual(len(m2.group(2)), 8)    # time length is 8
            self.assertEqual(m2.group(2)[0:3],ts_time[0:3])

    def test_mailto(self):
        """
        Validate a mailto: link

        We can't use the standard way of comparing the output to a known
        data set, since mailto: links are encoded as HTML entities to help
        foil spambots. As such, each time we render the HTML file, the output
        is different. So, we need to parse the output and find the encoded
        entities, decode them, and compare them to what they were originally.
        """
        self.process('mailto', False)
        g1 = r'<a href=\"(.*)\">([\w]*)</a>'
        from re import findall

        d = {
            "me": "mailto:myemail@mydomain.com",
            "you": "mailto:your.email_address@your-domain.com",
            "feedback": "mailto:email@yourdomain.com?subject=Your%20Film%20Title%20Feedback"
        }

        # Find all the <a href="encoded_mailto_link">varname</a> lines
        output = self.capturedOutput.getvalue()
        m = findall(g1, output)
        self.assertEqual(len(m), 3)
        for mailto_set in m:
            # extract the mailto link and the variable name from a match
            mailto, var_name = mailto_set

            self.assertEqual(decode(mailto), d.get(var_name))
        
        google="https://www.google.com?s=\"testing%20stuff\""
        self.assertTrue(output.find(google) != -1)

        decoded = decode(output)
        encode1 = "mailto:info@domain.com"
        self.assertTrue(decoded.find(encode1) != -1)

        encode2 = "mailto:info@www.testdomain.net?a=\"this%20is%20a%20test\""
        self.assertTrue(decoded.find(encode2) != -1)


if __name__ == '__main__':
    suite3 = TestLoader().loadTestsFromTestCase(TestSMD)
    TextTestRunner(verbosity=2).run(suite3)
