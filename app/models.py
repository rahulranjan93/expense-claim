from datetime import datetime
from app import db

class Test(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Test {}>'.format(self.username)

class Role(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    role = db.Column(db.String(64))

    def __repr__(self):
        return '<Role {}>'.format(self.role)

class Employee(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    team = db.Column(db.String(64), index=True)
    role = db.Column(db.String(64), db.ForeignKey('role.id'))
    claims = db.relationship('Claim', backref='claimant', lazy='dynamic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Employee {}>'.format(self.name)

class Claim(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    amount = db.Column(db.Integer)
    team = db.Column(db.String(64), index=True)
    emp_id = db.Column(db.String(64), db.ForeignKey('employee.id'))
    status = db.Column(db.String(64))
    type = db.Column(db.String(64))
    claim_data = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Claim {}>'.format(self.id)

class File(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True)
    url = db.Column(db.String(256))
    claim_id = db.Column(db.String(64), db.ForeignKey('claim.id'))
    emp_id = db.Column(db.String(64), db.ForeignKey('employee.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<File {}>'.format(self.name)