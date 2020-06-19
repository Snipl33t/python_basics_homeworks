# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You should enter two numbers. The program is going to divide them by one another.\n"""


def my_division(dividend: int, divider: int) -> int or float:
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("You divided by zero, so assume the answer is infinity")
        # As we didn't use any libraries yet - the result is just a large number
        return 10 ** 500


# Greet user
print(welcome_string)

# Ask user to enter numbers
while True:
    try:
        user_in1 = int(input("Enter your dividend "))
        user_in2 = int(input("Enter your divider "))
        break
    except ValueError:
        print("You should enter an integer number!")

# Print the result
print("Result: ", my_division(dividend=user_in1, divider=user_in2))
