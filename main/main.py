from flask import Blueprint, render_template, request, redirect
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def authentication_page():
    return render_template('base.html', title="Authentication")


@main.route('/register', methods=['GET', 'POST'])
def registration_page():
    return render_template('register.html', title="Registration")


@main.route('/reset_password')
@login_required
def reset_password():
    return render_template('reset.html', title="Reset password")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
