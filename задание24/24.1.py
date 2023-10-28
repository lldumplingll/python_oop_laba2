class Employee :
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSal(self):
        return self.__salary

employees = [
    Employee(name='john', salary=200020),
    Employee(name='eric', salary=855520),
    Employee(name='kyle', salary=855211),
]