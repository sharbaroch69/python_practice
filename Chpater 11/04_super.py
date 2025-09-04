# multilevel inheritance example:
class employee:
    a = 5  # class attribute
    def __init__(self):
        print("The constructor of employee")


class programmer(employee):
    def __init__(self):
        super().__init__()
        print("The constructor of programmer")
        self.b = 10

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("The constructor of manager")
        self.c = 15

o = manager()
# print(o.b)
# print(o.a)
# print(o.c)
print(manager.a)  # accessing class attribute using class name
# print(programmer.a)  # accessing class attribute using class name
# print(employee.a)  # accessing class attribute using class name
# print("--------------------------------------------------")