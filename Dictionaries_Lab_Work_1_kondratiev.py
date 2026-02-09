# =========================
# ЗАДАНИЕ 1: sensors + num_cameras
# =========================

# 1) Добавить датчик в "кладовую" (pantry) со значением 22
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["pantry"] = 22
print("sensors:", sensors)

# 2) Убрать # и исправить SyntaxError в словаре num_cameras
# Было (с ошибками):
# num_cameras = {"backyard": 6, "garage": 2 "driveway" 1}

num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print("num_cameras:", num_cameras)

# =========================
# ЗАДАНИЕ 2: Словарь переводов (English -> Sindarin)
# =========================

translations = {
    "mountain": "orod",
    "bread": "bass",
    "friend": "mellon",
    "horse": "roch"
}

print(translations)

# =========================
# ЗАДАНИЕ 3: animals_in_zoo
# =========================

# 1) Пустой словарь
animals_in_zoo = {}

# 2) Добавить зебр
animals_in_zoo["zebras"] = 8

# 3) Добавить обезьян
animals_in_zoo["monkeys"] = 12

# 4) Добавить динозавров
animals_in_zoo["dinosaurs"] = 0

# 5) Вывести словарь
print(animals_in_zoo)

# =========================
# ЗАДАНИЕ 4: user_ids
# =========================

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# 1) Добавить двух пользователей
user_ids["theLooper"] = 138475
user_ids["stringQueen"] = 85739

# 2) Вывести результат
print(user_ids)

# =========================
# ЗАДАНИЕ 5: oscar_winners
# =========================

oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

# 1) Добавить "Supporting Actress": "Viola Davis"
oscar_winners["Supporting Actress"] = "Viola Davis"

# 2) Не меняя определение словаря выше, заменить Best Picture на Moonlight
oscar_winners["Best Picture"] = "Moonlight"

print(oscar_winners)

# =========================
# ЗАДАНИЕ 6: drinks_to_caffeine через zip + dict comprehension
# =========================

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# 1) zipped_drinks — итератор пар (drink, caffeine_mg)
zipped_drinks = zip(drinks, caffeine)

# 2) Создать словарь drinks_to_caffeine генератором словаря
drinks_to_caffeine = {drink: mg for drink, mg in zipped_drinks}

print(drinks_to_caffeine)

# =========================
# ЗАДАНИЕ 7: plays + library
# =========================

songs = [
    "Like a Rolling Stone",
    "Satisfaction",
    "Imagine",
    "What's Going On",
    "Respect",
    "Good Vibrations"
]
playcounts = [78, 29, 44, 21, 89, 5]

# 1) Создать plays через dict comprehension + zip
plays = {song: count for song, count in zip(songs, playcounts)}

# 2) Вывести plays
print("plays (before):", plays)

# 3) Добавить "Purple Haze": 1
plays["Purple Haze"] = 1

# 4) Пользователь прослушал "Respect" 5 раз -> обновить значение
plays["Respect"] = 5

print("plays (after):", plays)

# 5) Создать library:
# - "The Best Songs": plays
# - "Sunday Feelings": пустой словарь
library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}

# 6) Вывести library
print("library:", library)
