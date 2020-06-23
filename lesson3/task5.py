# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

The function outputs the total sum of numbers you enter until you enter 'q'.\n"""


def sum_func(func_sum=0):
    user_list = input("Enter numbers delimited with spaces, enter 'q' to quit: ").split(' ')
    if 'q' in user_list:
        user_list.remove('q')
        try:
            print(f'Final sum is: {func_sum + sum(list(map(int, user_list)))}')
        except ValueError:
            print(f'One of the numbers is incorrect! Final sum is: {func_sum}')
        finally:
    else:
        try:
            user_list = list(map(int, user_list))
            func_sum += sum(user_list)
        except ValueError:
            print('You should enter integer values!')
            return
        finally:
            print(f'Total sum is: {func_sum}')
            return sum_func(func_sum)


# Greet user
print(welcome_string)

# Use the function
sum_func()
