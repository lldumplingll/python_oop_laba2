class User:
    def __init__(self):
        self.__name = None
        self.__surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurn(self, surname):
        self.__surname = surname

    def getSurn(self):
        return self.__surname


class Employee(User):
    def getNameandSurn(self):
        return self.__name + ' ' + self.__surname


employee = Employee()
employee.setName("Sonya")
employee.setSurn("Kirova")
print(employee.getName())
print(employee.getSurn())
print(employee.getNameandSurn())