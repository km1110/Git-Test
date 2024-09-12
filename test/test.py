class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def greet(self):
        return f"Hello, {self.name}! i am {self.age} years old."

    def grow(self):
        self.age += 1
        if self.age < 10:
            self.height += 2
        elif self.age < 20:
            self.height += 1

    def eat(self):
        self.weight += 1

    def exercise(self):
        self.weight -= 1
        if self.age < 10:
            self.height += 1
