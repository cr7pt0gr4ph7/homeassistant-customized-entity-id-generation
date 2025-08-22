"""Customized Entity ID Generation integration for Home Assistant."""

from __future__ import annotations

import asyncio

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Event, HomeAssistant

from .const import DOMAIN, LOGGER, PLATFORMS
from .monkey_patches import apply_patches, revert_patches


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""

    LOGGER.debug(
        "Custom entity ID generation is being enabled using the following options: %s",
        entry.data,
    )

    apply_patches(entry)

    # Success!
    LOGGER.debug("Successfully loaded the custom entity ID generation integration")
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""

    LOGGER.debug("Custom entity ID generation is being disabled, and monkey-patches will be reverted")

    revert_patches(entry)

    # Success!
    LOGGER.debug("Successfully unloaded the custom entity ID generation integration")
    return True
