from functools import wraps
from flask import Flask, render_template, url_for, g, request, flash, session
import sqlite3
import os
from itsdangerous import URLSafeSerializer
from werkzeug.utils import redirect
from FDatBase import FDatBase


DATABASE = '/project_db'
DEBUG = True
SECRET_KEY = '85d48ceca6ffa559d4998e419014cf064f0d162008c8fbc0bd126f38212c40d6'
sec = URLSafeSerializer(SECRET_KEY)
"""login_manager = LoginManager()"""


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'project_db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for('main_page'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=["POST", "GET"])
def main_page():
    session.clear()
    db = get_db()
    dbase = FDatBase(db)

    if request.method == "POST":
        res_email = dbase.Check(request.form['email'])
        res_password = dbase.CheckPass(request.form['password'], res_email)
        id = dbase.GetId(res_email)
        if res_email and res_password:
            return redirect(url_for('profile', id=id))
        else:
            flash("Please, try again")
            return redirect(url_for('main_page'))
    return render_template('auth.html')


@app.route('/register', methods=["POST", "GET"])
def AddInfo():
    db = get_db()
    dbase = FDatBase(db)

    if request.method == "POST":
        res = dbase.AddInfo(request.form['email'], request.form['password'])
        if not res:
            flash('Error. PLease, try again', category='error')
            return redirect(url_for('register'))
        else:
            flash('Your information is submitted successfully! You can now log in into your account!')
            return redirect(url_for('main_page'))
    return render_template('register.html', title="Registration")


@app.route('/profile/<id>', methods=["POST", "GET"])
def profile(id):
    db = get_db()
    dbase = FDatBase(db)
    if request.method == 'POST' or request.method == 'GET':
        stocks = db.execute(f"SELECT symbol FROM account")
        balance = dbase.GetBalance(id)
        return render_template('profile.html', stocks=stocks, balance=balance, id=id)


@app.route('/stocks', methods=["POST", "GET"])
def stocks():
    db = get_db()
    dbase = FDatBase(db)
    symstocks = db.execute(f"SELECT symbol FROM stock").fetchall()
    return render_template('stocks.html', stocks=symstocks)


@app.route('/buy/<symbol>', methods=['POST', 'GET'])
def buy(symbol):
    db = get_db()
    dbase = FDatBase(db)
    '''id = session.get()'''
    if request.method == 'POST':
        shares = request.form.get("shares")
        if not shares:
            return flash("provide number of shares")
        elif not shares.isnumeric():
            return flash("provide numeric")
        total_shares = int(shares)

        symbol = symbol.upper()

        cash = db.execute(f"SELECT cash FROM maininfo WHERE id = {id}")
        cash_available = cash[0]["cash"]
        price_quoted = symbol["price"]
        price_buy = price_quoted * total_shares
        cash_updated = cash_available - price_buy

        if cash_updated < 0:
            return flash("user has not enough money")

        else:
            db.execute(f"UPDATE maininfo SET cash = {cash_updated} WHERE id = {id}")
            rows = db.execute(f"SELECT * FROM account WHERE id = {id} and symbol = {symbol}")

            if len(rows) == 0:
                db.execute(f"INSERT INTO account (id, symbol, shares) VALUES ({id}, {symbol}, {total_shares})")

            else:
                db.execute(f"UPDATE account SET shares = (shares + {total_shares}) WHERE id = {id} AND symbol={symbol}")

            flash("BOUGHT !")

            return redirect(url_for('profile'))

    else:
        return render_template("buy.html", symbol=symbol)


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


"""@app.route('/sell', methods=['POST', 'GET'])
@login_required
def sell():
    user_id = session["user_id"]
    if request.method == 'POST':"""

if __name__ == "__main__":
    app.run(debug=True)
