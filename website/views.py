
from flask import Blueprint, redirect, render_template, request, url_for, jsonify
from werkzeug.utils import secure_filename
from .models import Print as PrintTable
from .models import Tshirt as TshirtTable
from .models import Artist
from .models import db
from .models import Category
from .models import Print_detail
from .models import purchase
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

@views.route('/tshirts_admin', methods=['GET', 'POST'])
def tshirts_admin():
    tshirts = TshirtTable.query.all()
    if request.method == 'GET':
        pass
    return render_template("t-shirts_admin.html", tshirts=tshirts)


@views.route('/tshirts_view/<id>')
def tshirts_view(id):
    tshirt = TshirtTable.query.filter_by(tshirt_id=id).first()
    list = Warehouse.query.filter_by(tshirt_id=id)
    sizes = []
    for item in list:
        sizes.append({'size':getSize(item.size_id), 'id' : item.size_id})
    print('tallas', sizes)
    return render_template("t-shirts_view.html", tshirt=tshirt, sizes=sizes)

@views.route('/tshirts_view_admin/<id>')
def tshirts_view_admin(id):
    tshirt = TshirtTable.query.filter_by(tshirt_id=id).first()
    list = Warehouse.query.filter_by(tshirt_id=id)
    sizes = []
    for item in list:
        sizes.append({'size':getSize(item.size_id), 'id' : item.size_id})
    print('tallas', sizes)
    return render_template("t-shirts_view_admin.html", tshirt=tshirt, sizes=sizes)

@views.route('/customize')
def customize():
    from .logic.t_shirt import precios
    prints = PrintTable.query.all()
    artists = Artist.query.all()    
    if request.method == 'POST':
        redirect(url_for('views.calcular_total'))
    return render_template("customize.html", prints=prints, artists=artists, precios=precios)


@views.route('/calcular_total', methods=['GET','POST'])
def calcular_total():
    """if request.method=='POST':
        purchase = Purchase(user_id=Customer.query.filter_by(user_id=sesion.getUser().getId()), total = sesion.getShoppingCart().getTotal())
        db.session.add(purchase)
        db.session.commit()
        pass"""
    return render_template('pagos.html')


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
@views.route('/upload-tshirt', methods=['GET', 'POST'])
def uploadTshirt():
    if request.method=='POST':
        uploaded_print = request.files.get('print')
        if uploaded_print.filename!='':
            filename = secure_filename(uploaded_print.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            uploaded_print.save(file_path)
            tshirt = TshirtTable(image=filename, cost=29500, name = request.form.get('print-name'), show=False)
            db.session.add(tshirt)
            db.session.commit()
            for i in range(4):
                print(i)
                db.session.add(Warehouse(tshirt_id=tshirt.tshirt_id, size_id=int(i)+1), 0)
                db.session.commit()
        return redirect(url_for('views.home'))
        """return redirect(url_for('views.design_details'))"""
    return render_template("upload_tshirt.html")

