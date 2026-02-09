# =========================
# ЗАДАНИЕ 1 (скрин 1)
# =========================

# 1) Запустите код ниже и получите IndentationError (у print(game) нет отступа).
# Чтобы файл не падал полностью, мы "запускаем" этот код через exec и ловим ошибку.

broken_code = """
board_games = ['Settlers of Catan', 'Carcassonne', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
print(game)
"""

print("1) Демонстрация IndentationError:")
try:
    exec(broken_code)
except IndentationError as e:
    print("Поймали ожидаемую ошибку:", e)

# 2) Исправьте отступ у print(game), чтобы ошибки не было.
print("\n2) Исправленный код (печать board_games):")
board_games = ['Settlers of Catan', 'Carcassonne', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
    print(game)

# 3) Напишите цикл, который выводит каждый вид спорта в sport_games.
print("\n3) Печать sport_games:")
for sport in sport_games:
    print(sport)

# =========================
# ЗАДАНИЕ 2 (скрин 2)
# =========================

promise = "I will not chew gum in class"

# Используйте range в for, чтобы распечатать обещание 5 раз
for _ in range(5):
    print(promise)

# =========================
# ЗАДАНИЕ 3 (скрин 3)
# =========================

# 1) Объединить студентов: пройти по students_period_A и добавить каждого в конец students_period_B
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

print("1) Добавляем студентов из A в B и печатаем каждого добавленного:")
for student in students_period_A:
    students_period_B.append(student)
    print(student)

print("\nИтоговый список B:", students_period_B)

# 3) Демонстрация опечатки: добавляем в students_period_A вместо students_period_B -> получится бесконечный цикл.
# Требование: "Выйдите из бесконечного цикла!" — поэтому ставим защитный break.

print("\n3) Демонстрация ошибки (append в тот же список) + выход через break:")

students_period_A_bug = ["Alex", "Briana", "Cheri", "Daniele"]

counter = 0
for student in students_period_A_bug:
    # ОПЕЧАТКА (ошибка): добавляем в тот же список, по которому идём
    students_period_A_bug.append(student)

    counter += 1
    print(f"Шаг {counter}: добавили {student}, длина списка стала {len(students_period_A_bug)}")

    if counter >= 10:
        print("Останавливаемся (break), иначе цикл станет бесконечным.")
        break

# Затем избавляемся от ошибки: снова добавляем в B, а не в A.
print("\nИсправление ошибки (добавляем в B, не в A):")
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    students_period_B.append(student)
    print(student)

print("Итоговый список B:", students_period_B)

# =========================
# ЗАДАНИЕ 4 (скрин 4)
# =========================

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

print("1) Печать всех пород:")
for breed in dog_breeds_available_for_adoption:
    print(breed)

print("\n2-3) Ищем нужную породу и выходим через break, когда нашли:")
for breed in dog_breeds_available_for_adoption:
    if breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break

# =========================
# ЗАДАНИЕ 5 (скрин 5)
# =========================

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# 1) Переменная для суммы
scoops_sold = 0

# 2) Цикл по каждому вложенному списку
# 3) Внутри — цикл по каждому числу и прибавление к scoops_sold
for store_sales in sales_data:
    for scoops in store_sales:
        scoops_sold += scoops

# 4) Вывод результата
print(scoops_sold)

# =========================
# ЗАДАНИЕ 6 (скрин 6)
# =========================

# 1) Список single_digits от 0 до 9
single_digits = list(range(10))

# 3) Пустой список squares
squares = []

# 2) Цикл по single_digits: печать каждой цифры
# 4) Внутри цикла добавляем квадрат в squares
print("2) Печать single_digits и заполнение squares:")
for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)

# 5) После цикла вывод squares
print("\n5) squares:")
print(squares)

# 6) Создать список cubes через list comprehension
cubes = [digit ** 3 for digit in single_digits]

# 7) Вывести cubes
print("\n7) cubes:")
print(cubes)
