from flask import render_template, flash, redirect, url_for, request, current_app
from app import db
from app.models import Mileage, Vehicle, Grease, OilChange, PreventativeMaintenance
from app.fleet import bp


@bp.route('/')
@bp.route('/index')
def index():
    return

@bp.route('/WRM_mileage')
def wrm_mileage():
    return


@bp.route('/HRM_mileage')
def hrm_mileage():
    return


@bp.route('/FRM_mileage')
def frm_mileage():
    return


@bp.route('/MRM_mileage')
def mrm_mileage():
    return