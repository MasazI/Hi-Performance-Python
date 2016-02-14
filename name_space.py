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
