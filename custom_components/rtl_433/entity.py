"""Support for rtl_433 entities."""
from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.select import SelectEntityDescription
from homeassistant.components.switch import SwitchEntityDescription

### Consider using an entity dict for every protocol in rtl_433
### https://developers.home-assistant.io/docs/entity_registry_index/


@dataclass
class RtlSelectEntityDescription(SelectEntityDescription):
    """Class describing RTL_433 select entities."""

    command: str | None = None
    default_options: list | None = None


    
