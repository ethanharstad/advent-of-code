import sys
from collections import defaultdict
filename = sys.argv[1]

symbols = '$*+-'

with open(filename) as f:
    data = [[c for c in line.strip()] for line in f]
rows = len(data)
cols = len(data[0])
numbers = defaultdict(list)

total = 0
for r in range(len(data)):
    valid = False
    num = 0
    gears = set()
    for c in range(len(data[r]) + 1):
        if c < cols and data[r][c].isdigit():
            # print(f"N: {r} {c} {data[r][c]}")
            num = num*10 + int(data[r][c])
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0<=r+dr<rows and 0<=c+dc<cols:
                        cc = data[r+dr][c+dc]
                        if not cc.isdigit() and cc != '.':
                            # print(f"S {r+dr}, {c+dc} {cc}")
                            valid = True
                        if cc == '*':
                            gears.add((r+dr, c+dc))
        elif num > 0:
            print(f"{num} {valid} {total}")
            for gear in gears:
                numbers[gear].append(num)
            if valid:
                total += num
                valid = False
            num = 0
            gears = set()

print(f"Sum of part numbers: {total}")

total_ratio = 0
for value in numbers.values():
    if len(value) == 2:
        total_ratio += value[0] * value[1]
print(f"Total Ratio: {total_ratio}")