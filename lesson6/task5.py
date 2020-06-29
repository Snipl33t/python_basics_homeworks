"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Используется для письма")


class Pencil(Stationery):
    def draw(self):
        print("Используется для рисования")


class Handle(Stationery):
    def draw(self):
        print("Используется для выделения текста")


pen = Pen("Ручка")
print(pen.title)
pen.draw()

pencil = Pencil("Карандаш")
print(pencil.title)
pencil.draw()

handle = Handle("Маркер")
print(handle.title)
handle.draw()
