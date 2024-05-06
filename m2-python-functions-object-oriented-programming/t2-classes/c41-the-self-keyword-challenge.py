# Write your code here
class OrderItem:
    "Creates an instance of OrderItem"
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity
        
    def description(self):
        return f"{self.quantity} x {self.item} at ${self.price} each"
        


# The code below will use your class to print values to the terminal after 
# it has been written. Comment the lines below back in to test it  

order_item_one = OrderItem("bowtie", 10, 3)
print(order_item_one.description())

order_item_two = OrderItem("Fez", 25, 1)
print(order_item_two.description())


