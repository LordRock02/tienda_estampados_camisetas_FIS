from .logic.store import login_usr, create_usr
from .logic.store import sesion
from .logic.t_shirt import Tshirt
from .logic.print import Print
import unittest


def test_login_pass():
    login_passes = login_usr('LordRock02', '1234')
    assert login_passes


def test_login_fail():
    login_fails = login_usr('LordRock02', '12345')
    assert not login_fails

def test_create_usr_pass():
    assert create_usr(nickname='rgt',email='rgt@gmail.com', password='1234', password2='1234') == ''

def test_create_usr_fail():
    assert not create_usr(nickname='rgt',email='rgt@gmail.com', password='1234', password2='1234643') == ''

def test_total_cart_pass():
 
    sesion.addToCart(tShirt=Tshirt(cost=10.25, prints=[Print(cost=5), Print(cost=10)]))
    sesion.addToCart(tShirt=Tshirt(cost=29.50, prints=[Print(cost=3), Print(cost=12)]))
    sesion.addToCart(tShirt=Tshirt(cost=33.20, prints=[Print(cost=8), Print(cost=13)]))
    sesion.addToCart(tShirt=Tshirt(cost=10.25, prints=[Print(cost=15), Print(cost=4)]))
    
    assert sesion.getShoppingCart().getTotal == 153.2

def test_total_cart_fail():
     
    sesion.addToCart(tShirt=Tshirt(cost=10.25, prints=[Print(cost=5), Print(cost=10)]))
    sesion.addToCart(tShirt=Tshirt(cost=29.50, prints=[Print(cost=3), Print(cost=12)]))
    sesion.addToCart(tShirt=Tshirt(cost=33.20, prints=[Print(cost=8), Print(cost=13)]))
    sesion.addToCart(tShirt=Tshirt(cost=10.25, prints=[Print(cost=15), Print(cost=4)]))
    
    assert sesion.getShoppingCart().getTotal == 153.2