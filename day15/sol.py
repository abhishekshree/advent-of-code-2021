import numpy as np
import heapq

map = np.genfromtxt("input.txt", dtype=int, delimiter=1)
height, width = map.shape


def neighbors(x, y, scale):
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    ok = lambda a, b: 0 <= a < width * scale and 0 <= b < height * scale
    return [(a, b) for a, b in out if ok(a, b)]


def cost(x, y):
    c = map[y % height, x % width]
    c = c + x // width + y // height
    c = 1 + (c - 1) % 9
    return c


def dijkstra(scale):
    distances = {(0, 0): 0}
    pq = [(0, (0, 0))]
    while len(pq) > 0:
        total, (x, y) = heapq.heappop(pq)
        if total <= distances[(x, y)]:
            for n in neighbors(x, y, scale):
                distance = total + cost(*n)
                if distance < distances.get(n, 1e308):
                    distances[n] = distance
                    heapq.heappush(pq, (distance, n))

    return distances[(width * scale - 1, height * scale - 1)]
