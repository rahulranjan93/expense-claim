from app import app
from app.models.employee import Employee
from flask import request, jsonify, g
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    employee = Employee.verify_auth_token(username_or_token)
    if not employee:
        # try to authenticate with email/password
        employee = Employee.query.filter_by(email=username_or_token).first()
        if not employee or not employee.verify_password(password):
            return False
    g.employee = employee
    return True


@app.route('/login')
@auth.login_required
def get_auth_token():
    token = g.employee.generate_auth_token(600)
    print(g.employee)
    return jsonify({'token': token.decode('ascii'), 'duration': 600, 'employee': g.employee.serialize})


@app.route('/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.employee.email})
