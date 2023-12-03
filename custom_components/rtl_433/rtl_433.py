import asyncio
import json
import logging
import websockets

from .const import WS_HOST

_LOGGER = logging.getLogger(__name__)

async def ws_events():
    url = f'{WS_HOST}/ws'

    try:
        async with websockets.connect(url) as ws:
            _LOGGER.info(f'Connected to {url}')

            while True:
                message = await ws.recv()
                yield message

    except websockets.exceptions.ConnectionClosedError:
        _LOGGER.warning('WebSocket connection closed unexpectedly.')
    except Exception as e:
        _LOGGER.error(f'Error in WebSocket connection: {e}')
