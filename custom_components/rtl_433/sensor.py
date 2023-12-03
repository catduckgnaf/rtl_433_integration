import asyncio
import json
import logging
import random

import aiohttp
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import *
from homeassistant.helpers.update_coordinator import (CoordinatorEntity,
                                                      DataUpdateCoordinator)
_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN, WS_HOST, MANUFACTURER, NAME, SENSORS
from homeassistant.util import slugify

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass, config, async_add_entities, discovery_info=None
):
    """Setup the sensor platform."""


class Rtl433Sensor(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator: DataUpdateCoordinator, hass, protocol, data_attribute, unit, device_class=False, icon=False):
        super().__init__(coordinator)
        self._state = None
        self._name = protocol[NAME] + " " + name
        self.protocol_id = protocol[protocol_ID]
        self.protocol_name = protocol[NAME]
        self.platform = "sensor"
        
    @property
    def unique_id(self):
        """Return the unique ID of the sensor."""
        return self._attr_unique_id


    @property
    def state(self):

        attributes = self.coordinator.data
        _LOGGER.debug(f"Sensor state: {attributes}")

        if not attributes:
            self._state = "unknown"
        else:
            self._state = attributes[self.attribute]

        return self._state
