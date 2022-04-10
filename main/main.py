from flask import Flask, render_template

app = Flask(__name__)


@app.route('/login')
def main_page():
    return render_template('auth.html')


@app.route('/register', methods=['GET', 'POST'])
def auth_page():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
