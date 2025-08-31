class employe:
    language = "python" #this is a class attribute
    salary = 50000

    def __init__(self, name, salary, language, ): # dunder init method
        self.name = name
        self.salary = salary
        self.language = language
        print("I am a constructor and I am called automatically when an object is created")

    def show(self):
        print(f"My name is {self.name}, language is {self.language} and salary is {self.salary}")
    def greet(self):
        print("Good morning")

awais = employe("Awais", 90000, "Java") # pass name and salary to constructor

awais.greet()
# awais.show()
awais.language = "C++" # changing the language attribute for awais object
print(awais.name, awais.language)