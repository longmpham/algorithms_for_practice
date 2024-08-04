class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")
        
    def make_sound(self):
        print("I am making a sound")
        
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self) # boiler plate init for inheritance
        print("Dog created")
    
    def make_sound(self): # this method overwrites the super class Animal's make_sound def
        print("RUFF RUFF")
        
myanimal = Dog()
myanimal.make_sound()