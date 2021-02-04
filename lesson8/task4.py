"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
"""


class OnlyDigitsError(Exception):
    def __init__(self, txt):
        self.txt = txt


class NoProductsError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Stock:
    def __init__(self, name):
        self.name = name
        self.__stock_dict = {}

    def __getitem__(self, item):
        try:
            return self.__stock_dict[item]
        except KeyError as e:
            raise TypeError('Key error')

    def __str__(self):
        out_str = ''
        test1 = self.__stock_dict
        for key, itm in self.__stock_dict.items():
            out_str += f'{len(self.__stock_dict[key])} {key}, '
        return f'{self.name} contains: {out_str[0:-2]}'

    @property
    def equipment(self):
        return self.__stock_dict

    def add(self, *args):
        if type(args[0]) is list:
            args = args[0]
        for obj in args:
            dict_key = obj.__class__.__name__
            if dict_key in self.__stock_dict:
                self.__stock_dict[dict_key].append(obj)
                if not self.__stock_dict[dict_key]:
                    self.__stock_dict.pop(dict_key)
            else:
                self.__stock_dict[dict_key] = []
                self.__stock_dict[dict_key].append(obj)
        print(f'Added {len(args)} device{"s" if len(args) != 1 else ""} to {self.name}')

    def move(self, other, *args):
        for obj in args:
            dict_key = obj.__class__.__name__
            device_type_objects = self.__stock_dict[dict_key]
            is_not_in_stock = True
            for idx, itm in enumerate(device_type_objects):
                if itm.brand is obj.brand and itm.model is obj.model:
                    other.add(self.__stock_dict[dict_key].pop(idx))
                    if not self.__stock_dict[dict_key]:
                        self.__stock_dict.pop(dict_key)
                    is_not_in_stock = False
            if is_not_in_stock:
                print(f'{obj.__class__.__name__} {obj.brand} {obj.model} is not in this stock')
            else:
                print(f'Moved {len(args)} device{"s" if len(args) != 1 else ""} from {self.name} to {other.name}')

    def move_amount(self, device, other):
        device_type_objects = self.__stock_dict[device]
        while True:
            amount = input(f'Enter the amount of devices "{device}" you would like to move from {self.name} to {other.name}: ')
            try:
                if amount.isdigit():
                    amount = int(amount)
                    break
                else:
                    raise OnlyDigitsError('Please enter an integer!')
            except OnlyDigitsError as e:
                print(e)
        try:
            if not len(device_type_objects):
                raise NoProductsError(f'Unfortunately, there are no devices "{device}" at {self.name}')
            elif amount > len(device_type_objects):
                amount = len(device_type_objects)
                print(f'Warning! The amount of devices at {self.name} is only {len(device_type_objects)}! Moving everything it has.')
            other.add([self.__stock_dict[device].pop() for i in range(0, amount)])
            if not self.__stock_dict[device]:
                self.__stock_dict.pop(device)
        except NoProductsError as e:
            print(e)

    def remove(self, *args):
        counter = len(args)
        for i in range(0, len(args)):
            dict_key = args[i].__class__.__name__
            try:
                self.__stock_dict[dict_key].remove(args[i])
                if not self.__stock_dict[dict_key]:
                    self.__stock_dict.pop(dict_key)
            except KeyError as e:
                print("No such an item in this stock!")
                counter -= 1
        print(f'Removed {counter} device{"s" if counter != 1 else ""} from {self.name}')


class OfficeEquipment:
    __list = []
    __dict = {}

    def __init__(self, brand, model):
        self.__list.append(self)
        self.brand = brand
        self.model = model

    @property
    def equipment_list(self):
        return self.__list[:]

    @property
    def equipment_dict(self):
        return self.__dict

    @equipment_dict.setter
    def equipment_dict(self, *args):
        dict_key = self.__class__.__name__
        if dict_key in self.__dict:
            self.__dict[dict_key].append(*args)
        else:
            self.__dict[dict_key] = []
            self.__dict[dict_key].append(*args)

    @classmethod
    def __class_getitem__(cls, item):
        try:
            return cls.__list[item]
        except TypeError as e:
            pass

        try:
            return cls.__dict[item]
        except KeyError as e:
            raise TypeError('Index error or Key error')

    def name_yourself(self):
        print(f"{self.__class__.__name__}: {self.brand} {self.model}")


class Printer(OfficeEquipment):
    def __init__(self, name, model, color, print_type):
        super().__init__(name, model)
        self.equipment_dict = [name, model, color, print_type]
        self.color = color
        self.type = print_type


class Scanner(OfficeEquipment):
    def __init__(self, name, model, scan_type):
        super().__init__(name, model)
        self.equipment_dict = [name, model, scan_type]
        self.scan_type = scan_type


class Xerox(OfficeEquipment):
    def __init__(self, name, model, xerox_type):
        super().__init__(name, model)
        self.equipment_dict = [name, model, xerox_type]
        self.xerox_type = xerox_type


# Two stocks
main_stock = Stock("Main stock")
stock1 = Stock("Subdivision 1")
stock2 = Stock("Subdivision 2")

# Init various devices
printer1 = Printer('HP', 'LaserJet Pro M 12', 'RGB', 'stationary')
printer2 = Printer('HP', 'DeskJet 2630', 'BW', 'stationary')
printer3 = Printer('Brother', 'L3730CDN', 'BW', 'stationary')
scanner = Scanner('Fujitsu', 'ScanSnap S1100', 'stationary')
xerox = Xerox('Xerox', 'WorkCentre 6515DNI', 'stationary')

scanner.name_yourself()

main_stock.add(printer1, printer2, printer3, scanner, xerox)

main_stock.move(stock1, scanner, printer1)

main_stock.move_amount('Printer', stock2)

stock1.remove(xerox)

print(main_stock)
print(stock1)
print(stock2)
