"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
"""


def parse_list(func_list: list) -> list:
    """
    Parses each element of list of lists of strings for numbers and turns them to integer
    :param func_list: list to parse
    :return: returns a list of lists of integers
    """
    temp_subj_list = []
    # For each subject
    for subjects in range(0, len(func_list)):
        temp_hours_list = []
        # For each hours in subject
        for list_str in func_list[subjects]:
            temp_str = ''
            # For each character in hour string
            for str_char in list_str:
                # If character is digit
                if str_char.isdigit():
                    # Combine the character with the previous character
                    temp_str += str_char
            # If the string is not empty write to the list of the current subject
            if temp_str:
                temp_hours_list.append(temp_str)
        # Write subjects hours to common list
        temp_subj_list.append(list(map(int, temp_hours_list)))
    return temp_subj_list


# Read from a txt file and convert the lines into list of lists
with open('task6.txt', 'r', encoding='UTF-8') as file:
    file_list = [lines.strip() for lines in file]

# Separate subject names from hours
file_list = [itm.split(': ') for itm in file_list]

# Put subject names into separate list
subject_list = [itm[0] for itm in file_list]

# Put hours into separate list
hours_list = [itm[1].split(' ') for itm in file_list]

# Parse the digits from hours list and receive a list
hours_list = parse_list(hours_list)

# Define keys for dictionary
subject_dict = dict.fromkeys(subject_list)

# Make a list of tuples from subjects and hours
subjects_hours_list = list(zip(subject_list, hours_list))

# Calculate the sum of each subject and put them into dictionary
for subject, hours in subjects_hours_list:
    subject_dict[subject] = sum(hours)

# Print the result
print(subject_dict)
