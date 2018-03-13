#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly

def main():
    beta0 = np.array([1, 2, -1])
    x = np.linspace(0, 1, 10)
    y = poly.polyval(x, beta0)

    sxx = np.var(x)
    sxy = np.cov(np.append(x, x.mean()), np.append(y, y.mean()))[0][1]

    hat_beta_1 = sxy / sxx
    hat_beta_0 = y.mean() - hat_beta_1 * x.mean()

    xp = np.linspace(0, 3, 100)
    yp0 = poly.polyval(xp, beta0)
    hat_yp = hat_beta_0 + hat_beta_1 * xp

    plt.plot(xp, yp0, label = 'True')
    plt.plot(xp, hat_yp, label = 'Estimate')
    plt.scatter(x, y, label = 'Trainning')
    plt.legend()
    plt.xlim([0, 3])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('plot.png')

if __name__ == '__main__':
    main()
