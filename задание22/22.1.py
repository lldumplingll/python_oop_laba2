class Validator:
    def getCorr(self, str):
        if (len(str) > 0):
            print("Correect")
        else:
            raise Exception('name is incorrect')

arrHelper = Validator()