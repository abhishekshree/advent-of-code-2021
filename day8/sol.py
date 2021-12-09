def find_numbers(numbers):
    one = next((x for x in numbers if len(x) == 2))
    four = next((x for x in numbers if len(x) == 4))
    seven = next((x for x in numbers if len(x) == 3))
    eight = next((x for x in numbers if len(x) == 7))
    nine = next((x for x in numbers if len(x) == 6 and all(y in x for y in four)))
    zero = next(
        (x for x in numbers if len(x) == 6 and x != nine and all(y in x for y in one))
    )
    six = next((x for x in numbers if len(x) == 6 and x != nine and x != zero))
    three = next((x for x in numbers if len(x) == 5 and all(y in x for y in one)))
    five = next(
        (x for x in numbers if len(x) == 5 and x != three and all(y in nine for y in x))
    )
    two = next((x for x in numbers if len(x) == 5 and x != three and x != five))
    return [zero, one, two, three, four, five, six, seven, eight, nine]


with open("input.txt", "r") as file:
    data = [
        [["".join(sorted(z)) for z in y.split()] for y in x.split(" | ")]
        for x in file.read().splitlines()
    ]
    p1, p2 = 0, 0
    for numbers, code in data:
        numbers = find_numbers(numbers)
        p1 += sum(1 for x in code if x in [numbers[y] for y in [1, 4, 7, 8]])
        p2 += int("".join([str(numbers.index(x)) for x in code]))
    print(p1)
    print(p2)
