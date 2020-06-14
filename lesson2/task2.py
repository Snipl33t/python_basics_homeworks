# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You should enter the list of arbitrary length with spaces as delimiters.
After that the elements are going to be swapped and displayed as a list.\n"""

# Greet user
print(welcome_string)

# Ask user to enter the list with space as delimiters (e.g.: 1 2 3 4 5 6 7)
my_list = input("Enter the list with spaces as delimiters: ").split(" ")

# For each index in from 1 to the length of the list with step 2
for idx in range(1, len(my_list), 2):
    # Swap the elements
    my_list[idx - 1], my_list[idx] = my_list[idx], my_list[idx - 1]

# Print the result
print("Result: ", my_list)
