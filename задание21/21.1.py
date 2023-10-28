class Student:
  pass

class Employee:
  pass

employee = Employee()
print(isinstance(employee, Employee))#true
print(isinstance(employee,Student))#false