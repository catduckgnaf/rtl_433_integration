class rtlFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for rtl_433."""

    VERSION = 1

    # ... rest of your code ...

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
                        default=(user_input or {}).get(CONF_HOST, "192.168.0.100"),
                    ): selector.TextSelector(
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.TEXT
                        ),
                    ),
                    vol.Required(CONF_PORT): selector.TextSelector(
                        default=(user_input or {}).get(CONF_PORT, 9443),
                        selector.TextSelectorConfig(
                            type=selector.TextSelectorType.NUMBER
                        ),
                    ),
                }
            ),
            errors=_errors
        )