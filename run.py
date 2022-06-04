from typing import Dict
import time

cache: Dict[int, int] = {}


def fibonacci_cache(N):
    if N <= 1:
        return N
    if N not in cache:
        cache[N] = fibonacci_cache(N - 1) + fibonacci_cache(N - 2)
    return cache[N]


start = time.time()
print(fibonacci_cache(33))
end = time.time()
print("With cache: %s seconds" % (end - start))


def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N - 1) + fibonacci(N - 2)


start = time.time()
print(fibonacci(33))
end = time.time()
print("Without cache: %s seconds" % (end - start))


def fibonacci_nocache(N):
    if N <= 1:
        return N
    two_ago, one_ago = 0, 1
    for n in range(0, N):
        current = one_ago + two_ago
        two_ago = one_ago
        one_ago = current
    return two_ago


print(fibonacci_nocache(33))
