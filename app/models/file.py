from datetime import datetime
from app import db


class File(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), index=True)
    url = db.Column(db.String(256))
    claim_id = db.Column(db.String(64), db.ForeignKey('claim.id'))
    emp_id = db.Column(db.String(64), db.ForeignKey('employee.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<File {}>'.format(self.name)
