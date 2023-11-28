from .sesion import Sesion
from ..models import db
from ..models import User as UserTable
from ..models import Customer
from ..models import Category
from ..models import Tshirt as TshirtTable
from .user import User
from .t_shirt import Tshirt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, redirect, render_template, request, url_for, jsonify


sesion = Sesion()

store = Blueprint('store', __name__)

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

@store.route('/get_tshirts', methods=['POST'])
def get_tshirts():
    tshirts = TshirtTable.query.all()
    
    products = []
    for tshirt in tshirts:
        products.append({
            'id' : tshirt.tshirt_id,
            'name' : tshirt.name,
            'image' : tshirt.image,
            'price' : tshirt.cost,
            'size' : tshirt.size
        })
    return jsonify(products)

@store.route('/load_shopping_cart', methods=['POST'])
def load_shopping_cart():
    shoppingList = sesion.getShoppingCart().getTShirts()
    products = []
    ids = []
    for product in shoppingList:
        tshirt = {
            'id' : product.getId(),
            'name' : product.getName(),
            'image' : product.getImage(),
            'price' : product.getPrice(),
            'size' : product.getSize()
        }
        ids.append(product.getId())
        if not tshirt in products:
            products.append(tshirt)
    for product in products:
        product['quantity'] = ids.count(product['id'])
            
    return jsonify(products)

@store.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method=='POST':
        tshirt=TshirtTable.query.filter_by(tshirt_id=request.form['id']).first()
        sesion.addToCart(Tshirt(id = tshirt.tshirt_id, name = tshirt.name , price= tshirt.cost , size = tshirt.size, image = tshirt.image))
        return('', 204)
    
@store.route('/remove', methods=['POST'])
def remove():
    for i in range(len(sesion.getShoppingCart().getTShirts())):
        print(sesion.getShoppingCart().getTShirts()[i].getId(), request.form['id'], sesion.getShoppingCart().getTShirts()[i].getId() == request.form['id']) 
        if str(sesion.getShoppingCart().getTShirts()[i].getId()) == request.form['id']:
            sesion.getShoppingCart().getTShirts().pop(i)
            return('tshirt was deleted', 204)
    return ('', 204)

@store.route('/pago')
def pago():
    return jsonify({'url' : 'calcular_total'})

@store.route('/isLoggedIn')
def is_logged_in():
    loggedIn: bool = sesion.isLoggedIn()
    return jsonify({ 'loggedIn' :  loggedIn})

@store.route('/redirect_login')
def redirect_login():
    return jsonify({'url' : '/sign-in'})

@store.route('/redirect_upload')
def redirect_upload():
    return jsonify({'url' : '/upload-design'})

@store.route('/getUser', methods=['POST'])
def getUser():
    usr = sesion.getUser()
    user = {
        'id' : 0,
        'nickname' : '',
        'name' : '',
        'lastName' : '',
        'email' : '',
        'role' : ''
    }
    if usr != None:
        user['id'] = usr.getId()
        user['nickname'] = usr.getNickname()
        user['name'] = usr.getName()
        user['lastName'] = usr.getLastName()
        user['email'] = usr.getEmail()
        user['role'] = usr.getRole()
    
    return jsonify({'user':user})
@store.route('redirect_home', methods=['GET'])
def redirect_home():
    return jsonify ({'url' : '/'})



        