#encoding: utf-8

import math
from math import sin

def test1(x):
    return math.sin(x)

def test2(x):
    return sin(x)

import dis
dis.dis(test1)

dis.dis(test2)

def test1_repeat():
    result = 0
    for i in xrange(100000000):
        result += sin(i)
    return result

def test2_repeat():
    result = 0
    local_sin = sin
    for i in xrange(100000000):
        result += local_sin(i)
    return result
