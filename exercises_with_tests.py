"""
Тема 13. Функции map, filter, reduce, any, all.

1. You will be implementing a basic case of the map-reduce pattern in programming. Given a vector stored as a list of
 integers, find the magnitude of the vector. Use the standard distance formula for n-dimensional Cartesian coordinates.
Source: https://edabit.com/challenge/sMtSzctTWs766rRL8

2. Create a function that takes a list and returns a new list containing only prime numbers.
Source: https://edabit.com/challenge/yXZhG7zq6dWhWhirt

3. Create a function that returns the indices of all occurrences of an item in the list.
Source: https://edabit.com/challenge/jwzgYjymYK7Gmro93

"""

from functools import *


# Exercise 1.
def add_elements(elem1, elem2):
    return elem1 + elem2


def magnitude(lst):
    squares_list = map(lambda x: x * x, lst)
    return reduce(add_elements, squares_list, 0) ** 0.5


# Exercise 2.
def is_prime(n):
    if n < 2:
        return False
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return True


def filter_primes(num):
    return list(filter(is_prime, num))


# Exercise 3.
def get_indices(lst, el):
    list1 = []
    for i in range(len(lst)):
        list1.append(el == lst[i])

    if all(list1):
        return list(range(0, len(lst)))

    if not any(list1):
        return []

    arr = []
    for i in range(len(lst)):
        if list1[i]:
            arr.append(i)

    return arr


# Tests.
def test_problem(func, test_data):
    """test helper"""
    for inputs, true_answer in test_data:
        if isinstance(inputs, tuple):
            answer = func(*inputs)
        else:
            answer = func(inputs)
        if answer != true_answer:
            print("wrong")
            return 0
    return 1


def test_magnitude(magnitude_func):
    test_data = [
        ([3, 4], 5),
        ([0, 0, -10], 10),
        ([], 0),
        ([2, 3, 6, 1, 8], 10.677078252031311),
        ([9, -9, 3], 13.076696830622021),
        ([-24, 94, 4, 0, 10], 97.61147473529944)

    ]
    return test_problem(magnitude_func, test_data)


def test_filter_primes(filter_primes_func):
    test_data = [
        ([7, 9, 3, 9, 10, 11, 27], [7, 3, 11]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
         [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        ([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097], [1009, 3, 61, 1087, 1091, 1093, 1097]),
        ([10007, 1009, 1007, 27, 147, 77, 1001, 70], [10007, 1009])

    ]
    return test_problem(filter_primes_func, test_data)


def test_get_indices(get_indices_func):
    test_data = [
        ((['a', 'a', 'b', 'a', 'b', 'a'], 'a'), [0, 1, 3, 5]),
        (([1, 5, 5, 2, 7], 7), [4]),
        (([1, 5, 5, 2, 7], 5), [1, 2]),
        (([1, 5, 5, 2, 7], 8), []),
        (([8, 8, 8, 8, 8], 8), [0, 1, 2, 3, 4]),
        (([True, False, True, False], True), [0, 2]),
        (([True, False, True, False], False), [1, 3])

    ]
    return test_problem(get_indices_func, test_data)


if test_magnitude(magnitude):
    print("Все тесты magnitude пройдены")

if test_filter_primes(filter_primes):
    print("Все тесты filter_prime пройдены")

if test_get_indices(get_indices):
    print("Все тесты get_indices пройдены")
