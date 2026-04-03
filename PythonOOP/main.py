class Dog:
    # Constructor - Bu nesne yaratılıcaksa bu şartlara uymak zorunda
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof")

dog1 = Dog("bruce","scottish")
print(dog1.name)
print(dog1.breed)
dog1.bark()