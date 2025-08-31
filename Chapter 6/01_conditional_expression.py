"""
A conditional expression (also known as the ternary operator) in Python allows you to 
assign a value to a variable based on a condition in a single line.
Syntax: value_if_true if condition else value_if_false
"""
# x = value_if_true if condition else value_if_false


a = int(input("Enter your age: "))
print("You are eligible to vote" if a >= 18 else ("Invalid age entered" if a <= 0 else "You are not eligible to vote"))

# another way to write this code is:
if a >= 18:
    print("You are eligible to vote")
    print("Good Luck")
else:
    print("You are not eligible to vote")
