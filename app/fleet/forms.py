from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Mileage, Vehicle, Grease, OilChange, PreventativeMaintenance

class MileageEntry(FlaskForm):
    costno = StringField('Vehicle Number', validators=[DataRequired(), Length(min=4, max=4)])
    current_odo = IntegerField('Current Month Odometer Reading', validators=[DataRequired()])
    previous_odo = IntegerField('Previous Month Odometer Reading', validators=[DataRequired()])
    date = DateField('Reading Date', validators=[DataRequired()])
    adjustment = IntegerField('Adjustment Amount', default=0)


class VehicleEntry(FlaskForm):
    costno = StringField('Vehicle Code', validators=[DataRequired()])
    grease_int = IntegerField('Grease Interval', validators=[DataRequired()])
    oil_change_int = IntegerField('Oil Change Interval', validators=[DataRequired()])
    preventative_maintenance_int = IntegerField('Preventative Maintenance Interval', validators=[DataRequired()])
