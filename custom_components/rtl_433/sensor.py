"""Sensor platform for rtl_433."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .const import DOMAIN
from .coordinator import rtlDataUpdateCoordinator
from .entity import IntegrationrtlEntity

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="rtl_433",
        name="Integration Sensor",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    entities = [
        IntegrationrtlSensor(coordinator, entity_description)
        for entity_description in ENTITY_DESCRIPTIONS
    ]
    async_add_devices(entities)


class IntegrationrtlSensor(IntegrationrtlEntity, SensorEntity):
    """integration_rtl Sensor class."""

    def __init__(
        self,
        coordinator: rtlDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
