#API GOV

from flask import Flask,request, url_for,render_template
from flask.views import View
#from flask_sqlalchemy import SQLAlchemy

################ CLASA VIEWURI #######################

class ShowUsers(View):
    def dispatch_request(self):
        users = User.query.all()
        return render_template('/users.html', objects = users)

app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))
################ INITIALIZARE APPLICATIE #################
app = Flask(__name__)

################ FISIERE TEMPLATES SI STATIC #############
'''
index.html
exemplu.html
profil.html
'''
############### VIEWURI USERI ####################

@app.route('/users/')
def show_users(page):
    users = User.query.all()
    return render_template('users.html')




################# PAGINA DE INDEX ########################
@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        print("Index si pagina principala!")
        return render_template("exemplu.html")
    else:
        return render_template("error.html")

################# PAGINA PROFILE cu argument NUME #################

@app.route("/<name>")
def profile(name):
    return render_template("profil.html", name=name)


################ TRATARE PAGINA EROARE ###################

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

############### VERIFICARE METODE CERUTE ################

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PATCH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE\n"

############# SECVENTA DE LOGARE ###################
@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    response = make_response()
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)



############# PAGINA DE CONTACT #####################

@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ == "__main__":
    app.run()
