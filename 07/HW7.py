#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def get_table():
    return np.matrix([-2, -1, 0, 3, 3.5]), np.matrix([0, 0, 1, 3, 3])

def get_uH():
    x, y = get_table()
    WH = np.matrix([-1, 1, 1]).T
    bH = np.matrix([-1, 1, -2]).T
    zH = WH * x + bH
    uH = zH
    uH[uH<0] = 0
    return uH

def get_Wb():
    _, y = get_table()
    uH = get_uH()
    X = np.vstack((uH, np.ones((1,5))))
    X = np.matrix(X)
    A = y * X.T * (X * X.T).I
    return np.ravel(A[0,:-1]), A[0,-1]

def p2_c():
    Wo, bo = get_Wb()
    print('The bias is', bo)
    print('The weights are', Wo)

def p2_d():
    x, _ = get_table()
    Wo, bo = get_Wb()
    uH = get_uH()
    yhat = Wo * uH + bo
    x = np.ravel(x)
    yhat = np.ravel(yhat)
    plt.stem(x, yhat)
    plt.xlabel('x')
    plt.ylabel(r'$\hat{y}$')
    plt.savefig('image/2d.png')

def predict(x, y, WH, bH, Wo, bo):
    zH = WH * x + bH
    uH = zH
    uH[uH<0] = 0
    yhat = Wo * uH + bo
    return yhat

def func_None():
    print('Cannot find function.');

def main(f):
    func_dict = {'p2_c':p2_c, 'p2_d':p2_d}
    return func_dict.get(f, func_None)()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Wrong arguments!')
