

# Config Flow
WS_ID = "ID of rtl_433 Webserver"
WS_HOST= "192.1688.0.100:9443"
SDR_ID = "ID of rtl_433 Gateway"
SDR_NAME = "ID of rtl_433 Gateway"
DEFAULT_NAME = "RTL_433 HTTP"
NAME = "RTL_433 HTTP"
DOMAIN = "rtl_433"
DEVICE_ID = "ID of Individual RF Device"
DEVICE_MODEL = "Model of RF Device"
DEVICE_FREQ = "Frequency of RF Device"

# Attributes
PLATFORMS = ['number', 'binary_sensor', 'sensor', 'switch']
MANUFACTURER = "RTL_SDR"

# Protocols
PROTOCOLS = {
        1: "Silvercrest Remote Control",
        2: "Rubicson, TFA 30.3197 or InFactory PT-310 Temperature Sensor",
        3: "Prologue, FreeTec NC-7104, NC-7159-675 temperature sensor",
        4: "Waveman Switch Transmitter",
        8: "LaCrosse TX Temperature / Humidity Sensor",
        10: "Acurite 896 Rain Gauge",
        11: "Acurite 609TXC Temperature and Humidity Sensor",
        12: "Oregon Scientific Weather Sensor",
        15: "KlikAanKlikUit Wireless Switch",
        16: "AlectoV1 Weather Sensor (Alecto WS3500 WS4500 Ventus W155/W044 Oregon)",
        17: "Cardin S466-TX2",
        18: "Fine Offset Electronics, WH2, WH5, Telldus Temperature/Humidity/Rain Sensor",
        19: "Nexus, FreeTec NC-7345, NX-3980, Solight TE82S, TFA 30.3209 temperature/humidity sensor",
        20: "Ambient Weather F007TH, TFA 30.3208.02, SwitchDocLabs F016TH temperature sensor",
        21: "Calibeur RF-104 Sensor",
        22: "X10 RF",
        23: "DSC Security Contact",
        25: "Globaltronics GT-WT-02 Sensor",
        26: "Danfoss CFR Thermostat",
        29: "Chuango Security Technology",
        30: "Generic Remote SC226x EV1527",
        31: "TFA-Twin-Plus-30.3049, Conrad KW9010, Ea2 BL999",
        32: "Fine Offset Electronics WH1080/WH3080 Weather Station",
        33: "WT450, WT260H, WT405H",
        34: "LaCrosse WS-2310 / WS-3600 Weather Station",
        35: "Esperanza EWS",
        36: "Efergy e2 classic",
        38: "Generic temperature sensor 1",
        39: "WG-PB12V1 Temperature Sensor",
        40: "Acurite 592TXR Temp/Humidity, 592TX Temp, 5n1 Weather Station, 6045 Lightning, 899 Rain, 3N1, Atlas",
        41: "Acurite 986 Refrigerator / Freezer Thermometer",
        42: "HIDEKI TS04 Temperature, Humidity, Wind and Rain Sensor",
        43: "Watchman Sonic / Apollo Ultrasonic / Beckett Rocket oil tank monitor",
        44: "CurrentCost Current Sensor",
        45: "emonTx OpenEnergyMonitor",
        46: "HT680 Remote control",
        47: "Conrad S3318P, FreeTec NC-5849-913 temperature humidity sensor",
        48: "Akhan 100F14 remote keyless entry",
        49: "Quhwa",
        50: "OSv1 Temperature Sensor",
        51: "Proove / Nexa / KlikAanKlikUit Wireless Switch",
        52: "Bresser Thermo-/Hygro-Sensor 3CH",
        53: "Springfield Temperature and Soil Moisture",
        54: "Oregon Scientific SL109H Remote Thermal Hygro Sensor",
        55: "Acurite 606TX Temperature Sensor",
        56: "TFA pool temperature sensor",
        57: "Kedsum Temperature & Humidity Sensor, Pearl NC-7415",
        58: "Blyss DC5-UK-WH",
        59: "Steelmate TPMS",
        60: "Schrader TPMS",
        63: "Efergy Optical",
        67: "Radiohead ASK",
        68: "Kerui PIR / Contact Sensor",
        69: "Fine Offset WH1050 Weather Station",
        70: "Honeywell Door/Window Sensor, 2Gig DW10/DW11, RE208 repeater",
        71: "Maverick ET-732/733 BBQ Sensor",
        73: "LaCrosse TX141-Bv2, TX141TH-Bv2, TX141-Bv3, TX141W, TX145wsdth, (TFA, ORIA) sensor",
        74: "Acurite 00275rm,00276rm Temp/Humidity with optional probe",
        75: "LaCrosse TX35DTH-IT, TFA Dostmann 30.3155 Temperature/Humidity sensor",
        76: "LaCrosse TX29IT, TFA Dostmann 30.3159.IT Temperature sensor",
        77: "Vaillant calorMatic VRT340f Central Heating Control",
        78: "Fine Offset Electronics, WH25, WH32B, WH24, WH65B, HP1000, Misol WS2320 Temperature/Humidity/Pressure Sensor",
        79: "Fine Offset Electronics, WH0530 Temperature/Rain Sensor",
        80: "IBIS beacon",
        81: "Oil Ultrasonic STANDARD FSK",
        82: "Citroen TPMS",
        83: "Oil Ultrasonic STANDARD ASK",
        84: "Thermopro TP11 Thermometer",
        85: "Solight TE44/TE66, EMOS E0107T, NX-6876-917",
        86: "Wireless Smoke and Heat Detector GS 558",
        87: "Generic wireless motion sensor",
        88: "Toyota TPMS",
        89: "Ford TPMS",
        90: "Renault TPMS",
        91: "inFactory, nor-tec, FreeTec NC-3982-913 temperature humidity sensor",
        92: "FT-004-B Temperature Sensor",
        93: "Ford Car Key",
        94: "Philips outdoor temperature sensor (type AJ3650)",
        95: "Schrader TPMS EG53MA4, PA66GF35",
        96: "Nexa",
        97: "ThermoPro TP08/TP12/TP20 thermometer",
        98: "GE Color Effects",
        99: "X10 Security",
        100: "Interlogix GE UTC Security Devices",
        102: "Sensible Living Mini-Plant Moisture Sensor",
        103: "Wireless M-Bus, Mode C&T, 100kbps (-f 868.95M -s 1200k)",
        104: "Wireless M-Bus, Mode S, 32.768kbps (-f 868.3M -s 1000k)",
        108: "Hyundai WS SENZOR Remote Temperature Sensor",
        109: "WT0124 Pool Thermometer",
        110: "PMV-107J (Toyota) TPMS",
        111: "Emos TTX201 Temperature Sensor",
        112: "Ambient Weather TX-8300 Temperature/Humidity Sensor",
        113: "Ambient Weather WH31E Thermo-Hygrometer Sensor, EcoWitt WH40 rain gauge",
        114: "Maverick et73",
        115: "Honeywell ActivLink, Wireless Doorbell",
        116: "Honeywell ActivLink, Wireless Doorbell (FSK)",
        129: "Eurochron temperature and humidity sensor",
        130: "IKEA Sparsnas Energy Meter Monitor",
        131: "Microchip HCS200/HCS300 KeeLoq Hopping Encoder based remotes",
        132: "TFA Dostmann 30.3196 T/H outdoor sensor",
        133: "Rubicson 48659 Thermometer",
        134: "AOK Weather Station rebrand Holman Industries iWeather WS5029, Conrad AOK-5056, Optex 990018",
        135: "Philips outdoor temperature sensor (type AJ7010)",
        136: "ESIC EMT7110 power meter",
        137: "Globaltronics QUIGG GT-TMBBQ-05",
        138: "Globaltronics GT-WT-03 Sensor",
        139: "Norgo NGE101",
        140: "Elantra2012 TPMS",
        141: "Auriol HG02832, HG05124A-DCF, Rubicson 48957 temperature/humidity sensor",
        142: "Fine Offset Electronics/ECOWITT WH51, SwitchDoc Labs SM23 Soil Moisture Sensor",
        143: "Holman Industries iWeather WS5029 weather station (older PWM)",
        144: "TBH weather sensor",
        145: "WS2032 weather station",
        146: "Auriol AFW2A1 temperature/humidity sensor",
        147: "TFA Drop Rain Gauge 30.3233.01",
        148: "DSC Security Contact (WS4945)",
        155: "Fine Offset Electronics WH1080/WH3080 Weather Station (FSK)",
        157: "Missil ML0757 weather station",
        158: "Sharp SPC775 weather station",
        159: "Insteon",
        170: "LaCrosse Technology View LTV-WR1 Multi Sensor",
        171: "LaCrosse Technology View LTV-TH Thermo/Hygro Sensor",
        172: "Bresser Weather Center 6-in-1, 7-in-1 indoor, soil, new 5-in-1, 3-in-1 wind gauge, Froggit WH6000, Ventus C8488A",
        173: "Bresser Weather Center 7-in-1, Air Quality PM2.5 / PM10",
        174: "EcoDHOME Smart Socket and MCEE Solar monitor",
        175: "LaCrosse Technology View LTV-R1, LTV-R3 Rainfall Gauge, LTV-W1/W2 Wind Sensor",
        176: "BlueLine Innovations Power Cost Monitor",
        177: "Burnhard BBQ thermometer",
        178: "Security+ (Keyfob)",
        179: "Cavius smoke, heat and water detector",
        180: "Jansite TPMS Model Solar",
        181: "Amazon Basics Meat Thermometer",
        182: "TFA Marbella Pool Thermometer",
        183: "Auriol AHFL temperature/humidity sensor",
        184: "Auriol AFT 77 B2 temperature sensor",
        185: "Honeywell CM921 Wireless Programmable Room Thermostat",
        186: "Hyundai TPMS (VDO)",
        187: "RojaFlex shutter and remote devices",
        188: "Marlec Solar iBoost+ sensors",
        189: "Somfy io-homecontrol",
        190: "Ambient Weather WH31L (FineOffset WH57) Lightning-Strike sensor",
        191: "Markisol, E-Motion, BOFU, Rollerhouse, BF-30x, BF-415 curtain remote",
        192: "Govee Water Leak Detector H5054, Door Contact Sensor B5023",
        193: "Clipsal CMR113 Cent-a-meter power meter",
        194: "Inkbird ITH-20R temperature humidity sensor",
        195: "RainPoint soil temperature and moisture sensor",
        196: "Atech-WS308 temperature sensor",
        197: "Acurite Grill/Meat Thermometer 01185M",
        204: "Jasco/GE Choice Alert Security Devices",
        205: "Telldus weather station FT0385R sensors",
        206: "LaCrosse TX34-IT rain gauge",
        207: "SmartFire Proflame 2 remote control",
        208: "AVE TPMS",
        209: "SimpliSafe Gen 3 Home Security System",
        210: "Yale HSA (Home Security Alarm), YES-Alarmkit",
        211: "Regency Ceiling Fan Remote (-f 303.75M to 303.96M)",
        212: "Renault 0435R TPMS",
        213: "Fine Offset Electronics WS80 weather station",
        214:  "EMOS E6016 weatherstation with DCF77",
        215: "Emax W6, rebrand Altronics x70634 Newentor Q9, Otio 810025, Protmex PT3390A, Jula Marquant 014331/32",
        216:  "ANT and ANT+ devices",
        217:  "EMOS E6016 rain gauge",
        218:  "Microchip HCS200/HCS300 KeeLoq Hopping Encoder based remotes (FSK)",
        219:  "Fine Offset Electronics WH45 air quality sensor",
        220:  "Maverick XR-30 BBQ Sensor",
        221:  "Fine Offset Electronics WN34 temperature sensor",
        222:  "Rubicson Pool Thermometer 48942",
        223:  "Badger ORION water meter, 100kbps (-f 916.45M -s 1200k)",
        224:  "GEO minim+ energy monitor",
        225:  "TyreGuard 400 TPMS",
        226:  "Kia TPMS (-s 1000k)",
        227:  "SRSmith Pool Light Remote Control SRS-2C-TX (-f 915M)",
        228:  "Neptune R900 flow meters",
        229:  "WEC-2103 temperature/humidity sensor",
        230:  "Vauno EN8822C",
        231:  "Govee Water Leak Detector H5054",
        232:  "TFA Dostmann 14.1504.V2 Radio-controlled grill and meat thermometer",
        233:  "CED7000 Shot Timer",
        234:  "Watchman Sonic Advanced / Plus, Tekelek",
        235:  "Oil Ultrasonic SMART FSK",
        236:  "Gasmate BA1008 meat thermometer",
        237:  "Flowis flow meters",
        238:  "Wireless M-Bus, Mode T, 32.768kbps (-f 868.3M -s 1000k)",
        239:  "Revolt NC-5642 Energy Meter",
        240:  "LaCrosse TX31U-IT, The Weather Channel WS-1910TWC-IT",
        241:  "EezTire E618, Carchet TPMS",
        242:  "Baldr / RainPoint rain gauge.",
        243:  "Celsia CZC1 Thermostat",
        244:  "Fine Offset Electronics WS90 weather station",
        245:  "ThermoPro TX-2C Thermometer and Humidity sensor",
        246:  "TFA 30.3151 Weather Station",
        247:  "Bresser water leakage",
        248:  "Nissan TPMS",
        249:  "Bresser lightning",
        250: "Schou 72543 Day Rain Gauge"
    }

