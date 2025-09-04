class employee:
    salary = 250
    increment = 1.5

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100

e = employee()
e.salaryafterincrement = 300
print(e.increment)
print(e.salaryafterincrement)

