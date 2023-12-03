import asyncio
import logging
import random

from homeassistant.components.number import RestoreNumber
from homeassistant.const import STATE_UNKNOWN
from homeassistant.helpers.entity import *
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (CoordinatorEntity,
                                                      DataUpdateCoordinator)
from homeassistant.util import slugify

_LOGGER = logging.getLogger(__name__)

from .const import (DEFAULT_TIME, DEFAULT_VOL, DOMAIN, WS_HOST,
                    MANUFACTURER, NAME)


async def async_setup_entry(
    hass, config, async_add_entities, discovery_info=None
):
    """Setup the number platform."""
    #config_id = config.unique_id
    #_LOGGER.debug(f"Configuring number entities for config {config_id}")
    #if config_id not in hass.data[DOMAIN]:
    #    await asyncio.sleep(random.randint(1,3))
    #protocols = hass.data[DOMAIN][config_id]["conf"]["protocols"]
    protocols = hass.data[DOMAIN][config.entry_id]["conf"]["protocols"]
    numbers = []
    for protocol in protocols:
        """For each protocol, we set a number for duration and volume"""
        _LOGGER.debug(f"Configuring numbers for protocol {protocol}")
        coordinator = coordinator = protocol["coordinator"]
        numbers.append(RtlNumber(coordinator, hass, protocol, "Watering Duration", "mdi:clock", "m"))
        numbers.append(RtlNumber(coordinator, hass, protocol, "Watering Volume", "mdi:water", hass.data[DOMAIN][config.entry_id]["conf"]["vol_unit"]))

    async_add_entities(numbers, True)

class RtlNumber(CoordinatorEntity, RestoreNumber):
    def __init__(self, coordinator: DataUpdateCoordinator, hass, protocol, number_suffix, icon, unit_of_measurement):
        super().__init__(coordinator)
        self._state = None
        self._name = protocol[NAME]
        self._id = self._name
        self.protocol_id = protocol[PROTOCOL_ID]
        self.platform = "number"
        self._attr_unique_id = slugify(f"{DOMAIN}_{self.platform}_{self.protocol_id}_{number_suffix.replace(' ', '_')}")
        self._attr_native_min_value = 0
        self._attr_native_max_value = 120
        self._attr_native_step = 5
        self._attr_native_unit_of_measurement = unit_of_measurement#"m"
        self._attr_icon = icon#"mdi:clock"
        self.number_suffix = number_suffix
        self._attr_device_info = DeviceInfo(
            identifiers={
                (DOMAIN, protocol[protocol_ID])
            },
            name=protocol[NAME],
            manufacturer=[MANUFACTURER],
            model=protocol[PROTOCOL_ID],
            configuration_url="http://" + [WS_HOST]
        )

        self._attrs = {}

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        restored_number = await self.async_get_last_number_data()
        if restored_number is not None and restored_number.native_value != STATE_UNKNOWN:
            _LOGGER.debug(f"Restoring value to {restored_number.native_value}")
            self._attr_native_value = restored_number.native_value
        else:
            _LOGGER.debug(f"No value found to restore -- setting default")
            if self.number_suffix == "Watering Volume":
                self._attr_native_value = DEFAULT_VOL
            else:
                self._attr_native_value = DEFAULT_TIME
        self.async_write_ha_state()

    @property
    def unique_id(self):
        return self._attr_unique_id

    @property
    def extra_state_attributes(self):
        return self._attrs

    @property
    def name(self):
        return f"{MANUFACTURER} {self._name} {self.number_suffix}"#Watering Duration"

    @property
    def device_info(self) -> DeviceInfo:
        return self._attr_device_info

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._attr_native_value = value
        self.async_write_ha_state()
        await self.coordinator.async_request_refresh()
