from .sesion import Sesion
from ..models import db
from ..models import User as UserTable
from ..models import Customer
from ..models import Category
from .user import User
from werkzeug.security import generate_password_hash, check_password_hash


sesion = Sesion()

__categories = [
    'videojuegos',
    'anime',
    'libros',
    'cyberpunk',
    'ciencia ficción',
    'fantasia',
    'historia',
    'romance',
    'comedia',
    'terror',
    'drama',
    'acción',
    'aventura',
    'deportes',
    'música',
    'arte',
    'cocina',
    'moda',
    'viajes',
    'naturaleza',
    'ciencia',
    'tecnología',
    'política',
    'filosofía',
    'religión',
    'derecho',
    'economía',
    'salud',
    'educación',
    'empleo',
    'negocios',
    'hogar',
    'familia',
    'amigos',
    'amor',
    'vida',
    'muerte',
    'sueños',
    'realidades',
    'pasado',
    'presente',
    'futuro',
    'universo',
    'multiverso',
    'omniverso',
    'infinito',
    'más allá',
    'todo',
    'nada',
]

__errorMessage = {
    1 : 'E-mail already exists',
    2 : 'Please fill all the fields',
    3 : 'Passswords don\'t match'
}

def insertCategories():
    categories = Category.query.all()
    if len(categories) == 0:
        for category in categories:
            db.session.add(Category(category_name=category))
            db.session.commit()

def login_usr(nickname, password):
    user = UserTable.query.filter_by(nickname=nickname).first()
    if user:
        if check_password_hash(user.password, password):
            sesion.setUser(User(id =user.user_id, name=user.name, lastName=user.last_name, nickname=user.nickname, email=user.email))  
            return True
    return False
def create_usr(nickname, email, password, password2):
    user = UserTable.query.filter_by(nickname=nickname).first()
    if user: 
        return __errorMessage.get(1)
    elif (password == '' or password2 == '') or nickname == '' or email == '':
        return __errorMessage.get(2)
    elif password!=password2:
        return __errorMessage.get(3)
    else: 
        user = UserTable(nickname=nickname, email = email, password = generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        new_customer = Customer(user_id=user.user_id)
        db.session.add(new_customer)
        db.session.commit()
        sesion.setUser(User(id =user.user_id, name=user.name, lastName=user.last_name, nickname=user.nickname, email=user.email))
    return ''

def insertTshirts():
    pass
