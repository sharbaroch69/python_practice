'''
***
* *     for n = 3
***
'''

a = int(input("Enter a number: "))
for i in range(1, a+1):
    if(i == 1 or i == a):  # i == 1 is for the first row and i == a is for the last row
        print("*" * a)
    else:
        print("*" + " " * (a-2) + "*") # Middle rows


