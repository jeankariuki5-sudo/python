# Class - This is a blueprint/template that is used to create objects
# we create a class using keyword class followed by the class name
# OOP is a programing paradigm which contains variables/properties/ x-tics/ attributes and functions/methods/behaviors/action together for easy maintenance and management of code
# A class simply wraps the functions and variables and you can access the fuctions without and variables only through the object from that class

class farmer:
    # Constructor - This is a special method that automatically runs whenever an object is created

    # it's written using __init__()
    # It referes to the current object being created

    def __init__(self):
        
        # Attributes- These are just variables that belong to an object
        # They are ussually written inside the constructor
        self.name = "John"
        self.litres = 50

    # Method - this is just a function inside a class. They define what an object can do
    # They use the self parameter to access the object attribute

    def display_info(self):
        print(f"Farmer name: {self.name}")
        print(f"Milk delivered: {self.litres}")
    
# Object is an instance of a class
# So we feed objects to access attributes and methods of the class
farmer1 = farmer()
farmer2 = farmer()

# Now using farmer 1 obj we can access attributes and methods in the farmer() class
farmer1.display_info()
farmer2.display_info()