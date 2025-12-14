from fastapi import FastAPI
from datetime import datetime, timezone
import random

app = FastAPI()


@app.get("/temperature")
async def get_temperature(location: str):
    sensor_id = get_sensor_id(location)

    return {
        "value": get_temperature(),
        "unit": "°C",
        "timestamp": get_now(),
        "location": location,
        "status": "active",
        "sensor_id": sensor_id,
        "sensor_type": "temperature",
        "description": ""
    }

@app.get("/temperature/{id}")
async def get_location(id: str):
    return {
        "value": get_temperature(),
        "unit": "°C",
        "timestamp": get_now(),
        "location": get_location(id),
        "status": "active",
        "sensor_id": id,
        "sensor_type": "temperature",
        "description": ""
    }

def get_sensor_id(location: str):
    location_to_sensor = {
        "Living Room": "1",
        "Bedroom": "2",
        "Kitchen": "3"
    }

    return location_to_sensor.get(location, "Unknown")

def get_location(id: str):
    sensor_to_location = {
        "1": "Living Room",
        "2": "Bedroom",
        "3": "Kitchen"
    }

    return sensor_to_location.get(id, "0")

def get_temperature():
    return random.uniform(-30, 30)

def get_now():
    return datetime.now(timezone.utc)
