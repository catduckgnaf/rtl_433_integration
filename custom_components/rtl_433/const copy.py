DOMAIN = "rtl_433"
STATUS_CMD = 3
START_CMD = 6
STOP_CMD = 7
CONFIG_CMD = 16
DISMISS_ALERT_CMD = 10
DEVICE_ID = "ID of Individual RF Device"
PROTOCOL_ID = "ID of RF Protocol"
PROTOCOL_NAME = "Name of RF Protocol"
DEVICE_MODEL = "Model of RF Device"
DEVICE_FREQ = "Frequency of RF Device"

## Config Flow
WS_ID = "ID of rtl_433 Webserver"
WS_HOST = "192.168.0.100:9443"
WS_IP = "192.1688.0.100"
WS_PORT = 9443
DEFAULT_TIME = 15
DEFAULT_NAME = "RTL_433 HTTP"
NAME = "RTL_433 HTTP"

## attributes
DEFAULT_VOL = 0
PLATFORMS = ['number', 'binary_sensor', 'sensor', 'switch']
ATTR_DEFAULT_TIME = 'Default Time'
ATTR_VOL = "Watering by Volume"
ATTR_DURATION = "Watering Duration"
ATTR_VOLUME = "Watering Volume"
ATTR_STATE = "is_watering"
MANUFACTURER = "RTL_SDR"

DOMAIN = "rtl_433"
STATUS_CMD = 3
START_CMD = 6
STOP_CMD = 7
CONFIG_CMD = 16
DISMISS_ALERT_CMD = 10
DEVICE_ID = "ID of Individual RF Device"
PROTOCOL_ID = "ID of RF Protocol"
PROTOCOL_NAME = "Name of RF Protocol"
DEVICE_MODEL = "Model of RF Device"
DEVICE_FREQ = "Frequency of RF Device"

# Config Flow
WS_ID = "ID of rtl_433 Webserver"
WS_HOST = "192.168.0.100:9443"
WS_IP = "192.1688.0.100"
WS_PORT = 9443
DEFAULT_TIME = 15
DEFAULT_NAME = "RTL_433 HTTP"
NAME = "RTL_433 HTTP"

# Attributes
DEFAULT_VOL = 0
PLATFORMS = ['number', 'binary_sensor', 'sensor', 'switch']
ATTR_DEFAULT_TIME = 'Default Time'
ATTR_VOL = "Watering by Volume"
ATTR_DURATION = "Watering Duration"
ATTR_VOLUME = "Watering Volume"
ATTR_STATE = "is_watering"
MANUFACTURER = "RTL_SDR"

