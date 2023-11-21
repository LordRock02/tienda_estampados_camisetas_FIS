from .user import User
from .shopping_cart import ShoppingCart
from .t_shirt import Tshirt

class Sesion():
    
    def __init__(self, user:User=None, shoppingCart:ShoppingCart=ShoppingCart()):
        self.__user = user
        self.__shoppingCart = shoppingCart

    def getUser(self):
        return self.__user

    def setUser(self, user:User):
        self.__user = user

    def getShoppingCart(self):
        return self.__shoppingCart
    
    def setShoppingCart(self, shoppingCart:ShoppingCart):
        self.__shoppingCart=shoppingCart

    def addToCart(self, tShirt:Tshirt):
        self.__shoppingCart.getTShirts().append(tShirt)
    
    def delUser(self):
        del self.__user

    def isActive(self):
        return self.__user != None
