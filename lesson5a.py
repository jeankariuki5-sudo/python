# inheritace--this allows the child class to inhreit attributes and methods from other classes 
# for inheritance to happen we have a parent class/super class  which the class is being inherted from and the child clas which is inheritiing

# afrer the child class in herits yt will have both the parent attriutes and the methods also its own attributes and methods
# creating an object
class Person:
    # constructor
    def __init__(self, name):
        self.name = name

    # methods display information
    def display_info(self):
        print(f"name of the person is {self.name}")

# child class which is inheriting from the Person class
class Farmer(Person):
    def __init__(self, name, liters):
        # parent constructor being called by the super function
        super().__init__(name)
        # attributes specified to the farmer
        self.liters = liters

    def display_milk(self):
        print(f"farmer's name: {self.name}")
        print(f"milk delivered: {self.liters}")

    # method overriding
    # the child class inherits from the parent class but then impliment the inherited functions on its own way
    def display_info(self):
        print(f"farmer name : {self.name}")

# creating an object
farmer1 = Farmer("john", 56)
farmer1.display_info()
# farmer1.display_milk()

# output before commentiong out
# name of the person is john
# farmer's name: john
# milk delivered: 56