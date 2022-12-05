import time
from functools import lru_cache

import redis
from redis_lru import RedisLRU

client = redis.Redis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n < 2:
        return n
    return n * factorial(n - 1)


@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


@lru_cache(maxsize=None)
def factorial_cache(n):
    if n < 2:
        return n
    return n * factorial_cache(n - 1)


def time_calculation():
    user_input = int(input('Enter a number: '))
    start_time = time.time()
    fibonacci(user_input)
    factorial(user_input)
    print(f'Fibonacci and factorial without cache: {(time.time() - start_time):.3f} seconds')

    start_time = time.time()
    fibonacci_cache(user_input)
    factorial_cache(user_input)
    print(f'Fibonacci and factorial with cache: {(time.time() - start_time):.3f} seconds')
