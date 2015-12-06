#encoding: utf-8

import time
from functools import wraps

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print("@timefn: " + fn.func_name + " took " + str(t2-t1) + "seconds")
        return result
    return measure_time
