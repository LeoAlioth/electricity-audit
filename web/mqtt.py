from flask import Flask, request, jsonify, current_app, g
import paho.mqtt.client as mqtt
from web.db import get_db

import click

mqtt_client = None


class Setting(dict):
    def __init__(self, setting_code: str, setting_value: str):
        dict.__init__(self, setting_code = setting_code, setting_value = setting_value)
    # def __repr__(self) -> str:
    #     return f"{type(self).__name__}(code={self.setting_code}, value={self.setting_value})"
        
def get_mqtt_client():
    if 'mqtt_client' not in g:
        db = get_db()
        current_app.config['MQTT_BROKER_URL'] = db.execute('select * from setting where setting_code = "MQTT_BROKER_URL"').fetchone()["setting_value"]
        current_app.config['MQTT_BROKER_PORT'] = int(db.execute('select * from setting where setting_code = "MQTT_BROKER_PORT"').fetchone()["setting_value"])
        current_app.config['MQTT_USERNAME'] = db.execute('select * from setting where setting_code = "MQTT_USERNAME"').fetchone()["setting_value"]
        current_app.config['MQTT_PASSWORD'] = db.execute('select * from setting where setting_code = "MQTT_PASSWORD"').fetchone()["setting_value"]
        current_app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
        current_app.config['MQTT_TLS_ENABLED'] = False  # If your server supports TLS, set it True
        current_app.config['MQTT_INPUT_METERS_TOPIC'] = db.execute('select * from setting where setting_code = "MQTT_INPUT_METERS_TOPIC"').fetchone()["setting_value"]
        current_app.config['MQTT_OUTPUT_METERS_TOPIC'] = db.execute('select * from setting where setting_code = "MQTT_OUTPUT_METERS_TOPIC"').fetchone()["setting_value"]
        mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        mqtt_client.on_connect = handle_connect
        mqtt_client.on_message = handle_mqtt_message
        mqtt_client.username_pw_set(current_app.config['MQTT_USERNAME'], current_app.config['MQTT_PASSWORD'])
        mqtt_client.connect(host = current_app.config['MQTT_BROKER_URL'], port = current_app.config['MQTT_BROKER_PORT'], keepalive = current_app.config['MQTT_KEEPALIVE'], )
        g.mqtt_client = mqtt_client

    return g.mqtt_client

def print_mqtt_settings():
    return current_app.config['MQTT_BROKER_URL'] + " " + str(current_app.config['MQTT_BROKER_PORT']) + " " + current_app.config['MQTT_USERNAME'] + " " + current_app.config['MQTT_PASSWORD'] + " " + str(current_app.config['MQTT_KEEPALIVE']) + " " + ("True" if current_app.config['MQTT_TLS_ENABLED'] else "False") + " " + current_app.config['MQTT_INPUT_METERS_TOPIC'] + " " + current_app.config['MQTT_OUTPUT_METERS_TOPIC']


def handle_connect(client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
       g.mqtt_client.subscribe(current_app.config['MQTT_INPUT_METERS_TOPIC']) # subscribe topic
   else:
       print('Bad connection. Code:', rc)

def handle_mqtt_message(client, userdata, message):
   data = dict(
       topic=message.topic,
       payload=message.payload.decode()
  )
   print('Received message on topic: {topic} with payload: {payload}'.format(**data))