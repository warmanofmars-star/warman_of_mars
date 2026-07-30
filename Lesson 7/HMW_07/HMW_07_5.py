import re

def is_israel_car_number(number):
    pattern = r"^(\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3})$"
    return bool(re.search(pattern, number))

# Проверки (Подходят)
print(is_israel_car_number("12-345-67"))    # True
print(is_israel_car_number("99-999-99"))    # True
print(is_israel_car_number("123-45-678"))   # True
print(is_israel_car_number("456-78-901"))   # True

# Проверки (Не подходят)
print(is_israel_car_number("12345678"))     # False (нет дефисов)
print(is_israel_car_number("12:345:67"))    # False (неправильный разделитель)
print(is_israel_car_number("1-234-56"))     # False (неверное количество цифр)
print(is_israel_car_number("1234-56-78"))   # False (неверный формат)