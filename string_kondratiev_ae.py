favour_word = "Python"   # можешь заменить на своё любимое слово
print(favour_word)

first_name = "Виталий"
last_name = "Красилов"

# первые 5 букв фамилии
new_account = last_name[:5]

# с 3-й по 6-ю буквы фамилии (в Python: индекс 2..5 => last_name[2:6])
temp_password = last_name[2:6]

print("first_name:", first_name)
print("last_name:", last_name)
print("new_account:", new_account)
print("temp_password:", temp_password)

def account_generator(first_name: str, last_name: str) -> str:
    return first_name[:3] + last_name[:3]

new_account = account_generator("Виталий", "Красилов")
print("new_account:", new_account)

def password_generator(first_name: str, last_name: str) -> str:
    return first_name[-3:] + last_name[-3:]

temp_password = password_generator("Виталий", "Красилов")
print("temp_password:", temp_password)


company_motto = "Мечты сбываются"

second_to_last = company_motto[-2]   # предпоследний символ
final_word = company_motto[-4:]      # последние 4 символа

print("company_motto:", company_motto)
print("second_to_last:", second_to_last)
print("final_word:", final_word)


first_name = "Bob"  # допустим, так ошибочно прислали

# Попытка изменить символ строки (вызовет ошибку TypeError)
try:
    first_name[0] = "R"
except TypeError as e:
    print("Ошибка:", e)

# Правильное исправление через создание новой строки
fixed_first_name = "R" + first_name[1:]
print("fixed_first_name:", fixed_first_name)

password = "theycallme\"crazy\"91"
print(password)

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print("poem_title:", poem_title)
print("poem_title_fixed:", poem_title_fixed)
print("poem_author:", poem_author)