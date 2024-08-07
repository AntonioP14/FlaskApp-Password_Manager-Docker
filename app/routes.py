from flask import Blueprint, render_template, request, redirect, url_for
from .models import Password
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

@bp.route('/add', methods=['POST'])
def add():
    service = request.form.get('service')
    username = request.form.get('username')
    password = request.form.get('password')
    
    new_password = Password(service=service, username=username, password=password)
    db.session.add(new_password)
    db.session.commit()
    
    return redirect(url_for('main.index'))
