"""
User enters a factorial he would like to calculate and the function calculates all the factorial in between as well
"""

from math import factorial


def fact(func_var: int):
    for itm in [el for el in range(1, func_var + 1)]:
        yield factorial(itm)  # next time called it will give this value


while True:
    try:
        n = int(input("Enter the desired factorial: !"))
        break
    except ValueError:
        print('Enter an integer!')
for el in fact(n):
    print(el)
