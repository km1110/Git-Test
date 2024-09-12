class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def greet(self):
        return f"Hello, {self.name}! i am {self.age} years old."
