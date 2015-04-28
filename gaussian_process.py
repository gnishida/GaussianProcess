import numpy
import math
import matplotlib.pyplot as plt
 
n = 100
theta0 = 1.0
theta1 = 16.0
theta2 = 0.0
theta3 = 0.0

def covariance_func(xi, xj):
    return theta0 * math.exp(-0.5 * theta1 * (xi - xj) * (xi - xj)) + theta2 + theta3 * xi * xj
 
def main():
    # sample n random variables
	xs = numpy.array([(x * 1.0 / n) * 2.0 - 1.0 for x in range(n)])
	print xs

	# compute covariance matrix
	color = ['r', 'g', 'b', 'c', 'm']
	for c in color:
		cov = numpy.zeros((n, n))
		for i in range(n):
			for j in range(n):
				cov[i][j] = covariance_func(xs[i], xs[j])

		# draw y from multivariate gaussian
		z = numpy.zeros((n))
		ys = numpy.random.multivariate_normal(z, cov)

		plt.plot(xs, ys, color=c)

	plt.xlim([-1.0, 1.0])
	plt.ylim([-3.0, 3.0])
	plt.show()


if __name__=='__main__':
    main()