class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def n(self):
        return self.name

employee_1 = Employee('Bloo', 100000)

print(employee_1.n())
