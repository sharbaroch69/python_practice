class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
a = programmer("Awais", "100,000", 72472)
y = programmer("Yasir", "120,000", 3885)
print(a.name, a.salary, a.pin, a.company)
print(y.name, y.salary, y.pin, y.company)
