# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You should enter a number from 1 to 12.
The program will determine which season is it.\n"""

# Greet user
print(welcome_string)

# Ask user to enter a month as a number
user_input = input("Enter a month as a number (1 - 12): ")

# Check if user typed an integer value and is in range [1:12]. If not, then ask again
while not (user_input.isdigit() and (0 < int(user_input) <= 12)):
    user_input = input("Please, enter a number between 1 and 12! ")

# After the checking process we can safely make a string into integer
user_input = int(user_input)

# Define a list with 5 strings, each index corresponds to a season number - 1
my_list = ['winter', 'spring', 'summer', 'autumn']

# Define a dictionary such that the keys are the corresponding season number - 1
my_dict = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn'}

# Print the result
print(f'Dictionary solution: month number {user_input} is {my_dict[user_input // 3 % 4]}.')
print(f'List solution: month number {user_input} is {my_list[user_input // 3 % 4]}.')
