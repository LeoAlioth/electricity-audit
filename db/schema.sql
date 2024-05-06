DROP TABLE IF EXISTS setting;
DROP TABLE IF EXISTS input_measurement;

CREATE TABLE setting (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  setting_code TEXT UNIQUE NOT NULL,
  setting_value TEXT NOT NULL
);

CREATE TABLE input_measurement (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  states_id text NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  value NUMBER_BASE NOT NULL
);

INSERT INTO setting(setting_code, setting_value) VALUES ('MQTT_BROKER_URL', '192.168.1.98');
INSERT INTO setting(setting_code, setting_value) VALUES ('MQTT_BROKER_PORT', '1883');
INSERT INTO setting(setting_code, setting_value) VALUES ('MQTT_INPUT_METERS_TOPIC', 'input-meters');
INSERT INTO setting(setting_code, setting_value) VALUES ('MQTT_OUTPUT_METERS_TOPIC', 'output-meters');
INSERT INTO setting(setting_code, setting_value) VALUES ('MQTT_USERNAME', 'electricity-audit');
INSERT INTO setting(setting_code, setting_value) VALUES ('MQTT_PASSWORD', 'electricity-audit-pass');
