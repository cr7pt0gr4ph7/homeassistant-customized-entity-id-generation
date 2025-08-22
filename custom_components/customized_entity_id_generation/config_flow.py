"""Customized Entity ID Generation integration for Home Assistant."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult

from .const import DOMAIN


class UptimeConfigFlow(ConfigFlow, domain=DOMAIN):
    """Config flow for out integration."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        if self._async_current_entries():
            return self.async_abort(reason="already_installed")

        return self.async_create_entry(title="Customized Entity ID Generation", data={})
