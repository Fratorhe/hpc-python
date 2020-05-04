import numpy as np 
import matplotlib.pyplot as plt
import timeit 

# Construct 1D Numpy array containing the values of xi in the interval [0,π/2] with spacing Δx=0.1.
# Evaluate numerically the derivative of sin in this interval (excluding the end points) using the above formula. Try to avoid for loops. 
# Compare the result to function cos in the same interval.


def vectorized(plot=False):
	delta_x = 0.001
	a = np.arange(0,np.pi*1,delta_x)

	sin_a = np.sin(a)

	sin_a_plus = sin_a[2:]
	sin_a_minus = sin_a[:-2]
	# this is the cosine computed numerically
	der_sin = (sin_a_plus - sin_a_minus)/(2*delta_x)

	# this is the function cosine
	cos_a = np.cos(a)

	# this is to check the difference
	diff = cos_a[1:-1]-der_sin


	if plot:
		plt.plot(a[1:-1], der_sin, label = 'numerical')
		plt.plot(a, cos_a, label = 'analytical')

		plt.legend()
		plt.show()	


def brute_force(plot=False):
	delta_x = 0.001
	a = np.arange(0,np.pi*1,delta_x)
	sin_a = np.sin(a)

	sin_a_plus = sin_a[2:]
	sin_a_minus = sin_a[:-2]

	der_sin = np.zeros(len(a)-2)
	
	for i in range(len(a)-2):
		sin_a_plus = sin_a[i+2]
		sin_a_minus = sin_a[i]
		der_sin[i] = (sin_a_plus - sin_a_minus)/(2*delta_x)


if __name__=='__main__':

	print(timeit.timeit(stmt = brute_force, number = 10000))
	print(timeit.timeit(stmt = vectorized,  number = 10000))