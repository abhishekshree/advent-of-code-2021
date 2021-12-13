# NOC
from parse import findall

instr = open('input.txt').read()
dots = findall("{:d},{:d}", instr)
folds = findall("{:l}={:d}", instr)

for axis, line in folds:
    dots = {
        (
            min(x, 2 * line - x) if axis == "x" else x,
            min(y, 2 * line - y) if axis == "y" else y,
        )
        for x, y in dots
    }
    print(len(dots))

for y in range(6):
    print(*[" #"[(x, y) in dots] for x in range(40)])
