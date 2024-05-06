# The "self" Keyword

# The self keyword is used to refer to the instance of the class. It is used to access variables that belong to the class.

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
    
owl = Bird('Owl', 'Twit Twoo!')
print(owl.description())

# This example of a class Bird has properties of kind and call. A function (or method) to describe the bird is included in the class.