# Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1) = 1
sum(2) = 2 + sum(1) = 2 + 1 = 3
sum(3) = 3 + sum(2) = 3 + 3 = 6
sum(4) = 4 + sum(3) = 4 + 6 = 10
sum(n) = 1 + 2 + ... + n

'''

def sum_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n-1)
    
#  Test the function
n = int(input("Enter a natural number: "))
print("The sum of first", n, "natural numbers is: ", sum_natural_numbers(n))

