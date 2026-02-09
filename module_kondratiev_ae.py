from dataclasses import dataclass
from datetime import datetime, date
import random
import string
from typing import Dict, List, Iterable, Tuple, Optional


# =============================================================================
# 1) datetime: current_time = datetime.now(); print(current_time)
# =============================================================================

def task_datetime() -> None:
    import datetime as dt  # требование задания: импортировать библиотеку datetime

    current_time = dt.datetime.now()
    print("Текущее время:", current_time)


# =============================================================================
# 2) random: list comprehension + random.choice
# =============================================================================

def task_random_list() -> None:
    import random  # требование задания: импортировать random

    random_list = []  # пустой список
    # превращаем в list comprehension: 101 число (range(101)), каждое 1..100
    random_list = [random.randint(1, 100) for _ in range(101)]

    randomer_number = random.choice(random_list)
    print("random_list (первые 10):", random_list[:10])
    print("randomer_number:", randomer_number)


# =============================================================================
# 3) matplotlib + random: построить график случайных чисел
# =============================================================================

def task_plot_random_numbers() -> None:
    # 1) import pyplot as plt
    from matplotlib import pyplot as plt
    # 2) import random ниже других импортов (сделано в функции)
    import random

    # 3) number_a = диапазон 1..12 (включительно)
    number_a = list(range(1, 13))

    # 4) number_b = случайная выборка из 12 чисел в диапазоне (1000)
    number_b = random.sample(range(1000), 12)

    # 5) plt.plot(number_a, number_b)
    plt.plot(number_a, number_b)

    # 6) plt.show()
    plt.show()


# =============================================================================
# 4) Задание 1: сотрудники — премии, индексация, отпуск
# =============================================================================

@dataclass
class Employee:
    fio: str
    position: str
    hire_date: date
    salary: int
    gender: str  # "M" или "F" (нужно для 23 февраля / 8 марта)

def _parse_ru_date(s: str) -> date:
    return datetime.strptime(s, "%d.%m.%Y").date()

def _tenure_days(emp: Employee, as_of: Optional[date] = None) -> int:
    as_of = as_of or date.today()
    return (as_of - emp.hire_date).days

def build_employees() -> List[Employee]:
    # Данные из таблицы на скриншоте
    return [
        Employee("Иванов Иван Иванович", "Менеджер", _parse_ru_date("22.10.2013"), 250_000, "M"),
        Employee("Сорокина Екатерина Матвеевна", "Аналитик", _parse_ru_date("12.03.2020"), 75_000, "F"),
        Employee("Струков Иван Сергеевич", "Старший программист", _parse_ru_date("23.04.2012"), 150_000, "M"),
        Employee("Корнеева Анна Игоревна", "Ведущий программист", _parse_ru_date("22.02.2015"), 120_000, "F"),
        Employee("Старчиков Сергей Анатольевич", "Младший программист", _parse_ru_date("12.11.2021"), 50_000, "M"),
        Employee("Бутенко Артем Андреевич", "Архитектор", _parse_ru_date("12.02.2010"), 200_000, "M"),
        Employee("Савченко Алина Сергеевна", "Старший аналитик", _parse_ru_date("13.04.2016"), 100_000, "F"),
    ]

def programmer_day_bonus(employees: Iterable[Employee]) -> Dict[str, int]:
    """
    Премия ко дню программиста (13 сентября): 3% от оклада каждому программисту.
    """
    bonuses: Dict[str, int] = {}
    for emp in employees:
        if "программист" in emp.position.lower():
            bonuses[emp.fio] = round(emp.salary * 0.03)
    return bonuses

def fixed_holiday_bonus(employees: Iterable[Employee], holiday: str) -> Dict[str, int]:
    """
    Премия фиксированная 2000:
      - 8 марта: всем сотрудницам
      - 23 февраля: всем сотрудникам (мужчинам)
    holiday: "8march" или "23feb"
    """
    bonuses: Dict[str, int] = {}
    if holiday not in {"8march", "23feb"}:
        raise ValueError("holiday должен быть '8march' или '23feb'")

    for emp in employees:
        if holiday == "8march" and emp.gender == "F":
            bonuses[emp.fio] = 2000
        elif holiday == "23feb" and emp.gender == "M":
            bonuses[emp.fio] = 2000
    return bonuses

