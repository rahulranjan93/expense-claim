from app import app, db
from app.models.employee import Employee
from app.models.claim import Claim
from app.routes.role import getAllRoles
from flask import request, jsonify, g
from datetime import datetime
from flask_httpauth import HTTPBasicAuth
import uuid
import json
auth = HTTPBasicAuth()


@app.route('/create_claim', methods=["POST"])
def create_claim():
    if request.method == "POST":
        c = Claim(
            amount=request.json['amount'],
            team=request.json['team'],
            emp_id=request.json['employee'],
            id=str(uuid.uuid4()),
            status="submitted",
            type=request.json['type'],
            claim_data= request.json['data'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(c)
        db.session.commit()
        return jsonify(claim=c.serialize)
    else:
        return {"value": "trying to get existing claim ?"}


@app.route('/get_all_claims/<user_id>', methods=["GET"])
def get_all_claims(user_id):
    if request.method == "GET":
        # Get employee object
        roles = getAllRoles()
        claimant = Employee.query.filter_by(id=user_id).first()
        self_claims = Claim.query.filter_by(emp_id=user_id).all()
        claimant_role = next(r for r in roles if r["id"] == claimant.role)

        if claimant_role["role"] == "Manager":
            review_claims = Claim.query.filter(
            (Claim.status == "submitted") | (Claim.team.in_(claimant.teams))).all()

        elif claimant_role["role"] == "HR":
            approved_claims = Claim.query.filter_by(type="team_expense", status="approved")
            submitted_claims = Claim.query.filter_by(type="company_expense", status="submitted")
            review_claims = approved_claims + submitted_claims

        elif claimant_role["role"] == "Finance":
            team_expense = Claim.query.filter_by(type="team_expense", status="validated")
            company_expense = Claim.query.filter_by(type="company_expense", status="validated")
            travel_expense = Claim.query.filter_by(type="travel_expense", status="submitted")
            internet_expense = Claim.query.filter_by(type="internet_expense", status="submitted")
            review_claims = team_expense + company_expense + travel_expense + internet_expense
        else:
            review_claims = []

        #data = json.dumps
        return jsonify(claims=
            {
                "self_claims": [i.serialize for i in self_claims],
                "review_claims": [i.serialize for i in review_claims]
            }
        )
    else:
        return {"value": "trying to get existing claim ?"}


@app.route('/approve_claim', methods=["PATCH"])
def approve_claim():
    if request.method == "PATCH":
        id = request.json["id"]
        claim = Claim.query.filter_by(id=id).first()
        claim.status = "approved"
        db.session.commit()
        return jsonify(claim=claim.serialize)
    else:
        return {"value": "trying to get existing claim ?"}


