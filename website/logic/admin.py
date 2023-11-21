from .user import User

class Admin(User):

    def __init__(self, id='', name='', lastName='', nickname='', email=''):
        super(Admin, self).__init__(id, name, lastName, nickname, email)