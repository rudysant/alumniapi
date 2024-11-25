from ninja import Router
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from ninja.errors import HttpError
from django.http import HttpRequest
from .models import AlumniUser
from .schemas import SignupSchema, LoginSchema, ProfileSchema

router = Router()

@router.post("/signup")
def signup(request: HttpRequest, data: SignupSchema):
    if AlumniUser.objects.filter(username=data.username).exists():
        raise HttpError(400, "Username already exists")
    user = AlumniUser.objects.create(
        username=data.username,
        password=make_password(data.password),
        fullname=data.fullname,
        address=data.address,
    )
    return {"success": True, "message": "User created successfully"}

@router.post("/login")
def login_user(request: HttpRequest, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        raise HttpError(400, "Invalid credentials")
    login(request, user)
    return {"success": True, "message": "Logged in successfully"}

@router.post("/logout")
def logout_user(request: HttpRequest):
    logout(request)
    return {"success": True, "message": "Logged out successfully"}

@router.get("/profile", response=ProfileSchema)
@login_required
def get_profile(request: HttpRequest):
    user = request.user
    return ProfileSchema(
        username=user.username,
        fullname=user.fullname,
        address=user.address,
        picture=user.picture.url if user.picture else None,
    )
