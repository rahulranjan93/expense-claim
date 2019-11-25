from flask import Flask, request
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_heroku import Heroku

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
heroku = Heroku(app)


@app.route("/")
def index():
    return {"value": "Hello World"}


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
