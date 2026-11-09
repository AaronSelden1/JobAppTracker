from flask import Blueprint
from flask import render_template
from .models import Application
main = Blueprint('main',__name__)

@main.route('/')
def home():
    applications = Application.query.all()
    return render_template('index.html', applications=applications)
