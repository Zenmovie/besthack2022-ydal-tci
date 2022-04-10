from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('auth.html')


@app.route('/register', methods=['GET', 'POST'])
def reg_page():
    return render_template('register.html', title="Registration")

@app.route('/register1')
def register():
    return  render_template('register1.html', title='Registration')

if __name__ == "__main__":
    app.run(debug=True)
