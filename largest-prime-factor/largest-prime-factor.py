# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def largest_prime_factor(number=None):
    if number is None:
        number = 600851475143

    # We only need to go up to the square root of the number
    # It's the largest number that could possibly be a factor
    sqrt = math.ceil(math.sqrt(number))
    largest = -1

    # Assemble a set of primes to iterate over
    # We'll also store a set so we don't need to search the list
    primes = []
    print("Assembling Primes...")

    # Assemble list of primes (takes some time)
    for n in range(2, sqrt):

        # Check if any of the current primes divide the number
        is_prime = True
        for prime in primes:
            if n % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(n)

    # Go through primes, find largest divisor
    for prime in primes:
        if number % prime == 0:
            largest = prime

    # If we don't have a largest prime
    if largest == -1:
        print("There is no largest prime.")
    else:
        print("The largest prime is %s" % largest)
