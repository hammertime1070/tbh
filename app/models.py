from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# import jwt
from app import db, login


class Mileage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    costno = db.Column(db.String(4), db.ForeignKey('vehicle.costno'))
    current_odo = db.Column(db.Integer)
    prev_odo = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    adjustments = db.Column(db.Integer)
    mileage = db.Column(db.Integer)


class Vehicle(db.Model):
    costno = db.Column(db.String(4), primary_key=True)
    grease_int = db.Column(db.Integer)
    oil_change_int = db.Column(db.Integer)
    preventative_maintenance_int = db.Column(db.Integer)


class Grease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_date = db.Column(db.DateTime)
    odometer_reading = db.Column(db.Integer)
    costno = db.Column(db.String(4), db.ForeignKey('vehicle.costno'))
    notes = db.Column(db.String(140))


class OilChange(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_date = db.Column(db.DateTime)
    odometer_reading = db.Column(db.Integer)
    costno = db.Column(db.String(4), db.ForeignKey('vehicle.costno'))
    notes = db.Column(db.String(140))


class PreventativeMaintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_date = db.Column(db.DateTime)
    odometer_reading = db.Column(db.Integer)
    costno = db.Column(db.String(4), db.ForeignKey('vehicle.costno'))
    notes = db.Column(db.String(140))