"""
Program calculates the amount of lines in the txt file and the amount of words in line.
"""

with open('task2.txt', 'r', encoding='UTF-8') as file:
    line_count = 0
    for line in file:
        print(f"Words in line: {len(line.split(' '))}")
        line_count += 1
    print(f'Lines: {line_count}')
