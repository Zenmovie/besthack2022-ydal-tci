from flask import Blueprint, render_template, request, redirect, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://///home/zenmovie/PycharmProjects/besthack2022-ydal-tci/main/db.sqlite"
db = SQLAlchemy(app)


@app.route('/')
def authentication_page():
    return render_template('base.html', title="Authentication")


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
