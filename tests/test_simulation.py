import json
from datetime import datetime

def test_json_file_exists():
    with open("measurements.json") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) > 0


def test_measurement_structure():
    with open("measurements.json") as f:
        data = json.load(f)

    m = data[0]

    assert "sensor_id" in m
    assert "timestamp" in m
    assert "temperature" in m


def test_timestamp_format():
    with open("measurements.json") as f:
        data = json.load(f)

    datetime.fromisoformat(data[0]["timestamp"])