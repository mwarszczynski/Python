from datetime import datetime
from flask import current_app
from app import db 
# #from app import login_manager
# from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(user_id):
#         return User.query.get(int(user_id))


books_authors = db.Table('BooksAuthors',
    db.Column('user_id', db.Integer, db.ForeignKey('book.book_id')),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.author_id'))
    )


class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), unique=False)
    bk = db.relationship('Authors', secondary=books_authors, backref=db.backref('subscribers', lazy='dynamic'))

    def __init__(self, title):
        self.title = title
        

class Authors(db.Model):
    author_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), unique=False)

    def __init__(self, first_name):
        self.first_name = first_name


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key = True)
    species = db.Column(db.String(20), unique=False)

    def __init__(self, species):
        self.species = species


class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
        email = db.Column(db.String(100), unique=True, nullable=False)
        image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
        password = db.Column(db.String(60), nullable=False)
        posts = db.relationship('Post', backref='author', lazy=True)

        def __repr__(self):
                return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        content = db.Column(db.Text, nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        def __repr__(self):
                return f"User('{self.title}', '{self.date_posted}', '{self.content}')"



