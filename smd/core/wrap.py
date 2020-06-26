#!/usr/bin/env python3

from .exception import ObjectNotFoundError

class WrapperStack(object):
    wrap_id = 'wrapstack'

    def __init__(self):
        pass

    @staticmethod
    def getWrapStack():
        from .thread import getTLS
        tls = getTLS()
        if tls is not None:
            stack = tls.getObjectFromTLS(WrapperStack.wrap_id)
            if stack is not None:
                return stack

            raise ObjectNotFoundError(f"Object {WrapperStack.wrap_id} not found in TLS")

        raise ObjectNotFoundError(f"Object TLS not found in thread local data")

    @staticmethod
    def getWrapStackPosition():
        stack = WrapperStack.getWrapStack()
        return len(stack) if stack is not None else 0

    @staticmethod
    def resetWrapStackPosition(pos, debugMsg):
        stack = WrapperStack.getWrapStack()
        debugMsg(f"Resetting wsp to {pos}<br />")
        if stack is None:
            debugMsg("WrapperStack is empty, nothing to do<br />")
            return False

        debugMsg(f"Current length of wsp stack is {len(stack)}<br />")
        if len(stack) <= pos:
            debugMsg("Returning because wrapper stack is already <= reset position")
            return False
        
        while(stack and len(stack) > pos):
            stack.pop()

        debugMsg(f"Length of wrapper stack is now: {len(stack)}<br />")
        return True
