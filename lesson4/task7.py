"""
User enters a factorial he would like to calculate and the function calculates all the factorial in between as well
"""


def fact(func_var: int):
    for itm in [el for el in range(1, func_var)]:
        func_var = func_var * itm
        yield func_var


while True:
    try:
        n = int(input("Enter the desired factorial: !"))
        break
    except ValueError:
        print('Enter an integer!')
for el in fact(n):
    print(el)
