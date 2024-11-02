# tests/test_sensor_registry.py

import pytest

from NeuLogPy.models.sensor import SensorConfig
from NeuLogPy.core.sensor_registry import SensorRegistry
from pydantic import ValidationError

def test_sensor_loading():
    registry = SensorRegistry(config_file="config/sensors.yaml")
    sensor = registry.get_sensor("Temperature")
    assert sensor is not None
    assert sensor.code == "Temperature"
    assert sensor.unit == "°C"

def test_invalid_sensor_config():
    invalid_data = {
        "sensors": {
            "InvalidSensor": {
                "code": 123,  # code should be a string, not an integer
                "unit": "units",
                "description": "Invalid sensor"
            }
        }
    }
    with pytest.raises(ValidationError):
        SensorConfig(**invalid_data)
