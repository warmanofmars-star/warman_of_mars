#Taks 1
def save_shopping_list(items):
    # Открываем файл на запись ("w" - write) с явным указанием кодировки utf-8
    with open("shopping.txt", "w", encoding="utf-8") as file:
        # Проходим циклом по всем элементам списка
        for item in items:
            # Записываем элемент и добавляем символ переноса строки \n
            file.write(f"{item}\n")

items = ["Milk", "Bread", "Apples", "Coffee"]
save_shopping_list(items)


#Task 2
import csv

with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Anna", "21"])
    writer.writerow(["Tom", "19"])
    writer.writerow(["Kate", "22"])

def read_students(filename):
    with open(filename, "r", encoding="utf-8") as file:
        # DictReader автоматически читает первую строку как ключи словаря
        reader = csv.DictReader(file)

        # Перебираем строки. Каждая строка (row) теперь является словарем
        for row in reader:
            print(f"Student: {row['name']} ({row['age']})")


read_students("students.csv")


#Task 3
import json

def save_profile(name, age, city):
    # Формируем словарь из переданных аргументов
    profile_data = {
        "name": name,
        "age": age,
        "city": city
    }

    # Открываем файл profile.json на запись
    with open("profile.json", "w", encoding="utf-8") as file:
        # dump() записывает словарь Python прямо в файл
        json.dump(profile_data, file, indent=4, ensure_ascii=False)


save_profile("Maria", 30, "Haifa")



#Task 4
from pathlib import Path

def create_reports_folder():
    # Создаем объект пути для нашей новой папки
    folder_path = Path("reports")

    # Создаем саму папку физически.
    # exist_ok=True не даст программе упасть с ошибкой, если папка уже существует
    folder_path.mkdir(exist_ok=True)

    # С помощью слэша (/) мы "приклеиваем" имя файла к пути папки
    file_path = folder_path / "result.txt"

    # Открываем файл по сформированному пути и записываем строку
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Homework completed successfully!\n")


create_reports_folder()