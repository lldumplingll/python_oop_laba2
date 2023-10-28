class Employee:
    position = None
    name = None
    age = None
    salary = None

employee = Employee()
employee.name = 'Bloo'
employee.age = 28
employee.salary = 100000

employee_1 = Employee()
employee_1.name = 'Kai'
employee_1.age = 30
employee_1.salary = 80000

print(f'зарплата Bloo: {employee.salary}')
print(f'зарплата Kai: {employee_1.salary}')