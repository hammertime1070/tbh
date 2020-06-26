from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login

class Mileage(db.model):


class Vehicle(db.model):
    costno = db.Column(db.String, primary_key=True)
    grease_int = db.Column(db.Integer)


class Grease(db.model):


class OilChange(db.model):


class PreventativeMaintenance(db.model):