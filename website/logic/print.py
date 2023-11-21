class Print:
    
    def __init(self, id=0, name='', author='', image='', cost=0):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__image = image
        self.__cost = cost

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getAuthor(self):
        return self.__author
    
    def setAuthor(self, author):
        self.__author = author

    def getImage(self):
        return self.__image
    
    def setImage(self, image):
        self.__image = image

    def getCost(self):
        return self.__cost
    
    def setCost(self, cost):
        self.__cost = cost