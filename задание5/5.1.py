class Employee:
    position = None
    name = None
    age = None
    salary = None

    def info(self):
        return 'Собрание сотрудников на первом этаже в 15:00'

employee = Employee()
employee.name = 'Bloo'
employee.age = 28
employee.salary = 100000

employee_1 = Employee()
employee_1.name = 'Kai'
employee_1.age = 30
employee_1.salary = 80000

print(employee.info())