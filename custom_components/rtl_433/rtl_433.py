import asyncio
import json
import logging
import random
import re
import websocket
import aiohttp
from json.decoder import JSONDecodeError

from .const import (CONFIG_CMD, DEFAULT_TIME, DISMISS_ALERT_CMD, START_CMD,
                    STATUS_CMD, STOP_CMD)

_LOGGER = logging.getLogger(__name__)

class rtl433http:

    def __init__(self):
        self._ip = None
        self._sdr_id = None

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value

    @property
    def sdr_id(self):
        return self._sdr_id

    @sdr_id.setter
    def sdr_id(self, value):
        self._sdr_id = value

    def clean_response(self, text):
        text = text.replace("api", "")
        clean = re.compile('<.*?>')
        cleaned_text = re.sub(clean, '', text)
        cleaned_text = cleaned_text.replace("api", "")
        return cleaned_text.strip()

    async def _request(self, data):
        headers = {
          "content-type": "application/json; charset=UTF-8"
        }
        url = "http://" + self.ip + "/api.shtml"
        response = await self._make_request(url, data, headers)
        
        if response.find("404") != -1:
            _LOGGER.debug("Got a 404 issue: Wait and try again")
            await asyncio.sleep(random.randint(1, 3))
            response = await self._make_request(url, data, headers)
        
        try:
            jsonresp = json.loads(self.clean_response(response))
        except JSONDecodeError:
            response = await self._make_request(url, data, headers)
            jsonresp = json.loads(self.clean_response(response))
        return jsonresp

    async def _make_request(self, url, data, headers):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, headers=headers) as resp:
                response = await resp.text()
        return response

    async def fetch_data(self, sdr_id, dev_id):
        status = await self.get_protocol_status(sdr_id, dev_id)
        return status

    async def get_protocol_status(self, sdr_id, dev_id):
        data = {
            "cmd": STATUS_CMD,
            "sdr_id": sdr_id,
            "dev_id": dev_id,
        }
        status = await self._request(data)
        return status

    async def turn_on(self, sdr_id, dev_id, seconds=None, volume=None):
        if (not seconds or seconds == 0) and not volume:
            seconds = DEFAULT_TIME
        data = {
            "cmd": START_CMD,
            "sdr_id": sdr_id,
            "dev_id": dev_id,
            "duration": int(float(seconds))
        }
        if volume and volume != 0:
            data["volume"] = volume
        _LOGGER.debug(f"Data to Turn ON: {data}")
        status = await self._request(data)
        _LOGGER.debug(f"Response: {status}")
        return status["ret"] == 0

    async def turn_off(self, sdr_id, dev_id):
        data = {
            "cmd": STOP_CMD,
            "sdr_id": sdr_id,
            "dev_id": dev_id,
        }
        status = await self._request(data)
        return status["ret"] == 0

    async def get_sdr_config(self, sdr_id):
        data = {
            "cmd": CONFIG_CMD,
            "sdr_id": sdr_id
        }
        status = await self._request(data)
        return status

    async def get_vol_unit(self, sdr_id):
        config = await self.get_sdr_config(sdr_id)
        return config["vol_unit"]

    async def get_version(self, sdr_id):
        config = await self.get_sdr_config(sdr_id)
        return config["ver"]

    async def get_end_devs(self, sdr_id):
        config = await self.get_sdr_config(sdr_id)
        return {
            "devs": config["end_dev"],
            "names": config["dev_name"],
        }

# ... (other import statements and code)
