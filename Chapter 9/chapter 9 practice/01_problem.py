with open("poem.txt") as f:
    content = f.read()
if "twinkle" in content:
    print("the word twinkle is present")
else:
    print("The word twinkle is not present")

