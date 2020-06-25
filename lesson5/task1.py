"""
Program creates a txt file with each line as a user input. Stops accepting the values if the string is empty.
"""

with open('task1.txt', 'w', encoding='UTF-8') as file:
    while True:
        user_input = input("Enter a line: ")
        if user_input == '':
            break
        file.write(f'{user_input}\n')
