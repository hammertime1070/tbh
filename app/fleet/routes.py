from flask import render_template, flash, redirect, url_for, request, current_app
from app import db
from app.fleet.forms import VehicleEntry
from app.models import Mileage, Vehicle, Grease, OilChange, PreventativeMaintenance
from app.fleet import bp


@bp.route('/')
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = VehicleEntry()
    if form.validate_on_submit():
        vehicle = Vehicle(costno=form.costno, grease_int=form.grease_int,
                          oil_change_int=form.oil_change_int,
                          preventative_maintenance_int=form.preventative_maintenance_int)
        db.session.commit(vehicle)
    return render_template('index.html', form=form)


# @bp.route('/WRM_mileage')
# def wrm_mileage():
#     return
#
#
# @bp.route('/HRM_mileage')
# def hrm_mileage():
#     return
#
#
# @bp.route('/FRM_mileage')
# def frm_mileage():
#     return
#
#
# @bp.route('/MRM_mileage')
# def mrm_mileage():
#     return