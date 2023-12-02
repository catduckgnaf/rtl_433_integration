"""Sensor platform for Rtl_433."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .const import DOMAIN
from .coordinator import RtlDataUpdateCoordinator
from .entity import IntegrationRtlEntity

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
        IntegrationRtlSensor(coordinator, entity_description)
        for entity_description in ENTITY_DESCRIPTIONS
    ]
    async_add_devices(entities)


class IntegrationRtlSensor(IntegrationRtlEntity, SensorEntity):
    """integration_Rtl Sensor class."""

    def __init__(
        self,
        coordinator: RtlDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
