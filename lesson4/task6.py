"""
1. Iterator, which generates numbers from 'start' to 'end' values
2. Iterator, which repeats list elements for set amount of times
"""

import itertools as it


def my_count(start: int = 0, stop: int = 10):
    """
    Prints values from 'start' until 'stop'
    :param start: starting value of the list
    :param stop: last value of list
    """
    for itm in it.count(start):
        if itm > stop:
            break
        else:
            print(itm)


def my_cycle(func_list: list, stop: int = 3):
    """
    Prints values from list in a cycle
    :param func_list: desired list to be repeated
    :param stop: number of times the list should be repeated
    """
    print(len(func_list))
    for idx, itm in enumerate(it.cycle(func_list)):
        if idx >= stop * len(func_list):
            break
        else:
            print(itm)


# Print variables for task 1
my_count()

# Define a list and print variables for task 2
my_list = ['I', 'am', 'looped', 1, 2, 3]
my_cycle(my_list, 1)
