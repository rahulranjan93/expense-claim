from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields


class RoleResponseSchema(ResponseSchema):
    id = fields.String()
    role = fields.String()


class RoleRequestSchema(RequestSchema):
    id = fields.String()
