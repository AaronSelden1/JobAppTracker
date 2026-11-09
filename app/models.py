from . import db
from flask_login import UserMixin

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(50), nullable=False, default='Applied')
    date_applied = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    job_url = db.Column(db.String(200), nullable=True)
    updates = db.relationship('ApplicationUpdate', backref='application', cascade='all, delete-orphan')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_application_user_id_user'), nullable=True)

class ApplicationUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    update_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    update_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    applications= db.relationship('Application', backref='user', lazy=True)