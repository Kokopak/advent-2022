from parse import parse, search
from shapely import LineString, MultiPolygon, Polygon, box, unary_union


def count_invalid_in_row(y_row, sensors, beacons):
    sensors_shape = unary_union(sensors)

    line = LineString(
        [(sensors_shape.bounds[0], y_row), (sensors_shape.bounds[2], y_row)]
    )

    count_beacons = len([b for b in beacons if b[1] == y_row])

    return line.intersection(sensors_shape).length + 1 - count_beacons


def find_distress_beacon(sensors, box_bounds):
    sensors_shape = unary_union(sensors)
    search_zone = box(*box_bounds)

    good_zones = search_zone.difference(search_zone.intersection(sensors_shape))

    if isinstance(good_zones, MultiPolygon):
        return good_zones.geoms[0].centroid
    else:
        return good_zones.centroid


sensors = []
beacons = set()
with open("input.txt") as f:
    for l in f.read().splitlines():
        x_sensor, y_sensor, x_beacon, y_beacon = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", l
        ).fixed

        distance = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)

        beacons.add((x_beacon, y_beacon))

        sensors.append(
            Polygon(
                [
                    (x_sensor - distance, y_sensor),
                    (x_sensor, y_sensor - distance),
                    (x_sensor + distance, y_sensor),
                    (x_sensor, y_sensor + distance),
                ]
            )
        )


p1 = count_invalid_in_row(2000000, sensors, beacons)
print(p1)

distress_beacon_coord = find_distress_beacon(sensors, (0, 0, 4000000, 4000000))

p2 = distress_beacon_coord.x * 4000000 + distress_beacon_coord.y
print(p2)
