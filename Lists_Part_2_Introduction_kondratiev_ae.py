# =========================
# 1) len(range) + изменение шага range
# =========================
list1 = range(2, 20, 2)
list1_len = len(list1)
print("list(list1) =", list(list1))
print("list1_len =", list1_len)

# меняем шаг: пропускаем 3 вместо 2 (step=3)
list1 = range(2, 20, 3)
list1_len_new = len(list1)
print("list(list1) with step=3 =", list(list1))
print("list1_len_new =", list1_len_new)
print("Изменение длины:", list1_len, "->", list1_len_new)

# =========================
# 2) shopping_list: длина, последний элемент (-1), элемент с индексом 5
# =========================
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']

print("shopping_list_len =", len(shopping_list))

last_element = shopping_list[-1]
element5 = shopping_list[5]

print("last_element =", last_element)
print("element5 =", element5)

# =========================
# 3) suitcase: срезы beginning, сколько элементов, middle (2 средних)
# =========================
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']

beginning = suitcase[0:2]
print("beginning (0:2) =", beginning)
print("Сколько элементов в suitcase? ->", len(suitcase))

# первые 4 элемента
beginning = suitcase[0:4]
print("beginning (0:4) =", beginning)

# два средних элемента (для длины 6 это индексы 2 и 3)
middle = suitcase[2:4]
print("middle (2 средних) =", middle)

# =========================
# 4) start: первые 3 элемента чемодана
# =========================
suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[:3]
print("start (first 3) =", start)

# =========================
# 5) Подсчёт голосов за Jake (счётчик)
# =========================
votes = [
    'Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie',
    'Jake', 'Jake', 'Jake', 'Laurie',
    'Cassie', 'Cassie',
    'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie',
    'Jake', 'Jake', 'Cassie', 'Laurie'
]

jake_votes = 0
for v in votes:
    if v == 'Jake':
        jake_votes += 1

print("jake_votes =", jake_votes)

# =========================
# 6) Сортировка адресов + print до/после
# =========================
addresses = [
    '221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place',
    '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.'
]

print("addresses BEFORE sort =", addresses)
addresses.sort()
print("addresses AFTER sort  =", addresses)

# =========================
# 7) Сортировка игр в новый список games_sorted
# =========================
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)

print("games =", games)
print("games_sorted =", games_sorted)

# =========================
# 8) inventory: длина, first/last, срез 2:6, первые 3, подсчёт односпальных, sort()
# =========================
inventory = [
    'двухспальная кровать', 'двухспальная кровать', 'изголовье',
    'двуспальная кровать', 'двуспальная кровать',
    'комод', 'комод',
    'стол', 'стол',
    'тумбочка', 'тумбочка',
    'королевский кровать',
    'двуспальная кровать',
    'две односпальные кровати', 'две односпальные кровати',
    'простыни', 'простыни',
    'подушка', 'подушка'
]

inventory_len = len(inventory)
print("inventory_len =", inventory_len)

first = inventory[0]
last = inventory[-1]
print("first =", first)
print("last  =", last)

inventory_2_6 = inventory[2:6]   # индексы 2,3,4,5
print("inventory_2_6 (2:6) =", inventory_2_6)

first_3 = inventory[:3]
print("first_3 =", first_3)

twin_beds = 0
for item in inventory:
    if item == 'две односпальные кровати':
        twin_beds += 1
print("twin_beds =", twin_beds)

print("inventory BEFORE sort =", inventory)
inventory.sort()
print("inventory AFTER sort  =", inventory)