#  Sensor Types
SENSORS = {
    
    "time": {
        "device_type": "sensor",
        "object_suffix": "UTC",
        "config": {
            "device_class": "timestamp",
            "name": "Timestamp",
            "entity_category": "diagnostic",
            "enabled_by_default": False,
            "icon": "mdi:clock-in"
        }
    },

    "battery_ok": {
        "device_type": "sensor",
        "object_suffix": "B",
        "config": {
            "device_class": "battery",
            "name": "Battery",
            "unit_of_measurement": "%",
            "value_template": "{{ float(value) * 99 + 1 }}",
            "state_class": "measurement",
            "entity_category": "diagnostic"
        }
    },

    "humidity": {
        "device_type": "sensor",
        "object_suffix": "H",
        "config": {
            "device_class": "humidity",
            "name": "Humidity",
            "unit_of_measurement": "%",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },
    "humidity_1": {
        "device_type": "sensor",
        "object_suffix": "H1",
        "config": {
            "device_class": "humidity",
            "name": "Humidity 1",
            "unit_of_measurement": "%",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },
    "humidity_2": {
        "device_type": "sensor",
        "object_suffix": "H2",
        "config": {
            "device_class": "humidity",
            "name": "Humidity 2",
            "unit_of_measurement": "%",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "moisture": {
        "device_type": "sensor",
        "object_suffix": "H",
        "config": {
            "device_class": "humidity",
            "name": "Moisture",
            "unit_of_measurement": "%",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "detect_wet": {
        "device_type": "binary_sensor",
        "object_suffix": "moisture",
        "config": {
            "name": "Water Sensor",
            "device_class": "moisture",
            "force_update": "true",
            "payload_on": "1",
            "payload_off": "0"
        }
    },

    "pressure_hPa": {
        "device_type": "sensor",
        "object_suffix": "P",
        "config": {
            "device_class": "pressure",
            "name": "Pressure",
            "unit_of_measurement": "hPa",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "pressure_kPa": {
        "device_type": "sensor",
        "object_suffix": "P",
        "config": {
            "device_class": "pressure",
            "name": "Pressure",
            "unit_of_measurement": "kPa",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "wind_speed_km_h": {
        "device_type": "sensor",
        "object_suffix": "WS",
        "config": {
            "device_class": "wind_speed",
            "name": "Wind Speed",
            "unit_of_measurement": "km/h",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "wind_avg_km_h": {
        "device_type": "sensor",
        "object_suffix": "WS",
        "config": {
            "device_class": "wind_speed",
            "name": "Wind Speed",
            "unit_of_measurement": "km/h",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "wind_avg_mi_h": {
        "device_type": "sensor",
        "object_suffix": "WS",
        "config": {
            "device_class": "wind_speed",
            "name": "Wind Speed",
            "unit_of_measurement": "mi/h",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "wind_avg_m_s": {
        "device_type": "sensor",
        "object_suffix": "WS",
        "config": {
            "device_class": "wind_speed",
            "name": "Wind Average",
            "unit_of_measurement": "km/h",
            "value_template": "{{ (float(value|float) * 3.6) | round(2) }}",
            "state_class": "measurement"
        }
    },

    "wind_speed_m_s": {
        "device_type": "sensor",
        "object_suffix": "WS",
        "config": {
            "device_class": "wind_speed",
            "name": "Wind Speed",
            "unit_of_measurement": "km/h",
            "value_template": "{{ float(value|float) * 3.6 }}",
            "state_class": "measurement"
        }
    },

    "gust_speed_km_h": {
        "device_type": "sensor",
        "object_suffix": "GS",
        "config": {
            "device_class": "wind_speed",
            "name": "Gust Speed",
            "unit_of_measurement": "km/h",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "wind_max_km_h": {
        "device_type": "sensor",
        "object_suffix": "GS",
        "config": {
            "device_class": "wind_speed",
            "name": "Wind max speed",
            "unit_of_measurement": "km/h",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "wind_max_m_s": {
        "device_type": "sensor",
        "object_suffix": "GS",
        "config": {
            "device_class": "wind_speed",
            "name": "Wind max",
            "unit_of_measurement": "km/h",
            "value_template": "{{ (float(value|float) * 3.6) | round(2) }}",
            "state_class": "measurement"
        }
    },

    "gust_speed_m_s": {
        "device_type": "sensor",
        "object_suffix": "GS",
        "config": {
            "device_class": "wind_speed",
            "name": "Gust Speed",
            "unit_of_measurement": "km/h",
            "value_template": "{{ float(value|float) * 3.6 }}",
            "state_class": "measurement"
        }
    },

    "wind_dir_deg": {
        "device_type": "sensor",
        "object_suffix": "WD",
        "config": {
            "name": "Wind Direction",
            "unit_of_measurement": "°",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "rain_mm": {
        "device_type": "sensor",
        "object_suffix": "RT",
        "config": {
            "device_class": "precipitation",
            "name": "Rain Total",
            "unit_of_measurement": "mm",
            "value_template": "{{ value|float|round(2) }}",
            "state_class": "total_increasing"
        }
    },

    "rain_rate_mm_h": {
        "device_type": "sensor",
        "object_suffix": "RR",
        "config": {
            "device_class": "precipitation_intensity",
            "name": "Rain Rate",
            "unit_of_measurement": "mm/h",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "rain_in": {
        "device_type": "sensor",
        "object_suffix": "RT",
        "config": {
            "device_class": "precipitation",
            "name": "Rain Total",
            "unit_of_measurement": "mm",
            "value_template": "{{ (float(value|float) * 25.4) | round(2) }}",
            "state_class": "total_increasing"
        }
    "temperature_C": {
        "device_type": "sensor",
        "object_suffix": "T",
        "config": {
            "device_class": "temperature",
            "name": "Temperature",
            "unit_of_measurement": "°C",
            "value_template": "{{ value|float|round(1) }}",
            "state_class": "measurement"
        }
    },
    "temperature_F": {
        "device_type": "sensor",
        "object_suffix": "F",
        "config": {
            "device_class": "temperature",
            "name": "Temperature",
            "unit_of_measurement": "°F",
            "value_template": "{{ value|float|round(1) }}",
            "state_class": "measurement"
        }
    },
    "humidity": {
        "device_type": "sensor",
        "object_suffix": "H",
        "config": {
            "device_class": "humidity",
            "name": "Humidity",
            "unit_of_measurement": "%",
            "value_template": "{{ value|float|round(1) }}",
            "state_class": "measurement"
        }
    },


  "rssi": {
        "device_type": "sensor",
        "object_suffix": "rssi",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
            "value_template": "{{ value|float|round(2) }}",
            "state_class": "measurement",
            "entity_category": "diagnostic"
        }
    },

    "snr": {
        "device_type": "sensor",
        "object_suffix": "snr",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
            "value_template": "{{ value|float|round(2) }}",
            "state_class": "measurement",
            "entity_category": "diagnostic"
        }
    },

    "noise": {
        "device_type": "sensor",
        "object_suffix": "noise",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
            "value_template": "{{ value|float|round(2) }}",
            "state_class": "measurement",
            "entity_category": "diagnostic"
        }
    },

    "depth_cm": {
        "device_type": "sensor",
        "object_suffix": "D",
        "config": {
            "name": "Depth",
            "unit_of_measurement": "cm",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "power_W": {
        "device_type": "sensor",
        "object_suffix": "watts",
        "config": {
            "device_class": "power",
            "name": "Power",
            "unit_of_measurement": "W",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },
  
    "energy_kWh": {
        "device_type": "sensor",
        "object_suffix": "kwh",
        "config": {
            "device_class": "power",
            "name": "Energy",
            "unit_of_measurement": "kWh",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },
  
    "current_A": {
        "device_type": "sensor",
        "object_suffix": "A",
        "config": {
            "device_class": "current",
            "name": "Current",
            "unit_of_measurement": "A",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },
  
    "voltage_V": {
        "device_type": "sensor",
        "object_suffix": "V",
        "config": {
            "device_class": "power",
            "name": "Voltage",
            "unit_of_measurement": "V",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },

    "light_lux": {
        "device_type": "sensor",
        "object_suffix": "lux",
        "config": {
            "device_class": "illuminance",
            "name": "Outside Luminance",
            "unit_of_measurement": "lx",
            "value_template": "{{ value|int }}",
            "state_class": "measurement"
        }
    },
    "lux": {
        "device_type": "sensor",
        "object_suffix": "lux",
        "config": {
            "device_class": "illuminance",
            "name": "Outside Luminance",
            "unit_of_measurement": "lx",
            "value_template": "{{ value|int }}",
            "state_class": "measurement"
        }
    },

    "uv": {
        "device_type": "sensor",
        "object_suffix": "uv",
        "config": {
            "name": "UV Index",
            "unit_of_measurement": "UV Index",
            "value_template": "{{ value|int }}",
            "state_class": "measurement"
        }
    },
    "uvi": {
        "device_type": "sensor",
        "object_suffix": "uvi",
        "config": {
            "name": "UV Index",
            "unit_of_measurement": "UV Index",
            "value_template": "{{ value|int }}",
            "state_class": "measurement"
        }
    },
    
        "power_W": {
        "device_type": "sensor",
        "object_suffix": "watts",
        "config": {
            "device_class": "power",
            "name": "Power",
            "unit_of_measurement": "W",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    
    },
  },

    "rain_rate_in_h": {
        "device_type": "sensor",
        "object_suffix": "RR",
        "config": {
            "device_class": "precipitation_intensity",
            "name": "Rain Rate",
            "unit_of_measurement": "mm/h",
            "value_template": "{{ (float(value|float) * 25.4) | round(2) }}",
            "state_class": "measurement"
        }
        
    "noise": {
        "device_type": "sensor",
        "object_suffix": "noise",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
            "value_template": "{{ value|float|round(2) }}",
            "state_class": "measurement",
            "entity_category": "diagnostic"
        }
    },

    "depth_cm": {
        "device_type": "sensor",
        "object_suffix": "D",
        "config": {
            "name": "Depth",
            "unit_of_measurement": "cm",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },
    "energy_kWh": {
        "device_type": "sensor",
        "object_suffix": "kwh",
        "config": {
            "device_class": "power",
            "name": "Energy",
            "unit_of_measurement": "kWh",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }
    },
  
    "current_A": {
        "device_type": "sensor",
        "object_suffix": "A",
        "config": {
            "device_class": "current",
            "name": "Current",
            "unit_of_measurement": "A",
            "value_template": "{{ value|float }}",
            "state_class": "measurement"
        }

    "storm_dist": {
        "device_type": "sensor",
        "object_suffix": "stdist",
        "config": {
            "name": "Lightning Distance",
            "unit_of_measurement": "mi",
            "value_template": "{{ value|int }}",
            "state_class": "measurement"
        }
    },
    "strike_distance": {
        "device_type": "sensor",
        "object_suffix": "stdist",
        "config": {
            "name": "Lightning Distance",
            "unit_of_measurement": "mi",
            "value_template": "{{ value|int }}",
            "state_class": "measurement"
        }
    },

    "strike_count": {
        "device_type": "sensor",
        "object_suffix": "strcnt",
        "config": {
            "name": "Lightning Strike Count",
            "value_template": "{{ value|int }}",
            "state_class": "total_increasing"
        }
    },

    "consumption_data": {
        "device_type": "sensor",
        "object_suffix": "consumption",
        "config": {
            "name": "SCM Consumption Value",
            "value_template": "{{ value|int }}",
            "state_class": "total_increasing",
        }
    },
  
    "consumption": {
        "device_type": "sensor",
        "object_suffix": "consumption",
        "config": {
            "name": "SCMplus Consumption Value",
            "value_template": "{{ value|int }}",
            "state_class": "total_increasing",
        }
    },
# Add configuration for other components (number, sensor, switch) based on your requirements

# Example of switch configuration
SWITCHES = {
    "example_switch": {
        "device_type": "switch",
        "config": {
            "name": "Example Switch",
            # Add other switch configuration options
        }
    },
    # Add more switches as needed
}



## binary_sensor.py
  "tamper": {
        "device_type": "binary_sensor",
        "object_suffix": "tamper",
        "config": {
            "device_class": "safety",
            "force_update": "true",
            "payload_on": "1",
            "payload_off": "0",
            "entity_category": "diagnostic"
        }
      "closed": {
        "device_type": "binary_sensor",
        "object_suffix": "closed",
        "config": {
            "device_class": "safety",
            "force_update": "true",
            "payload_on": "1",
            "payload_off": "0",
        }
    },

    "alarm": {
        "device_type": "binary_sensor",
        "object_suffix": "alarm",
        "config": {
            "device_class": "safety",
            "force_update": "true",
            "payload_on": "1",
            "payload_off": "0",
            "entity_category": "diagnostic"
        }
    "detect_wet": {
        "device_type": "binary_sensor",
        "object_suffix": "moisture",
        "config": {
            "name": "Water Sensor",
            "device_class": "moisture",
            "force_update": "true",
            "payload_on": "1",
            "payload_off": "0"
        }
    },
    
    
## device automation

    "channel": {
        "device_type": "device_automation",
        "object_suffix": "CH",
        "config": {
           "automation_type": "trigger",
           "type": "button_short_release",
           "subtype": "button_1",
        }
    },

    "button": {
        "device_type": "device_automation",
        "object_suffix": "BTN",
        "config": {
           "automation_type": "trigger",
           "type": "button_short_release",
           "subtype": "button_1",
        }
    },
# Use secret_knock to trigger device automations for Honeywell ActivLink
# doorbells. We have this outside of mappings as we need to configure two
# different configuration topics.
secret_knock_mappings = [

    {
        "device_type": "device_automation",
        "object_suffix": "Knock",
        "config": {
            "automation_type": "trigger",
            "type": "button_short_release",
            "subtype": "button_1",
            "payload": 0,
        }
    },

    {
        "device_type": "device_automation",
        "object_suffix": "Secret-Knock",
        "config": {
            "automation_type": "trigger",
            "type": "button_triple_press",
            "subtype": "button_1",
            "payload": 1,
        }
    },
    
## number.py

## button.py

## switch.py

