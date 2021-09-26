# Реализовать класс Road(дорога).  определить атрибуты: length(длина), width(ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными; определить метод расчёта массы асфальта, необходимого
# для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв.метра дороги
# асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self, weight=25, thikness=5):
        print(f"масса асфальта - {self._length * self._width * 25 * 5 / 1000} тонн")


def main():
    while True:
        try:
            road_1 = Road(int(input("Ширина дороги: ")), int(input("Длина дороги: ")))
            road_1.mass_calc()
            break
        except ValueError:
            print("Only integer!")


if __name__ == "__main__":
    main()
