"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

numbers_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'
}

# Read from a txt file and convert the lines into list of lists
with open('task4.txt', 'r', encoding='UTF-8') as file:
    file_list = [(lines.strip().split(' — ')) for lines in file]

with open('task4_output.txt', 'w', encoding='UTF-8') as file_output:
    for itm in range(0, len(file_list)):
        file_output.write(f'{numbers_dict[file_list[itm][0]]} - {file_list[itm][1]}\n')

# print(employees_list)

# # Convert salary to int
# for i in range(0, len(employees_list)):
#     employees_list[i][1] = int(employees_list[i][1])
#
# # Create a list of tuples out of the list
# employees_list = list(map(tuple, employees_list))
#
# # Convert this list of tuples into the dictionary
# employees_dict = dict((name, salary) for name, salary in employees_list)
#
# # Print the employees whose salary is lower then 20k rubbles
# for employee in employees_dict:
#     salary = employees_dict[employee]
#     if salary < 20000:
#         print(f'Employee {employee} has a salary, which is less then 20k rub: {salary} rubbles')
#
# # Calculate the average salary
# print(f'Average employee salary is: {sum(employees_dict.values()) / len(employees_dict.values())} rubbles')