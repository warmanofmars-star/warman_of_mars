# Task 1
def print_list_reverse(lst):
    # Проверяем, что аргумент — это именно список (отсекает None и другие типы)
    # и что список не пустой (len(lst) == 0 отсекается через not lst)
    if type(lst) is not list or not lst:
        print("Wrong list")
        return

    # Выводим список в обратном порядке с помощью среза
    print(lst[::-1])


# Проверки:
print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse([])
print_list_reverse(None)
print_list_reverse("123")

print("********************************************************************************")


# Task 2
def is_valid_point(point):
    # 1. Проверка на None и пустой кортеж
    if point is None or point == ():
        return None

    # 2. Проверка, что это именно кортеж
    if type(point) is not tuple:
        return False

    # 3. Проверка длины (ровно 2 элемента)
    if len(point) != 2:
        return False

    # 4. Проверка типов внутри кортежа (строго int или float, исключая bool)
    x, y = point
    if type(x) not in (int, float) or type(y) not in (int, float):
        return False

    return True


# Проверки:
print(is_valid_point((3, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))

print("********************************************************************************")


# Task 3
def print_sublist_reverse(lst, start, finish):
    # Проверяем сам список
    if type(lst) is not list or not lst:
        print("Wrong args")
        return

    # Проверяем, что индексы - целые числа (строго int)
    if type(start) is not int or type(finish) is not int:
        print("Wrong args")
        return

    # Проверяем выход за пределы и логику индексов
    if start < 0 or finish >= len(lst) or start > finish:
        print("Wrong args")
        return

    # Делаем копию списка, чтобы не менять исходный объект
    result = lst.copy()

    # Вырезаем нужный кусок (finish + 1, чтобы включить finish),
    # разворачиваем его и вставляем на то же место
    result[start:finish + 1] = result[start:finish + 1][::-1]

    print(result)


# Проверки:
print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([1, 2, 3], "0", 2)
print_sublist_reverse([1, 2], 0, 5)

print("********************************************************************************")


# Task 4
def get_students_by_grade(students):
    # Проверяем на None, пустой словарь и соответствие типу dict
    if type(students) is not dict or not students:
        return {}

    result = {}

    # .items() отдает нам пары (ключ, значение)
    for student, grade in students.items():
        # Если такой оценки еще нет в новом словаре, создаем под нее пустой список
        if grade not in result:
            result[grade] = []

        # Добавляем имя студента в список оценок
        result[grade].append(student)

    return result


# Проверки:
data = {"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}
print(get_students_by_grade(data))

print(get_students_by_grade({}))
print(get_students_by_grade(None))
print(get_students_by_grade(123))
