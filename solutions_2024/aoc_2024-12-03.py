from aocd import get_data
from aocd import submit

import re

# SETUP, READ DATA
YEAR = 2024
DAY = 3
input_raw = get_data(day=DAY, year=YEAR)

# PART 1
valid_muls = []


pattern = re.compile(r'mul\((\d+),(\d+)\)')
matches = pattern.findall(input_raw)

for match in matches:
    x, y = map(int, match)
    valid_muls.append((x, y))

answer_1 = 0
for valid_mul in valid_muls:
    answer_1 += valid_mul[0] * valid_mul[1]

print(answer_1)         # 166357705
# submit(answer_1, part="a", day=DAY, year=YEAR)


# PART 2
valid_inputs = []

pattern = re.compile(r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)')

matches = pattern.finditer(input_raw)
switch = True
for match in matches:
    if match.group(1) and match.group(2) and switch:
        x, y = int(match.group(1)), int(match.group(2))
        valid_inputs.append((x,y))
    elif match.group(0) == 'do()':
        switch = True
    elif match.group(0) == "don't()":
        switch = False

answer_2 = 0
for valid_mul in valid_inputs:
    answer_2 += valid_mul[0] * valid_mul[1]

print(answer_2)         # 166357705
# submit(answer_2, part="b", day=DAY, year=YEAR)
