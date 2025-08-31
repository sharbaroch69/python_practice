class employe:
    language = "python" #this is a class attribute
    salary = 50000

    def show(self):
        print(f"My name is {self.name}, language is {self.language} and salary is {self.salary}")
    def greet(self):
        print("Good morning")

awais = employe()
awais.name = "Awais" # this is an instance atttribute
awais.salary = 70000 # Note: instance attributes take preference over class attributes during attribute access
# print(awais.name, awais.language, awais.salary)

awais.greet()
awais.show()