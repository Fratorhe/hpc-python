import timeit
import numpy

# the following code for calculating the difference of neighbouring elements in an array:

# brute force using a for loop
def brute_force():
	arr = numpy.arange(1000)
	dif = numpy.zeros(999, int)
	for i in range(1, len(arr)):
	    dif[i-1] = arr[i] - arr[i-1]


# can be re-written as a vectorised operation:

# vectorised operation
def vectorized():
	arr = numpy.arange(1000)
	dif = arr[1:] - arr[:-1]


if __name__=='__main__':

	print(timeit.timeit(stmt = brute_force, number = 10000))
	print(timeit.timeit(stmt = vectorized,  number = 10000))