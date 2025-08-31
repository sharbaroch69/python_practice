import os

path = "C:\\Program Files"
for name in os.listdir(path):
    full_path = os.path.join(path, name)
    if os.path.isfile(full_path):
        print(name)
