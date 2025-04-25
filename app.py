import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager, UserMixin,
    login_user, logout_user,
    login_required, current_user
)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "secret123")

# Configuración de SQLAlchemy: conexión por defecto a MySQL y un bind a PostgreSQL
db_uri = os.getenv('MYSQL_DATABASE_URI')
pg_uri = os.getenv('POSTGRES_DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_BINDS'] = {
    'postgres': pg_uri
}
db = SQLAlchemy(app)

# Modelos
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class LoginLog(db.Model):
    __bind_key__ = 'postgres'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Rutas
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            # Registrar login en PostgreSQL
            log = LoginLog(user_id=user.id)
            db.session.add(log)
            db.session.commit()
            return redirect(url_for('home'))
        flash('Credenciales inválidas', 'danger')
    return render_template('login.html')

@app.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Crear tablas si no existen en ambas bases
    with app.app_context():
        db.create_all()
        db.create_all(bind='postgres')
    app.run(host='0.0.0.0', port=5000, debug=True)