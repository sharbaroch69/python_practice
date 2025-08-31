class calculator:
    def __init__(self, num):
        self.num = num
    def square(self):
        return (f"The square of {self.num} is {self.num ** 2}")
    def cube(self):
        return (f"The cube of {self.num} is {self.num ** 3}")
    def square_root(self):
        return (f"The square root of {self.num} is {self.num ** 0.5}")

a = calculator(4)
print(a.square())
print(a.cube())
print(a.square_root())
