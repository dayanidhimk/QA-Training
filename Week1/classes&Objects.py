class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Dog's name: {self.name}\nDog's age: {self.age}")
    

dog1 = Dog("Tommy", 5)
dog1.details()