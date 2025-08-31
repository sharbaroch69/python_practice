# Write a python program using function to convert Celsius to Fahrenheit.

# formula
'''
c/5 = f-32/9
f = (c * 9/5) + 32

so convert it
c/5 = f-32/9 # step 1
c = 5*(f-32)/9 # step 2
'''
# function to convert Fahrenheit to Celsius
def f_to_c(f):
    # return (f - 32) * 5/9 # normal way
    return round((f - 32) * 5/9, 2) # round to 2 decimal places

f = float(input("Enter temperature in F: "))
print("Temperature in C is: ", f_to_c(f))

# Convert Celsius to Fahrenheit

def c_to_f(c):
    # return (c * 9/5) + 32, 2
    return round((c * 9/5) + 32, 2) # round to 2 decimal places

c = float(input("Enter temperature in C: "))
print("Temperature in F is: ", c_to_f(c))