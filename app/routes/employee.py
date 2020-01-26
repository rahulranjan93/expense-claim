import json
from app import app, registry, db
from app.models.employee import Employee
from app.routes.role import getAllRoles
from flask import request, jsonify, g
from datetime import datetime
from flask_httpauth import HTTPBasicAuth
import uuid
from app.schemas.employee import CreateEmployeeResponseSchema, CreateEmployeeRequestSchema

auth = HTTPBasicAuth()


@registry.handles(
    rule="/create_employee",
    method="POST",
    response_body_schema=CreateEmployeeResponseSchema,
    request_body_schema=CreateEmployeeRequestSchema
)
def create_employee():
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    roles = getAllRoles()
    data = json.loads(request.data)
    role = data.get("role", None)
    user_role = role if role else "Employee"
    e = Employee(teams=data.get("teams", None),
                 name=data.get("name", None),
                 email=data.get("email", None),
                 id=str(uuid.uuid4()),
                 created_at=datetime.utcnow(),
                 updated_at=datetime.utcnow())

    for role in roles:
        if role["role"] == user_role:
            e.role = role["id"]

    e.hash_password(request.json['password'])
    db.session.add(e)
    db.session.commit()

    return e.serialize, 200


@registry.handles(
    rule="/delete_employee",
    method="POST",
)
def delete_employee():
    id = request.json['id']
    r = Employee.query.filter_by(id=id).delete()
    db.session.commit()
    return "employee deleted successfully"


@registry.handles(
    rule="/change_team",
    method="PATCH",
)
def change_team():
    id = request.json['id']
    employee = Employee.query.filter_by(id=id).first()
    employee.teams = request.json['teams']
    db.session.commit()
    return "Team changed successfully"
