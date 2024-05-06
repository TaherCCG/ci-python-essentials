# Functions + Classes: Methods

# In Python, a method is a function that belongs to an object. It is a function that could be called on an object.

"""Functions and Classes: Methods

A method is a function that is within a class or object. When you have seen the term method used in the lessons so far it has 
concerned the built-in methods such as append() for a list. You can create your methods within your classes. When you create 
an instance of that class, then you can call the method using dot notation. In the class instance unit, we used the description 
method on the object owl, which was instantiated from the Bird class. This is referred to as invoking the description() method.
Not all methods in a class need to be public. If you want to indicate to other developers that a method is private, then prefix 
the method name with an underscore. A private method is one that cannot be accessed except within the class. We will use private 
methods in an upcoming unit.


In the runnable example, there is a method that returns a description of the instance. If we create an owl instance, we can call
that method and print the result to the terminal. The class attribute is within the scope of the method so that it can be used. 
However, the parrot variable created in the method is local to the method so it could not be used in the class.

"""

# Runnable Example:

class Bird:
    """
    Bird class
    """
    # class attribute
    definition = "a warm-blooded egg-laying vertebrate animal distinguished by the possession of feathers, wings, a beak, and typically by being able to fly."

    def __init__(self, kind, call):
        # instance attribute
        self.kind = kind
        self.call = call

    def description(self):
        """
        describe the bird
        """
        parrot = "Norwegian Blue"
        return f"A {self.kind} goes {self.call} and is {self.definition} It is not a {parrot}" 


owl = Bird('owl', 'Twit Twoo!')
print(owl.description())