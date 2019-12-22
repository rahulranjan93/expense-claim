from app import app, db
from app.models import Employee, Role
from flask import request
from datetime import datetime
import uuid

@app.route('/')
@app.route('/index')
def index():
    employees = Employee.query.all()
    names = []
    for e in employees:
        names.append(e.name)
        print(names)
    return "Hello"

@app.route('/create', methods=["POST"])
def create():
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    if request.method == "POST":
        e = Employee( email = request.json['email'],
        name = request.json['name'],
        role = request.json['role'],
        team = request.json['team'],
        id = uuid.uuid4(),
        created_at = datetime.utcnow(),
        updated_at =datetime.utcnow())

        e.hash_password(request.json['password'])
        db.session.add(e)
        db.session.commit()
        return "employee added successfully"
    else:
        return {"value": "trying to get user ?"}

@app.route('/createRole', methods=["POST"])
def createRole():

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

@app.route('/deleteRole', methods=["POST"])
def deleteRole():

    if request.method == "POST":
        id = request.json['id']
        r = Role.query.filter_by(id=id).delete()
        db.session.commit()
        return "role deleted successfully"
    else:
        return {"value": "trying to get user ?"}
