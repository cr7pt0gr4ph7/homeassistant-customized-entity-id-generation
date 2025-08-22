"""Monkey-patches for the Home Assistant framework code."""
from typing import TYPE_CHECKING

from homeassistant.exceptions import InvalidStateError
import homeassistant.helpers.entity_registry as module_entity_registry
import homeassistant.helpers.entity as module_entity

from .const import (
    ATTR_PATCHES_APPLIED,
    ATTR_ORIGINAL_FUNCTIONS,
    ATTR_ENTITY_SLUGIFY,
    ATTR_ENTITY_REGISTRY_SLUGIFY,
)

import slugify as unicode_slug

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry


def apply_patches(entry: ConfigEntry):
    # We want to tweak the functionality of
    #
    #   - homeassistant.helpers.entity_registry.EntityRegistry.async_generate_entity_id
    #   - homeassistant.helpers.entity.async_generate_entity_id
    #
    # ...without having to manually patch every module that has already
    # imported those functions. Instead, we resort to replacing the internal
    # functions that are being called by the above two functions.
    #
    if entry.runtime_data is dict and entry.runtime_data[ATTR_PATCHES_APPLIED]:
        raise InvalidStateError("Custom Entity ID Generation patches have already been applied!")

    entry.runtime_data = {
        ATTR_PATCHES_APPLIED: True,
        ATTR_ORIGINAL_FUNCTIONS: {
            ATTR_ENTITY_SLUGIFY: module_entity.slugify,
            ATTR_ENTITY_REGISTRY_SLUGIFY: module_entity_registry.slugify,
        },
    }

    def _patched_slugify(text: str | None, *, separator: str = "_") -> str:
        """Slugify a given text."""
        if text == "" or text is None:
            return ""
        replacements = [
            ['ß', 'ss'],
            ['Ä', 'ae'],
            ['ä', 'ae'],
            ['Ö', 'oe'],
            ['ö', 'oe'],
            ['Ü', 'ue'],
            ['ü', 'ue'],
        ]
        slug = unicode_slug.slugify(text, separator=separator, replacements=replacements)
        return "unknown" if slug == "" else slug

    # Replace the original functions with the patched versions
    module_entity.slugify = _patched_slugify
    module_entity_registry.slugify = _patched_slugify

def revert_patches(entry: ConfigEntry):
    if not entry.runtime_data is dict:
        return

    if entry.runtime_data[ATTR_PATCHES_APPLIED]:
        module_entity.slugify = entry.runtime_data[ATTR_ORIGINAL_FUNCTIONS][ATTR_ENTITY_SLUGIFY]
        module_entity_registry.slugify = entry.runtime_data[ATTR_ORIGINAL_FUNCTIONS][ATTR_ENTITY_REGISTRY_SLUGIFY]

    # Discard runtime data
    entry.runtime_data = None
    pass
