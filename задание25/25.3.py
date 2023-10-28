class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSal(self):
        return self.__salary

    def add(self, employee):
        self.employees.append(employee)

    def show(self):
        for employee in self.employees:
            print(employee.getName(), employee.getSal())

class EmployeesCollection:
    def __init__(self):
        self.employees = []
        self.salary = []

ec = EmployeesCollection()
ec.add(Employee('john', 832257))
ec.add(Employee('eric', 7755255))
ec.add(Employee('kyle', 4554555))