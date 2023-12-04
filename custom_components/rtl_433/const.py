from enum import Enum
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

class BinarySensorDeviceClass(Enum):
    BATTERY = "battery"
    POWER = "power"
    MOTION = "motion"
    TAMPER = "tamper"
    MOISTURE = "moisture"
    DOOR = "door"
    SAFETY = "safety"
class SensorDeviceClass(Enum):
    TIMESTAMP = "timestamp"
    BATTERY = "battery"
    HUMIDITY = "humidity"
    PRESSURE = "pressure"
    WIND_SPEED = "wind_speed"
    SIGNAL_STRENGTH = "signal_strength"
    ILLUMINANCE = "illuminance"
    POWER = "power"
    MOTION = "motion"
    SOUND_PRESSURE = "sound_pressure"
    CARBON_DIOXIDE = "carbon_dioxide"
    VOLTAGE = "voltage"
    CURRENT = "current"
    PRECIPITATION = "precipitation"
    PRECIPITATION_INTENSITY = "precipitation_intensity"

class EntityCategory(Enum):
    DIAGNOSTIC = "diagnostic"

class StateClass(Enum):
    MEASUREMENT = "measurement"
    TOTAL_INCREASING = "total_increasing"

class RTL433SensorEntityDescription:
    def __init__(
        self,
        name,
        key,
        device_class=None,
        unit_of_measurement=None,
        value_template=None,
        state_class=None,
        entity_category=None,
    ):
        self.name = name
        self.key = key
        self.device_class = device_class
        self.unit_of_measurement = unit_of_measurement
        self.value_template = value_template
        self.state_class = state_class
        self.entity_category = entity_category
class BinarySensorEntityDescription:
    def __init__(
        self,
        name,
        key,
        device_class=None,
        unit_of_measurement=None,
        value_template=None,
        state_class=None,
        entity_category=None,
    ):
        self.name = name
        self.key = key
        self.device_class = device_class
        self.unit_of_measurement = unit_of_measurement
        self.value_template = value_template
        self.state_class = state_class
        self.entity_category = entity_category       
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
        19: "Nexus, FreeTec NC-7345 temperature/humidity sensor",
        20: "Ambient Weather F007TH, F016TH temperature sensor",
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
        40: "Acurite 592TXR Temp/Humidity, Lightning, 899 Rain, 3N1, Atlas",
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
        73: "LaCrosse TX141-Bv2, TX141TH-Bv2, TX141-Bv3, TX141W, TX145wsdth, sensor",
        74: "Acurite 00275rm,00276rm Temp/Humidity with optional probe",
        75: "LaCrosse TX35DTH-IT, TFA Dostmann 30.3155 Temperature/Humidity sensor",
        76: "LaCrosse TX29IT, TFA Dostmann 30.3159.IT Temperature sensor",
        77: "Vaillant calorMatic VRT340f Central Heating Control",
        78: "Fine Offset Electronics, WH25, Temperature/Humidity/Pressure Sensor",
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
        134: "AOK Weather Station, iWeather WS5029, Conrad AOK-5056, Optex 990018",
        135: "Philips outdoor temperature sensor (type AJ7010)",
        136: "ESIC EMT7110 power meter",
        137: "Globaltronics QUIGG GT-TMBBQ-05",
        138: "Globaltronics GT-WT-03 Sensor",
        139: "Norgo NGE101",
        140: "Elantra2012 TPMS",
        141: "Auriol HG02832, HG05124A-DCF, Rubicson 48957 temperature/humidity sensor",
        142: "Fine Offset Electronics/ECOWITT WH51, SwitchDoc Soil Moisture Sensor",
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
        172: "Bresser Weather Center 3-in-1 wind gauge, Froggit WH6000, Ventus C8488A",
        173: "Bresser Weather Center 7-in-1, Air Quality PM2.5 / PM10",
        174: "EcoDHOME Smart Socket and MCEE Solar monitor",
        175: "LaCrosse Technology View LTV-R1, LTV-R3 Rainfall Gauge, LTV-W1/W2 Win",
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
        215: "Emax W6, rebrand Altronics x70634 Newentor Q9, Otio 810025",
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
BINARY_SENSORS: [dict[str, BinarySensorEntityDescription]] = {
    "tamper": BinarySensorEntityDescription(
        name="Tamper",
        key="tamper",
        device_class=BinarySensorDeviceClass.TAMPER,
        entity_category=EntityCategory.DIAGNOSTIC
    ),
    "detect_wet": BinarySensorEntityDescription(
        name="Water Sensor",
        key="moisture",
        device_class=BinarySensorDeviceClass.MOISTURE,
    ),
    "closed": BinarySensorEntityDescription(
        name="Door Closed",
        key="Door",
        device_class=BinarySensorDeviceClass.DOOR,

    ),

    "alarm": BinarySensorEntityDescription(
        name="Alarm",
        key="alarm",
        device_class=BinarySensorDeviceClass.SAFETY,
    ),
}

