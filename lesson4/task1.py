"""
This program allows user to calculate employee's salary by using the console and writing working hours, tariff and bonus
"""

from sys import argv

hours, tariff, bonus = map(int, argv[1:])

print(f"Employee's salary is {hours * tariff + bonus}")
