class Dog:
    # Constructor - Bu nesne yaratılıcaksa bu şartlara uymak zorunda
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof")

class Owner:
    def __init__(self,name,address, number):
        self.name = name
        self.address = address
        self.number = number

owner1 = Owner("Sadik","Mersin","+9085")
dog1 = Dog("bruce","scottish",owner1)
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name)
dog1.bark()