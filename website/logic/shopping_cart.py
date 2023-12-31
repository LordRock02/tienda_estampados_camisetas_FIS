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
    def getSubTotal(self, id):
        cost = 0
        for tShirt in self.__tShirts:
            if str(tShirt.getId()) == str(id):
                cost+=tShirt.getTotalCost()
        return cost
    def getQuantityPerModel(self):
        quantityPerModel = {}
        ids = []
        for tShirt in self.__tShirts:
            if not tShirt.getId() in quantityPerModel.keys():
                quantityPerModel.update({tShirt.getId() : 1})
            else:
                quantityPerModel[tShirt.getId()] += 1
        return quantityPerModel