# key: name
BINARY_SENSORS: Final[dict[str, BinarySensorEntityDescription]] = {
    "tamper": BinarySensorEntityDescription(
        name="Tamper",
        key="tamper",
        device_class=BinarySensorDeviceClass.TAMPER,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
    ),
    "detect_wet": BinarySensorEntityDescription(
        name="Water Sensor",
        key="moisture",
        device_class=BinarySensorDeviceClass.MOISTURE,
    ),
    "closed": BinarySensorEntityDescription(
        name="Door Closed",
        key="Door"
        device_class=BinarySensorDeviceClass.DOOR,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
    ),
    "alarm": BinarySensorEntityDescription(
        name="Alarm",
        key="alarm",
        device_class=BinarySensorDeviceClass.SAFETY,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_registry_enabled_default=False,
    ),
}

    

# Binary Sensors
BINARY_SENSORS = {
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
    },
    "closed": {
        "device_type": "binary_sensor",
        "object_suffix": "closed",
        "config": {
            "device_class": "door",
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
}

# Sensor Types
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
    "signal": {
        "device_type": "sensor",
        "object_suffix": "signal",
        "config": {
            "device_class": "signal_strength",
            "unit_of_measurement": "dB",
            "value_template": "{{ value|float|round(2) }}",
            "state_class": "measurement",
            "entity_category": "diagnostic"
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
}




# Device Automations
DEVICE_AUTOMATIONS = {
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
}

# Switches
SWITCHES = {
    "example_switch": {
        "device_type": "switch",
        "config": {
            "name": "Example Switch",
            # Add other switch configuration options
        }
    },
}

# Numbers
NUMBERS = {
    # Add number configurations...
}

# Button
BUTTONS = {
    # Add button configurations...
}

# Use secret_knock to trigger device automations for Honeywell ActivLink doorbells.
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
]
