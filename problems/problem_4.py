"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindromic(n):
    str_n = str(n)
    middle = len(str_n) // 2
    return all(str_n[i] == str_n[-(i + 1)] for i in range(middle + 1))


def largest_palindrome(n=3):
    x = int('9' * n)
    y = int('1' + '0' * (n - 1))
    current_max = 0
    previous_j = 0
    for i in range(x - y + 1):
        for j in range(x - y + 1):
            p = (x - i) * (x - j)
            if is_palindromic(p):
                if x - i <= previous_j:
                    return p, previous_j, int(p / previous_j)
                if current_max < p:
                    current_max = p
                    previous_j = x - j
                    break


if __name__ == '__main__':
    print(largest_palindrome(2))
    print(largest_palindrome(3))
