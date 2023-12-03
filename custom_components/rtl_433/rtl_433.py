import asyncio
import json
import logging
import websockets

from .const import WS_HOST

_LOGGER = logging.getLogger(__name__)
exit_flag = False  # Global variable to signal graceful exit


async def ws_events():
    url = f'{WS_HOST}/ws'

    try:
        async with websockets.connect(url) as ws:
            _LOGGER.info(f'Connected to {url}')

            while True:
                if exit_flag:
                    break

                message = await ws.recv()
                yield message

    except websockets.exceptions.ConnectionClosedError as e:
        _LOGGER.warning(f'WebSocket connection closed unexpectedly: {e}')
    except websockets.exceptions.WebSocketException as e:
        _LOGGER.error(f'WebSocket error: {e}')


async def process_websocket_messages():
    async for message in ws_events():
        # Process the WebSocket message here
        _LOGGER.debug(f'Received WebSocket message: {message}')


async def main():
    # Initialize your Home Assistant or application here

    # Start processing WebSocket messages
    await process_websocket_messages()

    # Perform cleanup or additional tasks if needed


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)  # Set logging level as needed
    asyncio.run(main())
