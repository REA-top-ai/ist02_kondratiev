def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с названием " + title + " with " + str(row_count) + " lines")


# 2) Вызов с title "Загрузки"
create_spreadsheet("Загрузки")

# 5) Вызов с title "Приложения" и row_count = 10
create_spreadsheet("Приложения", 10)
