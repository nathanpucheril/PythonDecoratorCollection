# @author Nathan Pucheril

def log(fn):
    import os
    from time import strftime
    def logger(*args):
        time = strftime("%Y-%m-%d %H:%M:%S")
        path = "log <function " + fn.__name__ + ">.txt"
        retval = fn(*args)
        with open(path, 'a+') as f:
            f.write("----\n")
            f.write("Return Value: " +  str(retval) + "     @ " + time + "\n\n")
        return retval
    return logger

@log
def test():
    return 5

test()
