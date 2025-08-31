f = open("file.txt")
print(f.read())
f.close()

# you can write this using with statement

with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file now

