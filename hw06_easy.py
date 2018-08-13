__author__ = 'Мишин Егор Олегович'
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print("\n Задача №1")

import math


class Triangle:        # Объявляем и описываем класс
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.ab = math.sqrt((x1-x2)**2 + (x1-y2)**2)  # Здесь е находим длины сторон
        self.bc = math.sqrt((x2-x3)**2 + (y2-y3)**2)
        self.ca = math.sqrt((x1-x3)**2 + (y1-y3)**2)

    def perimeter(self):
        self.perimeter = self.ab + self.bc + self.ca
        return self.perimeter

    def square(self):
        self.semiperimeter = self.perimeter / 2   # находим полупериметр
        self.square = math.sqrt(self.semiperimeter * (self.semiperimeter-self.ab) * (self.semiperimeter-self.bc) *
                                (self.semiperimeter-self.ca))    # По формуле Герона находим площадь
        return self.square

    def height(self):
        self.height = self.square * 2 / self.ab
        return self.height


#triangle1 = Triangle(1, 4, 2, 3, 5, 1)
triangle = Triangle(1, 1, 4, 1, 1, 5)

print('AB =', triangle.ab)
print('BC =', triangle.bc)
print('CA =', triangle.ca)
print('Периметр треугольника =', triangle.perimeter())
print('Площадь треугольника =', triangle.square())
print('Высота треугольника =', triangle.height())



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print("\n Задача №2")

class Trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.ab = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        self.bc = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        self.cd = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        self.da = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        self.ah = (self.da - self.bc) / 2
        self.height = math.sqrt(self.ab ** 2 - self.ah ** 2)


    def perimeter(self):
        self.perimeter = self.ab + self.bc + self.cd + self.da
        return self.perimeter

    def square(self):
        self.square = (self.bc + self.da) * self.height / 2
        return self.square

    def check(self):
        if self.ab == self.cd:
            return "Трапеция равнобокая"
        else:
            return "Трапеция не равнобокая"

trapeze = Trapeze(1,1,4,5,10,5,13,1)

print('\n AB = {},\n BC = {},\n CD = {},\n DA = {}'.format(trapeze.ab, trapeze.bc, trapeze.cd, trapeze.da))
print(trapeze.check())
print("Периметр трапеции равен ", trapeze.perimeter())
print("Площадь трапеции равна ", trapeze.square())
