import math
import sys

def check_prime(number):
    sqrt_number = math.sqrt(number)
    number_float = float(number)
    for i in xrange(2, int(sqrt_number)+1):
        if (number_float / i).is_integer():
            return False
    return True

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    if(argc != 2):
                    print 'Usage: python %s num' % argvs[0]
                    quit()
    num = argvs[1]
    print "check_prime: " + num + "=", check_prime(int(num))
    print "check_prime: " + num + "+19=", check_prime(int(num)+19)
