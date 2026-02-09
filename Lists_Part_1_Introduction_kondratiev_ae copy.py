# =========================
# 1) Список: "торт" и 1
# =========================
product = ["торт", 1]
print("product =", product)

# =========================
# 2) Список бытовой химии: список из списков [название, количество]
# =========================
household_chemicals = [
    ["стиральный порошок", 1],
    ["средство для мытья посуды", 1],
]
print("household_chemicals =", household_chemicals)

# =========================
# 3) zip: имена людей + имена собак
# =========================
Names = ["Ben", "Holly", "Ann"]
dogs_names = ["Sharik", "Gab", "Beethoven"]

names_and_dogs_names = zip(Names, dogs_names)              # zip-объект
list_of_names_and_dogs_names = list(names_and_dogs_names)  # превращаем в список
print("list_of_names_and_dogs_names =", list_of_names_and_dogs_names)

# =========================
# 4) Заказы Марии (append + print)
# =========================
orders = ["маргаритки", "васильки"]
print("orders (start) =", orders)

orders.append("тюльпаны")
orders.append("розы")
print("orders (final) =", orders)

# =========================
# 5) new_orders через + и исправление broken_prices
# =========================
orders = ["маргаритка", "лютик", "львиный зев", "гардения", "лилия"]
new_orders = orders + ["сирень", "ирис"]
print("new_orders =", new_orders)

# Было бы ошибкой: [5, 3, 4, 5, 4] + 4
broken_prices = [5, 3, 4, 5, 4] + [4]  # корректно: складываем список со списком
print("broken_prices =", broken_prices)

# =========================
# 6) range: list1 0..8, list2 0..7
# =========================
list1 = range(0, 9)   # 0..8 (9 не включается)
list2 = range(0, 8)   # 0..7
print("list(list1) =", list(list1))
print("list(list2) =", list(list2))

# =========================
# 7) range: list1 старт 5, шаг 3, stop=15 (15 не включается)
# =========================
list1 = range(5, 15, 3)  # 5, 8, 11, 14
print("list(list1) (5..15 step 3) =", list(list1))

# 8) range: list2 старт 0, шаг 5, до 40 (чтобы включить 40, ставим stop=41)
list2 = range(0, 41, 5)  # 0,5,10,...,40
print("list(list2) (0..40 step 5) =", list(list2))

# =========================
# 9) Клиенты: first_names, age, all_ages, zip, ids
# =========================
first_names = ["Эйнсли", "Бен", "Чани", "Депак"]
print("first_names =", first_names)

age = []
age.append(42)  # возраст Депака
print("age =", age)

all_ages = [32, 41, 29] + age
print("all_ages =", all_ages)

name_and_age = list(zip(first_names, all_ages))
print("name_and_age =", name_and_age)

ids = range(0, 4)  # 0..3
print("list(ids) =", list(ids))
