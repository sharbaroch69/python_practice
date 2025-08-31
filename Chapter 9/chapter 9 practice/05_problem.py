words = ["donkey", "loosi", "kuto"]
with open("replaceme.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open("replaceme.txt", "w")  as f:
    f.write(content)