def index_salaries(employees: Iterable[Employee], as_of: Optional[date] = None) -> Dict[str, int]:
    """
    Индексация:
      - > 10 лет стажа: +7%
      - иначе: +5%
    """
    as_of = as_of or date.today()
    updated: Dict[str, int] = {}
    for emp in employees:
        years = _tenure_days(emp, as_of=as_of) / 365.25
        factor = 1.07 if years > 10 else 1.05
        updated[emp.fio] = round(emp.salary * factor)
    return updated

def vacation_eligible(employees: Iterable[Employee], as_of: Optional[date] = None) -> List[str]:
    """
    Список сотрудников, отработавших > 6 месяцев.
    """
    as_of = as_of or date.today()
    eligible: List[str] = []
    for emp in employees:
        if _tenure_days(emp, as_of=as_of) > 183:  # ~6 месяцев
            eligible.append(emp.fio)
    return eligible

def task_employees_demo() -> None:
    employees = build_employees()

    print("\n--- Премия ко дню программиста (3% программистам) ---")
    for fio, bonus in programmer_day_bonus(employees).items():
        print(f"{fio}: {bonus}")

    print("\n--- Премии 8 марта (2000 сотрудницам) ---")
    for fio, bonus in fixed_holiday_bonus(employees, "8march").items():
        print(f"{fio}: {bonus}")

    print("\n--- Премии 23 февраля (2000 сотрудникам) ---")
    for fio, bonus in fixed_holiday_bonus(employees, "23feb").items():
        print(f"{fio}: {bonus}")

    print("\n--- Индексация зарплат ---")
    indexed = index_salaries(employees)
    for emp in employees:
        print(f"{emp.fio}: было {emp.salary}, стало {indexed[emp.fio]}")

    print("\n--- В отпуск (стаж > 6 месяцев) ---")
    for fio in vacation_eligible(employees):
        print(fio)


# =============================================================================
# 5) Задание 2: розыгрыш в ТЦ — вывести первые 5 выигрышных номеров
# =============================================================================

def sum_digits(n: int) -> int:
    return sum(int(ch) for ch in str(abs(n)))

def mall_lottery_winners(
    user_numbers: Iterable[int],
    admin_number: int,
    max_winners: int = 5,
) -> List[int]:
    """
    Выигрышный номер: сумма цифр номера делится нацело на admin_number.
    Возвращает первые max_winners выигрышных номеров в порядке обхода.
    """
    winners: List[int] = []
    for num in user_numbers:
        if admin_number != 0 and sum_digits(num) % admin_number == 0:
            winners.append(num)
            if len(winners) >= max_winners:
                break
    return winners

def task_mall_lottery_demo() -> None:
    # Случайный выбор администрацией числа от 1 до 9
    admin_number = random.randint(1, 9)

    # Сгенерируем "пользовательские номера" (например, 10000..99999)
    user_numbers = [random.randint(10_000, 99_999) for _ in range(10_000)]

    winners = mall_lottery_winners(user_numbers, admin_number, max_winners=5)

    print("\n--- Розыгрыш в ТЦ ---")
    print("Число администрации:", admin_number)
    print("Первые 5 выигрышных номеров:")
    for w in winners:
        print(w)


# =============================================================================
# 6) Самостоятельная работа: монетка, кубик, пароль
# =============================================================================

def coin_toss(attempts: int) -> List[str]:
    """Выводит результаты бросков монеты: 'Орел' / 'Решка'."""
    results = [random.choice(["Орел", "Решка"]) for _ in range(attempts)]
    return results

def dice_roll(attempts: int) -> List[int]:
    """Выводит результаты бросков кубика (1..6)."""
    return [random.randint(1, 6) for _ in range(attempts)]

def generate_password(length: int) -> str:
    """
    Генерирует пароль из букв английского алфавита a..z, A..Z.
    """
    alphabet = string.ascii_letters  # a-zA-Z
    return "".join(random.choice(alphabet) for _ in range(length))

