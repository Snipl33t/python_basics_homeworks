"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
"""

import json

# Read from a txt file and convert the lines into list of lists
with open('task7.txt', 'r', encoding='UTF-8') as file:
    file_list = [lines.strip().split() for lines in file]

# Define dictionary keys as first column of file_list
firm_dict = dict.fromkeys([itm[0] for itm in file_list])

# Set counters
sum_val = 0
average_count = 0

# For every firm in the list
for lines in file_list:
    # Make profit and expenses an integer
    lines[2] = int(lines[2])
    lines[3] = int(lines[3])

    # If there are expenses - write expenses in the list
    if lines[3]:
        firm_dict[lines[0]] = lines[3]
    # Else write profit in the list, calculate sum and increase counter
    else:
        firm_dict[lines[0]] = lines[2]
        sum_val += lines[2]
        average_count += 1

# Define a final list
dict_list = [firm_dict, {"average_profit": sum_val // average_count}]

# Output it into the file
with open('task7_json.txt', 'w', encoding='UTF-8') as file:
    json.dump(dict_list, file)
