from __future__ import annotations

import logging
import secrets

import voluptuous as vol
from homeassistant import config_entries

from .const import DEFAULT_NAME, DOMAIN, WS_PORT, WS_IP

_LOGGER = logging.getLogger(__name__)

@config_entries.HANDLERS.register(DOMAIN)
class RtlFlowHandler(config_entries.ConfigFlow):

    VERSION = 1

async def async_step_user(self, user_input=None):
    """Handle a flow start."""
    _LOGGER.debug(f"Starting async_step_user of {DEFAULT_NAME}")

    errors = None

    if user_input is not None:
        # Filter out any extra keys from user_input
        expected_keys = ['WS_IP', 'WS_PORT']
        filtered_user_input = {key: user_input[key] for key in expected_keys if key in user_input}

        await self.async_set_unique_id(secrets.token_hex(8))
        self._abort_if_unique_id_configured()
        return self.async_create_entry(title=DEFAULT_NAME, data=filtered_user_input)

    new_user_input = {
        vol.Required(WS_IP, description="Enter the IP address of the RTL_433 webserver", default=WS_IP): str,
        vol.Required(WS_PORT, description="Enter the port number of the RTL_433 webserver", default=WS_PORT): int,
    }

    schema = vol.Schema(new_user_input)

    return self.async_show_form(step_id="user", data_schema=schema, errors=errors)