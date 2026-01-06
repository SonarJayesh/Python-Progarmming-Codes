"""
Qs. Create a class called Order which stores item & its price.
Use Dunder function_gt__() to convey that:
order1 > order2 if price of order1 > price of order2
"""

class Order:
    def __init__(self,itemName,itemPrice):
        self.itemName = itemName
        self.itemPrice = itemPrice

    def __gt__(self, order2):
        return self.itemPrice > order2.itemPrice


order1 = Order("Chips",20)
order2 = Order("Coffie",15)

print(order1 > order2)