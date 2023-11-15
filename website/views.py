from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from .models import *
import os

from website import UPLOAD_FOLDER

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/prints', methods=['GET', 'POST'])
def prints():
    prints = Print.query.all()
    artists = Artist.query.all()
    if request.method == 'GET':
        pass
    return render_template("prints.html", prints=prints, artists=artists)

@views.route('/tshirts')
def tshirts():
    return render_template("t-shirts.html")
@views.route('/pago')
def pago():
    return render_template("pagos.html")
@views.route('/upload-design', methods=['GET', 'POST'])
def uploadDesign():
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
        new_print = Print(image=filename, cost=10, artist_id='1', print_name=request.form.get('print-name'))
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