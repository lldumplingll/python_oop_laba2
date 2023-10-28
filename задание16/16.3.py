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


employee_1 = Employee("John", 34, 89000)
print(employee_1.getName())
print(employee_1.getAge())
print(employee_1.getSal())