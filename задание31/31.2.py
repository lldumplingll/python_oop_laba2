class Employee:
    name = None
    age = None

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Employee_1(Employee):
    def setAge(self, age):
        if age > 0:
            self.age = age
        else:
            print("Возраст указан неверно")

emp = Employee_1()
emp.setName('Sonya')
emp.setAge(39)

print(emp.getName())
print(emp.getAge())