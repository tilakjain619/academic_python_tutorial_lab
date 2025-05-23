#Define classes and create objects in Python. Implement methods and attributes in classes.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

    def info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

dog1.bark()
dog1.info()

dog2.bark()
dog2.info()
