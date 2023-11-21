from typing import List
from .t_shirt import Tshirt
class ShoppingCart:

    def __init__(self, tShirts:List[Tshirt]=[]):
        self.__tShirts =tShirts

    def getTShirts(self):
        return self.__tShirts
    
    def setTShirts(self, *tShirts:Tshirt):
        self.__tShirts = tShirts

    def getTotal(self):
        cost = 0
        for tShirt in self.__tShirts:
            cost+=tShirt.getTotalCost()
        return cost