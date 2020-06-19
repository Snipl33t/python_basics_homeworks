# This string provides a greeting message to a user and some basic instructions
# It is intentionally written in different lines for the ease of reading while being in the code editor
welcome_string = """Hello, user!

You should enter your personal info.\n"""


def data_storage(name, surname, year_of_birth, city, email, phone) -> str:
    return f'\nYour personal details:\n' \
           f'Name: {name}\nSurname: {surname}\nYear of birth: {year_of_birth}\nCity: {city}\nEmail: {email}\nPhone: {phone}'


# Greet user
print(welcome_string)

# Ask user to enter name
user_in1 = input("Enter your name ")

# Ask user to enter surname
user_in2 = input("Enter your surname ")

# Ask user to enter date of birth
user_in3 = input("Enter your date of birth ")

# Ask user to enter city
user_in4 = input("Enter your city ")

# Ask user to enter email
user_in5 = input("Enter your email ")

# Ask user to enter phone number
user_in6 = input("Enter your phone number ")

# print the data
print(data_storage(name=user_in1, surname=user_in2, year_of_birth=user_in3, city=user_in4, email=user_in5, phone=user_in6))
