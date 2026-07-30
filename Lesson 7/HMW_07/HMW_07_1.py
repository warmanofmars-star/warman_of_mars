import re

def is_positive_less_than_300(value):
    # Шаблон разбит на три логические части через оператор | (ИЛИ)
    pattern = r"^([1-9]|[1-9]\d|[12]\d\d)$"
    return bool(re.search(pattern, str(value)))

# Проверки (Подходят)
print(is_positive_less_than_300("1"))    # True
print(is_positive_less_than_300("15"))   # True
print(is_positive_less_than_300("99"))   # True
print(is_positive_less_than_300("100"))  # True
print(is_positive_less_than_300("299"))  # True

# Проверки (Не подходят)
print(is_positive_less_than_300("0"))      # False
print(is_positive_less_than_300("03"))     # False
print(is_positive_less_than_300("300"))    # False
print(is_positive_less_than_300("-5"))     # False
print(is_positive_less_than_300("3.14"))   # False
print(is_positive_less_than_300("abc"))    # False