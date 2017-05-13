"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def rearrange_digits(d):
    return "".join(sorted(str(d)))


if __name__ == '__main__':
    i = 10
    while True:
        two_i = i * 2
        three_i = i * 3
        four_i = i * 4
        five_i = i * 5
        six_i = i * 6
        if len(str(six_i)) > len(str(i)):
            i = six_i
        else:
            if rearrange_digits(two_i) == rearrange_digits(i) \
                    == rearrange_digits(three_i) == rearrange_digits(four_i) \
                    == rearrange_digits(five_i) == rearrange_digits(six_i):
                print(i)
                break
            i += 1
