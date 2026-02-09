"""Задание: определить истинность логических выражений.

Утверждение первое:
    (6 * 6) - 1 == 8 + 1
Утверждение второе:
    13 - 7 != (3 * 2) + 1
Утверждение третье:
    3 * (2 - 1) == 4 - 1

Программа выводит True/False для каждого утверждения.
"""

statement_one = (6 * 6) - 1 == 8 + 1
statement_two = 13 - 7 != (3 * 2) + 1
statement_three = 3 * (2 - 1) == 4 - 1

print("Утверждение 1:", statement_one)
print("Утверждение 2:", statement_two)
print("Утверждение 3:", statement_three)


"""Задание: определить истинность логических выражений.

Утверждение первое:
    (6 * 6) - 1 >= 8 + 1
Утверждение второе:
    13 - 7 <= (3 * 2) + 1
Утверждение третье:
    3 * (2 - 1) > 4 - 1
"""

statement_one = (6 * 6) - 1 >= 8 + 1
statement_two = 13 - 7 <= (3 * 2) + 1
statement_three = 3 * (2 - 1) > 4 - 1

print("Утверждение 1:", statement_one)
print("Утверждение 2:", statement_two)
print("Утверждение 3:", statement_three)


"""Задание про bool и строку.

1) Попробуйте создать переменную bool_variable = true и вывести.
   В Python ключевые слова True/False пишутся с заглавной буквы.
   Поэтому 'true' (в нижнем регистре) приведёт к NameError.

2) Замените значение на 'true' (в кавычках) и проверьте type().

3) Создайте bool_variable_2 с логическим типом истины и проверьте type().
"""

print("Шаг 1. Пробуем сделать bool_variable = true (как в задании)...")

try:
    bool_variable = eval("true")
    print("bool_variable =", bool_variable)
except NameError as e:
    print("Ошибка:", e.__class__.__name__, "—", e)
    print("Причина: в Python логические значения — это True/False (с заглавной буквы), а 'true' не определён.")

print("\nШаг 2. Делаем bool_variable = 'true' (строка)")
bool_variable = "true"
print("bool_variable =", bool_variable)
print("type(bool_variable) =", type(bool_variable))
print("Почему это не логическая переменная: это строка, а не булево значение.")

print("\nШаг 3. Создаём настоящую логическую переменную")
bool_variable_2 = True
print("bool_variable_2 =", bool_variable_2)
print("type(bool_variable_2) =", type(bool_variable_2))

"""Задача про проверку пользователя.

Сюжет: охранник Дмитрий устанавливает игры на чужих ПК.
Нужно:
1) Ввести переменную user_name
2) Создать сообщение для Дмитрия (Dmitriy_check)
3) Создать сообщение для других сотрудников (welcome)
4) Написать if, который проверяет user_name
5) Вывести результат для user_name='Дмитрий' и user_name='Ангелина'
"""

Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome = "Добро пожаловать"

def check_user(user_name: str) -> str:
    if user_name == "Дмитрий":
        return Dmitriy_check
    return welcome

# Проверка работы программы (как просит задание)
for test_name in ("Дмитрий", "Ангелина"):
    print(f"user_name = {test_name!r} -> {check_user(test_name)}")



"""Задание: блокировка после 3 неправильных попыток.

1) Ввести переменную enter_number (количество попыток)
2) if:
   - если enter_number < 3: вывести "Попробуйте еще раз. У вас осталось (3 - enter_number) попыток"
   - если enter_number >= 3: вывести сообщение о блокировке
3) Проверить вывод в консоли

Скрипт демонстрирует работу на enter_number = 1, 2, 3.
"""

def attempts_message(enter_number: int) -> str:
    if enter_number < 3:
        return f"Попробуйте еще раз. У вас осталось {3 - enter_number} попыток"

    return (
        "Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. "
        "Для разблокировки обратитесь в службу поддержки"
    )

for enter_number in (1, 2, 3):
    print(f"enter_number = {enter_number} ->", attempts_message(enter_number))


"""Задание: проверить истинность выражений (AND).

Проверить истинность следующих выражений:
1) (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
2) (4 * 2 <= 8) and (7 - 1 == 6)

Результат проверки поместить в переменные statement_one и statement_two.
"""

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

print("statement_one =", statement_one)
print("statement_two =", statement_two)


"""Задача: проверка пользователя + номер АРМ.

Сотрудники и их АРМ:
- Дмитрий -> 1
- Ангелина -> 2
- Василий -> 3
- Екатерина -> 4

Правила:
- Если номер АРМ и имя пользователя соответствуют -> "Добро пожаловать!"
- Если номер АРМ не совпадает и имя пользователя не Дмитрий -> "Логин или пароль не верный, попробуйте еще раз"
- Если номер АРМ не совпадает и имя пользователя Дмитрий ->
    "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
"""

SPECIAL_MESSAGE = (
    "Дмитрий, твое рабочее место находится в другой комнате. "
    "Отойди от чужого компьютера и займись работой!"
)

def check_access(user_name: str, arm: int) -> str:
    users_to_arm = {
        "Дмитрий": 1,
        "Ангелина": 2,
        "Василий": 3,
        "Екатерина": 4,
    }

    expected_arm = users_to_arm.get(user_name)

    if expected_arm is None:
        return "Логин или пароль не верный, попробуйте еще раз"

    if arm == expected_arm:
        return "Добро пожаловать!"

    if user_name == "Дмитрий":
        return SPECIAL_MESSAGE

    return "Логин или пароль не верный, попробуйте еще раз"

# --- проверка работы ---
examples = [
    ("Дмитрий", 1),
    ("Ангелина", 1),
    ("Дмитрий", 2),
    ("Екатерина", 4),
]

for user_name, arm in examples:
    print(f"user_name={user_name!r}, ARM={arm} -> {check_access(user_name, arm)}")


"""Задание: проверить истинность выражений (OR).

Проверить истинность следующих выражений:
1) (2 - 1 > 3) or (-5 * 2 == -10)
2) (9 + 5 <= 15) or (7 != 4 + 3)

Результат проверки поместить в переменные statement_one и statement_two.
"""

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

print("statement_one =", statement_one)
print("statement_two =", statement_two)


"""Задание: провести рефакторинг задачи про Дмитрия, используя else.

- если user_name == 'Дмитрий' -> вывести спец.сообщение
- иначе -> вывести "Добро пожаловать!"

Показать результат для 'Дмитрий' и 'Ангелина'.
"""

Dmitriy_check = (
    "Дмитрий, твое рабочее место находится в другой комнате. "
    "Отойди от чужого компьютера и займись работой!"
)
welcome = "Добро пожаловать!"

def check_user(user_name: str) -> str:
    if user_name == "Дмитрий":
        return Dmitriy_check
    else:
        return welcome

for test_name in ["Дмитрий", "Ангелина"]:
    print(f"user_name = {test_name}: {check_user(test_name)}")


"""Задача: система грейдов по среднему баллу.

Условия:
- 4.0 или выше -> "A"
- 3.0 или выше -> "B"
- 2.0 или выше -> "C"
- 1.0 или выше -> "D"
- 0.0 или выше -> "F"

Использовать переменную grade и оператор elif.
"""

def get_letter_grade(grade: float) -> str:
    if grade >= 4.0:
        return "A"
    elif grade >= 3.0:
        return "B"
    elif grade >= 2.0:
        return "C"
    elif grade >= 1.0:
        return "D"
    else:
        return "F"

# Демонстрация
for grade in [4.0, 3.7, 3.0, 2.5, 1.0, 0.0]:
    print(f"grade = {grade} -> {get_letter_grade(grade)}")
