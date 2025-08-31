# multilevel inheritance example:
class employee:
    a = 5

class programmer(employee):
    b = 10

class manager(programmer):
    c = 15

o = manager()
print(o.b)
print(o.a)
print(o.c)
print(manager.a)  # accessing class attribute using class name
print(programmer.a)  # accessing class attribute using class name
print(employee.a)  # accessing class attribute using class name
