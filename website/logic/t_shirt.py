from .print import Print
from typing import List

precios = {
    'small': 29500,
    'medium': 29500,
    'large': 29500,
    'xlarge': 29500
}

class Tshirt:

    def __init__(self, name='default', cost=0, size='', prints: List[Print]=[]):
        self.__name = name
        self.__cost = cost
        self.__size = size
        self.__prints = prints

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getCost(self):
        return self.__cost
    
    def setCost(self, cost):
        self.__cost = cost
    
    def getSize(self):
        return self.__size
    
    def setSize(self, size):
        self.__size = size

    def getPrints(self):
        return self.__prints
    
    def getTotalCost(self):
        cost = self.__cost
        for print in self.__prints:
            cost += print.getCost()
        return cost