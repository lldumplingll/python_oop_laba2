class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSal(self):
        return self.__salary

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setSal(self, salary):
        self.__salary = salary


employee_1 = Employee("John", 34, 89000)
print(employee_1.getName())
print(employee_1.getAge())
print(employee_1.getSal())

employee_1.setName('Liza')
employee_1.setAge(26)
employee_1.setSal(100000)

print(employee_1.getName())
print(employee_1.getAge())
print(employee_1.getSal())
