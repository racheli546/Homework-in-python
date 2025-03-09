import time
from functools import wraps
from tabnanny import check


def timeit(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()
        total = end - start
        print(f'Function {function.__name__}{args} {kwargs} Took {total:.4f} seconds')
        return result
    return wrapper



def cache(function):
    cache_dict = {}
    @wraps(function)
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if(key not in cache_dict):
            cache_dict[key] = function(*args, *kwargs)
        return cache_dict[key]
    return wrapper


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1 )+ fibonacci(n-2)

@cache
def fibonacci_cached(n):
    if n<=1:
        return n
    return fibonacci(n-1 )+ fibonacci(n-2)

n= 35
print("Fibonacci without cache:")
timeit(fibonacci)(n)

print("\nFibonacci with cache:")
timeit(fibonacci_cached)(n)

print("\nFibonacci with cache again:")
timeit(fibonacci_cached)(n)