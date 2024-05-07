# Class Composition

# Inheritance is not always the best way to reuse code. Sometimes, you may want to use a class within another class without 
# the need for inheritance. This is known as class composition

"""
In object-orientated programming, two significant concepts are inheritance and composition.

Inheritance is what we have used up until now in this lesson. For example, a subclass Parrot inherits from a Bird class. 
The inheritance relationship, in this case, is that a Parrot is a Bird. Any code where you use class Bird you could equally 
use class Parrot without changing the desired outcome of your program.

Composition is where one class contains the object of another class. In this case, we could have a Bird class and a Tail class. 
The composition relationship here would be that a Parrot has a tail so would inherit from both Bird and Tail. However, a Kiwi 
does not have a tail, so would only inherit from Bird. That way, you can have a Duck and a Parrot class that reuse Tail but are 
themselves not derived from each other. A Parrot is not a Duck, but both of them have a Tail. With composition, you cannot use 
class Tail interchangeably with Bird. The Tail class is not a subclass of Bird.

The purpose of both mixin and composite is to reduce the amount of unnecessary duplication of code. With the Bird example, you 
can have many bird subclasses, but if some of them share certain properties, then there is the opportunity to move them into a 
class with a composite relationship. You could, for example, reuse the Tail class in another program where you have a Reptile base class.
"""

print("Runnable Example: 1")
# Runnable Example: 1

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Engine:
    def __init__(self, capacity, fuel):
        self.capacity = capacity
        self.fuel = fuel
    
class InternalCombustion(Vehicle, Engine):
    def __init__(self, make, model, capacity, fuel):
        Vehicle.__init__(self, make, model)
        Engine.__init__(self, capacity, fuel)
        
class Electric(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, make, model)
        
volkswagen = InternalCombustion("Volkswagen", "Golf", 1.7, "Diesel")
tesla = Electric("Tesla", "X")

print(volkswagen.make)
print(tesla.make)

print("\n\n\n")
"""
In this example, Electric inherits from Vehicle. Therefore the tesla object is a Vehicle. However, InternalCombustion class has a 
composition relationship with Engine. The volkswagen has an engine, but it is not an engine. The Engine class could be reused for a 
PowerBoat class without PowerBoat and InternalCombustion being derived from one another.

In the runnable example, we extend our simple Human Resources application. The first additional class is ExternalContract for employees 
who are not direct employees of the company but are contract employees. This has an instance attribute to take the cost of the contract 
and a method that returns that added to the employee salary.

Finally, we have the ContractDeveloper class. This is for developers who are not direct employees. This has a composition relationship 
with ExternalContract. A contract developer has an external contract. A direct developer does not. You can reuse this ExternalContract 
for any other job class you create. Here we have also included the HolidayMixin. This class uses composition and mixin. The method details 
for ContractDeveloper inherits from Employee but also provides for the cost of the contract.

We have instantiated two developers here, one direct and one contract. See how their details differ. Also, we use the method from the 
mixin to see how much annual leave they have accrued. For the direct developer, you can also call the method to see their salary.
"""

print("Runnable Example: 2")
# Runnable Example: 2

class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, fname, sname, no_of_years):
        # instance attribute
        self.fname = fname
        self.sname = sname
        self.no_of_years = no_of_years
        Employee.employee_no +=1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"First Name: {self.fname}\n Surname: {self.sname}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"

class ExternalContract:
    """
    Class for contract employees
    """

    def __init__(self, contract_cost):
        self.contract_cost = contract_cost

    def cost(self):
        """
        Returns the contract cost added to the salary
        """
        return self.contract_cost + 30000


class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    """
    def calculate_holidays(self, no_of_years):
        """
        Returns holidays as an integer
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if self.no_of_years < 3:
            bonus = holidays + 1
        elif self.no_of_years <= 5:
            bonus = holidays + 2
        elif self.no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class. 
    """
    def __init__(self, fname, sname, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, fname, sname, no_of_years)

    def calculate_salary(self):
        """
        Returns salary plus bonus as an integer
        """
        base = 30000
        if self.prog_language.lower() == 'python':
            bonus = base * 0.10
        else:
            bonus = 0
        return base + bonus

    def details(self):
        """
        Method to return direct developer details as a string
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}'


class ContractDeveloper(HolidayMixin, Employee, ExternalContract):
    """
    Class is subclass of Employee, composition relationship
    with ExternalContract and using HolidayMixin
    """
    def __init__(self, fname, sname, no_of_years, prog_language, contract_cost):
        self.prog_language = prog_language
        self.contract_cost = contract_cost
        Employee.__init__(self, fname, sname, no_of_years)   

    def details(self):
        """
        Returns inherited details plus contract cost
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}\n Contract cost: {ExternalContract.cost(self)}'


dev = DirectDeveloper("Eric", "Praline", 2, "python")
# There is no composition relationship here. A DirectDeveloper is an Employee
print(dev.details())
print(dev.calculate_holidays(dev.no_of_years))
print(f'${dev.calculate_salary()}')

contractor = ContractDeveloper("Luigi", "Vercotti", 10, "python", 100000)
# When the contractor details are printed the Contract cost is obtained from ExternalContract class
# There is a composition relationship as contractor has an ExternalContract
# However, an external contract is not an employee
# ExternalContract is an object that could be reused by many other objects. 
print(contractor.details())
# The mixin can also be used
print(contractor.calculate_holidays(contractor.no_of_years))




