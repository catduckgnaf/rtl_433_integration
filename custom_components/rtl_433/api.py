"""rtl_433 API WS Client."""
from __future__ import annotations

import asyncio
import socket

import aiohttp
import async_timeout

class IntegrationBlueprintApiClientError(Exception):
    """Exception to indicate a general API error."""

class IntegrationBlueprintApiClientCommunicationError(
    IntegrationBlueprintApiClientError
):
    """Exception to indicate a communication error."""

class IntegrationBlueprintApiClientAuthenticationError(
    IntegrationBlueprintApiClientError
):
    """Exception to indicate an authentication error."""

class IntegrationBlueprintApiClient:
    """rtl_433 HTTP API WS Client."""

    BASE_URL = "https://jsonplaceholder.typicode.com/posts/1"

    def __init__(
        self,
        host: str,
        port: int,
        session: aiohttp.ClientSession,
    ) -> None:
        """Initialize API client."""
        self._host = host
        self._port = port
        self._session = session

    async def async_get_data(self) -> any:
        """Get data from the API."""
        return await self._api_wrapper(method="get", url=self.BASE_URL)

    async def async_set_title(self, new_title: str) -> any:
        """Set title data via the API."""
        return await self._api_wrapper(
            method="patch",
            url=self.BASE_URL,
            data={"title": new_title},
            headers={"Content-type": "application/json; charset=UTF-8"},
        )

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> any:
        """Wrapper for API calls."""
        try:
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=data,
                )
                if response.status in (401, 403):
                    raise IntegrationBlueprintApiClientAuthenticationError(
                        "Invalid credentials",
                    )
                response.raise_for_status()
                return await response.json()

        except asyncio.TimeoutError as exception:
            raise IntegrationBlueprintApiClientCommunicationError(
                "Timeout error fetching information",
            ) from exception
        except aiohttp.ClientResponseError as exception:
            raise IntegrationBlueprintApiClientCommunicationError(
                f"HTTP error fetching information: {exception.status}"
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise IntegrationBlueprintApiClientCommunicationError(
                "Error fetching information",
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            raise IntegrationBlueprintApiClientError(
                "Something really wrong happened!"
            ) from exception
