from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PLATFORM, CONF_HOST, CONF_PORT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN
from .api import IntegrationRtlApiClient
from .coordinator import Rtl433DataUpdateCoordinator
from .config_flow import RtlFlowHandler

# Define PLATFORMS in the global scope
PLATFORMS = [PLATFORM.SENSOR, PLATFORM.BINARY_SENSOR]

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the integration."""
    config_entries.async_setup_implementation(hass, config)

    # Register the config flow handler
    config_entries.HANDLERS.register(DOMAIN, RtlFlowHandler)

    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up this integration using UI."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator = Rtl433DataUpdateCoordinator(
        hass=hass,
        client=IntegrationRtlApiClient(
            host=entry.data[CONF_HOST],
            port=entry.data[CONF_PORT],
            session=async_get_clientsession(hass),
        ),
    )

    await coordinator.async_config_entry_first_refresh()

    # Use PLATFORM_SCHEMA instead of directly using PLATFORM
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORM_SCHEMA)
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    if unloaded := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
    return unloaded

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
