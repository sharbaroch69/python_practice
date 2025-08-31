'''
for n = 3
  *  
 *** 
*****
'''


n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1)) # to print odd numbers (2*i-1)
  