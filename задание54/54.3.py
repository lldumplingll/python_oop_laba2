class Rectangle:
    __height = None
    __width = None

    def __init__(self, height, width):

        self.__height = height
        self.__width = width

    def getSquare(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__height + self.__width)