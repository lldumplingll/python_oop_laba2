class User:
    __name = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Employee(User):
    pass


student = Employee()
student.setName('john')
name = student.getName()
print(name)