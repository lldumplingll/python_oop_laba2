class Text:

    def __init__(self, text):
        self.__text = text

    def lenT(self):
        return len(self.__text)

    def countL(self):
        count = 0
        for i in self.__text:
            if i.isalpha():
                count += 1
        return count

    def countS(self):
        count = 0
        for i in self.__text:
            if i == " ":
                count += 1
        return count

    def lenWiS(self):
        count = 0
        for i in self.__text:
            if i != " ":
                count += 1
        return count

    def textToMassive(self):
        self.__massive = self.__text.split()
        return self.__massive

    def textToMassiveBySentece(self):
        self.__massive = self.__text.split(".")
        return self.__massive