def task_self_study_demo() -> None:
    print("\n--- Монетка (пример: 10 бросков) ---")
    for r in coin_toss(10):
        print(r)

    print("\n--- Кубик (пример: 10 бросков) ---")
    for r in dice_roll(10):
        print(r)

    print("\n--- Пароль (пример: длина 12) ---")
    print(generate_password(12))


# =============================================================================
# 7) Проект "Скраббл" — подсчёт очков
# =============================================================================

LETTERS = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N",
    "O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
POINTS = [1,3,3,2,1,4,2,4,1,8,5,1,3,4,1,3,10,1,1,1,1,4,4,8,4,10]

def build_letter_to_points() -> Dict[str, int]:
    letter_to_points = {letter: point for letter, point in zip(LETTERS, POINTS)}
    # пустая плитка
    letter_to_points[" "] = 0
    return letter_to_points

LETTER_TO_POINTS = build_letter_to_points()

def score_word(word: str, letter_to_points: Dict[str, int] = LETTER_TO_POINTS) -> int:
    """
    Возвращает стоимость слова.
    - Поддерживает lowercase/uppercase.
    - Неизвестные символы игнорируются (можно изменить на raise, если нужно).
    """
    total = 0
    for ch in word:
        total += letter_to_points.get(ch.upper(), 0)
    return total

def build_player_to_words() -> Dict[str, List[str]]:
    # Таблица на скриншоте
    return {
        "player1": ["BLUE", "TENNIS", "EXIT"],
        "wordNerd": ["EARTH", "EYES", "MACHINE"],
        "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
        "Prof Reader": ["ZAP", "COMA", "PERIOD"],
    }

def update_point_totals(player_to_words: Dict[str, List[str]]) -> Dict[str, int]:
    player_to_points: Dict[str, int] = {}
    for player, words in player_to_words.items():
        player_points = 0
        for w in words:
            player_points += score_word(w)
        player_to_points[player] = player_points
    return player_to_points

def play_word(player_to_words: Dict[str, List[str]], player: str, word: str) -> None:
    """
    Добавляет слово игроку (если игрока нет — создаст).
    """
    player_to_words.setdefault(player, []).append(word)

def task_scrabble_demo() -> None:
    print("\n--- Scrabble ---")
    player_to_words = build_player_to_words()

    # тест score_word
    print("score_word('BLUE') =", score_word("BLUE"))

    # считаем очки игроков
    player_to_points = update_point_totals(player_to_words)
    print("Очки игроков:")
    for player, pts in player_to_points.items():
        print(f"{player}: {pts}")

    # доп. пример: добавить слово
    play_word(player_to_words, "player1", "PYTHON")
    player_to_points = update_point_totals(player_to_words)
    print("\nПосле play_word(player1, 'PYTHON'):")
    print("player1:", player_to_points["player1"])


# =============================================================================
# Меню запуска
# =============================================================================

def main() -> None:
    actions = {
        "1": ("datetime: current_time", task_datetime),
        "2": ("random: list + choice", task_random_list),
        "3": ("matplotlib: plot random numbers", task_plot_random_numbers),
        "4": ("Сотрудники: премии/индексация/отпуск", task_employees_demo),
        "5": ("Розыгрыш в ТЦ: первые 5 winners", task_mall_lottery_demo),
        "6": ("Самостоятельная работа: монета/кубик/пароль", task_self_study_demo),
        "7": ("Проект Scrabble", task_scrabble_demo),
        "0": ("Запустить демо (без графика)", None),
        "q": ("Выход", None),
    }

    while True:
        print("\nВыберите задание:")
        for k in ["1","2","3","4","5","6","7","0","q"]:
            print(f"  {k} — {actions[k][0]}")

        choice = input("> ").strip().lower()

        if choice == "q":
            break
        if choice == "0":
            # демо без matplotlib, чтобы не открывать окно случайно
            task_datetime()
            task_random_list()
            task_employees_demo()
            task_mall_lottery_demo()
            task_self_study_demo()
            task_scrabble_demo()
            continue

        action = actions.get(choice)
        if not action:
            print("Неизвестный выбор.")
            continue

        func = action[1]
        if func is None:
            print("Нет действия.")
            continue

        func()


if __name__ == "__main__":
    main()