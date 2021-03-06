"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from problems.problem_3 import next_prime

if __name__ == '__main__':
    n = 0
    np = next_prime()
    for _ in range(10001):
        n = next(np)
    print(n)
