# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You should enter the arbitrary string with spaces as delimiters.
After that the elements the elements of the string will be separated in spaces, numerated and outputted.
The string is cropped if bigger then 10.\n"""

# Greet user
print(welcome_string)

# Ask user to enter a string with spaces as delimiters
user_list = input("Enter a string with spaces as delimiters: ").split(" ")

# Print the result
print("\nThe output is:")
for idx, itm in enumerate(user_list, 1):
    print(f'{idx}. {itm[:10]}')
