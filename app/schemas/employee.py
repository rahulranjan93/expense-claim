from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields


class CreateEmployeeResponseSchema(ResponseSchema):
    id: fields.String()
    name: fields.String()
    email: fields.String()
    teams: fields.List(fields.String)
    role: fields.String()


class CreateEmployeeRequestSchema(RequestSchema):
    role = fields.String()
    teams = fields.List(fields.String)
    name = fields.String()
    email = fields.String()

