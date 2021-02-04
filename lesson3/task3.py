# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

The function outputs the sum of two variables.\n"""


def my_func(x, y, z):
    my_list = [x, y, z]
    # Pop a maximum variable by finding its index
    max1 = my_list.pop(my_list.index(max(my_list)))
    # Pop again
    max2 = my_list.pop(my_list.index(max(my_list)))
    return max1 + max2


# Greet user
print(welcome_string)

# Ask user to enter variables with spaces as delimiters
while True:
    user_list = input("Enter 3 numbers with spaces as delimiters ").split(' ')
    try:
        user_list = list(map(int, user_list))
        # Calculate the sum
        sum_val = my_func(*user_list)
        # Print the data
        print(f'Sum of two maximum values is: {sum_val}')
        break
    except ValueError:
        print('You should enter integer values!')
    except TypeError:
        print("You should enter only 3 numbers!")
