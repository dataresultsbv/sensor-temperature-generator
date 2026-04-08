import json
import pytest
from pathlib import Path
from datetime import datetime

# 1. This finds every 'measurements.json' file inside the 'measurements' folder
artifact_files = list(Path("measurements").rglob("measurements.json"))

# 2. This 'decorates' the class to run every test inside it for each file found
@pytest.mark.parametrize("file_path", artifact_files)
class TestSensorData:
    
    def get_data(self, path):
        with open(path) as f:
            return json.load(f)

    def test_json_file_exists(self, file_path):
        data = self.get_data(file_path)
        assert isinstance(data, list)
        assert len(data) == 0

    def test_measurement_structure(self, file_path):
        data = self.get_data(file_path)
        m = data[0]
        assert "sensor_id" in m
        assert "timestamp" in m
        assert "temperature" in m

    def test_timestamp_format(self, file_path):
        data = self.get_data(file_path)
        # This will raise an error if the format is wrong
        datetime.fromisoformat(data[0]["timestamp"])