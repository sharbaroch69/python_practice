# you can write self or any other name instead of self and results wont change but self is a convention

from random import randint
class train:
    def __init__(self, name, age, train_no, fro, to):
        self.name = name
        self.age = age
        self.train_no = train_no
        self.fro = fro
        self.to = to
    def book(self):
        return f"Congratulations {self.name} your ticket from {self.fro} to {self.to} has been booked successfully. Your Train no. is {self.train_no}."
    def getstatus(self):
        return f"Train no. {self.train_no} from {self.fro} to {self.to} is running on time."
    def getfare(self, fare):
        return f"Ticket fare from {self.fro} to {self.to} is {randint(1000, 5000)}"
a = train("awais", 25, randint(1500, 5000), "Lahore", "Karachi")
print(a.book())
print(a.getstatus())
print(a.getfare(randint(1000, 5000)))



