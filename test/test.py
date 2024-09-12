class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def greet(self):
        return f"Hello, {self.name}! i am {self.age} years old."
