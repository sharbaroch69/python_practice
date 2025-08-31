with open("copy_file copy.txt") as f:
    content = f.read()
with open("renamed by python.txt", "w") as f:
    f.write(content)

# after ranaming file delete the old file