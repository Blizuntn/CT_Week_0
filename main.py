# Question 1
# This function will take a name and print out a greeting

def hello_name(user_name):
    print("hello_" + user_name.upper())


hello_name("Michael")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds():
    for i in range(1, 100):
        if i % 2 == 1:
            print(i)


first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list


def max_num_in_list(a_list):
    return (max(a_list))


max_num_in_list([1, 34, 99, 56, 26, 203])

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400.


def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
        if a_year % 100 == 0:
            return False
            if a_year % 400 == 0:
                return True
    else:
        return False


is_leap_year(2036)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.import random


def is_consecutive(a_list):
    new_list = sorted(a_list)
    if new_list == list(range(min(new_list), max(new_list) + 1)):
        return True
    else:
        return False


is_consecutive(list(range(1, 100, 1)))
