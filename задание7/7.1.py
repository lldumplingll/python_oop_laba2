class Employee:
  name = None
  salary = None

  def this(self):
    print(self.name)

employee_1 = Employee()
employee_1.name = 'Kai'
employee_1.salary = 80000

employee_1.this()
