# -*- coding: utf-8 -*-

# ============================================================
# Задание 1
# 1. Создайте класс Employee с методом __init__().
# 2. Определите переменную класса new_id = 1.
# 3. Внутри __init__() определите self.id = Employee.new_id.
# 4. Увеличьте Employee.new_id на 1.
# 5. Добавьте метод say_id(), который выводит:
#    "My id is " и затем ID экземпляра.
# 6. Создайте e1 и e2, затем вызовите их say_id().
# ============================================================

class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print(f"My id is {self.id}")


e1 = Employee()
e2 = Employee()

print("Задание 1:")
e1.say_id()
e2.say_id()


# ============================================================
# Задание 2
# 1. Создайте класс Admin, наследующийся от Employee.
# 2. Внутри тела класса используйте pass.
# 3. Создайте e3 = Admin().
# 4. Вызовите e3.say_id().
# ============================================================

class Admin(Employee):
    pass


e3 = Admin()

print("\nЗадание 2:")
e3.say_id()


# ============================================================
# Задание 3
# Переопределите say_id() в Admin так, чтобы он выводил:
# "I am an Admin"
# ============================================================

class Admin(Employee):
    def say_id(self):
        print("I am an Admin")


e3 = Admin()

print("\nЗадание 3:")
e3.say_id()


# ============================================================
# Задание 4
# Измените Admin.say_id() так, чтобы он также вызывал
# метод say_id() класса Employee.
# Вывод должен содержать и ID администратора,
# и то, что он является администратором.
# ============================================================

class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("I am an Admin")


e3 = Admin()

print("\nЗадание 4:")
e3.say_id()


# ============================================================
# Задание 5
# 1. Определите класс Manager, который наследуется от Admin.
# 2. Внутри Manager определите say_id(), который говорит,
#    что менеджеры отвечают за дело.
# 3. Внутри Manager.say_id() вызовите метод say_id() класса Admin.
# 4. Создайте e4 = Manager() и вызовите e4.say_id().
# ============================================================

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am in charge")


e4 = Manager()

print("\nЗадание 5:")
e4.say_id()


# ============================================================
# Задание 6
# Класс User уже "добавлен":
# - атрибуты username и role
# - метод say_user_info()
#
# Нужно:
# 1. Сделать Admin наследником Employee и User,
#    причём Employee должен быть указан первым.
# 2. Внутри Admin.__init__() вызвать User.__init__()
#    и передать: экземпляр Admin, id и строку "Admin".
# 3. Проверить через e3.say_user_info().
# ============================================================

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"My username is {self.username} and my role is {self.role}")


class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        super().say_id()
        print("I am an Admin")


class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am in charge")


e3 = Admin()

print("\nЗадание 6:")
e3.say_user_info()


# ============================================================
# Задание 7
# 1. Определите переменную meeting и установите её равной списку,
#    который содержит экземпляр каждого класса:
#    Employee(), Admin(), Manager().
# 2. Используя цикл for, вызовите .say_id() на каждом экземпляре.
# ============================================================

meeting = [Employee(), Admin(), Manager()]

print("\nЗадание 7:")
for attendee in meeting:
    attendee.say_id()


# ============================================================
# Задание 8
# Теперь есть класс Meeting с:
# - атрибутом списка attendees
# - dunder-методом __add__(), который добавляет Employee
#   в список attendees
#
# Нужно:
# 1. Перегрузить len(), определив __len__(),
#    который возвращает длину attendees.
# 2. Создать m1 и добавить e1, e2, e3.
# 3. Вывести len(m1).
# ============================================================

class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        self.attendees.append(employee)
        print(f"Added attendee with id {employee.id}")
        return self

    def __len__(self):
        return len(self.attendees)


m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3

print("\nЗадание 8:")
print(len(m1))


# ============================================================
# Задание 9
# 1. Определите абстрактный класс AbstractEmployee.
# 2. Перенесите в него логику старого Employee,
#    но метод say_id() оставьте абстрактным.
# 3. Сделайте Employee наследником AbstractEmployee.
# 4. Реализуйте в Employee метод say_id(), который выводит self.id.
#
# Примечание:
# В условии предлагается сначала сделать Employee пустым и увидеть
# ошибку TypeError, но в итоговом файле сразу дана исправленная версия,
# чтобы код полностью выполнялся.
# ============================================================

from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


class Employee(AbstractEmployee):
    def say_id(self):
        print(f"My id is {self.id}")


print("\nЗадание 9:")
abstract_e1 = Employee()
abstract_e1.say_id()


# ============================================================
# Задание 10
# 1. В классе Employee уже есть атрибут id.
# 2. Добавьте внутри __init__() атрибут с одним подчёркиванием: _id
# 3. Добавьте атрибут с двойным подчёркиванием: __id
# 4. Передайте экземпляр Employee в dir() и выведите результат.
#    В списке вы увидите id, _id и искажённое имя __id:
#    _Employee__id
# ============================================================

class Employee:
    def __init__(self):
        self.id = 1
        self._id = "single underscore"
        self.__id = "double underscore"


e = Employee()

print("\nЗадание 10:")
print(dir(e))
