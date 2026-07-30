import re

def is_israel_mobile(phone):
    pattern = r"^(?:\+972|0)5\d(?:-?\d){7}$"
    return bool(re.search(pattern, phone))

# Проверки (Подходят)
print(is_israel_mobile("0541234567"))        # True
print(is_israel_mobile("054-1234567"))       # True
print(is_israel_mobile("+97254-123-4567"))   # True
print(is_israel_mobile("058-12-34-567"))     # True

# Проверки (Не подходят)
print(is_israel_mobile("54-1234567"))        # False
print(is_israel_mobile("054--12-4567"))      # False (два дефиса подряд)
print(is_israel_mobile("+972054-123-4567"))  # False (лишний 0 после +972)
print(is_israel_mobile("97254-123-4567"))    # False (нет плюса)