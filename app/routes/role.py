from app import db, registry, auth
from app.models.role import Role
from flask import request, jsonify
from app.schemas.role import RoleResponseSchema, RoleRequestSchema

import uuid


@registry.handles(
    rule="/create_role",
    method="POST",
    response_body_schema=RoleResponseSchema()
)
def create_role():
        r = Role(
            role=request.json['role'],
            id=str(uuid.uuid4())
        )
        db.session.add(r)
        db.session.commit()
        return r.serialize , 200


@registry.handles(
    rule="/delete_role",
    method="POST",
    response_body_schema=RoleResponseSchema(),
    request_body_schema=RoleRequestSchema()
)
def delete_role():
        id = request.json['id']
        r = Role.query.filter_by(id=id).delete()
        db.session.commit()
        return "role deleted successfully"


def getAllRoles():
    db_roles = Role.query.all()
    roles = []
    for role in db_roles:
        roles.append({'id': role.id, 'role': role.role})
    return roles
