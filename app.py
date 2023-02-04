from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder='templates')


app = Flask(__name__)


@app.route('/')
def index():
    #return "azul a thama3zouzthiw"
    return render_template('fonction.py')

@app.route('/user/')
def user(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    app.run(debug = True)
    #manager.run()