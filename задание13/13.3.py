class Employee:
    __name = None
    __age = None
    __salary = None
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def show(self):
        return self.__name, self.__age, self.__salary

employee_1 = Employee('Bloo', 28, 100000)

print(employee_1.show())