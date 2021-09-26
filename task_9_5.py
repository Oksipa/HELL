# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод
# должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title="Канцелярская принадлежность"):
        self.title = title

    def draw(self):
        print(f'Пробуй рисовать! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f"Пробуй рисовать при помощи ручки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Пробуй рисовать при помощи карандаша {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Пробуй рисовать при помощи маркера {self.title}")


stationery = Stationery()
stationery.draw()
pen = Pen("Паркер")
pen.draw()
pencil = Pencil("Кохинор")
pencil.draw()
handle = Handle("COPIC")
handle.draw()
