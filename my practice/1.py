# Step 1: Define a class
class Car:
    def __init__(self, brand, model):  # constructor (runs when you create an object)
        self.brand = brand
        self.model = model

    def display_info(self):  # method (function inside class)
        print(f"Car: {self.brand} {self.model}")

# Step 2: Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

# Step 3: Use methods
car1.display_info()
car2.display_info()
car3.display_info()
