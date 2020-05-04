import numpy 
from functools import wraps
from time import time
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % \
          (f.__name__, te-ts))
        return result
    return wrap

# The expression is enclosed in quotes and will be evaluated using a single C-loop. 
# Speed-ups in comparison to NumPy are typically between 0.95 and 4. 
# Performance improves normaly most with arrays that do not fit in CPU cache.

import numexpr

@timing
def evaluate(x_values):
	x = x_values
	poly = numexpr.evaluate("((.25*x + .75)**x - 1.5)*x**2")

	return poly

@timing
def normal_expression(x_values):
	poly = ((.25*x_values + .75)**x_values - 1.5)*x_values**2
	return poly

if __name__=="__main__":

	x = numpy.random.random((10000000, 5))
	y = numpy.random.random((10000000, 5))

	polyx = evaluate(x)
	polyx_2 = normal_expression(x)

