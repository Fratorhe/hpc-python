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


from fib import fibonacci
@timing
def fib_python(n):
    fibonacci(n)

from fib_c import fibonacci as fibonacci_c
@timing
def fib_c(n):
    fibonacci_c(n)

from fib_cached import fibonacci as fibonacci_cached
@timing
def fib_cached(n):
    fibonacci_c(n)

from solution.fib_py import fibonacci_cached
@timing
def fib_cached_solution(n):
    fibonacci_cached(n)

if __name__=="__main__":
    n = 30

    fib_python(n)
    fib_c(n)
    fib_cached(n)
    fib_cached_solution(n)