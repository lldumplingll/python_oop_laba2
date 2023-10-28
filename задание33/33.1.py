class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name

    def getSurn(self):
        return self.surname


class Student(User):
    def __init__(self, name, surname, year):
        super().__init__(name, surname)
        self.year = year

    def getYear(self):
        return self.year