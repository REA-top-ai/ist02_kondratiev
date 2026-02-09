# =========================
# ЗАДАНИЕ 1: zodiac_elements (earth + fire)
# =========================

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# 1) Вывести список знаков "земли"
print(zodiac_elements["earth"])

# 2) Вывести список знаков "огня"
print(zodiac_elements["fire"])

# =========================
# ЗАДАНИЕ 2: KeyError "energy" + исправление
# =========================

zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# 1) Демонстрация KeyError (чтобы файл не падал — ловим ошибку)
print("1) Пробуем получить zodiac_elements['energy'] (должен быть KeyError):")
try:
    print(zodiac_elements["energy"])
except KeyError:
    print("KeyError: 'energy'")

# 2) Добавляем ключ "energy" и проверяем, что ошибки больше нет
zodiac_elements["energy"] = "Not a Zodiac element"
print("\n2) После добавления ключа 'energy':")
print(zodiac_elements["energy"])

# =========================
# ЗАДАНИЕ 3: try/except + добавление matcha
# =========================

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

# 1) try/except — попытаться вывести caffeine_level["matcha"]
print("1) Пытаемся вывести уровень кофеина в matcha:")
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")

# 2) Добавить matcha: 30 над блоком try и снова попробовать
caffeine_level["matcha"] = 30

print("\n2) После добавления matcha:")
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Неизвестный уровень кофеина")

# =========================
# ЗАДАНИЕ 4: .get() с default
# =========================

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# 1) tc_id для teraCoder, default=100000
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

# 2) stack_id для superStackSmash, default=100000
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

# =========================
# ЗАДАНИЕ 5: dict_keys (users + classes)
# =========================

user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# 1) users = dict_keys всех ключей user_ids
users = user_ids.keys()

# 2) classes (или lessons) = dict_keys всех ключей num_exercises
classes = num_exercises.keys()

# 3) Вывести users
print(users)

# 4) Вывести lessons/classes
print(classes)

# =========================
# ЗАДАНИЕ 6: total_exercises (сумма значений словаря)
# =========================

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# 1) total_exercises = 0
total_exercises = 0

# 2) Добавить каждое значение из num_exercises в total_exercises
for value in num_exercises.values():
    total_exercises += value

# 3) Вывести total_exercises
print(total_exercises)

# =========================
# ЗАДАНИЕ 7: Tarot spread (past/present/future)
# =========================

tarot = {
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World",
    22: "The Fool"
}

# 1) Пустой словарь spread
spread = {}

# 2) Карта 13 -> "past"
spread["past"] = tarot[13]

# 3) Карта 22 -> "present"
spread["present"] = tarot[22]

# 4) Карта 10 -> "future"
spread["future"] = tarot[10]

print(spread)
