# To print the multiplication table of the number in reverse order.
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {11 - i} = {n * (11 - i)}") 
    pass
# This will print the multiplication table of the number in reverse order.
# we used a for loop to iterate through the numbers 1 to 10.
# 11 - i gives us the reverse order of the multiplication table. 
# because we are subtracting the current value of i from 11, 
# which starts at 10 and goes down to 1.



# another way


n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * (i)}")

