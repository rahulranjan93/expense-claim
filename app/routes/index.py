from app import app
from app.models.employee import Employee
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@app.route('/')
@app.route('/index')
def index():
    employees = Employee.query.all()
    names = []
    for e in employees:
        names.append(e.name)
        print(names)
    return "Hello"







