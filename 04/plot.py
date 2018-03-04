#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    x1 = np.array([30, 50, 70, 80, 100])
    x2 = np.array([0, 1, 1, 2, 1])
    y1 = [1, 3, 4]
    y2 = [0, 2]
    plt.scatter(x1[y1], x2[y1], marker='o')
    plt.scatter(x1[y2], x2[y2], marker='x')
    plt.xlabel(r'Income (thousands \$), $x_{i1}$')
    plt.ylabel(r'Num websites, $x_{i2}$')
    plt.savefig('image/3a.png')

if __name__ == '__main__':
    main()
