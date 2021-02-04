# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

In this task I would like you to enter variable n.
The output is calculated by the formula (if it can be called like that):
n + nn + nnn (e.g. 3 + 33 + 333 = 369).\n"""

# Greet user
print(welcome_string)

# Ask user to enter variable n
n = input("Enter an integer n: ")

# Check if user typed an integer value. If not, then ask again
while not n.isdigit():
    n = input("Please, enter an integer variable! Should be a simple number\n")

# Calculate result according to the "formula"
argument1 = int(n)
argument2 = int(n + n)
argument3 = int(n + n + n)
result = argument1 + argument2 + argument3

# Display result
print(f'The result is: {result}')
