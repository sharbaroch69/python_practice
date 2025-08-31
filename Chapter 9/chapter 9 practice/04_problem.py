content = "donkey"
with open("donkeytext.txt") as f:
    content = f.read()
contentnew = content.replace("donkey", "#######")
with open("donkeytext.txt", "w")  as f:
    f.write(contentnew)