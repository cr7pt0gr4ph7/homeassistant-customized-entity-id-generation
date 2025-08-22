"""Customized Entity ID Generation integration for Home Assistant."""

import logging
from typing import Final

from homeassistant.const import Platform

DOMAIN: Final = "customized_entity_id_generation"
LOGGER = logging.getLogger(__package__)

PLATFORMS: Final = [
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.EVENT,
    Platform.NUMBER,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.TIME,
]

ATTR_PATCHES_APPLIED = "patches_applied"
ATTR_ORIGINAL_FUNCTIONS = "original_functions"
ATTR_ENTITY_SLUGIFY = "entity.slugify"
ATTR_ENTITY_REGISTRY_SLUGIFY = "entity_registry.slugify"
