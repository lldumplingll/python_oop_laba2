class Validator:
    def getCorr(self, str):
        if (len(str) > 0):
            print("Correect")
        else:
            raise Exception('name is incorrect')

    def isEmail(self, str):
        if str.startswith('@mail.com'):
            print("Correect")
        else:
            raise Exception('name is incorrect')

    def isDomen(self, str):
        if str.startswith('www.'):
            print("Correect")
        else:
            raise Exception('name is incorrect')

arrHelper = Validator()

c1 = arrHelper.isEmail("@mail.com")
print(c1)

c2 = arrHelper.isDomen("21")
print(c2)
