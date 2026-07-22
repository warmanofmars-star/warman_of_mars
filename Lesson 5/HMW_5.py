#Task 1
def get_list_element(items, index):
    try:
        # Пытаемся получить элемент по индексу
        return items[index]
    except IndexError:
        # Перехватываем ошибку отсутствия индекса
        return "Index is out of range"

# Проверка:
numbers = [10, 20, 30]
print("Задача 1:")
print(get_list_element(numbers, 1))
print(get_list_element(numbers, 10))


#Task 2
def get_user_data(user, key):
    try:
        # Пытаемся получить значение по ключу
        return user[key]
    except KeyError:
        # Перехватываем ошибку отсутствующего ключа
        return "Key was not found"

# Проверка:
user = {
    "name": "Anna",
    "age": 30
}
print("\nЗадача 2:")
print(get_user_data(user, "name"))
print(get_user_data(user, "email"))


#Task 3
def calculate_average(first_value, second_value):
    try:
        # Преобразуем оба значения в числа (используем float, чтобы работало и с дробями)
        num1 = float(first_value)
        num2 = float(second_value)
        return (num1 + num2) / 2
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"

# Проверка:
print("\nЗадача 3:")
print(calculate_average("10", "20"))
print(calculate_average("hello", "20"))
print(calculate_average(None, 20))


#Task 4
def read_number():
    try:
        user_input = input("Enter a number: ")
        # Пытаемся преобразовать введенное значение в целое число
        number = int(user_input)
    except ValueError:
        # Этот блок сработает только при ошибке преобразования
        print("Invalid number")
    else:
        # Этот блок сработает ТОЛЬКО если код в try выполнился успешно (без ошибок)
        print("Number was entered successfully")
    finally:
        # Этот блок сработает В ЛЮБОМ СЛУЧАЕ (успешно или с ошибкой)
        print("Program finished")

# Проверка (закомментирована, чтобы не останавливать выполнение):
#print("\nЗадача 4:")
#read_number()


#Task 5
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is not realistic")

    # Если проверки пройдены, можем просто вывести сообщение или вернуть True
    print(f"Age {age} is valid.")


# Проверка:
print("\nЗадача 5:")
try:
    validate_age(-5)
except ValueError as e:
    print(f"Поймали ошибку: {e}")

try:
    validate_age(150)
except ValueError as e:
    print(f"Поймали ошибку: {e}")

validate_age(25)