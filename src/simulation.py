import json
import os

def generate_measurements(amount_of_sensors=3, amount_of_minutes=10):
    import random
    from datetime import datetime, timedelta

    STARTING_TEMPERATURE = 20.0
    MAX_VARIATION_PER_MINUTE = 0.5

    sensors = {
        sensor_id: STARTING_TEMPERATURE + random.uniform(-2, 2)
        for sensor_id in range(1, amount_of_sensors + 1)
    }

    current_ts = datetime.now()
    measures = []

    for minute in range(amount_of_minutes):
        for sensor_id in sensors:
            change = random.uniform(-MAX_VARIATION_PER_MINUTE, MAX_VARIATION_PER_MINUTE)
            sensors[sensor_id] += change

            measures.append({
                "sensor_id": sensor_id,
                "timestamp": current_ts.isoformat(),
                "temperature": round(sensors[sensor_id], 2)
            })

        current_ts += timedelta(minutes=1)

    return measures


if __name__ == "__main__":
    data = generate_measurements()

    os.makedirs("output", exist_ok=True)

    file_path = os.path.join("output", "measurements.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Generated {file_path} for : {data}")