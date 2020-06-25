"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('task5.txt', 'w', encoding='UTF-8') as file:
    file.write('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16')

with open('task5.txt', 'r', encoding='UTF-8') as file:
    file_list = [(lines.strip().split()) for lines in file]

file_list = list(map(int, file_list[0]))
print(sum(file_list))
