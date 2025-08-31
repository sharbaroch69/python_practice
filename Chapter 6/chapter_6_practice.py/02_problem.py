marks1 = int(input("Enter marks of sub Math: "))
marks2 = int(input("Enter marks of sub Science: "))
marks3 = int(input("Enter marks of sub English: "))

#  Check for total percentage
total_percentage = (marks1 + marks2 + marks3)/3
if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("congrats! You are Passed", total_percentage)
else:
    print("You Failed, Try again next time", total_percentage)