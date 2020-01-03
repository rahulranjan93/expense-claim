from app import db
from datetime import datetime
import json

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

    def to_json(self):
        return json.dumps(self.__dict__)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'emp': self.emp_id,
            'team': self.team,
            'status': self.status,
            'type': self.type,
            'data': self.claim_data
        }