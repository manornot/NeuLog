# core/sensor_registry.py

from models.sensor import Sensor, SensorConfig
from utils.file_loader import load_yaml

class SensorRegistry:
    def __init__(self, config_file="config/sensors.yaml"):
        raw_data = load_yaml(config_file)
        self.sensor_config = SensorConfig(**raw_data)  # Validate and load the sensor config

    def get_sensor(self, name):
        """Retrieve a sensor by name."""
        return self.sensor_config.sensors.get(name)

    def add_sensor(self, name, code, unit="", description=""):
        """Add a new sensor and validate it using the Sensor Pydantic model."""
        self.sensor_config.sensors[name] = Sensor(code=code, unit=unit, description=description)

    def list_sensors(self):
        """List all sensors with their details."""
        for name, details in self.sensor_config.sensors.items():
            print(f"{name} (Code: {details.code}, Unit: {details.unit}) - {details.description}")
