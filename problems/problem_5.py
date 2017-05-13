"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce
from operator import mul

from problems.problem_3 import next_prime


def get_primes(n):
    results = []
    np = next_prime()
    while True:
        p = next(np)
        if p > n:
            return results
        results.append(p)


def smallest_multiple(n):
    primes = get_primes(n)
    product = reduce(mul, primes)
    for i in range(1, n + 1):
        if product % i:
            for j in primes:
                if not product * j % i:
                    product = product * j
                    break

    return product


if __name__ == '__main__':
    print(smallest_multiple(20))
