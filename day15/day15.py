from dataclasses import dataclass

from parse import parse


@dataclass
class Sensor:
    x: int
    y: int
    man_distance: int


def count_invalid_in_row(y_row, sensors):
    sensor_ranges = []
    for sensor in sensors:
        diff_y = sensor.man_distance - abs(y_row - sensor.y)

        if diff_y >= 0:
            dc_min = sensor.x - diff_y
            dc_max = sensor.x + diff_y
            sensor_ranges.append((dc_min, dc_max))

    sensor_ranges.sort()

    min_x = 0
    max_x = -float("infinity")

    total = 0

    for sensor_range in sensor_ranges:
        if not (sensor_range[0] >= min_x and sensor_range[1] <= max_x):
            if max_x != -float("infinity"):
                total -= len(
                    range(max(sensor_range[0], min_x), min(max_x, sensor_range[1]) + 1)
                )

            min_x, max_x = sensor_range
            total += max_x - min_x + 1

        print(sensor_range, total)

    print(sensor_ranges)
    print(total)


sensors = []
with open("input.txt") as f:
    for l in f.read().splitlines():
        x_sensor, y_sensor, x_beacon, y_beacon = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", l
        ).fixed

        distance = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)

        sensors.append(Sensor(x=x_sensor, y=y_sensor, man_distance=distance))

# print(sensors)
count_invalid_in_row(11, sensors)
