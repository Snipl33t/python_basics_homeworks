"""
Program outputs the values which have no repetition in the input list
"""

inp_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_list = [itm for itm in inp_list if inp_list.count(itm) == 1]
print(my_list)
