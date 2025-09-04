class number:
    def __init__ (self, n):
        self.n = n
    def __add__ (self, num):
        return self.n + num.n
    
n = number(5)
m = number(4)
print(n + m)

'''
Operators in Python can be overloaded using the following methods:
p1+p2 # p1._add_(p2)
p1-p2 # p1.sub_(p2)
p1*p2 # p1.mul_(p2)
p1/p2 # p1.truediv_(p2)
p1//p2 # p1. _ floordiv_ (p2)
'''