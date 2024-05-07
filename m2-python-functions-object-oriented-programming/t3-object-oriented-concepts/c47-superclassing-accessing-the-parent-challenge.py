# Superclassing: Accessing the Parent Challenge

class BaseOrderItem():
    """
    Creates instance of BaseOrderItem
    """
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
    
    """
    Returns total based on price * quantity ordered
    """
    def total_price(self):
        return self.price * self.quantity

# write your code here

class ShoeOrderItem(BaseOrderItem):
    """Creates instance of ShoeOrderItem"""
    
    def __init__(self, product, price, quantity, size):
        super().__init__(product, price, quantity)
        self.size = size


    def describe(self):
        total_price = self.total_price()
        return f"Order: {self.product} in size {self.size}, quantity: {self.quantity}, total price: {total_price}"
    
shoe_order = ShoeOrderItem("Ladies Nike Trainers", 40, 2, 42)

print(shoe_order.describe())