# Numbers
NUMBERS = {
    # Add number configurations...
}

# Button
BUTTONS = {
    # Add button configurations...
}

SENSORS = {
    "time": RTL433SensorEntityDescription(
        name="Timestamp",
        key="time",
        device_class=SensorDeviceClass.TIMESTAMP,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    "battery_ok": RTL433SensorEntityDescription(
        name="Battery",
        key="battery_ok",
        device_class=SensorDeviceClass.BATTERY,
        unit_of_measurement="%",
        value_template="{{ float(value) * 99 + 1 }}",
        state_class=StateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    "humidity": RTL433SensorEntityDescription(
        name="Humidity",
        key="humidity",
        device_class=SensorDeviceClass.HUMIDITY,
        unit_of_measurement="%",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "humidity_1": RTL433SensorEntityDescription(
        name="Humidity 1",
        key="humidity_1",
        device_class=SensorDeviceClass.HUMIDITY,
        unit_of_measurement="%",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "humidity_2": RTL433SensorEntityDescription(
        name="Humidity 2",
        key="humidity_2",
        device_class=SensorDeviceClass.HUMIDITY,
        unit_of_measurement="%",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "moisture": RTL433SensorEntityDescription(
        name="Moisture",
        key="moisture",
        device_class=SensorDeviceClass.HUMIDITY,
        unit_of_measurement="%",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "pressure_hPa": RTL433SensorEntityDescription(
        name="Pressure",
        key="pressure_hPa",
        device_class=SensorDeviceClass.PRESSURE,
        unit_of_measurement="hPa",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "pressure_kPa": RTL433SensorEntityDescription(
        name="Pressure",
        key="pressure_kPa",
        device_class=SensorDeviceClass.PRESSURE,
        unit_of_measurement="kPa",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "wind_speed_km_h": RTL433SensorEntityDescription(
        name="Wind Speed",
        key="wind_speed_km_h",
        device_class=SensorDeviceClass.WIND_SPEED,
        unit_of_measurement="km/h",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "wind_avg_mi_h": RTL433SensorEntityDescription(
        name="Wind Speed",
        key="wind_avg_mi_h",
        device_class=SensorDeviceClass.WIND_SPEED,
        unit_of_measurement="mi/h",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "wind_avg_m_s": RTL433SensorEntityDescription(
        name="Wind Speed",
        key="wind_avg_m_s",
        device_class=SensorDeviceClass.WIND_SPEED,
        unit_of_measurement="m/s",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "wind_speed_m_s": RTL433SensorEntityDescription(
        name="Wind Speed",
        key="wind_speed_m_s",
        device_class=SensorDeviceClass.WIND_SPEED,
        unit_of_measurement="m/s",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "gust_speed_km_h": RTL433SensorEntityDescription(
        name="Gust Speed",
        key="gust_speed_km_h",
        device_class=SensorDeviceClass.WIND_SPEED,
        unit_of_measurement="km/h",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "noise": RTL433SensorEntityDescription(
        name="Noise",
        key="noise",
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        unit_of_measurement="dB",
        value_template="{{ value|float|round(2) }}",
        state_class=StateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    "signal": RTL433SensorEntityDescription(
        name="Signal Strength",
        key="signal",
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        unit_of_measurement="dB",
        value_template="{{ value|float|round(2) }}",
        state_class=StateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
    ),
    "uv": RTL433SensorEntityDescription(
        name="UV Index",
        key="uv",
        unit_of_measurement="UV Index",
        value_template="{{ value|int }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "lux": RTL433SensorEntityDescription(
        name="Outside Luminance",
        key="lux",
        device_class=SensorDeviceClass.ILLUMINANCE,
        unit_of_measurement="lx",
        value_template="{{ value|int }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "uvi": RTL433SensorEntityDescription(
        name="UV Index",
        key="uvi",
        unit_of_measurement="UV Index",
        value_template="{{ value|int }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "power_W": RTL433SensorEntityDescription(
        name="Power",
        key="power_W",
        device_class=SensorDeviceClass.POWER,
        unit_of_measurement="W",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "depth_cm": RTL433SensorEntityDescription(
        name="Depth",
        key="depth_cm",
        unit_of_measurement="cm",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "rain_mm": RTL433SensorEntityDescription(
        name="Rain Total",
        key="rain_mm",
        device_class=SensorDeviceClass.PRECIPITATION,
        unit_of_measurement="mm",
        value_template="{{ value|float|round(2) }}",
        state_class=StateClass.TOTAL_INCREASING,
    ),
    "rain_rate_mm_h": RTL433SensorEntityDescription(
        name="Rain Rate",
        key="rain_rate_mm_h",
        device_class=SensorDeviceClass.PRECIPITATION_INTENSITY,
        unit_of_measurement="mm/h",
        value_template="{{ value|float }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "rain_in": RTL433SensorEntityDescription(
        name="Rain Total",
        key="rain_in",
        device_class=SensorDeviceClass.PRECIPITATION,
        unit_of_measurement="mm",
        value_template="{{ (value|float) * 25.4 | round(2) }}",
        state_class=StateClass.TOTAL_INCREASING,
    ),
    "strike_distance": RTL433SensorEntityDescription(
        name="Lightning Distance",
        key="strike_distance",
        unit_of_measurement="mi",
        value_template="{{ value|int }}",
        state_class=StateClass.MEASUREMENT,
    ),
    "motion": RTL433SensorEntityDescription(
        name="Motion",
        key="motion",
        device_class=SensorDeviceClass.MOTION,
    ),
    "light_level": RTL433SensorEntityDescription(
        name="Light Level",
        key="light_level",
        device_class=SensorDeviceClass.ILLUMINANCE,
        unit_of_measurement="lux",
    ),
    "sound_level": RTL433SensorEntityDescription(
        name="Sound Level",
        key="sound_level",
        device_class=SensorDeviceClass.SOUND_PRESSURE,
        unit_of_measurement="dB",
    ),
    "co2": RTL433SensorEntityDescription(
        name="CO2 Level",
        key="co2",
        device_class=SensorDeviceClass.CARBON_DIOXIDE,
        unit_of_measurement="ppm",
    ),
    "voltage": RTL433SensorEntityDescription(
        name="Voltage",
        key="voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        unit_of_measurement="V",
    ),
    "current": RTL433SensorEntityDescription(
        name="Current",
        key="current",
        device_class=SensorDeviceClass.CURRENT,
        unit_of_measurement="A",
    ),
}

class AutomationType(Enum):
    TRIGGER = "trigger"

class ButtonType(Enum):
    SHORT_RELEASE = "button_short_release"
    TRIPLE_PRESS = "button_triple_press"

class SecretKnockMappings:
    @staticmethod
    def create_mapping(object_suffix, automation_type, button_type, payload):
        return {
            "device_type": "device_automation",
            "object_suffix": object_suffix,
            "config": {
                "automation_type": automation_type.value,
                "type": button_type.value,
                "subtype": "button_1",
                "payload": payload,
            },
        }

secret_knock_mappings = [
    SecretKnockMappings.create_mapping(
        object_suffix="Knock",
        automation_type=AutomationType.TRIGGER,
        button_type=ButtonType.SHORT_RELEASE,
        payload=0,
    ),
    SecretKnockMappings.create_mapping(
        object_suffix="Secret-Knock",
        automation_type=AutomationType.TRIGGER,
        button_type=ButtonType.TRIPLE_PRESS,
        payload=1,
    ),
]
