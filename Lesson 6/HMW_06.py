#Task 1
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
       return f"{self.name} works as {self.position} and earns {self.salary}"

# Создаем двух сотрудников
emp1 = Employee("Anna", "QA Engineer", 7000)
emp2 = Employee("Maxim", "Test Automation Engineer", 8500)

# Выводим информацию
print(emp1.get_info())
print(emp2.get_info())

print("*" *15)

#Task 2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        # Проверяем, достаточно ли товара на складе
        if amount <= self.quantity:
            self.quantity -= amount
            return None # Успешная покупка ничего не возвращает
        else:
            return "Not enough products" # Ошибка, если просят слишком много

# Проверяем работу класса
laptop = Product("MacBook", 1500, 5)

print(laptop.buy(2))
print("Remaining balance after purchase 2:", laptop.quantity)

print(laptop.buy(10))
print("The balance has not changed.:", laptop.quantity)

print("*" *15)

#Task 3
# Базовый класс
class Vehicle:
    def move(self):
        return "Vehicle is moving"

# Дочерний класс Car наследуется от Vehicle
class Car(Vehicle):
    def move(self):
        return "Car is driving"

# Дочерний класс Bicycle наследуется от Vehicle
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is riding"

# Проверка
my_car = Car()
my_bike = Bicycle()
generic_vehicle = Vehicle()

print(generic_vehicle.move())
print(my_car.move())
print(my_bike.move())

print("*" *15)

#Task 4
class User:
    # Атрибут класса (общий для всех объектов этого класса)
    country = "Israel"

    def __init__(self, username, age):
        # Атрибуты экземпляра (уникальные для каждого объекта)
        self.username = username
        self.age = age

# Создаем трех пользователей
user1 = User("Alice", 28)
user2 = User("Bob", 32)
user3 = User("Charlie", 25)

print("--- До изменения ---")
print(f"User: {user1.username}, Age: {user1.age}, Country: {user1.country}")
print(f"User: {user2.username}, Age: {user2.age}, Country: {user2.country}")
print(f"User: {user3.username}, Age: {user3.age}, Country: {user3.country}")

# Меняем атрибут на уровне всего класса

User.country = "Canada"

print("\n--- После изменения ---")
print(f"User: {user1.username}, Age: {user1.age}, Country: {user1.country}")
print(f"User: {user2.username}, Age: {user2.age}, Country: {user2.country}")
print(f"User: {user3.username}, Age: {user3.age}, Country: {user3.country}")