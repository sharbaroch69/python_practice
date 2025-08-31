with open("pythonf.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line.lower()):
        print(f"yes Python found on line {lineno}") # if found in more than one line code will be like this:
        break
    lineno += 1
else:
    print(f"no python not found on line {lineno}")
    lineno += 1