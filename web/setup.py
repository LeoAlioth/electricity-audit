import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, jsonify
)

from web.db import get_db, init_db
from web.mqtt import print_mqtt_settings, get_mqtt_client

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
    get_mqtt_client()
    return {'success': True}

@bp.route('/readMqttSettings')
def readMqttSettings():
    result = print_mqtt_settings()
    return {'success': True, 'body': result}


@bp.route('/publish')
def publish_message():
   # request_data = request.get_json()
   publish_result = get_mqtt_client().publish(current_app.config["MQTT_OUTPUT_METERS_TOPIC"], "i was here")
   return jsonify({'code': publish_result[0]})