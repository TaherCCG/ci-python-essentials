# Class Composition & Mixins Challenge

class TicketMixin:
    """Mixin to calculate ticket price based on age"""
    def calculate_ticket_price(self, age):
        if self.age < 12:
            return 0
        elif self.age < 18:
            return 15
        elif self.age < 60:
            return 20
        else:
            return 10
    
class Customer(TicketMixin):
    """Create instance of Customer"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describe(self):
        price = self.calculate_ticket_price(self.age)
        return f"{self.name} age {self.age} ticket price is {price}"
        
customer = Customer("Ryan Phillips", 22)

print(customer.describe())


