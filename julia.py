# encoding:utf-8

import time

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def calculate_z_serial_purepython(maxiter, zs, cs):
    '''
    ジュリア漸化式を用いた計算
    '''
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]

        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


def calc_pure_python(desired_width, max_iterations):
    '''
    座標リストzsとパラメータリストcsを生成し、ジュリア集合を生成する
    '''
    x_step = (float(x2 - x1)/float(desired_width))
    y_step = (float(y1 - y2)/float(desired_width))

    x = []
    y = []

    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []

    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print "Length of x: ", len(x)
    print "Total elements: ", len(zs)

    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()

    duration = end_time - start_time

    print calculate_z_serial_purepython.func_name + " took", duration, "sec"

    assert sum(output) == 33219980


def test():
    calc_pure_python(1000, 300)


if __name__ == '__main__':
    test()
