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

INSERT INTO setting(setting_code, setting_value) VALUES ('mqtt_hostname', 'ha.lan');
INSERT INTO setting(setting_code, setting_value) VALUES ('mqtt_port', '1883');
INSERT INTO setting(setting_code, setting_value) VALUES ('mqtt_source_topic', 'electricity_meters');
INSERT INTO setting(setting_code, setting_value) VALUES ('mqtt_destination_topic', 'virtual_electricity_meters');
INSERT INTO setting(setting_code, setting_value) VALUES ('mqtt_username', 'electricity-audit');
INSERT INTO setting(setting_code, setting_value) VALUES ('mqtt_password', 'electricity-audit-pass');
