from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
import os

from website import UPLOAD_FOLDER

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/prints')
def prints():
    return render_template("prints.html")

@views.route('/tshirts')
def tshirts():
    return render_template("t-shirts.html")
@views.route('/upload-design', methods=['GET', 'POST'])
def uploadDesign():
    if request.method=='POST':
        print('hola')
        uploaded_print = request.files.get('print')
        if uploaded_print.filename!='':
            filename = secure_filename(uploaded_print.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            uploaded_print.save(file_path)
            
        return redirect(url_for('views.home'))
    return render_template("upload_print.html")