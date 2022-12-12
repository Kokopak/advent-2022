import heapq
from collections import defaultdict


def dijkstra(graph, starting_vertex):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


graph = defaultdict(dict)

S = (0, 0)
E = (0, 0)

a_elevations = set()

with open("input.txt") as f:
    grid = {}

    for r, l in enumerate(f.readlines()):
        for c, letter in enumerate(l.strip()):
            grid[(r, c)] = letter

    ROWS = max(grid, key=lambda x: x[0])[0]
    COLS = max(grid, key=lambda x: x[1])[1]

    for r in range(ROWS + 1):
        for c in range(COLS + 1):
            coord = (r, c)

            if grid[coord] in ("S", "a"):
                a_elevations.add(coord)

            for nr, nc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if r + nr >= 0 and c + nc >= 0 and r + nr <= ROWS and c + nc <= COLS:
                    neighbor = (r + nr, c + nc)

                    elevation_current = 0
                    elevation_neighbor = 0

                    if grid[coord] == "S":
                        S = coord
                        elevation_current = ord("a")
                    elif grid[coord] == "E":
                        E = coord
                        elevation_current = ord("z")
                    else:
                        elevation_current = ord(grid[coord])

                    if grid[neighbor] == "S":
                        elevation_neighbor = ord("a")
                    elif grid[neighbor] == "E":
                        elevation_neighbor = ord("z")
                    else:
                        elevation_neighbor = ord(grid[neighbor])

                    if (
                        elevation_neighbor <= elevation_current
                        or elevation_neighbor == elevation_current + 1
                    ):
                        graph[coord][neighbor] = 1

p1 = dijkstra(graph, S)[E]
print(p1)

p2 = float("infinity")

for a in a_elevations:
    min_dis = dijkstra(graph, a)[E]

    if min_dis < p2:
        p2 = min_dis

print(p2)
