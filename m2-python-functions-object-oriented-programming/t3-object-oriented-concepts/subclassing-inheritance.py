# Subclassing & Inheritance

"""
Inheritance is a way to form new classes using classes that have already been defined. The newly formed classes are called derived classes, 
the classes that we derive from are called base classes. Important benefits of inheritance are code reuse and reduction of complexity of a program. 
The derived classes (descendants) override or extend the functionality of base classes (ancestors).
"""

"""
Subclassing is a useful way of creating a specialised version of a class with its methods but re-using existing methods and properties of 
the parent (or base) class. We could create a Parrot class which subclasses the Bird class created in previous units. We can use the existing 
methods on the parent/base class, and we don’t have to supply the bird kind or call because that’s coded into the Parrot class. To subclass/inherit 
from a superclass/parent, add the name of the parent class inside parentheses as part of the subclass name. To call a method on the parent class, 
precede the parent method name with the parent class name and a period.



Here we’ve created a Parrot class which subclasses Bird. We can use the existing methods on the parent class, and we don’t have to supply the bird 
kind or call because that’s coded into the Parrot class. They are inherited. We can add specialized behaviour such as the additional property of color.
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
        return f"A {self.kind} goes {self.call} and is {self.definition}" 


class Parrot(Bird):
    def __init__(self, color):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.color = color


parrot = Parrot('blue')
print(parrot.color)
print(parrot.description())

