class User:
    def setN(self,name):
        self.name = name

    def getN(self):
        return self.name

class Employee(User):
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname


employee = Employee("Sonya", "Kirova", 90000)

employee.set_name("Rita")
employee.set_surname("Urova")
employee.set_salary(78000)

print(employee.get_name())
print(employee.get_surname())
print(employee.get_salary())

employee.setN("Tina")
print(employee.getN())