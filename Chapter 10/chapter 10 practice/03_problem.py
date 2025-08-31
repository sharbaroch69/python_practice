class demo:
    a = 4

o = demo()
print(o.a) # prints the class attribute becuase instance attribute is not present
o.a = 0 # instance attribute created
print(o.a) # prints the instance attribute
print(demo.a) # prints the class attribute means instance attribute cant change class attribute
