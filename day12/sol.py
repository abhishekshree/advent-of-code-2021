from typing import DefaultDict

l = [
    "EG-bj",
    "LN-end",
    "bj-LN",
    "yv-start",
    "iw-ch",
    "ch-LN",
    "EG-bn",
    "OF-iw",
    "LN-yv",
    "iw-TQ",
    "iw-start",
    "TQ-ch",
    "EG-end",
    "bj-OF",
    "OF-end",
    "TQ-start",
    "TQ-bj",
    "iw-LN",
    "EG-ch",
    "yv-iw",
    "KW-bj",
    "OF-ch",
    "bj-ch",
    "yv-TQ",
]

data = [line.split("-") for line in l]

graph = DefaultDict(set)

for a, b in data:
    graph[a].add(b)
    graph[b].add(a)


def dfs(start, repeat):
    if start[-1] == "end":
        return 1
    ans = 0
    for v in graph[start[-1]]:
        if not (v.islower() and v in start):
            ans += dfs(start + (v,), repeat)
        elif repeat and start.count(v) == 1 and v != "start":
            ans += dfs(start + (v,), False)
    return ans


print("1:", dfs(("start",), False))
print("2:", dfs(("start",), True))
