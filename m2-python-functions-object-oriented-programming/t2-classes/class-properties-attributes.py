#Class Properties & Attributes

# Properties are the variables that belong to a class. They are the characteristics of the class. They are accessed using the dot notation.
# Attributes are the variables that belong to an object. They are the characteristics of the object. They are accessed using the dot notation.

"""
A class can contain data. If you create a Python variable within the class, it is known as a class attribute. As it is created outside the 
constructor function, it is shared between all objects of this class. However, if you create a Python variable within the constructor function,
it is known as an instance attribute. An instance attribute is only accessible from the scope of an object instantiated from the class.

When we access these attributes from the class or from the object, they are referred to as properties. A class attribute can be accessed as a 
class property or an instance property. If you try and access an instance attribute as a class property, then you will raise an AttributeError.



In the runnable example, there is both a class attribute of definition and two instance attributes of kind and call. The owl object 
instantiated from the Bird class is able to access the class and instance properties with dot notation. The Bird class, however, 
can only access the class property. Trying to access call gives the following error; AttributeError: type object 'Bird' has no 
attribute 'call'
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
        return f"A {self.kind} goes {self.call}" 

owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())
print(owl.definition)
print(owl.call)
print(Bird.definition)
print(Bird.call)