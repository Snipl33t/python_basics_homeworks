# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

In this task I would like you to enter any integer.
The output is the maximum number from this integer (e.g. i = 523 => max = 5).\n"""

# Greet user
print(welcome_string)

# Ask user to enter variable n
user_var = input("Enter an integer n: ")

# Check if user typed an integer value. If not, then ask again
while not user_var.isdigit():
    user_var = input("Please, enter an integer variable! Should be a simple number\n")

# After the checking process we can safely make a string into integer
user_var = int(user_var)

# Initially set max_var to zero for the initial comparison
max_var = 0

# While user_var is bigger then zero do the following
while user_var > 0:
    # get current digit and write it in cur_var
    cur_var = user_var % 10

    # if current variable is bigger then maximum variable
    if cur_var > max_var:
        # then overwrite the maximum variable with current one
        max_var = cur_var

    # as the code has processed current digit - decrease user_var by one digit
    user_var //= 10

# Display results
print(f'Maximum digit is: {max_var}')
