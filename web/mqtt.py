from flask import Flask, request, jsonify, current_app, g
from flask_mqtt import Mqtt
from web.db import get_db

import click

def get_mqtt_client():
    if 'mqtt_client' not in g:
        current_app.config['MQTT_BROKER_URL'] = 'ha.local'
        current_app.config['MQTT_BROKER_PORT'] = 1883
        current_app.config['MQTT_USERNAME'] = 'electricity-audit'  # Set this item when you need to verify username and password
        current_app.config['MQTT_PASSWORD'] = 'electricity-audit-pass'  # Set this item when you need to verify username and password
        current_app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
        current_app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True
        current_app.config['MQTT_INPUT_METERS_TOPIC'] = '/electricity-audit/input-meters'
        current_app.config['MQTT_OUTPUT_METERS_TOPIC'] = '/electricity-audit/output-meters'
        g.mqtt_client = Mqtt(current_app)

    return g.mqtt_client

def print_mqtt_settings():
    db = get_db()
    setting: str = db.execute("select * from setting").fetchone()
    print("these are the settings:")
    print(setting)
    return setting 