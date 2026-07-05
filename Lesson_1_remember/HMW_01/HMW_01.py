# Case 1
def print_string_reverse(s):
    # Проверяем, что s не None.
    # Затем метод .strip() удаляет пробелы по краям.
    # Если после удаления пробелов строка пустая, значит она состояла только из них (или пустая).
    if s is None or s.strip() == "":
        print("Wrong string")
    else:
        print(s[::-1])


# Проверка:
print_string_reverse("Shalom")
print_string_reverse("   ")
print_string_reverse(None)

print ("*******************************************************************************")
# Case 2
def is_isr_phone_number(phone):
    # Базовая проверка на None и пустоту
    if phone is None or phone.strip() == "":
        return None

    # Проверяем сразу три условия:
    # 1. Длина ровно 10 символов
    # 2. Начинается на '0'
    # 3. Состоит только из цифр (метод .isdigit())
    if len(phone) == 10 and phone.startswith('0') and phone.isdigit():
        return True

    # Если хотя бы одно условие не выполнено, возвращаем False
    return False


# Проверки:
print(is_isr_phone_number("0521234567"))
print(is_isr_phone_number("521234567"))
print(is_isr_phone_number("05212345a7"))
print(is_isr_phone_number(""))


print ("********************************************************************************")
#Case 3
def print_substring_reverse(s, start, finish):
    # 1. Проверка на None и пустую строку
    if s is None or s.strip() == "":
        print("Wrong args")
        return

    # 2. Проверка индексов:
    # - start не должен быть меньше 0
    # - finish не должен выходить за пределы строки (len(s) - 1 — это максимальный индекс)
    # - start не должен быть больше finish
    if start < 0 or finish >= len(s) or start > finish:
        print("Wrong args")
        return

    # Разрезаем строку на три части:
    prefix = s[:start]  # До начала реверса
    reversed_part = s[start:finish + 1][::-1]  # Часть для реверса
    suffix = s[finish + 1:]  # После реверса

    # Склеиваем и выводим
    print(prefix + reversed_part + suffix)


# Проверки:
print_substring_reverse("Shalom", 1, 3)
print_substring_reverse("Shalom", 3, 1)
print_substring_reverse("Shalom", 0, 10)


print ("********************************************************************************")
#Case 4
def get_words_reverse(s):
    # На случай, если передадут None или пустую строку, чтобы код не упал с ошибкой
    if not s or not s.strip():
        return s

    # .split() по умолчанию разбивает строку по пробелам и возвращает список слов
    words = s.split()

    # Разворачиваем список слов задом наперед с помощью [::-1]
    # и склеиваем их обратно в строку через пробел с помощью " ".join()
    return " ".join(words[::-1])


# Проверка:
print(get_words_reverse("Hello my nice world"))


print ("********************************************************************************")
#Case 5
def print_words_reverse_in_column(s):
    if not s or not s.strip():
        return

    # Разбиваем строку на список слов
    words = s.split()

    # Итерируемся по каждому слову
    for word in words:
        # Печатаем текущее слово, предварительно развернув его
        print(word[::-1])


# Проверка:
print_words_reverse_in_column("Hello my nice world")
