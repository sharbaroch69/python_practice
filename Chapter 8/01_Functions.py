# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))

# average = (a + b + c) / 3
# print(f"The average is: {average}")


# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))

# average = (a + b + c) / 3
# print(f"The average is: {average}")
 

# if we have to perform this operation multiple times, we can define a function.

# function definition
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    average = (a + b + c) / 3
    print(f"The average is: {average}")


# call the function
avg()

# you can call the function multiple times
avg()
avg()
avg()
avg()


# better way
#  how many times to perform this function
times = int(input("How many times do you want to calculate the average? "))
for _ in range(times):
    avg()