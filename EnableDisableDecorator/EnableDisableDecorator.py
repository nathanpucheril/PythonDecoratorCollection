#@author Nathan Pucheril
# Useful for disabling certain functions decorated with this

def enable(fn):
  return fn

def disable(fn):
    def passed(*args,**kwargs):
        pass
    return passed

###USAGE###
# decorators_enabled = True
# enabler = enable if decorators_enabled else disable
# @enabler
# def func():
#     ...
#
