# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You are going to be provided with a list of different types of data.
After that the type of each element will be displayed.\n"""

# Create a list with different types of variables
my_list = [1, 12, 1.42, True, "hello", False, 12.23, "Hey world", [1, 2, 4], {4, 8, 2}, (1, 3, 9)]

# Greet user
print(welcome_string)
print(f'The list: {my_list}')

# Check the type of each element of the list
for item in my_list:
    print(f'{item}\t-\t{type(item)}')
