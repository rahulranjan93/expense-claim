from app import app, db
from app.models.employee import Employee
from app.routes.role import getAllRoles
from flask import request, jsonify, g
from datetime import datetime
from flask_httpauth import HTTPBasicAuth
import uuid
auth = HTTPBasicAuth()


@app.route('/create', methods=["POST"])
def create():
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    roles = getAllRoles()
    if request.method == "POST":
        e = Employee( email = request.json['email'],
        name = request.json['name'],
        team = request.json['team'],
        id = uuid.uuid4(),
        created_at = datetime.utcnow(),
        updated_at =datetime.utcnow())

        for role in roles:
            if role["role"] == "Employee":
                e.role = role["id"]

        e.hash_password(request.json['password'])
        db.session.add(e)
        db.session.commit()
        return "employee added successfully"
    else:
        return {"value": "trying to get user ?"}



@auth.verify_password
def verify_password(username_or_token, password):
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
