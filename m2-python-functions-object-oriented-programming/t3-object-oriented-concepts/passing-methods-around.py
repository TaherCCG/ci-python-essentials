# Passing Methods Around

"""One thing you may have noticed in the examples is that methods are passed around from superclass or mixin to subclass. 
This is possible in Python as a method is itself an object. Methods are functions within a class so in the same way functions
are passed around so are methods.

If we return to the Parrot example, we see that we can use the description method belonging to the Bird class with an instance
of the Parrot class. The method has been passed from the superclass to the subclass and is available for use by an object 
instantiated from the subclass.
"""

# Runnable Example:
print("Runnable Example:")

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
