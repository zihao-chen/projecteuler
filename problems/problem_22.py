"""

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

import pkg_resources


def read_file():
    txt = pkg_resources.resource_string("resources", "problem_22.txt").decode("utf-8")
    txt = txt.replace('"', "")
    names = txt.split(",")
    names.sort()
    return names


def name_value(name):
    return sum(ord(i) - 64 for i in name)


if __name__ == '__main__':
    name_list = read_file()
    working_list = (list(enumerate(name_list, 1)))
    print(sum(index * name_value(name) for index, name in working_list))
