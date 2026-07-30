import re

def is_number_from_1_to_255(value):
    pattern = r"^([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"
    return bool(re.search(pattern, str(value)))

# Проверки (Подходят)
print(is_number_from_1_to_255("1"))    # True
print(is_number_from_1_to_255("25"))   # True
print(is_number_from_1_to_255("100"))  # True
print(is_number_from_1_to_255("255"))  # True

# Проверки (Не подходят)
print(is_number_from_1_to_255("0"))       # False
print(is_number_from_1_to_255("256"))     # False
print(is_number_from_1_to_255("025"))     # False
print(is_number_from_1_to_255("-12.5"))   # False