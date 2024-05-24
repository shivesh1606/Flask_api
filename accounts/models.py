from sqlalchemy import inspect
from datetime import datetime
from flask_validator import ValidateEmail, ValidateString, ValidateCountry
from sqlalchemy.orm import validates

from .. import db # from __init__.py

# ----------------------------------------------- #

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Account(db.Model):
# Auto Generated Fields:
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    first_name     = db.Column(db.String(100), nullable=False)
    last_name     = db.Column(db.String(100), nullable=False)
    company        = db.Column(db.String(100))
    age          = db.Column(db.Integer)
    city      = db.Column(db.String(100))
    state      = db.Column(db.String(100))
    zip      = db.Column(db.String(100))    
    email        = db.Column(db.String(100), nullable=False, unique=True)
    web      = db.Column(db.String(100))
    

# Validations => https://flask-validator.readthedocs.io/en/latest/index.html
    @classmethod
    def __declare_last__(cls):
        ValidateEmail(Account.email, True, True, "The email is not valid. Please check it") # True => Allow internationalized addresses, True => Check domain name resolution.
        ValidateString(Account.first_name, True, True, "The username type must be string")
        ValidateString(Account.last_name, True, True, "The username type must be string")


# Set an empty string to null for username field => https://stackoverflow.com/a/57294872
    @validates('first_name, last_name')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '': return None
        else: return value


# How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.email