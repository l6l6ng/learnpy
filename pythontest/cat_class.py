class Cat:
    def __init__(self,color,legs):
        self.color = color
        self.legs = legs

    def bark(self):
        print('Woo')

felix = Cat("ginger",4)
rover = Cat("dog-colored",4)
stumpy = Cat("brown",3)

print felix.color
felix.bark()