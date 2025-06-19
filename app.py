from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(50))
    nazwisko = db.Column(db.String(50))
    klasa = db.Column(db.String(20))
    srednia_ocen = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route('/theFlask')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_user():
    imie = request.form.get('imie')
    nazwisko = request.form.get('nazwisko')
    klasa = request.form.get('klasa')
    srednia_ocen = float(request.form.get('srednia_ocen'))
    new_user = User(imie=imie, nazwisko=nazwisko, klasa=klasa, srednia_ocen=srednia_ocen)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/users')
def users():
    user_list = User.query.all()
    return render_template('users.html', users=user_list)

if __name__ == '__main__':
    app.run(debug=True)
