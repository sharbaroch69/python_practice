# function to print multiplication table of a number

def multiply(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiply(5)