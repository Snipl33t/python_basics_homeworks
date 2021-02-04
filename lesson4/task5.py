"""
Program makes an array with even values in range [100, 1000] and return multiplication of each element
"""

from functools import reduce

# Create a list from given range with even values
my_list = [itm for itm in range(100, 1001) if not itm & 1]

# Calculate the multiplication of each value by another
result = reduce(lambda x, y: x * y, my_list)

# Print the result
print(f'List: {my_list}\nResult: {result}')
