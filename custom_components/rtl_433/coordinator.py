from __future__ import annotations

from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryAuthFailed
from custom_components.rtl_433.api import Rtl433ApiClient
import logging
import asyncio
import json
import websockets

class Rtl433DataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: ConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        client: Rtl433ApiClient,
        ws_host: str,
    ) -> None:
        """Initialize the coordinator."""
        self.client = client
        self.ws_host = ws_host
        super().__init__(
            hass=hass,
            logger=logging.getLogger(__name__),  # Adjust logger as needed
            name="rtl_433",
            update_interval=timedelta(minutes=60),
        )

    async def _async_update_data(self):
        """Update data via library."""
        try:
            # Connect to rtl_433's HTTP WebSocket API
            async with websockets.connect(f'{self.ws_host}/ws') as ws:
                self.logger.info(f'Connected to {self.ws_host}')
                
                while True:
                    # Fetch data from the WebSocket
                    message = await ws.recv()
                    self.handle_event(message)

        except ConfigEntryAuthFailed as exception:
            raise ConfigEntryAuthFailed(f"Authentication error: {exception}") from exception
        except UpdateFailed as exception:
            raise UpdateFailed(f"Communication error: {exception}") from exception

    def handle_event(self, message):
        """Handle each JSON event."""
        try:
            # Decode the message as JSON
            data = json.loads(message)

            #
            # Your custom handling logic here
            #

        except json.JSONDecodeError as e:
            self.logger.error(f'Error decoding JSON: {e}')
