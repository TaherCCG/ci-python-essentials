# Creating Class Instances

# You can create multiple instances of a class. An instance is an individual object of the class in memory. It exists live in RAM until the point it is removed.

"""
Let's return to the Bird class. When you create an instance of the class, it is the initializer code that runs. This is the __init__ method.
This method assigns the values to the object properties. The self keyword is a reference to the current instance of the class and is used to 
access variables that belong to the class. To create an instance of the class, you need to provide the same quantity of values as there are 
properties (in this case two). Once you have an instance of that class, you can access the variables and methods using the dot notation.

owl = Bird('Owl', 'Twit Twoo!')
owl.call
owl.description()


The dot notation can also be used to modify the properties of objects with the use of the assignment operator. The del keyword can be used 
to delete a property or an object. Try creating and editing other instances of the Bird class.
"""

# Runnable Example:

class Bird:
    """
    Bird class
    """
    def __init__(self, kind, call):
        #properties
        self.kind = kind
        self.call = call

    #behaviour
    def description(self):
        """
        describe the bird
        """
        return f"A {self.kind} goes {self.call}" 
    
    def bird_call(self):
        print(self.call.upper())

owl = Bird('Owl', 'Twit Twoo!')
print(owl.call)
print(owl.description())
crow = Bird('Crow', 'Caaaw!')
print(crow.description())
owl.call = 'screech'
print(owl.description())
pigeon = Bird('Pigeon', 'Coo')
print(pigeon.description())