class Pizza(object):
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowd(self):
        return False


pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowd)
pizza.pineapple_allowd = True
print pizza.pineapple_allowd