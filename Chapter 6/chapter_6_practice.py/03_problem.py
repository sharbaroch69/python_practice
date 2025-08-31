p1 = "make a lot of money"
p2 = "buy now"
p3 = "limited time offer"
p4 = "click here"
p5 = "subscribe this"

comment = input("Enter the comment: ")
if p1 in comment or p2 in comment or p3 in comment or p4 in comment or p5 in comment:
    print("This comment is spam")
else:
    print("This comment is not spam")