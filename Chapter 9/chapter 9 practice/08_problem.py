with open("file.txt") as f:
    content = f.read()
with open("copy_file.txt", "w") as f:
    f.write(content)