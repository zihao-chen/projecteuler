"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from problems.problem_3 import is_prime


def next_prime(n):
    """Find prime number up to n"""
    i = 1
    known_prime = []
    while i < n:
        if is_prime(i, known_prime):
            known_prime.append(i)
            yield i
        i += 1


# TODO: slow as a snail
if __name__ == '__main__':
    np = next_prime(2000000)
    print(sum(np))
