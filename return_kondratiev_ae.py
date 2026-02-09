def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit

# 3) target = 100, margin = 20
low_limit, high_limit = get_boundaries(100, 20)

# 4) Вывод строки с подстановкой значений
print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")

# task_repeat_stuff.py

def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats

# 2) Пример вызова вне функции
repeat_stuff("Row", 3)

# 5) Соединить repeat_stuff("Row", 3) и "Your Boat." -> lyrics
lyrics = repeat_stuff("Row", 3) + "Your Boat."

# 6) song = repeat_stuff(...) вызов только со stuff (num_repeats по умолчанию)
song = repeat_stuff("Row")

# 7) Вывести песню
print(song)
