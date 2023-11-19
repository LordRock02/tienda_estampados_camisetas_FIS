class Sesion():
    
    def __init__(self):
        self.__user = None
        pass
    def getUser(self):
        return self.__user

    def setUser(self, user):
        self.__user = user
    
    def delUser(self):
        del self.__user

    def isActive(self):
        return self.__user != None
