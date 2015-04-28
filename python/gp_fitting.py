import math
import numpy
import matplotlib.pyplot as plt
 
n = 100
ns = 8
 
theta0 = 1.0
theta1 = 50.0
theta2 = 0.0
theta3 = 0.0
 
beta = 2.0
 
def func(x):
    return math.sin(x * 4.0)
 
def covariance_func(xi, xj):
    return theta0 * math.exp(-0.5 * theta1 * (xi - xj) * (xi - xj)) + theta2 + theta3 * xi * xj
 
def main():
    # plot ground truth
    xs = [(x * 1.0 / n) * 2.0 - 1.0 for x in range(n)]
    ys = [func(x) for x in xs]
    plt.plot(xs, ys)
 
    # generate observation
    xt = [(x * 1.0 / ns) * 2.0 - 1.0 for x in range(ns)]
    yt = [func(x) + numpy.random.normal() * 0.1 for x in xt]
    plt.scatter(xt, yt, color='r')
 
    # construct covariance
    cov = numpy.zeros((ns, ns))
    for i in range(ns):
        for j in range(ns):
            cov[i][j] = covariance_func(xt[i], xt[j])
            if i == j:
            	cov[i][j] = cov[i][j] + 1 / beta
    i_cov = numpy.linalg.inv(cov)
 
    y_lo = [0.0] * n
    y_mi = [0.0] * n
    y_hi = [0.0] * n
    tt = [y - numpy.random.normal() / beta for y in yt]
    for k in range(n):
        v = numpy.zeros((ns))
        for i in range(ns):
            v[i] = covariance_func(xs[k], xt[i])
        c = covariance_func(xs[k], xs[k]) + 1.0 / beta
        mu = numpy.dot(v, numpy.dot(i_cov, tt))
        sigma = c - numpy.dot(v, numpy.dot(i_cov, v))
 
        y_lo[k] = mu - sigma * 2.0
        y_mi[k] = mu
        y_hi[k] = mu + sigma * 2.0
 
    plt.plot(xs, y_lo, 'g--')
    plt.plot(xs, y_mi, 'g-')
    plt.plot(xs, y_hi, 'g--')
 
    plt.xlim([-1.2, 1.2])
    plt.ylim([-5.0, 5.0])
    plt.show()
 
 
if __name__=='__main__':
    main()