from typing import Any


class User:

    def __init__(self, id='', name='', lastName='', nickname='', email=''):
        self.__id = id
        self.__name = name
        self.__lastName = lastName
        self.__nickname = nickname
        self.__email = email

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getLast_name(self):
        return self.__lastName
    
    def setLast_name(self, lastName):
        self.__lastName = lastName

    def getNickname(self):
        return self.__nickname
    
    def setNickname(self, nickname):
        self.__nickname = nickname    

    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email