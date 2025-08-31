# inheritance example:

class employee:
    company = "Google"
    def show(self):
        print(f"the name of the employee is {self.name} and he works in {self.company}")
class programmer(employee):
    company = "Fiverr"
    def getLanguage(self):
        return f"The language is {self.language}"


awais = employee()
yasir = programmer()
awais.name = "Awais"
yasir.name = "Yasir"
yasir.language = "Python"
awais.show()
yasir.show()
print(yasir.getLanguage())