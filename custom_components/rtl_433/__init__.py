import asyncio
import logging
import random
from datetime import timedelta
from json.decoder import JSONDecodeError

import async_timeout
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant import core
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import IntegrationError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (DataUpdateCoordinator,
                                                      UpdateFailed)

from .const import DOMAIN, WS_HOST, NAME, PLATFORMS, WS_ID
from .entity import *

_LOGGER = logging.getLogger(__name__)

async def async_setup(_hass, _config):
    return True

async def async_setup_entry(hass: core.HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the platform."""

    ws_host = entry.data.get(WS_HOST)

    protocol_config = entry.data.get("protocol_config", {})

    devices = {
        "devs": protocol_config.get("end_dev", []),
        "names": protocol_config.get("protocol_name", []),
    }
    _LOGGER.debug(f"Found devices: {devices}")

    coordinator_conf = {
        WS_HOST: ws_host,
    }
    protocol_list = []
    for counter, protocol_id in enumerate(devices["devs"]):
        coordinator = RtlCoordinator(hass, coordinator_conf, protocol_id)
        device_name = devices["names"][counter]
        protocol_list.append({
            NAME: device_name,
            WS_ID: protocol_id,
            WS_HOST: ws_host,
            "coordinator": coordinator
        })
        await coordinator.async_config_entry_first_refresh()
        _LOGGER.debug(f"Coordinator has synced for {protocol_id}")
    _LOGGER.debug(f"List of Devices: {protocol_list}")

    vol_unit = gateway_config.get("vol_unit", "")
    _LOGGER.debug(f"Setting volume unit to {vol_unit}")

    conf = {
        WS_HOST: ws_host,
        "Protocol": protocol_list,
        "vol_unit": vol_unit,
    }

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {"conf": conf}
    _LOGGER.debug(hass.data[DOMAIN])
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    # Reload entry when it's updated.
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True

async def async_unload_entry(hass: core.HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a component config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok

async def async_remove_config_entry_device(hass: core.HomeAssistant, entry: ConfigEntry, device) -> bool:
    device_registry(hass).async_remove_device(device.id)
    return True

class RtlCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, protocol, conf, protocol_id):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=13),
        )
        self.protocol_api = protocol
        self.conf = conf
        self.hass = hass
        self.protocol_id = protocol_id

    async def _async_update_data(self):
        protocol_id = self.conf.get("protocol_ID", "")

        try:
            async with async_timeout.timeout(10):
                return await self.protocol_api.fetch_data(protocol_id, self.protocol_id)
        except async_timeout.TimeoutError:
            _LOGGER.warning("Timeout while fetching data")
        except Exception as e:
            _LOGGER.error(f"Error updating data: {e}")

async def async_reload_entry(hass: core.HomeAssistant, entry: ConfigEntry) -> None:
    await hass.config_entries.async_reload(entry.entry_id)
