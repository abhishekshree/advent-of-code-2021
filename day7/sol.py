infile = "input2.txt"
data = list(map(int, open(infile).read().split(",")))

max_value = max(data)

def fuel_cost(x):
    return sum(abs(d-x) for d in data)

def fuel_cost2(x):
    sum_cost = 0
    for d in data:
        steps = abs(d-x)
        sum_cost += steps*(steps+1)/2
    
    return int(sum_cost)

fuel_arr = []
for x in range(max_value+1):
    fuel_arr.append(fuel_cost2(x))

print(min(fuel_arr))
