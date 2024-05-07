# Superclassing: Accessing the Parent

"""We have already looked at how to inherit properties from one class to another. The class that inherits is the subclass. 
Therefore, if you refer to the class, it is inheriting from the superclass. Up till now in this lesson when referring to the 
superclass in a subclass, we have explicitly used the superclass name in front of the inherited attributes or properties. 
To improve the maintainability of your code, use the super() function in place of the superclass name. Therefore, if you ever
change the superclass you only then need to change the argument in the subclass definition not everywhere else in the code.


Let's look at a simple example. When we look at simple shapes, you can see that a square is a special type of rectangle where 
the width and height are the same. How would you show this relationship in object-orientated programming?
"""

# Runnable Example: 1
print("Runnable Example: 1")
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)


"""
As you can see the reference to superclass Rectangle is replaced with the function super() in the subclass Square.

In the runnable example, we return to the Bird classes. You can see the use of super() to denote which instance attributes 
are inherited from the superclass Bird. It is also used in the subclass methods to inherit the superclass description 
method to avoid repetition of code.
"""

# Runnable Example: 2
print("Runnable Example: 2")

class Bird(object):
    """
    Bird superclass
    """
    def __init__(self, kind, call):
        # instance attributes
        self.kind = kind
        self.call = call

    def description(self):
        """
        Returns description string including instance attributes
        """
        return f'A {self.kind} goes {self.call}'


class Fowl(Bird):
    """
    Subclass of the superclass Bird
    """
    def __init__(self, kind, call, type):
        self.fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds that includes\n'
                                       'turkey, grouse, chicken, New World quail and Old World quail,\n'
                                       'ptarmigan, partridge, pheasant, junglefowl and the Cracidae\n',
                           'waterfowl': 'Waterfowl is an order of birds that comprises about 180 living species\n'
                                        'in three families: Anhimidae (the screamers), Anseranatidae\n'
                                        '(the magpie goose), and Anatidae,the largest family, which\n'
                                        'includes over 170 species of waterfowl,\n'
                                        'among them the ducks, geese, and swans.\n'}
        self.type = type
        # Uses super() function to state kind, call from superclass Bird
        super().__init__(kind, call)


    def description(self):
        """
        Returns string from superclass description method and
        appends a string to include additional information
        """
        return f'{super().description()} \nSome interesting facts about the {self.kind} : A {self.kind} is of type {self.type}. {self.fowl_types[self.type.lower()]}'

class Seabird(Bird):
    """
    Subclass of Bird superclass for sea birds
    """
    def __init__(self, kind, call, diving_depth):
        # super() is used to denote what is inherited from Bird
        super().__init__(kind, call)
        self.diving_depth = diving_depth

    def get_description(self):
        """
        Returns description from superclass using super() function
        Appends additional information as a string
        """
        return f'{super().description()} and also, a {self.kind} dives to a depth of {self.diving_depth} metres.'


gannet = Seabird('Gannet', 'Squawk', 3)
print(gannet.get_description())

duck = Fowl('Mallard', 'Quack!', 'Waterfowl')
print(duck.description())