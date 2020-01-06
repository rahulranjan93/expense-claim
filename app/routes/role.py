from app import app, db
from app.models.role import Role
from flask import request
from flask_httpauth import HTTPBasicAuth
import uuid

auth = HTTPBasicAuth()


@app.route('/create_role', methods=["POST"])
def create_role():
    print("hello")
    if request.method == "POST":
        r = Role(
            role=request.json['role'],
            id=uuid.uuid4()
        )
        db.session.add(r)
        db.session.commit()
        return "role added successfully"
    else:
        return {"value": "trying to get user ?"}


@app.route('/delete_role', methods=["POST"])
def delete_role():
    if request.method == "POST":
        id = request.json['id']
        r = Role.query.filter_by(id=id).delete()
        db.session.commit()
        return "role deleted successfully"
    else:
        return {"value": "trying to get user ?"}


def getAllRoles():
    db_roles = Role.query.all()
    roles = []
    for role in db_roles:
        roles.append({'id': role.id, 'role': role.role})
    return roles
