from itertools import combinations

data = [[int(y) for y in x] for x in open("input.txt", "r").read().splitlines()]

grid = {(x, y): data[y][x] for x in range(len(data[0])) for y in range(len(data))}

adjescents = set([x for x in combinations([-1, 0, 1] * 2, 2) if x != (0, 0)])
adj = lambda x, y: [(x + a, y + b) for a, b in adjescents if (x + a, y + b) in grid]

flashed, i, prev = 0, 0, set()

while len(prev) < len(grid):
    prev = set()
    grid = {k: v + 1 for k, v in grid.items()}
    while any(v > 9 for k, v in grid.items() if k not in prev):
        for k, v in grid.items():
            if k not in prev and v > 9:
                prev.add(k)
                for other in adj(*k):
                    grid[other] += 1
    flashed += len(prev)
    grid.update({k: 0 for k in prev})
    i += 1
    if i == 100:
        print(flashed)
print(i)
