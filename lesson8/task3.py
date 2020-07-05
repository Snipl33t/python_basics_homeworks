"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyDigitsError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    user_list = []
    while True:
        user_var = input('Enter integer for a list, enter "stop" to exit: ')
        if user_var != 'stop':
            try:
                if user_var.isdigit():
                    user_list.append(int(user_var))
                else:
                    raise OnlyDigitsError('Only integer values can be added to this list!')
            except OnlyDigitsError as e:
                print(e)
        else:
            break

    print(f'Final list is: {user_list}')
