import re

def is_valid_time(time):
    pattern = r"^([01]\d|2[0-3]):[0-5]\d$"
    return bool(re.search(pattern, time))

# Проверки (Подходят)
print(is_valid_time("00:00"))  # True
print(is_valid_time("09:30"))  # True
print(is_valid_time("14:45"))  # True
print(is_valid_time("23:59"))  # True

# Проверки (Не подходят)
print(is_valid_time("24:00"))   # False
print(is_valid_time("12:60"))   # False
print(is_valid_time("8:30"))    # False (нет ведущего нуля)
print(is_valid_time("123:45"))  # False
print(is_valid_time("12-30"))   # False