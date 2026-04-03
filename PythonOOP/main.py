class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof")

dog1 = Dog()
dog1.bark()