from homeassistant.const import Platform

DOMAIN = "china_workday"

# Keep the existing unique ID so upgrading does not create a duplicate entity.
LEGACY_UNIQUE_ID = "china-workday.is_workday"

SUPPORTED_PLATFORMS = [
    Platform.BINARY_SENSOR
]
