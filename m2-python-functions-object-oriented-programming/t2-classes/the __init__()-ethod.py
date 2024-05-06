"""The __init__() Method

The first thing to note is that a function within a class is known as a method. A particular type of method that runs when
an instance of the class is created is an initializer. The __init__ method is known as a dunder, double-underscore or magic
method, and these tend to be used on classes mainly. They use double underscores so as not to conflict with your own defined 
classes.

An __init__() method on its own would simply create an empty class object. However, an __init__() method can take arguments. 
One of the advantages of object-orientated programming is the ability to model the real world in code. If you were writing 
software to use in a car factory or dealership, you could use a class to create an object Car that has the same properties 
and attributes as a real car.

In the runnable example, we have initialized a Car object with attributes 'Green', 'Ford', 'Mustang' and 'Gasoline'.
Note the use of the self keyword. The next unit will explain this further.

"""

# Runnable Example:

class Car:
	def __init__(self, color, make, model, fueltype):
		self.color = color
		self.make = make
		self.model = model
		self.fueltype = fueltype

bullitt = Car('Green', 'Ford', 'Mustang', 'Gasoline')