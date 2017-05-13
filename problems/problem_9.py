"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def brute_force_solve(n):
    for a in range(n, 0, -1):
        for b in range(n - a, 0, -1):
            for c in range(n - b - a, 0, -1):
                if a + b + c == n and c ** 2 + b ** 2 == a ** 2:
                    return a, b, c


if __name__ == '__main__':
    print(brute_force_solve(12))
    print(brute_force_solve(1000))
