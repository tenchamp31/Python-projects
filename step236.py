class Protected:
    def __init__(self):
        self._protectedVar = 0                      #creating protected attribute with 1 underscore


obj = Protected()
obj._protectedVar = 45
print(obj._protectedVar)




class Protected:
    def __init__(self):
        self.__privateVar = 12                  #creating private attribute with 2 underscore

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(47)
obj.getPrivate()
