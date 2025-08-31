# parents inheritance example:

class employee:
    company = "Google"
    def show(self):
        print(f"the name of the employee is {self.name} and he works in {self.company}")

class coder:
    language = "Python"
    def printlanguage(self):
        return f"The language is {self.language}"
class programmer(employee, coder): # Programmer class inherits from employee and coder
    company = "Fiverr"
    def showlanguage(self):
        return f"The Name of company is {self.company} and language is {self.language}"


awais = employee()
yasir = programmer()
awais.name = "Awais"
yasir.name = "Yasir"
yasir.printlanguage()
yasir.showlanguage()
print(yasir.printlanguage())
print(yasir.showlanguage())
print(yasir.show())