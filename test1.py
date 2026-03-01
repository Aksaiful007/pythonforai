#trying to create a class in python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} the {self.breed} says Woof!"
print(Dog(name="Buddy", breed="Golden Retriever").bark())
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")
print(dog1.bark())
print(dog2.bark())