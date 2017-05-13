"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""


def check_pattern(n, pattern='1234567890'):
    return "".join(str(n)[::2]) == pattern


if __name__ == '__main__':
    end_point = 1929394959697989990
    start_point = 1020304050607080900
    for i in range(int(start_point ** 0.5) // 10 * 10, int(end_point ** 0.5) + 1, 10):
        if check_pattern(i ** 2):
            print(i)
            break
        else:
            i += 1
