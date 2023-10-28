class Student:
    name = None
    surname = None

    def cape(self, str):
        return str.capitalize()

    def show(self):
        return student.name[0], student.surname[0]


student = Student()
student.name = 'Ira'
student.surname = 'Kurova'

print(student.show())
