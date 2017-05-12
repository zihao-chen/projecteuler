"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def next_prime():
    """Find prime number up to n"""
    i = 1
    known_prime = []
    while True:
        if is_prime(i, known_prime):
            known_prime.append(i)
            yield i
        i += 1


def is_prime(n, known_prime):
    return n > 1 and all(n % i for i in known_prime)


def largest_prime(n):
    np = next_prime()
    i = next(np)
    limit = int(n ** 0.5)
    while i < limit:
        if not n % i:
            n = n / i
        else:
            i = next(np)
        if n <= i:
            return i


if __name__ == '__main__':
    print(largest_prime(13195))
    print(largest_prime(600851475143))
