"""Adds config flow for rtl_433."""
from __future__ import annotations

import asyncio
import subprocess
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.helpers import selector

from .const import DOMAIN, LOGGER

class rtlFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for rtl_433."""

    VERSION = 1

    async def _test_connection(self, host: str, port: int) -> bool:
        """Test the connection to the specified host and port."""
        try:
            result = await asyncio.to_thread(subprocess.run, 
                ["ping", "-c", "1", f"{host}:{port}"],  # Adjust for Windows if needed
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return result.returncode == 0
        except Exception as e:
            LOGGER.error(f"Error testing connection: {e}")
            return False

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.FlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}
        if user_input is not None:
            host = user_input[CONF_HOST]
            port = user_input[CONF_PORT]

            # Test the connection before proceeding
            try:
                if not await self._test_connection(host, port):
                    _errors["base"] = "cannot_connect"
            except Exception as e:
                LOGGER.error(f"Error testing connection: {e}")
                _errors["base"] = "unknown"

            if not _errors:
                # Continue with additional credential testing if needed
                # try:
                #     await self._test_credentials(host=host, port=port)
                # except IntegrationrtlApiClientAuthenticationError as exception:
                #     LOGGER.warning(exception)
                #     _errors["base"] = "auth"
                # except IntegrationrtlApiClientCommunicationError as exception:
                #     LOGGER.error(exception)
                #     _errors["base"] = "connection"
                # except IntegrationrtlApiClientError as exception:
                #     LOGGER.exception(exception)
                #     _errors["base"] = "unknown"

                return self.async_create_entry(
                    title=host,
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_HOST,
                        default=(user_input or {"192.168.0.100"}).get(CONF_HOST),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.TEXT
                        ),
                    ),
                    vol.Required(CONF_PORT): selector.TextSelector(
                        default=(user_input or {9443}).get(CONF_PORT),
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.NUMBER
                        ),
                    ),
                }
            ),
            errors=_errors,
        )
