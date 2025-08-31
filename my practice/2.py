# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} started.")

# Child Class
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # call parent constructor
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

car1 = Car("Tesla", "Model 3")
car1.start()         # inherited method
car1.display_info()  # child method
