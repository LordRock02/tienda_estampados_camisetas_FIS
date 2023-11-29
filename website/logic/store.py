from .sesion import Sesion
from ..models import db
from ..models import User as UserTable
from ..models import Customer
from ..models import Category
from ..models import Tshirt as TshirtTable
from ..models import Admin
from ..models import Size
from ..models import Warehouse
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

__sizes = [
    'small',
    'medium',
    'large',
    'xlarge'
]

__admin = {
    'nickname' : 'admin',
    'name' : 'admin',
    'lastname' : 'admin',
    'password' : '1234',
    'email' : 'admin@neonkrakencoders.com'
}

__errorMessage = {
    1 : 'E-mail already exists',
    2 : 'Please fill all the fields',
    3 : 'Passswords don\'t match'
}

__tshirts = [
    {
        'name' : 'captain america',
        'image' : '1.png',
        'price' : 29500,
        'show' : True,
        'stock' : 20
    },
    {
        'name' : 'smile',
        'image' : '2.png',
        'price' : 29500,
        'show' : True,
        'stock' : 20
    },
    {
        'name' : 'oscar el rabias',
        'image' : '3.png',
        'price' : 29500,
        'show' : True,
        'stock' : 20
    }
]

def insertCategories():
    categories = Category.query.all()
    if len(categories) == 0:
        for category in __categories:
            db.session.add(Category(category_name=category))
            db.session.commit()

def insertSizes():
    sizes = Size.query.all()
    if len(sizes) == 0:
        for size in __sizes:
            db.session.add(Size(name=size))
            db.session.commit()
def insertAdmin():
    admins = Admin.query.all()
    if len(admins) == 0:
        create_usr(__admin['nickname'], __admin['email'], __admin['password'], __admin['password'], __admin['name'], __admin['lastname'])
        user = UserTable.query.filter_by(nickname=__admin['nickname']).first()
        db.session.add(Admin(user_id=user.user_id))
        db.session.commit()

def insertInitialTshirts():
    tshirts = TshirtTable.query.all()
    if len(tshirts) == 0:
        for tshirt in __tshirts:
            t_shirt = TshirtTable(name=tshirt['name'], image=tshirt['image'], show=tshirt['show'], cost=tshirt['price'])
            db.session.add(t_shirt)
            db.session.commit()
            for i in range(len(__sizes)):
                db.session.add(Warehouse(tshirt_id=t_shirt.tshirt_id, size_id=i+1, stock=tshirt['stock']))
                db.session.commit()

def login_usr(nickname, password):
    user = UserTable.query.filter_by(nickname=nickname).first()
    if user:
        admin = Admin.query.filter_by(user_id= user.user_id).first()
        role:str
        if check_password_hash(user.password, password):
            if admin:
                role = 'admin'
            else:
                role = 'user'
            sesion.setUser(User(id =user.user_id, name=user.name, lastName=user.last_name, nickname=user.nickname, email=user.email, role=role))  
            return True
    return False
def create_usr(nickname, email, password, password2, name, lastname):
    user = UserTable.query.filter_by(nickname=nickname).first()
    if user: 
        return __errorMessage.get(1)
    elif (password == '' or password2 == '') or nickname == '' or email == '':
        return __errorMessage.get(2)
    elif password!=password2:
        return __errorMessage.get(3)
    else: 
        user = UserTable(nickname=nickname, email = email, password = generate_password_hash(password), name = name, last_name=lastname)
        db.session.add(user)
        db.session.commit()
        new_customer = Customer(user_id=user.user_id)
        db.session.add(new_customer)
        db.session.commit()
        sesion.setUser(User(id =user.user_id, name=user.name, lastName=user.last_name, nickname=user.nickname, email=user.email))
    return ''

def insertTshirts():
    pass

def getSize(id):
    return __sizes[id-1]

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
        ids.append({
            'id' : product.getId(),
            'size' : product.getSize()
        })
        if not tshirt in products:
            products.append(tshirt)
    for product in products:
        product['quantity'] = ids.count({'id' : product['id'], 'size' : product['size']})
    print('hello from load_shopping_cart', products)
            
    return jsonify(products)

"""@store.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method=='POST':
        tshirt=TshirtTable.query.filter_by(tshirt_id=request.form['id']).first()
        sesion.addToCart(Tshirt(id = tshirt.tshirt_id, name = tshirt.name , price= tshirt.cost , image = tshirt.image))
        return('', 204)"""
    
@store.route('/add_to_cart', methods=['POST', 'GET'])
def add_to_cart():
    if request.method=='POST':
        tshirt=TshirtTable.query.filter_by(tshirt_id=request.form['id']).first()
        size = Size.query.filter_by(size_id = request.form['size']).first()
        quantity = request.form['quantity']
        print(quantity)
        for i in range(int(quantity)):
            print('hello from add_to_cart')
            sesion.addToCart(Tshirt(id = tshirt.tshirt_id, name = tshirt.name , price= tshirt.cost , image = tshirt.image, size=size.size_id))
        return('', 204)
    
@store.route('/remove', methods=['POST'])
def remove():
    print('hello from remove')
    for i in range(len(sesion.getShoppingCart().getTShirts())):
        print('info carrito',sesion.getShoppingCart().getTShirts()[i].getId(), request.form['id'], sesion.getShoppingCart().getTShirts()[i].getSize(), request.form['size'], str(sesion.getShoppingCart().getTShirts()[i].getSize()) == request.form['size']) 
        if str(sesion.getShoppingCart().getTShirts()[i].getId()) == request.form['id']:
            if str(sesion.getShoppingCart().getTShirts()[i].getSize()) == request.form['size']:
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
@store.route('redirect_customize', methods=['GET'])
def redirect_customize():
    return jsonify ({'url' : '/customize'})

@store.route('/redirect_tshirt_view', methods=['GET', 'POST'])
def redirect_tshirt_view():
    id = request.args.get('id')
    return jsonify ({'url' : url_for('views.tshirts_view', id = id)})

@store.route('/get_stock')
def get_stock(id, size):
    stock = Warehouse.query.filter(tshirt_id=id, size_id = size).first()
    return jsonify ({'stock' : stock.stock})


        