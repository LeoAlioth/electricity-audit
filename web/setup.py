import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from web.db import get_db, init_db
from web.mqtt import print_mqtt_settings

bp = Blueprint('setup', __name__, url_prefix='/setup')

@bp.route('/mqtt', methods=('GET', 'POST'))
def mqtt():
    return render_template('setup/mqtt.html')

@bp.route('/devices', methods=('GET', 'POST'))
def devices():
    return render_template('setup/devices.html')

@bp.route('/db', methods=('GET', 'POST'))
def db():
    return render_template('setup/db.html')

@bp.route('/initDb')
def initDB():
    init_db()  
    return {'success': True}

@bp.route('/initMqtt')
def initMqtt():
    result = print_mqtt_settings()
    return {'success': True, 'body': result}