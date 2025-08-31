def morning():
    print("Good morning")

morning()
# this is normal function


#  now function with parameters or arguments
def morning(name):
    print(f"Good morning, {name}!")

# calling the function with arguments
morning("Harry")
morning("Rohan")


# we can use multiple arguments
def morning(name, time):
    print(f"Good morning, {name}! Its {time}")

# calling the function with multiple arguments
morning("Harry", "8 AM")
morning("Rohan", "9 AM")


# use of return
# 1st example
def morning(name, time):
    print(f"Good morning, {name}! Its {time}")
    return time


a = morning("Harry", "8 AM")
print(a)

# 2nd example
def morning(name, time):
    return f"Good morning, {name}! Its {time}"


b = morning("Rohan", "9 AM")
print(b)