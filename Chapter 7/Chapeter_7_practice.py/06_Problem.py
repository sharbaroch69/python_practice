# factorial is like 5! = 5 * 4 * 3 * 2 * 1
n = int(input("Enter a number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")