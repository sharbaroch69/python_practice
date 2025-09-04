class employee:
    a = 5  # class attribute
    def show(self):
        print(f"The class value of attribute is {self.a}")

e = employee()
e.a = 10
e.show()


class employee:
    a = 5  # class attribute
    @classmethod
    def show(cls): # replace self with cls in classmethod
        print(f"The class value of attribute is {cls.a}")

e = employee()
e.a = 10 # this will not affect becuase of classmethod and the output would be 5
e.show()