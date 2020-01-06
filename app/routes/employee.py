from app import app, db
from app.models.employee import Employee
from app.routes.role import getAllRoles
from flask import request, jsonify, g
from datetime import datetime
from flask_httpauth import HTTPBasicAuth
import uuid
auth = HTTPBasicAuth()


@app.route('/create_employee', methods=["POST"])
def create_employee():
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    roles = getAllRoles()
    if request.method == "POST":
        print(request.json['role'])
        user_role = "Employee" if (request.json['role'] is None) else (request.json['role'])
        e = Employee( email = request.json['email'],
        name = request.json['name'],
        team = request.json['team'],
        id = str(uuid.uuid4()),
        created_at = datetime.utcnow(),
        updated_at =datetime.utcnow())

        for role in roles:
            if role["role"] == user_role:
                e.role = role["id"]

        e.hash_password(request.json['password'])
        db.session.add(e)
        db.session.commit()

        return jsonify(employee=e.serialize)
    else:
        return {"value": "trying to get user ?"}

@app.route('/delete_employee', methods=["POST"])
def delete_employee():

    if request.method == "POST":
        id = request.json['id']
        r = Employee.query.filter_by(id=id).delete()
        db.session.commit()
        return "employee deleted successfully"
    else:
        return {"value": "trying to get user ?"}

@app.route('/change_team', methods=["PATCH"])
def change_team():

    if request.method == "PATCH":
        id = request.json['id']
        employee = Employee.query.filter_by(id=id).first()
        employee.teams = request.json['teams']
        db.session.commit()
        return "Team changed successfully"
    else:
        return {"value": "trying to get user ?"}
