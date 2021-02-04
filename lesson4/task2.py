"""
Program takes list and makes another list of i-th elements, which satisfy the condition i > i-1
"""

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Iterate through 2 lists simultaneously, 1 list is a regular input list, another starts from 1st element and hence the
# values can be compared in a for loop
output_list = [itm2 for itm1, itm2 in zip(my_list, my_list[1:]) if itm2 > itm1]

# Print the list
print(output_list)
