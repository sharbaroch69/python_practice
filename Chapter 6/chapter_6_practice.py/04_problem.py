a = input("Enter username: ")
if(len(a) < 10):
    print("Username is too short, please enter at least 10 characters.")
else:
    print("Welcome, " + a + "!")