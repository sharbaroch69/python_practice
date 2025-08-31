a = int(input("Enter your age: ")) 

#  if statement no. 1
if a%2 == 0:        # a%2 means a divided by 2
    print("You entered an even number.")
else:
    print("You entered an odd number.")
    # End of if statement no. 1

# if statement no. 2
if a >= 18:
    print("You are eligible to vote")
    print("Good Luck")
elif a < 0:
    print("Invalid age entered.")
else:
    print("You are not eligible to vote.")
# End of if statement no. 2



# both statements will execute independently.
