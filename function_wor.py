
# =========================
# Задача 1. Температура
# =========================
def f_to_c(f_temp: float) -> float:
    """Переводит температуру из Фаренгейта в Цельсий."""
    return (f_temp - 32) * 5 / 9


def c_to_f(c_temp: float) -> float:
    """Переводит температуру из Цельсия в Фаренгейт."""
    return c_temp * (9 / 5) + 32


# =========================
# Задача 2. Сила, энергия, работа
# =========================
def get_force(mass: float, acceleration: float) -> float:
    """F = m * a"""
    return mass * acceleration


def get_energy(mass: float, c: float = 3 * 10**8) -> float:
    """E = m * c^2 (c по умолчанию = 3 * 10^8)"""
    return mass * (c**2)


def get_work(mass: float, acceleration: float, distance: float) -> float:
    """Работа = сила * расстояние; сила считается через get_force."""
    force = get_force(mass, acceleration)
    return force * distance


# =========================
# Задача 3. Текст через функции
# =========================
def wardrobe_preferences(clothes: str) -> None:
    print("У меня большой гардероб")
    for time_of_day in ["утром", "днем", "вечером", "ночью"]:
        print(f"{time_of_day.capitalize()} лучше всего подходит {clothes}")


def meal_preferences(meal: str) -> None:
    print("Мои предпочтения в еде")
    for time_of_meal in ["завтрак", "обед", "ужин"]:
        print(f"На {time_of_meal} лучше всего подходит {meal}")


# =========================
# Задача 4. Проверка доступа — через функции
# =========================
def check_user_name(user_name: str) -> str:
    """Часть 1: только имя пользователя."""
    dmitriy_check = (
        "Дмитрий, твое рабочее место находится в другой комнате. "
        "Отойди от чужого компьютера и займись работой!"
    )
    welcome = "Добро пожаловать"

    if user_name == "Дмитрий":
        return dmitriy_check
    return welcome


def check_access_with_arm(user_name: str, arm: int) -> str:
    """Часть 2: имя + номер АРМ."""
    expected_arm_by_user = {
        "Дмитрий": 1,
        "Ангелина": 2,
        "Василий": 3,
        "Екатерина": 4,
    }

    dmitriy_check = (
        "Дмитрий, твое рабочее место находится в другой комнате. "
        "Отойди от чужого компьютера и займись работой!"
    )
    wrong_login = "Логин или пароль не верный, попробуйте еще раз"
    welcome = "Добро пожаловать!"

    expected = expected_arm_by_user.get(user_name)

    # Если пользователя нет в списке — считаем как неверные данные
    if expected is None:
        return wrong_login

    # Если соответствуют имя и АРМ — приветствие
    if arm == expected:
        return welcome

    # Если имя Дмитрий, но АРМ не его — спец. уведомление
    if user_name == "Дмитрий":
        return dmitriy_check

    # Иначе — ошибка
    return wrong_login


# =========================
# Задача 5. Грейд по среднему баллу — через функции
# =========================
def get_letter_grade(grade: float) -> str:
    """
    Возвращает буквенный грейд:
      4.0+ -> A
      3.0+ -> B
      2.0+ -> C
      1.0+ -> D
      0.0+ -> F
    """
    if grade >= 4.0:
        return "A"
    elif grade >= 3.0:
        return "B"
    elif grade >= 2.0:
        return "C"
    elif grade >= 1.0:
        return "D"
    elif grade >= 0.0:
        return "F"
    else:
        # На случай некорректного отрицательного балла
        raise ValueError("Средний балл (grade) не может быть отрицательным.")


def main() -> None:
    # ---- Задача 1: проверка функций ----
    f100_in_celsius = f_to_c(100)
    c0_in_fahrenheit = c_to_f(0)

    print("=== Задача 1 ===")
    print(f"100°F = {f100_in_celsius:.2f}°C")
    print(f"0°C = {c0_in_fahrenheit:.2f}°F")
    print()

    # ---- Задача 2: сила, энергия, работа ----
    train_mass = 22680
    train_acceleration = 10
    train_distance = 100

    train_force = get_force(train_mass, train_acceleration)
    print("=== Задача 2 ===")
    print(train_force)
    print(f"Поезд GE поставляет {train_force} ньютонов силы")

    bomb_mass = 1
    bomb_energy = get_energy(bomb_mass)
    print(f"1 кг бомбы составляет {bomb_energy} Джоулей")

    train_work = get_work(train_mass, train_acceleration, train_distance)
    print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров.")
    print()

    # ---- Задача 3: гардероб + еда (через функции) ----
    clothes = "домашняя одежда"
    meal = "каша"  # можно заменить на свои предпочтения

    print("=== Задача 3 ===")
    wardrobe_preferences(clothes)
    print()
    meal_preferences(meal)
    print()

    # ---- Задача 4: проверка доступа (через функции) ----
    print("=== Задача 4 ===")
    for name in ["Дмитрий", "Ангелина"]:
        print(f"user_name={name!r} -> {check_user_name(name)}")

    print("--- Проверка с АРМ ---")
    test_cases = [
        ("Дмитрий", 1),   # правильный АРМ
        ("Дмитрий", 2),   # Дмитрий за чужим ПК
        ("Ангелина", 2),  # правильно
        ("Ангелина", 1),  # неверный АРМ
        ("Неизвестный", 1),
    ]
    for name, arm in test_cases:
        print(f"user_name={name!r}, ARM={arm} -> {check_access_with_arm(name, arm)}")
    print()

    # ---- Задача 5: грейды (через функции) ----
    print("=== Задача 5 ===")
    grades_to_test = [4.2, 3.5, 2.7, 1.1, 0.0]
    for grade in grades_to_test:
        letter = get_letter_grade(grade)
        print(f"grade={grade} -> {letter}")


if __name__ == "__main__":
    main()