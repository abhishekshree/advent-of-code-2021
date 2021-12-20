from typing import Counter
from more_itertools import pairwise

poly, pair = open("input.txt", mode="r").read().split("\n\n")
pair = {j[0]: j[1] for j in [i.split(" -> ") for i in pair.split("\n")]}


def part1(poly):
    poly = [list(poly)]
    for s in range(10):
        np = [poly[-1][0]]
        for i in range(1, len(list(poly[-1]))):
            ins = pair.get("".join([poly[-1][i - 1], poly[-1][i]]))
            np.append(ins)
            np.append(poly[-1][i])
        poly.append(np)

    dvs = list(dict(sorted(Counter(poly[-1]).items(), key=lambda i: i[1])).values())
    print(dvs[-1] - dvs[0])


def part2():
    elements = dict()
    polymers = dict()

    for p in list(poly):
        elements.update({p: elements.get(p, 0) + 1})

    for p in pairwise(poly):
        polymers.update({"".join(p): polymers.get("".join(p), 0) + 1})

    for i in range(40):
        polymers2 = dict()
        for pk, pv in polymers.items():
            pe1, pe2 = list(pk)
            polymers2.update(
                {
                    "".join([pe1, pair[pk]]): polymers2.get("".join([pe1, pair[pk]]), 0)
                    + pv
                }
            )
            polymers2.update(
                {
                    "".join([pair[pk], pe2]): polymers2.get("".join([pair[pk], pe2]), 0)
                    + pv
                }
            )
            elements.update({pair[pk]: elements.get(pair[pk], 0) + pv})

        polymers = dict(polymers2)

    dvs = list(dict(sorted(elements.items(), key=lambda i: i[1])).values())
    print(dvs[-1] - dvs[0])
