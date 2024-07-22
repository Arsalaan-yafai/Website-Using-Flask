from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db: SQLAlchemy = SQLAlchemy(app)
sno,name,email,phone_number,message,date
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(120), nullable=True)
    date = db.Column(db.String(12), nullable=False)
"""
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        '''Fetch data and add it to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry =contact(name = name, email = email, phone_number = phone, message = message)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')
@app.route("/post")
def post():
    return render_template('post.html')
app.run(debug=True)