from typing import Any


class User:

    def __init__(self, id='', name='', lastName='', nickname='', email='', role=''):
        self.__id = id
        self.__name = name
        self.__lastName = lastName
        self.__nickname = nickname
        self.__email = email
        self.__role = role

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getLastName(self):
        return self.__lastName
    
    def setLastName(self, lastName):
        self.__lastName = lastName

    def getNickname(self):
        return self.__nickname
    
    def setNickname(self, nickname):
        self.__nickname = nickname    

    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email

    def getRole(self):
        return self.__role
    
    def setRole(self, role):
        self.__role = role