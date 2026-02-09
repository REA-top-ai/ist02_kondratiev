# =========================
# ПРОЕКТ: СКРАББЛ (очки)
# =========================

# 1) Даны списки letters и points — объединяем в словарь letter_to_points (через zip + dict comprehension)
letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
points = [
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4,
    1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
]

letter_to_points = {letter: point for letter, point in zip(letters, points)}

# 2) Добавляем пустую плитку " " со значением 0
letter_to_points[" "] = 0


# 3-5) Функция score_word(word): считает очки слова
def score_word(word: str) -> int:
    """
    Возвращает количество очков за слово.
    Поддерживает ввод в нижнем регистре (приводим к upper()).
    Неизвестные символы дают 0 очков.
    """
    total = 0
    for ch in word.upper():
        total += letter_to_points.get(ch, 0)
    return total


# Доп. задание: play_word(player, word) — добавить слово игроку
def play_word(player: str, word: str, player_to_words: dict[str, list[str]]) -> None:
    """
    Добавляет слово в список слов игрока.
    Если игрока нет — создаёт запись.
    """
    if player not in player_to_words:
        player_to_words[player] = []
    player_to_words[player].append(word)


# Доп. задание: update_point_totals() — пересчитать очки всех игроков
def update_point_totals(player_to_words: dict[str, list[str]]) -> dict[str, int]:
    """
    Возвращает словарь player_to_points на основе player_to_words.
    """
    player_to_points: dict[str, int] = {}

    # 9-11) Вложенные циклы: для каждого игрока суммируем очки всех его слов
    for player, words in player_to_words.items():
        player_points = 0
        for w in words:
            player_points += score_word(w)
        player_to_points[player] = player_points

    return player_to_points


def main() -> None:
    # 6) Тестируем score_word через print
    print("Тест score_word('BLUE'):", score_word("BLUE"))

    # 7) Словарь player_to_words по таблице
    player_to_words = {
        "player1": ["BLUE", "TENNIS", "EXIT"],
        "wordNerd": ["EARTH", "EYES", "MACHINE"],
        "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
        "Prof Reader": ["ZAP", "COMA", "PERIOD"],
    }

    # 8) Пустой словарь player_to_points
    player_to_points = {}

    # 9-12) Заполняем player_to_points итоговыми очками игроков
    player_to_points = update_point_totals(player_to_words)

    # 12) Выводим текущее положение
    print("\nТекущие очки игроков (player_to_points):")
    print(player_to_points)

    # ---- Дополнительно (пример использования play_word) ----
    # Добавим слово игроку и пересчитаем:
    play_word("player1", "scrabble", player_to_words)  # нижний регистр тоже поддерживается
    player_to_points = update_point_totals(player_to_words)

    print("\nПосле play_word('player1', 'scrabble'):")
    print(player_to_points)


if __name__ == "__main__":
    main()
