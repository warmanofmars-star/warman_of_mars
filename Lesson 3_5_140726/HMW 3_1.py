# Task 1
def create_profile(name, age=18, city='Unknown'):
    # Возвращаем словарь с переданными или дефолтными значениями
    return {
        "name": name,
        "age": age,
        "city": city
    }


print(create_profile("Anna"))
print(create_profile("Tom", 25))
print(create_profile(city="Haifa", name="Maria"))

print("*" * 15)


# Task 2
def sum_even_numbers(*numbers):
    # filter оставит только те числа, для которых условие n % 2 == 0 истинно
    even_numbers = filter(lambda n: n % 2 == 0, numbers)
    return sum(even_numbers)


print(sum_even_numbers(1, 2, 3, 4, 5, 6))
print(sum_even_numbers(7, 9))
print(sum_even_numbers())


# другой вариант (вспомнил функцию sum())
def sum_even_numbers(*numbers):
    return sum(n for n in numbers if n % 2 == 0)


print("*" * 15)


# Task 3
def print_pet_info(name, **info):
    print(f"Name: {name}")

    # Проверяем, есть ли что-то в словаре info
    if not info:
        print("No additional information")
    else:
        # Если словарь не пустой, проходимся по его парам ключ-значение
        for key, value in info.items():
            print(f"{key}: {value}")


print_pet_info("Lucky", age=4, color="White", breed="Spitz")
print("-" * 15)
print_pet_info("Lucky")

print("*" * 15)


# Task 4
def merge_lists(*lists):
    # Создаем пустой список, в который будем собирать результаты
    result = []

    # Проходимся по каждому переданному списку из кортежа lists
    for lst in lists:
        # Метод .extend() распаковывает список и добавляет его элементы в конец result
        # (более продвинутая версия метода .append(), который в нашем случае создал просто
        # список в списке)
        result.extend(lst)

    return result


print(merge_lists([1, 2], [3], [4, 5], []))
print(merge_lists())

print("*" * 15)


# Task 5
def build_message(*words, separator=" "):
    # Метод строк .join() берет разделитель и склеивает им элементы последовательности
    return separator.join(words)


print(build_message("Hello", "world"))
print(build_message("2026", "07", "15", separator="-"))


