#!/usr/bin/env python

from .constants import Constants
from .thread import getTLS

class Debug(object):
    def __init__(self, classtag, initial_state=False):
        self._state = initial_state
        self._tag = '{}.{}'.format(classtag,id(self))
        self._tls = getTLS()
        self._dbgTrack = self._tls.getObjectFromTLS(Constants.debugTracker)
        self._dbgXface = self._dbgTrack.xfaces
        self._dbgXface.register_xface(self)

    def global_suspend(self, suspend):
        # used to globally suspend debug messages
        self._dbgXface.suspend_xface(suspend)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, newvalue):
        self._state = True if newvalue else False

    @property
    def output(self):
        self._out

    @output.setter
    def output(self, output):
        self._out = output

    @property
    def tag(self):
        return self._tag

    def on(self):
        self.state = True

    def off(self):
        self.state = False

    def toggle(self):
        self.state = not self.state

    def enabled(self):
        return self.state

    def print_msg(self, msg, context=None):
        s = '{:>20}: {}{}<br />\n'.format(self._tag, '{}'.format('' if context is None else '({})'.format(context)), msg)
        self._dbgXface.oprint('<span class="debug">{}</span>'.format(s))

    def print(self, msg, context=None):
        if not self.state:
            return

        self.print_msg(msg, context)

class DebugTrackerXface(object):
    def __init__(self, reg_xface, suspend_xface, oprint):
        self._register_xface = reg_xface
        self._suspend_xface = suspend_xface
        self._oprint = oprint
    
    @property
    def register_xface(self):
        return self._register_xface
    
    @property
    def suspend_xface(self):
        return self._suspend_xface
    
    @property
    def oprint(self):
        return self._oprint

class DebugTracker(object):
    def __init__(self, output=None):
        self.suspendCounter=0
        self._debug_tags = {}
        self._msg_cache = []
        self._debug = None
        self._interfaces = DebugTrackerXface(self.debug_register_xface, self.debug_suspend_xface, self.print)

        # This is the output method. print() by default, unless passed in
        self._out = output if output is not None else print

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, dbgObj):
        self._debug = dbgObj

    @property
    def xfaces(self):
        return self._interfaces

    def print(self, s):
        if self.suspendCounter == 0:
            self._out(s)
        else:
            self._msg_cache.append(s)

    def output(self, s):
        # We only want to print if at least one debug tag is on
        # This prevents spurious messages from being output when
        # debug tracking is not currently enabled.
        if self.debug_active():
            self.sys_debug.print_msg(s)

    @property
    def debug_tags(self):
        return self._debug_tags

    @debug_tags.setter
    def debug_tags(self, args):
        return self._debug_tags

    def _is_registered(self, tag):
        return True if tag in self.debug_tags else False

    def _check_valid(self, tag):
        if not self._is_registered(tag):
            raise NameError("tag {} is not registered".format(tag))

    def _get_tag(self, tag):
        if not self._is_registered(tag):
            raise NameError("tag {} is unknown".format(tag))

        return self.debug_tags[tag]

    def _get_state(self, tag):
        if not self._is_registered(tag):
            raise NameError("tag {} is unknown".format(tag))

        return self.debug_tags[tag].state

    def dump_cache(self):
        msgs = self._msg_cache[::-1]
        self._msg_cache = []
        if len(msgs):
            self.output("Dumping debug cache.")
            while len(msgs):
                self._out(msgs.pop())

    def debug_suspend_xface(self, suspend):
        if suspend == True:
            self.output("Debug output has been suspended.")
            self.suspendCounter += 1
        else:
            self.suspendCounter -= 1
            if self.suspendCounter < 0:
                raise ValueError("Debug suspend counter went below zero.")
            elif self.suspendCounter == 0:
                # Dump any cached messages
                self.dump_cache()
                self.output("Debug output will be resumed.")
            else:
                # cache a debug output decrement counter message
                self.output("Debug output suspendCounter--")

    def debug_register_xface(self, obj):
        if not isinstance(obj, Debug):
            raise NameError("obj must be instance of Debug class")

        if self._is_registered(obj.tag):
            raise NameError("tag {} already registered".format(obj.tag))

        self.debug_tags[obj._tag] = obj

    def debug_active(self):
        # Check to see if any debug trackers are enabled
        for var in self.debug_tags:
            if self.debug_tags[var].enabled():
                return True

        return False

    def call(self, which, method):
        from .regex import RegexSafe
        reObj = RegexSafe(which)
        
        for var in sorted(self.debug_tags):
            if reObj.is_match(var) is None:
                continue

            self._check_valid(var)
            eval('self._get_tag(var).{}()'.format(method))
            _fmtinfo = ['strong', 'enabled'] if self._get_state(var) else ['em', 'disabled']
            s = '<{2}>Method({1}): {0} is now {3}</{2}><br />'.format(var, method, _fmtinfo[0], _fmtinfo[1])
            self._out('<span class="debug green">{}</span>'.format(s))

    def on(self, tag):
        self.call(tag, 'on')

    def off(self, tag):
        self.call(tag, 'off')

    def toggle(self, tag):
        self.call(tag, 'toggle')

    def enabled(self, tag):
        self.call(tag, 'enabled')

    def dumpTags(self):
        self._out('<div><h3>Registered debug tags</h3>')
        for tag in sorted(self.debug_tags):
            self._out('<span class="debug green"><{1}>{0}</{1}></span><br />'.format(tag, 'strong' if self.debug_tags[tag].state else 'em'))
        self._out('</div>')


if __name__ == '__main__':
    print("Library module. Not directly callable.")
