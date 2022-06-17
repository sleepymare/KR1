import string
import json
import re
from statistics import mean


def fact(x):
    if x > 1:
        return x * fact(x - 1)
    else:
        return 1


def filter_even(li):
    return list(filter(lambda x: x % 2 == 0, li))


def square(li):
    return list(map(lambda x: x * x, li))


def bin_search(li, element):
    low = 0
    high = len(li) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if li[mid] == element:
            return mid
        elif li[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def is_palindrome(my_string):
    new_str = ""
    reverse_str = ""

    for x in my_string.strip():
        new_str = new_str + x.replace(" ", "")
        reverse_str = x.replace(" ", "") + reverse_str

    new_str = new_str.translate(str.maketrans('', '', string.punctuation))
    reverse_str = reverse_str.translate(str.maketrans('', '', string.punctuation))

    new_str = ''.join([i for i in new_str if not i.isdigit()])
    reverse_str = ''.join([i for i in reverse_str if not i.isdigit()])

    if new_str.lower() == reverse_str.lower():
        print("YES")
    else:
        print("NO")


def calculate(path2file):
    given_file = open(path2file, 'r')
    result = ''
    lines = given_file.readlines()

    for line in lines:
        arr = line.split()
        num = eval(f'{arr[1]}{arr[0]}{arr[2]}')
        result += str(num) + ','

    given_file.close()

    return result[:len(result) - 1]


def substring_slice(path2file_1, path2file_2):
    given_file1 = open(path2file_1, 'r')
    given_file2 = open(path2file_2, 'r')
    result = ''
    lines1 = given_file1.readlines()
    lines2 = given_file2.readlines()

    for x in range(len(lines1)):
        arr = lines2[x].split()
        result += lines1[x][int(arr[0]):int(arr[1]) + 1] + ' '

    given_file1.close()
    given_file2.close()

    return result[:len(result) - 1]


def decode_ch(string_of_elements):
    with open("periodic_table.json", encoding='utf-8') as read_file:
        periodic_table = json.load(read_file)

    result = ''
    arr = re.findall('[A-Z][^A-Z]*', string_of_elements)
    for elem in arr:
        result += periodic_table[elem]
    return result


class Student:
    def __init__(self, name, surname, fullname, list_of_grades=None):
        if list_of_grades is None:
            list_of_grades = [3, 4, 5]
        self.list_of_grades = list_of_grades
        self.name = name
        self.surname = surname
        self.fullname = fullname

    def greetings(self):
        print("Hello I am", self.fullname)

    def mean_grade(self):
        return mean(self.list_of_grades)

    def is_otl(self):
        if self.mean_grade() > 4.5:
            print("YES")
        else:
            print("NO")

    def print(self):
        print(self.fullname)

    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'
