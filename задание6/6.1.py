class Employee:
    def this(self, name, salary):
        return name + ' ' + salary

employee_1 = Employee()
employee_1.name = 'Kai'
employee_1.salary = 80000


print(employee_1.this('Kai', '80000'))