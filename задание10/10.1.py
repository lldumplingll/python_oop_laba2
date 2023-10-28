class Employee:
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

employee_1 = Employee('Bloo', 28, 100000, 'director')

print(employee_1.name, employee_1.age, employee_1.salary, employee_1.position)