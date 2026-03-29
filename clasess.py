# -*- coding: utf-8 -*-

# ============================================================
# Задание 1
# Определите пустой класс с именем Facade.
# ============================================================

class Facade:
    pass


# ============================================================
# Задание 2
# Создайте экземпляр Facade и сохраните его в facade_1.
# ============================================================

facade_1 = Facade()


# ============================================================
# Задание 3
# 1. Вызовите type() для facade_1 и сохраните результат в facade_1_type.
# 2. Выведите facade_1_type.
# ============================================================

facade_1_type = type(facade_1)
print("Задание 3:", facade_1_type)


# ============================================================
# Задание 4
# Создайте класс Grade с переменной класса minimum_passing = 65.
# ============================================================

class Grade:
    minimum_passing = 65


# ============================================================
# Задание 5
# Создайте класс Rules и добавьте метод washing_brushes(),
# который возвращает нужную строку.
# ============================================================

class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


# ============================================================
# Задание 6
# 1. Создайте класс Circle с переменной класса pi = 3.14.
# 2. Добавьте метод area(self, radius), который возвращает:
#    pi * radius ** 2
# ============================================================

class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2


circle_for_area = Circle()
print("Задание 6:", circle_for_area.area(5))


# ============================================================
# Задание 7
# 1. Добавьте конструктор __init__(self, diameter).
#    В первом подпункте он мог бы выглядеть так:
#
#    class Circle:
#        def __init__(self, diameter):
#            pass
#
# 2. Итоговый вариант для задания: конструктор выводит сообщение
#    при создании нового круга.
# ============================================================

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print(f"New circle with diameter: {diameter}")

    def area(self, radius):
        return self.pi * radius ** 2


teaching_table = Circle(36)


# ============================================================
# Задание 8
# 1. Измените класс Circle:
#    - в конструкторе установите self.radius = diameter / 2
# 2. Создайте объекты:
#    - medium_pizza с диаметром 12
#    - teaching_table с диаметром 36
#    - round_room с диаметром 11460
# 3. Добавьте метод circumference(self), который возвращает:
#    2 * pi * radius
# 4. Выведите длины окружностей этих объектов.
# ============================================================

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print("Задание 8:")
print("medium_pizza circumference =", medium_pizza.circumference())
print("teaching_table circumference =", teaching_table.circumference())
print("round_room circumference =", round_room.circumference())


# ============================================================
# Задание 9
# 1. Вызовите dir() для числа 5 и выведите результат.
# 2. Определите функцию this_function_is_an_object.
# 3. Выведите результат вызова dir() для этой функции.
# ============================================================

print("Задание 9: dir(5)")
print(dir(5))


def this_function_is_an_object(*args, **kwargs):
    return {
        "args": args,
        "kwargs": kwargs,
    }


print("Задание 9: dir(this_function_is_an_object)")
print(dir(this_function_is_an_object))


# ============================================================
# Задание 10
# Добавьте метод __repr__() в класс Circle, который возвращает:
# "Circle with radius {radius}"
# Затем выведите medium_pizza, teaching_table и round_room.
# ============================================================

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print("Задание 10:")
print(medium_pizza)
print(teaching_table)
print(round_room)
