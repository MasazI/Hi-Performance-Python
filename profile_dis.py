# encoding: utf-8

def fn_expressive(upper = 1000000):
    total = 0
    for n in xrange(upper):
        total += n
    return total


def fn_terse(upper = 1000000):
    return sum(xrange(upper))

print("同じ計算結果になる: %s" % (fn_expressive() == fn_terse()))


