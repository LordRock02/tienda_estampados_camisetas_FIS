from flask import Blueprint, redirect, render_template, request, url_for, jsonify
from werkzeug.utils import secure_filename
from .models import Print as PrintTable
from .models import Tshirt as TshirtTable
from .models import Artist
from .models import db
from .models import Category
from .models import Print_detail
from .logic.store import *
from .logic.t_shirt import Tshirt
from .logic.shopping_cart import ShoppingCart
import os

from website import UPLOAD_FOLDER

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    tshirts = TshirtTable.query.all()
    return render_template("home.html", tshirts=tshirts)

@views.route('/prints', methods=['GET', 'POST'])
def prints():
    prints = PrintTable.query.all()
    artists = Artist.query.all()
    if request.method == 'GET':
        pass
    return render_template("prints.html", prints=prints, artists=artists)

@views.route('/tshirts', methods=['GET', 'POST'])
def tshirts():
    tshirts = TshirtTable.query.all()
    if request.method == 'GET':
        pass
    return render_template("t-shirts.html", tshirts=tshirts)



@views.route('/tshirts_view', methods=['GET', 'POST'])
def tshirts_view():
    from .logic.t_shirt import precios
    return render_template('t-shirts_view.html', precios=precios)


@views.route('/calcular_total', methods=['GET'])
def calcular_total():
    return render_template('pagos.html', size='xd', quantity=len(sesion.getShoppingCart().getTShirts()), total=sesion.getShoppingCart().getTotal())




@views.route('/pago')
def pago():
    return render_template("pagos.html")




@views.route('/upload-design', methods=['GET', 'POST'])
def uploadDesign():
    print(f'usuario: {sesion.getUser().getNickname()}')
    artist = Artist.query.filter_by(user_id=sesion.getUser().getId()).first()
    if artist: 
        print('se encontro artista')
    else: 
        print('no se encontro artista')
        artist = Artist(user_id=sesion.getUser().getId(), artist_info=f'@{sesion.getUser().getNickname()}')
        db.session.add(artist)
        db.session.commit()
    categories = Category.query.all()
    category_list = []
    if request.method=='POST':
        uploaded_print = request.files.get('print')
        if uploaded_print.filename!='':
            filename = secure_filename(uploaded_print.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            uploaded_print.save(file_path)
        selected_categories = request.form.getlist('selected_categories[]')
        for category in selected_categories:
            if(category!=''):
                category_list.append(category)
            """print(f"Selected category: {category}")"""
        for category in category_list:
            print(category)
        new_print = PrintTable(image=filename, cost=10, artist_id=artist.artist_id, print_name=request.form.get('print-name'))
        db.session.add(new_print)
        db.session.commit()
        print(f'id de la estampa agregada {new_print.print_id}')
        for category in category_list:
            new_print_detail = Print_detail(print_id=new_print.print_id, category_id=category)
            db.session.add(new_print_detail)
            db.session.commit()
        return redirect(url_for('views.home'))
        """return redirect(url_for('views.design_details'))"""
    return render_template("upload_print.html", categories=categories)

@views.route('/get_tshirts', methods=['POST'])
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

@views.route('/load_shopping_cart', methods=['POST'])
def load_shopping_cart():
    shoppingList = sesion.getShoppingCart().getTShirts()
    products = []
    for product in shoppingList:
        tshirt = {
            'id' : product.getId(),
            'name' : product.getName(),
            'image' : product.getImage(),
            'price' : product.getPrice(),
            'size' : product.getSize(),
            'quantity' : 0
            }
        if products.count(tshirt) == 0:
            products.append(tshirt) 
    for product in shoppingList:
        for i in range(len(products)):
            tshirt = products[i]
            if tshirt['id'] == product.getId():
                tshirt['quantity'] += 1
            products[i] = tshirt
    return jsonify(products)

@views.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if request.method=='POST':
        print(request.form['id'])
        tshirt=TshirtTable.query.filter_by(tshirt_id=request.form['id']).first()
        sesion.addToCart(Tshirt(id = tshirt.tshirt_id, name = tshirt.name , price= tshirt.cost , size = tshirt.size, image = tshirt.image))
        print('agregada:' ,tshirt.name, tshirt.cost, tshirt.size)
        print('total', sesion.getShoppingCart().getTotal())
        return('', 204)
    
@views.route('/remove', methods=['POST'])
def remove():
    pass