from aocd import get_data
from aocd import submit

from collections import Counter

# SETUP , READ DATA
YEAR = 2024
DAY = 1
input_raw = get_data(day=DAY, year=YEAR)

# PARSE DATA
list_1, list_2 = [], []

for line in input_raw.strip().split('\n'):
    if line:  # Skip empty lines
        # Split on whitespace and convert to integers
        num1, num2 = map(int, line.split())
        list_1.append(num1)
        list_2.append(num2)

assert len(list_1) == len(list_2)

list_1 = sorted(list_1)
list_2 = sorted(list_2)


# PART 1
list_diff = [abs(a - b) for a, b in zip(list_1, list_2)]

answer_1 = sum(list_diff)

print(f"answer_1 = {answer_1:,}")     # 1,830,467
submit(answer_1, part="a", day=DAY, year=YEAR)


# PART 2
counter_list_2 = Counter(list_2)
answer_2 = 0
for i in list_1:
    tmp_score = i * counter_list_2.get(i, 0)
    answer_2 += tmp_score

print(f"answer_2 = {answer_2:,}")     # 26,674,158
submit(answer_2, part="b", day=DAY, year=YEAR)