class animals:
    pass
class pets(animals):
    pass
class dogs(pets):
    def bark(self):
        print("Woof Woof")

d = dogs()
d.bark()