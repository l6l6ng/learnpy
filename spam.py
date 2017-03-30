class Spam1:
    __egg = 7
    def print_egg(self):
        print self.__egg

s = Spam1()
s.print_egg()
print s._Spam1__egg
# print s.__egg