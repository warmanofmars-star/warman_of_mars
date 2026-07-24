class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "..."

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

