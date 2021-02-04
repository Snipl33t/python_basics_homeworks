"""
Program reads from a txt file, first column of which contains an employees name and the second oen contains salary.
Program outputs which employees have a salary less then 20k rubbles and also calculates the average salary among them.
"""

# Read from a txt file and convert the lines into list of lists
with open('employees.txt', 'r', encoding='UTF-8') as file:
    employees_list = [(lines.strip().split()) for lines in file]

# Convert salary to int
for i in range(0, len(employees_list)):
    employees_list[i][1] = int(employees_list[i][1])

# Create a list of tuples out of the list
employees_list = list(map(tuple, employees_list))

# Convert this list of tuples into the dictionary
employees_dict = dict((name, salary) for name, salary in employees_list)

# Print the employees whose salary is lower then 20k rubbles
for employee in employees_dict:
    salary = employees_dict[employee]
    if salary < 20000:
        print(f'Employee {employee} has a salary, which is less then 20k rub: {salary} rubbles')

# Calculate the average salary
print(f'Average employee salary is: {sum(employees_dict.values()) // len(employees_dict.values())} rubbles')