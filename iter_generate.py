# encoding:utf-8

def range(start, stop, step=1):
    '''
    simple implementation of range
    '''
    numbers = []
    while start < stop:
        numbers.append(start)
        start += step
        return numbers

def xrange(start, stop, step=1):
    '''
    simple implementatin of xrange
    '''
    while start < stop:
        yield start
        start += step

for i in range(0, 10000):
    pass

for i in xrange(0, 10000):
    pass

def test_range():
    for i in range(0, 10000000):
        pass

def test_xrange():
    for i in xrange(0, 10000000):
        pass
