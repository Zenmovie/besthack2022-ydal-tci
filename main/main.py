from flask import Blueprint, render_template, request, redirect, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user
import os
main = Blueprint('main', __name__)
SECRET_KEY = '85d48ceca6ffa559d4998e419014cf064f0d162008c8fbc0bd126f38212c40d6'
app = Flask(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'project_db')))
db = SQLAlchemy(app)


@app.route('/')
def authentication_page():
    return render_template('base.html', title="Authentication")

@app.route('/login')
def login():
    return render_template('auth.html', title='Login')

@app.route('/register', methods=['GET', 'POST'])
def registration_page():
    return render_template('register.html', title="Registration")


@app.route('/reset_password')
@login_required
def reset_password():
    return render_template('reset.html', title="Reset password")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
