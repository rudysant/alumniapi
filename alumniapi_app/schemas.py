from ninja import Schema
from typing import Optional

class SignupSchema(Schema):
    username: str
    password: str
    fullname: str
    address: Optional[str] = None

class LoginSchema(Schema):
    username: str
    password: str

class ProfileSchema(Schema):
    username: str
    fullname: str
    address: Optional[str] = None
    picture: Optional[str] = None
