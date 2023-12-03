import asyncio
import json
import logging
import random

import aiohttp
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers import entity_platform, service
from homeassistant.helpers.entity import *
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (CoordinatorEntity,
                                                      DataUpdateCoordinator)
from homeassistant.util import slugify

_LOGGER = logging.getLogger(__name__)


from .const import DOMAIN, WS_HOST, MANUFACTURER, NAME, BINARY_SENSORS
from .entity import *


async def async_setup_entry(
    hass, config, async_add_entities, discovery_info=None
):
    """Setup the sensor platform."""
    #config_id = config.unique_id
    #_LOGGER.debug(f"Configuring binary sensor entities for config {config_id}")
    #if config_id not in hass.data[DOMAIN]:
    #    await asyncio.sleep(random.randint(1,3))
    #devices = hass.data[DOMAIN][config_id]["conf"]["devices"]
    devices = hass.data[DOMAIN][config.entry_id]["conf"]["devices"]
    binary_sensors = []
    for device in devices:
        coordinator = device["coordinator"]
        _LOGGER.debug(f"Configuring binary sensors for Device {device}")
        binary_sensors.append(RtlBinarySensor(coordinator, hass, device=device, name="closed", data_attribute="closed"))
        binary_sensors.append(RtlBinarySensor(coordinator, hass, device=device, data_attribute="tamper", icon="mdi:meter-electric-outline"))
    async_add_entities(binary_sensors, True)

    platform = entity_platform.async_get_current_platform()
    platform.async_register_entity_service("dismiss_alerts", {}, "_dismiss_alerts")
    platform.async_register_entity_service("dismiss_alert", {}, "_dismiss_alert")

class RtlBinarySensor(CoordinatorEntity, BinarySensorEntity):

    def __init__(self, coordinator: DataUpdateCoordinator, hass, device, data_attribute, name=False, device_class=False, icon=False):
        super().__init__(coordinator)
        self._state = None
        if not name:
            name = data_attribute.replace("_", " ").title()
        self._name = device[NAME] + " " + name
        self._id = self._name
        self._data_check_attribute = data_attribute
        self.device_id = device[DEVICE_ID]
        self.device_name = device[NAME]
        self.device_api = coordinator.device_api
        self.platform = "binary_sensor"
        self._attr_unique_id = slugify(f"{DOMAIN}_{self.platform}_{data_attribute}_{self.device_id}")
        if device_class:
            self._attr_device_class = device_class
        if icon:
            self._attr_icon = icon
        self._attrs = {}
        self._attr_device_info = DeviceInfo(
            #entry_type=DeviceEntryType.SERVICE,
            identifiers={
                (DOMAIN, device[DEVICE_ID])
            },
            name=device[NAME],
            manufacturer=MANUFACTURER,
            model=device[DEVICE_ID],
            configuration_url="http://" + [WS_HOST] + "/"
        )

    @property
    def unique_id(self):
        """Return the unique ID of the sensor."""
        return self._attr_unique_id

    @property
    def name(self):
        return f"{MANUFACTURER} {self._name}"

    @property
    def extra_state_attributes(self):
        return self._attrs

    @property
    def state(self):
        attributes = self.coordinator.data
        data_attr = attributes[self._data_check_attribute]
        state = "on" if data_attr else "off"
        return state

    @property
    def device_info(self) -> DeviceInfo:
        return self._attr_device_info

    async def _dismiss_alerts(self):
        _LOGGER.debug(f"Dismissing all alerts for {self.entity_id}")
        await self.device_api.dismiss_alert(self.coordinator.get_sdr_id(), self.device_id)


    async def _dismiss_alert(self):
        split_name = self._data_check_attribute.split("_")
        alert_type = split_name[len(split_name)-1]
        alert_id = self.alert_lookup(alert_type)
        if alert_id is not None:
            _LOGGER.debug(f"Dismissing {alert_type} alert for {self.entity_id}")
            await self.device_api.dismiss_alert(self.coordinator.get_sdr_id(), self.device_id)
        else:
            _LOGGER.debug("No matching alert found. Do nothing")

    def alert_lookup(self, alert_name):
        alerts = {
            "open" :0,
            "closed": 1,
            "tamper": 2
        }
        if alert_name in alerts:
            return alerts[alert_name]
        else:
            return None
