from flask import *
from controllers.registrationcontroller import registerblueprint
#from controllers.riotlogin import riotloginblueprint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('register.register_page'))

#   return render_template('index.html)



### redirct rutiner
@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

@app.route('/kristallkulan', methods=['GET'])
def kristallkulan():
    return render_template('kristallkulan.html')


@app.route('/nyheter', methods=['GET'])
def nyheter():
    return render_template('nyheter.html')


@app.route('/schema', methods=['GET'])
def schema():
    return render_template('schema.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/kontakt', methods=['GET'])
def kontakt():
    return render_template('kontakt.html')



@app.route('/riotlogin', methods=['GET'])
def riotlogin():
    return render_template('riotlogin.html')

#filer som behövs göras
app.register_blueprint(registerblueprint)
#app.regsiter_blueprint(savepickems)
#app.register_blueprint(userjavascriptdata)'
#app.register_bluepruint(riotfindmostkills)
#






#Future dev
#app.register_blueprint(riotloginblueprint)
#@app.route('/riotlogin', methods=['GET'])
#def riotlogin():
#    return render_template('riotlogin.html')




if __name__ == '__main__':
    app.run(debug=True)
