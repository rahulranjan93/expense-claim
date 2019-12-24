from flask import Flask
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



if __name__ == "__main__":
    app.run(debug=True)