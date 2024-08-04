# the goal of polymorphism is to use classes and inheritance to call on class specific functions with general functions
# that way things "can" be easier to use. For example below, we have Animal as the super class, Dog and Cat are inherited from Animal
# we then define a function pet_speak(Animal) which takes the class 
# as an argument and inside this function we can use the speak() function.


class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says RUFF RUFF"
    
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says MEOW MEOW"

# def pet_speak(pet) -> Animal: # this takes a class type Animal!
def pet_speak(pet): # this takes a class type Animal!
    print(pet.speak())

milo = Dog("milo")
kiki = Cat("kiki")
# print(milo.speak())
# print(kiki.speak())


for pet in [milo, kiki]:
    print(type(pet))
    print(pet.speak())
    pet_speak(pet)