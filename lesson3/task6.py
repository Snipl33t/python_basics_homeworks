# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

The function outputs a capitalized string.
Initial string:

this is a lower case string and now every word is capitalized

Output:\n"""


def int_func(func_str) -> str:
    # Split by spaces
    func_list = func_str.split(' ')
    # Capitalize each element of the list and then join with spaces and output
    return ' '.join(list(map(lambda x: x.capitalize(), func_list)))


# Greet user
print(welcome_string)

# Use the function
print(int_func("this is a lower case string and now every word is capitalized"))
