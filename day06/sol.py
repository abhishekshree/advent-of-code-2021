from functools import lru_cache

infile = "input2.txt"
data = list(map(int, open(infile).read().split(",")))


@lru_cache(maxsize=None)
def descend(day, end):
    if end - day <= 8:
        return 1
    return 1 + sum(descend(day, end) for day in range(day + 9, end + 1, 7))


print(sum(descend(fish - 8, 80) for fish in data))
print(sum(descend(fish - 8, 256) for fish in data))
