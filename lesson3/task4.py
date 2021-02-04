# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

The function outputs x^y.\n"""


def my_func1(x, y):
    if y >= 0:
        raise ValueError
    i = 1
    val = 1 / x
    while i < abs(y):
        val *= 1 / x
        i += 1
    return val


def my_func2(x, y):
    if y >= 0:
        print('y should be negative!')
        return 0
    return x ** y


# Greet user
print(welcome_string)

# Ask user to enter variables with spaces as delimiters
while True:
    try:
        user_x = int(input("Enter x: "))
        user_y = int(input("Enter power y, negative variable: "))
        # Print the data
        print(f'x^y without using ** = {my_func1(user_x, user_y)}')
        print(f'x^y using ** = {my_func2(user_x, user_y)}')
        break
    except ValueError:
        print('You should enter integer values! x is positive, y is negative!')
    except TypeError:
        print("You should enter only 2 numbers!")
