from flask import *
from controllers.registrationcontroller import registerblueprint

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('register.register_page'))
#   return render_template('index.html)





#filer som behövs göras
app.register_blueprint(registerblueprint)
#app.register_blueprint(loginblueprint)
#app.regsiter_blueprint(savepickems)
#app.register_blueprint(userjavascriptdata)'
#app.register_bluepruint(riotfindmostkills)
#
#
#
#



if __name__ == '__main__':
    app.run(debug=True)