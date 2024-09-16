import os

import requests
from flask import current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy import or_
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt

from db import db
from blocklist import BLOCKLIST
from models import UserModel
from schemas import UserSchema, UserRegisterSchema
from tasks import send_user_registration_email

blp = Blueprint("Users", "users", description="Operations on users")

@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        if UserModel.query.filter(
            or_(
                UserModel.username == user_data["username"],
                UserModel.email == user_data["email"]
                )
        ).first():
            abort(409, message="A user with this username or email already exists.")
        
        user = UserModel(
            username=user_data["username"], 
            email=user_data["email"],
            password=pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()
        current_app.queue.enqueue(send_user_registration_email, user.email, user.username)

        return {"message": "User created successfully."}, 201


@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        else:
            abort(401, message="Invalid username or password.")

@blp.route("/refresh")
class UserRefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        user_id = get_jwt_identity()
        access_token = create_access_token(identity=user_id, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"access_token": access_token}, 200

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "User logged out successfully."}, 200


@blp.route("/users/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        if not user:
            abort(404, message="User not found.")
        return UserSchema().dump(user)

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        if not user:
            abort(404, message="User not found.")
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully."}, 200