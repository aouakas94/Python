from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder='templates')


app = Flask(__name__)


@app.route('/index')
def index():
    #return "azul a thama3zouzthiw"
    return render_template('index.html',title="bienvenue ")

@app.route('/test')
def indexs():
    return "azul a fellawen"
    #return render_template('index.html',title="bienvenue ")



if __name__ == '__main__':
    app.run(debug=True)
    