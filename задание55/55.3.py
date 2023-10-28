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