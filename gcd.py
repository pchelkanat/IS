import math
import random
import time

import numpy as np


def gen_odd(keysize):
    while True:
        num = random.randrange(2 ** keysize - 1)
        if num % 2 != 0:
            return num


def make_odd(num):
    if num != 0:
        while num % 2 == 0:
            num /= 2
    return num


def M_JWA(x, y, k):
    r = (x * eea(k, y)[2]) % k
    f1 = np.array([k, 0])
    f2 = np.array([r, 1])

    while f2[0] >= math.sqrt(k):
        f1 = f1 - f1[0] // f2[0] * f2
        f1, f2 = f2, f1
    print(np.array([f1, f2]))
    return np.array([f1, f2])


def ewsa(u, v):
    k = 2 ** 6  #для примера
    #k = 2 ** 64  # для больших
    n = math.trunc(math.log2(u))
    if n ** 0.4 > k:
        m = math.trunc(0.4 * math.log2(n)) + 1
        m = m + m % 2
        k = 2 ** m
    iteration = 1
    while u * v != 0:
        print("iteration", iteration)
        if u < v:
            u, v = v, u
            print("uv1", u, v)
        elif u / v < math.sqrt((k)):
            M = np.array(M_JWA(u, v, k))
            u, v = (abs(M[0, 1] * u - M[0, 0] * v) / k), (abs(M[1, 1] * u - M[1, 0] * v) / k)
            print("uv2", u, v)
        else:
            u, v = v, u % v
            print("uv3", u, v)
        u, v = make_odd(u), make_odd(v)
        iteration += 1
    return u + v


def eea(a, b):
    x, x1 = 1, 0
    y, y1 = 0, 1
    while b:
        q = a // b
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a, b = b, a - q * b
    if y == -1:
        y += a
    return a, x, y


if __name__ == '__main__':

    a, b = 28865, 19203 #пример
    #a, b = gen_odd(50), gen_odd(50)
    #a, b = 1425, 125
    print(a, b)

    start_time = time.time()
    print(eea(a, b)[0])
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    print(ewsa(a, b))
    print("--- %s seconds ---" % (time.time() - start_time))
