#!/usr/bin/env python
from io import TextIOWrapper
import csv

from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    # Add other product fields here as necessary

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

def load_csv(csv_file: TextIOWrapper, model):
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # skip the headers
    for row in csv_reader:
        record = model(*row)
        db.session.add(record)
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        csv_file = TextIOWrapper(file, encoding='utf-8')
        if 'categories' in filename:
            load_csv(csv_file, Category)
        elif 'products' in filename:
            load_csv(csv_file, Product)
        elif 'users' in filename:
            load_csv(csv_file, User)
        return redirect(url_for('upload_csv'))
    return '''
            <form method='post' action='/' enctype='multipart/form-data'>
              <input type='file' name='file'>
              <input type='submit' value='Upload'>
            </form>
           '''

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

