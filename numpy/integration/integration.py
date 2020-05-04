import numpy as np
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


@timing
def integrate(y, delta_x, a, b):
	vect_x = np.arange(a,b,delta_x)

	x = vect_x
	x_min_1     = x[0:-1]
	x_mid_point = (x[1:]+x_min_1)/2

	integral = np.sum(y(x_mid_point)*delta_x)
	print(integral)
	return integral

if __name__=="__main__":

	delta_x = 0.0000001
	a = 0
	b = np.pi/2
	# sin_a = np.sin(vect_x)

	integrate(y=np.sin, delta_x = delta_x,a=a, b=b)