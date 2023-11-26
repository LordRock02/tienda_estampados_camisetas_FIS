from .print import Print
from typing import List

precios = {
    'small': 29500,
    'medium': 29500,
    'large': 29500,
    'xlarge': 29500
}

class Tshirt:

    def __init__(self, id=0, name='default', price=0, size='', image = '', prints: List[Print]=[]):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__size = size
        self.__image = image
        self.__prints = prints

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getPrice(self):
        return self.__price
    
    def setPrice(self, price):
        self.__price = price
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size):
        self.__size = size

    def getImage(self):
        return self.__image
    
    def setImage(self, image):
        self.__image = image

    def getPrints(self):
        return self.__prints
    
    def getTotalCost(self):
        cost = self.__price
        for print in self.__prints:
            cost += print.getCost()
        return cost