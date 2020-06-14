# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You should enter the arbitrary value, which will be placed in the list according to its value (rating).\n"""

my_list = [7, 5, 3, 3, 2]

# Greet user
print(welcome_string)
print(f"The initial list is {my_list}\n")

# Ask user to enter a number
user_input = input("Enter a rating element: ")

# Check if user typed an integer value. If not, then ask again
while not user_input.isdigit():
    user_input = input("Please, enter a real number! ")

# After the checking process we can safely make a string into integer
user_input = int(user_input)

# If user_input is in the list
if my_list.count(user_input):
    # then find index of the number from the end of the list
    idx = my_list[::-1].index(user_input)
    # insert user_input on the right of the found value
    my_list.insert(len(my_list) - idx, user_input)
else:
    # for each item in the list
    for itm in my_list:
        # if user_input is greater than item
        if user_input > itm:
            # find items index
            idx = my_list.index(itm)
            # insert user_input on that index
            my_list.insert(idx, user_input)
            break
        elif itm == my_list[-1]:
            # if item is equal to the last value of the list, then add user_input at the end of the list
            my_list.append(user_input)
            break

# Print the result
print(f"The resulting list is {my_list}")
