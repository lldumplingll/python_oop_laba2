class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def n(self):
        return self.name

    def s(self):
        return self.salary

    def s_up(self):
        return self.salary + self.salary*0.1

employee_1 = Employee('Bloo', 100000)

print(employee_1.n(), employee_1.s(), employee_1.s_up())
