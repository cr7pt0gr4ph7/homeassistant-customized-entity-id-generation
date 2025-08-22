# Customized Entity ID Generation

This integration monkey-patches the Home Assistant framework code to customize the way entity IDs are generated.

Available customizations:

- Translating German umlauts and special characters `ä`/`ö`/`ü`/`ß` to `ae`/`oe`/`ue`/`ss` instead of `a`/`o`/`u`/`s`,
  matching the standard German convention of translating those letters to ASCII-only.

> [!WARNING]
>
> **This integration monkey-patches a number of internals in the [Home Assistant framework code](https://github.com/home-assistant/core) and might break in future versions of Home Assistant**
>
> If you suspect that the integration isn't working anymore, or causes other stuff to break,
> it is sufficient to simply remove the integration and restart Home Assistant.
>
> Entity IDs generated after the integration was removed will obviously not receive the customizations,
> but any already generated entity IDs will be left unchanged and kept as-is, including the customizations applied during their generation.

# Installation

## Installing the integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

#### Via HACS
* Add this repo as a ["Custom repository"](https://hacs.xyz/docs/faq/custom_repositories/) with type "Integration"
* Click "Install" in the new "Customized Entity ID Generation" card in HACS.
* Install
* Restart Home Assistant
* Continue with [Activating the integration](#activating-the-integration)

#### Manual Installation
* Copy the entire `custom_components/customized_entity_id_generation/` directory to your server's `<config>/custom_components` directory
* Restart Home Assistant
* Continue with [Activating the integration](#activating-the-integration)

## Activating the integration

* Open `Settings > Devices & Services > Integrations` and click `+ Add Integration`
* Search for and then select `Customized Entity ID Generation`
