"""Adds config flow for rtl_433."""
from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.helpers import selector

from .const import DOMAIN, LOGGER

class BlueprintFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for rtl_433."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.FlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}
        if user_input is not None:
            try:
                # Replace username with host and password with port
                await self._test_credentials(
                    host=user_input[CONF_HOST],
                    port=user_input[CONF_PORT],
                )
            except IntegrationBlueprintApiClientAuthenticationError as exception:
                LOGGER.warning(exception)
                _errors["base"] = "auth"
            except IntegrationBlueprintApiClientCommunicationError as exception:
                LOGGER.error(exception)
                _errors["base"] = "connection"
            except IntegrationBlueprintApiClientError as exception:
                LOGGER.exception(exception)
                _errors["base"] = "unknown"
            else:
                return self.async_create_entry(
                    title=user_input[CONF_HOST],
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

