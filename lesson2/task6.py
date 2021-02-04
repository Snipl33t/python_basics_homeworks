# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You are going to be asked specific parameters of different things (like name, amount, etc).
The structure that you made will be outputted as well as the products analytics.\n"""

# Greet user
print(welcome_string)

# Initialize variables
my_dict_list = []
user_answer = 0

while user_answer != 'N':
    user_answer = 0

    # Ask user to enter the name
    name = input("Enter product name: ")

    # Ask user to enter the price
    price = input("Enter product price: ")
    # Check if user typed an integer value. If not, then ask again
    while not price.isdigit():
        price = input("Please, enter a real number! ")
    # After the checking process we can safely make a string into integer
    price = int(price)

    # Ask user to enter the amount
    amount = input("Enter product amount: ")
    # Check if user typed an integer value. If not, then ask again
    while not amount.isdigit():
        amount = input("Please, enter a real number! ")
    # After the checking process we can safely make a string into integer
    amount = int(amount)

    # Ask user to enter the units
    units = input("Enter product units: ")

    # Append the dictionary to list
    my_dict_list.append({"name": name, "price": price, "amount": amount, "units": units})

    # If user wants to continue - type 'Y', otherwise type 'N'
    while not (user_answer == 'Y' or user_answer == 'N'):
        user_answer = input("Continue? Y/N: ")

# Numerate the list, turn it to tuple and make a list of tuples
my_tuple_list = list(enumerate(my_dict_list, 1))

print(f'Final structure: {my_tuple_list}\n')

# # Debug
# my_tuple_list = [
# (1, {"name": "Computer", "price": 20000, "amount": 5, "units": "pieces"}),
# (2, {"name": "Printer", "price": 2123, "amount": 15, "units": "pieces"}),
# (3, {"name": "Scanner", "price": 4000, "amount": 50, "units": "pieces"})
# ]

# Create a new dictionary with keys same as in the previous dictionary and with elements as lists
my_dict_output = {}
for key in my_tuple_list[0][1]:
    my_dict_output[key] = []

# For each tuple in my_tuple_list
for itm in my_tuple_list:
    # For each key in my_dict_output
    for key in my_dict_output:
        # Write in my_dict_output by key to the corresponding list the values
        my_dict_output[key].append(itm[1][key])

print(f'Products analytics: {my_dict_output}')
