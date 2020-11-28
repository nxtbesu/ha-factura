from homeassistant import config_entries, core
from homeassistant.core import HomeAssistant


async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Factura component."""

    """
    Set up the electricity price sensor from configuration.yaml.
    ```yaml
    pvpc_hourly_pricing:
      - name: PVPC manual ve
        tariff: electric_car
      - name: PVPC manual nocturna
        tariff: discrimination
        timeout: 3
    ```
    """

    # @TODO: Add setup code.
    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up pvpc hourly pricing from a config entry."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, PLATFORM)
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, PLATFORM)
