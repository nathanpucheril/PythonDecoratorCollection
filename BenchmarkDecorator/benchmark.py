# @author Nathan Pucheril

class benchmark(object):

    def __init__(self, mode = "simple"):
        import time as t
        self.t = t
        self.mode = mode
        self.__total_time = 0
        self.__total_calls = 0

        ### MODES
        self.SIMPLE = "simple"
        self.CUMALATIVE = "cumalative"
        self.DETAILED = "detailed"

    def __call__(self, fn, *args, **kwargs):
        def caller(*args, **kwargs):
            retval, time = self.__timer(fn, *args, **kwargs)
            self.__total_calls += 1
            self.__total_time += time
            output = "<fn " + fn.__name__ + ">:  "
            output += "Time: " + str(time) + " s "
            if self.mode == self.CUMALATIVE or self.mode == self.DETAILED:
                output += " | Cumulative Time: " + str(self.__total_time) + " s "
            if self.mode == self.DETAILED:
                output += " | Calls: " + str(self.__total_calls) + " call(s)"
            print(output)
            return retval
        return caller

    def __timer(self, fn, *args, **kwargs):
        start = self.t.clock()
        retval = fn(*args, **kwargs)
        end = self.t.clock()
        return (retval, end - start)
