from flask import Flask, abort, request, jsonify, g, url_for
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_heroku import Heroku
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
heroku = Heroku(app)

auth = HTTPBasicAuth()

from app import routes, models
from app.models import Employee


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    print("aaaaaaaa",username_or_token)
    employee = Employee.verify_auth_token(username_or_token)
    if not employee:
        # try to authenticate with email/password
        employee = Employee.query.filter_by(email=username_or_token).first()
        if not employee or not employee.verify_password(password):
            return False
    g.employee = employee
    return True


@app.route('/token')
@auth.login_required
def get_auth_token():
    token = g.employee.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.employee.email})

@app.route("/number/<number>")
def get_number(number):
    return {"value": number}


@app.route('/login', methods=["GET", "POST"])
def login_page():

    if request.method == "POST":

        attempted_username = request.json['username']
        attempted_password = request.json['password']
        if attempted_username == "admin" and attempted_password == "password":
            print({attempted_username, attempted_password})
            return {"attempted_username": attempted_username, "attempted_password": attempted_password}

        else:
            return {"value": "Invalid credentials. Try Again."}

    else:
        return {"value": "trying to login?"}


if __name__ == "__main__":
    app.run(debug=True)
