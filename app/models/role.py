from app import (db)


class Role(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    role = db.Column(db.String(64))

    def __repr__(self):
        return '<Role {}>'.format(self.role)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'role': self.role,
        }
