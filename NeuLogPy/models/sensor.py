# models/sensor.py

from pydantic import BaseModel, Field

class Sensor(BaseModel):
    code: str
    unit: str = Field(default="")
    description: str

class SensorConfig(BaseModel):
    sensors: dict[str, Sensor]
