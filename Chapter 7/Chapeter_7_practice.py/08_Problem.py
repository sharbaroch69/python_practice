'''
for n = 3
*  
*** 
*****
'''


n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*" * (2*i-1)) # to print odd numbers: 1, 3, 5...  use (2*i-1)
  