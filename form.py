'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
'''
            <form>
            <label for="username">Nom d'utilisateur :</label>
            <input type="text" id="name" name="username">
            </br>
            </br>

            <label for="password">Mot de passe :</label>
            <input type="password" id="password" name="password">
            </br>
            <label>Genre :</label>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male">Masculin</label>
            <input type="radio" id="female" name="gender" value="female">
            <label for="female">Féminin</label>
            </br>
            <label>Langues :</label>
            <input type="checkbox" id="french" name="languages" value="french">
            <label for="french">Français</label>
            <input type="checkbox" id="english" name="languages" value="english">
            <label for="english">Anglais</label>
            </br>
            <input type="submit" value="Envoyer">
            <input type="reset" value="Réinitialiser">
            </form>


    '''
    


'''
@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']


    #return 'votre nom est : {}'.format(name)
    return 'votre nom est : {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
'''

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/result" method="post">
            <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    return 'You entered: {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
