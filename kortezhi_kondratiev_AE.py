# ==============================
# ЗАДАНИЕ: Проверка экзамена ГИБДД
# ==============================

# Кортеж правильных ответов (вопросы 1..20)
correct_answers = (
    1, 2, 3, 2, 1,
    2, 1, 3, 1, 2,
    1, 2, 3, 3, 2,
    1, 2, 1, 2, 1
)

print("Введите ответы сдающего (20 чисел: 1/2/3). Можно в одну строку через пробелы.")
user_answers = []

# Собираем ровно 20 ответов
while len(user_answers) < len(correct_answers):
    remaining = len(correct_answers) - len(user_answers)
    raw = input(f"Осталось ввести {remaining}: ").strip()

    if not raw:
        continue

    parts = raw.replace(",", " ").split()
    for p in parts:
        if len(user_answers) >= len(correct_answers):
            break
        try:
            ans = int(p)
        except ValueError:
            print(f"'{p}' не число")
            continue

        if ans not in (1, 2, 3):
            print(f"'{ans}' не в диапазоне 1..3")
            continue

        user_answers.append(ans)

# Сравнение
if tuple(user_answers) == correct_answers:
    print("Экзамен сдан")
else:
    print("Экзамен провален")
