import asyncio
import logging
import random
from datetime import timedelta
from json.decoder import JSONDecodeError

import async_timeout
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from h11 import Data
from homeassistant import core
from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry
from homeassistant.exceptions import IntegrationError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.discovery import async_load_platform
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import (DataUpdateCoordinator,
                                                      UpdateFailed)

from .const import DOMAIN, WS_HOST, NAME, PLATFORMS, WS_ID
from .rtl_433 import rtl433http

_LOGGER = logging.getLogger(__name__)

async def async_setup(_hass, _config):
    return True

async def async_setup_entry(hass: core.HomeAssistant, entry: ConfigEntry)-> bool:
    """Set up the platform."""

    ws_host = entry.data.get(WS_HOST)

    SDR = rtl433http()
    SDR.set_ip(ws_host)
    try:
        sdr_id = await sdr.get_sdr_id()
    except JSONDecodeError:
        try:
            await asyncio.sleep(random.randint(1,3))
            sdr_id = await sdr.get_sdr_id()
        except JSONDecodeError:
            await asyncio.sleep(random.randint(1,3))
            sdr_id = await sdr.get_sdr_id()

    _LOGGER.debug(f"Found SDR_ID: {sdr_id}")

    gateway_config = await sdr.get_sdr_config(sdr_id)
    if "end_dev" not in gateway_config:
        raise IntegrationError("RTL_433 needs to be updated")

    devices = {
        "devs": sdr_config["end_dev"],
        "names": sdr_config["dev_name"],
    }
    _LOGGER.debug(f"Found devices: {devices}")

    coordinator_conf = {
        WS_HOST: ws_host,
        SDR_ID: sdr_id,
    }
    counter = 0
    protocol_list = []
    for tap_id in devices["devs"]:
        coordinator = RtlCoordinator(hass, linker, coordinator_conf, tap_id)
        device_name = devices["names"][counter]
        tap_list.append({
            NAME: device_name,
            TAP_ID: tap_id,
            WS_HOST: ws_host,
            "coordinator": coordinator
        })
        counter = counter + 1
        await coordinator.async_config_entry_first_refresh()
        _LOGGER.debug(f"Coordinator has synced for {tap_id}")
    _LOGGER.debug(f"List of Devices: {tap_list}")

    vol_unit = gateway_config["vol_unit"]
    _LOGGER.debug(f"Setting volume unit to {vol_unit}")

    conf = {
        WS_HOST: ws_host,
        "Protocol": protocol_list,
        "vol_unit": vol_unit,
    }

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {"conf": conf}
    _LOGGER.debug(hass.data[DOMAIN])
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    # Reload entry when its updated.
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

class RtltapCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, sdr, conf, protocol_id):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=13),
        )
        self.protocol_api = sdr
        self.conf = conf
        self.hass = hass
        self.protocol_id = protocol_id


    async def _async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """

        #tap_id = self.conf["taps"][TAP_ID]
        sdr_id = self.conf[sdr_ID]

        try:
            # Note: asyncio.TimeoutError and aiohttp.ClientError are already
            # handled by the data update coordinator.
            async with async_timeout.timeout(10):
                return await self.protocol_api.fetch_data(sdr_id, self.protocol_id)
        except:# ApiAuthError as err:
            await asyncio.sleep(random.randint(1,3))
            async with async_timeout.timeout(10):
                return await self.protocol_api.fetch_data(sdr_id, self.protocol_id)
            # Raising ConfigEntryAuthFailed will cancel future updates
            # and start a config flow with SOURCE_REAUTH (async_step_reauth)
        #    raise ConfigEntryAuthFailed from err
        #except ApiError as err:
        #    raise UpdateFailed(f"Error communicating with API: {err}")

async def async_reload_entry(hass: core.HomeAssistant, entry: ConfigEntry) -> None:
    """Reload the config entry when it changed."""
    await hass.config_entries.async_reload(entry.entry_id)
