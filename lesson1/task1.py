# Initialize variables
var_int = 256
var_float = 1.354
var_string = 'Hello world!'
var_bool = True

# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

In this task I would like you to enter different types of variables.
They will be displayed just before the program ends.
The initialized variables are provided below:\n"""
init_vars_string = f'Integer variable = {var_int}\nFloat variable = {var_float}\nString variable = {var_string}\nBoolean variable = {var_bool}\n'

# Greet user and display variables
print(welcome_string)
print(init_vars_string)

# Ask user to enter integer variables
print("Now it's your turn to enter variables!")

# Receive an integer value from user and put it in user_int1
user_int1 = input("Please enter an integer variable: ")

# Check if user typed an integer value. If not, then ask again
while not user_int1.isdigit():
    user_int1 = input("Please, enter an integer variable! Should be a simple number\n")

# After the checking process we can safely make a string into integer
user_int1 = int(user_int1)

# Receive an integer value from user and put it in user_int2
user_int2 = input("Please enter another integer variable: ")

# Check if user typed an integer value. If not, then ask again
while not user_int2.isdigit():
    user_int2 = input("Please, enter an integer variable! Should be a simple number\n")

# After the checking process we can safely make a string into integer
user_int2 = int(user_int2)

# Receive an float value from user and put it in user_float1
user_float1 = input("Please enter a float variable: ")
# TODO: find out from future python basics courses on how can I parse the float value from string

# After the checking process we can safely make a string into float
user_float1 = float(user_float1)

# Receive an float value from user and put it in user_float2
user_float2 = input("Please enter another float variable: ")
# TODO: find out from future python basics courses on how can I parse the float value from string

# After the checking process we can safely make a string into float
user_float2 = float(user_float2)

# Receive an string from user and put it in user_string1
user_string1 = input("Please enter a string: ")

# Receive an string from user and put it in user_string2
user_string2 = input("Please enter another string: ")

# Display user variables
user_vars_string1 = f'Int variable 1 = {user_int1}\nFloat variable 1 = {user_float1}\nString variable 1 = {user_string1}\n'
user_vars_string2 = f'Int variable 2 = {user_int2}\nFloat variable 2 = {user_float2}\nString variable 2 = {user_string2}\n'
print("\nThank you! These are the variables you've typed:\n\n" + user_vars_string1 + user_vars_string2)
