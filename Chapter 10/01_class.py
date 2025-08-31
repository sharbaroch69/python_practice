class employe:
    language = "python" #this is a class attribute
    salary = 50000

harry = employe()
harry.name = "Harry" # this is an instance atttribute
harry.salary = 70000
print(harry.name, harry.language, harry.salary)
# this will print: Harry python 70000 instead of Harry python 50000

awais = employe()
awais.name = "Awais" # this is an instance atttribute
print(awais.name, awais.language, awais.salary)
