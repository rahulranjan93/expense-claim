from app import app, db
from app.models import Employee, Role
from flask import request,abort, jsonify, g, url_for
from datetime import datetime
from flask_httpauth import HTTPBasicAuth
import uuid
import requests
import xmltodict
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

@app.route('/getAllTeams', methods=["GET"])
def get_all_teams():
    teams = []
    response = requests.get(
        'http://m7.tm00.com/tmpartnerservice/Services/PartnerDropdownlistService.svc/GetDropdownvaluesByHostIdAndListId/47/Team',
        headers={
            "Content-Type": "application/json",
            "Authorization": "18:E6LfjeMCP"
        },
    )

    responseContentJson =  xmltodict.parse(response.content)
    if responseContentJson["PartnerDDLValue"] is not None :
        listItems = responseContentJson["PartnerDDLValue"]["ListItems"]["a:ListItem"]
        for item in listItems :
            teams.append(item["a:ListItemValue"])

    return jsonify(teams)







