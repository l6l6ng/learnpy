class A:
    def spam(self):
        print 1

class B(A):
    def spam(self):
        print 2
        # super().spam()

b = B()
b.spam()