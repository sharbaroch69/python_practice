'''
***
**      n = 3
*

'''


def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

# Test the function
n = int(input("Enter a number: "))
pattern(n)