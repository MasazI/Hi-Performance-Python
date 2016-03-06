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
    simple implementatin of xrange (speed improving and memory reduction)
    '''
    while start < stop:
        yield start
        start += step

for i in range(0, 10000):
    pass

for i in xrange(0, 10000):
    pass

def test_range():
    for i in range(0, 100000000):
        pass

def test_xrange():
    for i in xrange(0, 100000000):
        pass

def list_comprehension_i(list_of_numbers):
    '''
    iterator list comprehension
    '''
    divisible_by_three = len([n for n in list_of_numbers if n % 3 == 0])
    print divisible_by_three

def list_comprehension_g(list_of_numbers):
    '''
    generator list comprehension. (memory reduction)
    '''
    divisible_by_three = sum((1 for n in list_of_numbers if n %3 == 0))
    print divisible_by_three

list_of_numbers = range(0, 10000)

list_comprehension_i(list_of_numbers)
list_comprehension_g(list_of_numbers)

def fibonacci():
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i + j

def fibonacci_transform():
    count = 0
    for f in fibonacci():
        if f > 5000:
            break
        if f % 2:
            count += 1
    return count

print fibonacci_transform()

