from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Mileage, Vehicle, Grease, OilChange, PreventativeMaintenance

class MileageEntry(FlaskForm):
    costno = StringField('Vehicle Number', validators=[DataRequired(), Length(min=4, max=4)])
    