import asyncio
import json
import logging
import random

import aiohttp
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.switch import SwitchEntity
from homeassistant.const import STATE_UNKNOWN
from homeassistant.helpers.entity import *
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (CoordinatorEntity,
                                                      DataUpdateCoordinator)
from homeassistant.util import slugify

_LOGGER = logging.getLogger(__name__)

from .const import  DOMAIN, WS_HOST, MANUFACTURER, NAME

async def async_setup_entry(
    hass, config, async_add_entities, discovery_info=None
):
    """Setup the switch platform."""

    protocols = hass.data[DOMAIN][config.entry_id]["conf"]["protocols"]
    switches = []
    for protocol in protocols:
        coordinator = protocol["coordinator"]
        _LOGGER.debug(f"Configuring switch for protocol {protocol}")
        switches.append(RtlSwitch(coordinator, hass, protocol))
    async_add_entities(switches, True)

class RtlSwitch(CoordinatorEntity, SwitchEntity):
    def __init__(self, coordinator: DataUpdateCoordinator, hass, protocol):
        super().__init__(coordinator)
        self._state = None
        self.protocol_id = protocol[PROTOCOL_ID]
        self.protocol_api = coordinator.protocol_api
        self.platform = "switch"
        self.hass = hass
        self._attr_unique_id = slugify(f"{DOMAIN}_{self.platform}_{self.protocol_id}")
        self._attr_icon = "mdi:water-pump"
        self._attrs = {
            "data": self.coordinator.data,
            "duration_entity": self.duration_entity,
            "volume_entity": self.volume_entity
        }
        self._attr_device_info = DeviceInfo(
            identifiers={
                (DOMAIN, protocol[PROTOCOL_ID])
            },
            name=[NAME],
            manufacturer=MANUFACTURER,
            configuration_url="http://" + [WS_HOST]
        )

    @property
    def unique_id(self):
        return self._attr_unique_id

    @property
    def name(self):
        return f"{MANUFACTURER} {self._name}"

    @property
    def duration_entity(self):
        name = self._name.replace(" ", "_")
        name = self._name.replace("-", "_")
        return f"number.{DOMAIN}_{name}_duration".lower()

    @property
    def volume_entity(self):
        name = self._name.replace(" ", "_")
        name = self._name.replace("-", "_")
        return f"number.{DOMAIN}_{name}_volume".lower()

    async def async_turn_on(self, **kwargs):
        duration = self.get_watering_duration()
        seconds = int(float(duration)) * 60
        #volume = self.get_watering_volume()
        #watering_volume = None
        #if volume != DEFAULT_VOL:
        #    watering_volume = volume
        gw_id = self.coordinator.get_gw_id()
        attributes = await self.protocol_api.turn_on(gw_id, self.protocol_id, seconds, self.get_watering_volume())
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        gw_id = self.coordinator.get_gw_id()
        attributes = await self.protocol_api.turn_off(gw_id, self.protocol_id)
        await self.coordinator.async_request_refresh()

    @property
    def is_on(self):
        return self.state()

    @property
    def device_info(self) -> DeviceInfo:
        return self._attr_device_info
